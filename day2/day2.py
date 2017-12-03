input_ = [
    [5, 1, 9, 5],
    [7, 5, 3],
    [2, 4, 6, 8]
]


def day2_part1():
    sum_list = []

    for row in input_:
        row.sort(reverse=True)
        sum_list.append(row[0] - row[-1])

    return sum(sum_list)


def day2_problem_part1():
    problem_input = []

    with open('input') as f:
        row = f.readline().strip().split()
        while row:
            print('Row: {}'.format(row), flush=True)
            problem_row = [int(elem) for elem in row]
            problem_row.sort(reverse=True)
            problem_input.append(problem_row)
            row = f.readline().strip().split()

    sum_list = []
    for row in problem_input:
        sum_list.append(int(row[0]) - int(row[-1]))

    return sum(sum_list)
