import math

from tqdm import tqdm

list_of_prob = {1: {1: 1}}


def get_next_probability():
    new_probs = {}
    for position, v in list_of_prob.items():
        for prev_dest, probability in v.items():
            size = abs(prev_dest)
            if size == 0:
                if position in new_probs:
                    new_probs[position][position] = new_probs[position].get(position, 0) + 2 * probability
                else:
                    new_probs[position] = {position: probability}
            else:
                val = position + size
                if val in new_probs:
                    new_probs[val][position] = new_probs[val].get(position, 0) + probability
                else:
                    new_probs[val] = {position: probability}
                val = position - size
                if val in new_probs:
                    new_probs[val][position] = new_probs[val].get(position, 0) + probability
                else:
                    new_probs[val] = {position: probability}
    return new_probs


def print_last_probability_distribution2():
    sorted_dict_asc = dict(sorted(list_of_prob.items()))
    for k, v in sorted_dict_asc.items():
        print(k, v)


def print_last_probability_distribution():
    res = {}
    for k, v in list_of_prob.items():
        position = k[0]
        res[position] = res.get(position, 0) + v
    sorted_dict_asc = dict(sorted(res.items()))
    print(sorted_dict_asc)


def get_avg():
    total = 0
    count = 0
    for position, v in list_of_prob.items():
        for _, probability in v.items():
            count += probability
            total += position * probability
    res = total / count
    return res


def get_avg_squared():
    total = 0
    count = 0
    for position, v in list_of_prob.items():
        for _, probability in v.items():
            count += probability
            total += position * position * probability
    res = total / count
    return res


def get_avg_with_parameters(mu, rho):
    total = 0
    count = 0
    for position, v in list_of_prob.items():
        for _, probability in v.items():
            count += probability
            val = (position - mu) / rho
            total += val * val * val * probability
    res = total / count
    return res


if __name__ == "__main__":
    for i in tqdm(range(3, 51)):
        print(i)
        list_of_prob = get_next_probability()
        #print_last_probability_distribution2()
        #print_last_probability_distribution()
    mu = get_avg()
    avg_squared = get_avg_squared()
    rho = math.sqrt(avg_squared - mu ** 2)
    res = get_avg_with_parameters(mu, rho)
    print(mu)
    print(rho)
    print(res)
