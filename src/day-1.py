def read_input(filename):
    with open(filename, 'r+') as file:
        return file.read()


def insert_numbers(values):
    l1 = []
    l2 = []
    for line in values.split('\n'):
        value_set = line.split('   ')
        l1.append(int(value_set[0]))
        l2.append(int(value_set[1]))
    return l1, l2


def part1(l1, l2):
    l1.sort()
    l2.sort()
    sum_of_differences = sum(abs(x - y) for x, y in zip(l1, l2))
    return sum_of_differences

def part2(l1,l2):
    res = 0
    for x in l1:
        res += (x * l2.count(x))
    return res


_input = read_input('1_input.txt')
output = insert_numbers(_input)
print(part1(output[0],output[1]))
print(part2(output[0],output[1]))