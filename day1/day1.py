
inputs = {
    '1122': 3,
    '1111': 4,
    '1234': 0,
    '91212129': 9,
}


# def count(number_list):
#     first, *tail = number_list

#     if len(tail) == 1:
#         return [int(first)] if first == tail[0] else []

#     if first == tail[0]:
#         return [int(first)] + count(tail)
#     else:
#         return count(tail)


def count(number_list, step=0):
    first, *tail = number_list

    if len(tail) == step + 1:
        return int(first) + int(tail[step]) if first == tail[step] else 0

    if first == tail[step]:
        return int(first) + int(tail[step]) + count(tail, step)
    else:
        return count(tail, step)


def day1_1part():
    for input_, result in inputs.items():
        sum_list = count(input_)
        if input_[0] == input_[-1]:
            sum_list.append(int(input_[0]))

        test_res = sum(sum_list)
        print('{} = {}'.format(input_, test_res))


inputs2 = {
    '1212': 6,
    '1221': 0,
    '123425': 4,
    '123123': 12,
    '12131415': 4
}


def day1_2part():
    for input_, result in inputs2.items():
        step = int(len(input_) / 2) - 1
        print(step)
        sum_ = count(input_, step)

        test_res = sum_
        print('{} = {}'.format(input_, test_res))


def day1_part1_prob():
    with open('input') as f:
        input_ = f.read().strip()

    sum_list = count(input_)
    if input_[0] == input_[-1]:
        sum_list.append(int(input_[0]))

    return sum(sum_list)


def day1_part2_prob():
    with open('input') as f:
        input_ = f.read().strip()

    step = int(len(input_) / 2) - 1
    sum_ = count(input_, step)

    print('{} = {}'.format(input_, sum_))


if __name__ == '__main__':
    # day1_1part()
    res = day1_part1_prob()
    print('{}'.format(res), flush=True)
