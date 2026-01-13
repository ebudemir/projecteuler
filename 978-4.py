import math
import threading
import queue
import time

def get_avg(list_of_prob):
    total = 0
    count = 0
    for position, v in list_of_prob.items():
        for _, probability in v.items():
            count += probability
            total += position * probability
    res = total / count
    return res


def get_avg_squared(list_of_prob):
    total = 0
    count = 0
    for position, v in list_of_prob.items():
        for _, probability in v.items():
            count += probability
            total += position * position * probability
    res = total / count
    return res


def get_avg_with_parameters(list_of_prob, mu, rho):
    total = 0
    count = 0
    for position, v in list_of_prob.items():
        for _, probability in v.items():
            count += probability
            val = (position - mu) / rho
            total += val * val * val * probability
    res = total / count
    return res


def create_2_to_3(q_out, name):
    list_of_prob = {(1, 1): 1}
    for (position, prev_dest), v in list_of_prob.items():
        size = abs(prev_dest)
        if size == 0:
            q_out.put((position, position, v))
        else:
            q_out.put((position + size, position, v / 2))
            q_out.put((position - size, position, v / 2))
    q_out.put((None, None, None))
    print(name)


def create_middle(q_in, q_out, name):
    while True:
        position, prev_dest, probability = q_in.get()
        #print(position, prev_dest, probability)
        if position is None:
            q_out.put((None, None, None))
            break
        size = abs(prev_dest)
        if size == 0:
            q_out.put((position, position, probability))
        else:
            q_out.put((position + size, position, probability / 2))
            q_out.put((position - size, position, probability / 2))
        q_in.task_done()
    print(name)


def create_final(q_in, name):
    new_probs = {}
    while True:
        position, prev_dest, probability = q_in.get()
        #print(position, prev_dest, probability)
        if position is None:
            #print(new_probs)
            mu = get_avg(new_probs)
            avg_squared = get_avg_squared(new_probs)
            rho = math.sqrt(avg_squared - mu ** 2)
            res = get_avg_with_parameters(new_probs, mu, rho)
            print(mu)
            print(rho)
            print(res)
            break
        size = abs(prev_dest)
        if size == 0:
            if position in new_probs:
                new_probs[position][position] = new_probs[position].get(position, 0) + probability
            else:
                new_probs[position] = {position: probability}
        else:
            val = position + size
            if val in new_probs:
                new_probs[val][position] = new_probs[val].get(position, 0) + probability / 2
            else:
                new_probs[val] = {position: probability / 2}
            val = position - size
            if val in new_probs:
                new_probs[val][position] = new_probs[val].get(position, 0) + probability / 2
            else:
                new_probs[val] = {position: probability / 2}
        q_in.task_done()
    print(name)


if __name__ == "__main__":
    q_in = queue.Queue()
    t1 = threading.Thread(target=create_2_to_3, args=(q_in, "create_2_to_3"))
    t1.start()
    t1.join()

    for i in range(3, 49):
        q_out = queue.Queue()
        t2 = threading.Thread(target=create_middle, args=(q_in, q_out, "create_" + str(i) + "_to_" + str(i+1)))
        t2.start()
        t2.join()
        q_in = q_out

    t3 = threading.Thread(target=create_final, args=(q_in, "create_" + str(i+1) + "_to_" + str(i+2)))
    t3.start()
    t3.join()
