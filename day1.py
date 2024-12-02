def part1():
    distance = 0
    numbers1, numbers2 = parse_input()
    numbers1.sort()
    numbers2.sort()
    for i in range(len(numbers1)):
        distance += abs(numbers1[i]-numbers2[i])
    print(distance)


def part2():
    n1, n2 = parse_input()
    similarity = 0
    for number in n1:
        for n in n2:
            if n == number:
                similarity += number
    print(similarity)


def parse_input():
    with open('./inputs/day1.txt') as f:
        lines = f.readlines()
        numbers1 = []
        numbers2 = []
        for line in lines:
            try:
                no1, no2 = line.split()
                numbers1.append(int(no1))
                numbers2.append(int(no2))
            except:
                continue
    f.close()
    return numbers1, numbers2


if __name__ == "__main__":
    part1()
    part2()