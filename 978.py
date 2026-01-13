import math

from tqdm import tqdm

list_of_prob = {(1,1): 1}


def get_next_probability():
    new_probs = {}
    for k, v in list_of_prob.items():
        position = k[0]
        prev_dest = k[1]
        size = abs(prev_dest)
        if size == 0:
            ky = (position, position)
            #print(k, v, ky, new_probs.get(ky, 0))
            new_probs[ky] = new_probs.get(ky, 0) + 2 * v
        else:
            ky = (position + size, position)
            #print(k, v/2, ky, new_probs.get(ky, 0))
            new_probs[ky] = new_probs.get(ky, 0) + v
            ky = (position - size, position)
            #print(k, v / 2, ky, new_probs.get(ky, 0))
            new_probs[ky] = new_probs.get(ky, 0) + v
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
    for k, v in list_of_prob.items():
        position = k[0]
        count += v
        total += position * v
    res = total / count
    return res


def get_avg_squared():
    total = 0
    count = 0
    for k, v in list_of_prob.items():
        position = k[0]
        count += v
        total += position * position * v
    res = total / count
    return res


def get_avg_with_parameters(mu, rho):
    total = 0
    count = 0
    for k, v in list_of_prob.items():
        position = k[0]
        count += v
        val = (position - mu) / rho
        total += val * val * val * v
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
    rho = math.sqrt(avg_squared - mu**2)
    res = get_avg_with_parameters(mu, rho)
    print(res)
