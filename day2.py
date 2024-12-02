def parse_input():
    with open("./inputs/day2.txt") as f:
        lines = f.readlines()
        reports = []
        for line in lines:
            report = [int(number) for number in line.split()]
            reports.append(report)
    f.close()
    return reports


def part1():
    reports = parse_input()
    increasing_no = 0
    safe_reports = 0
    for report in reports:
        for i in range(len(report)):
            if i == 0:
                continue
            diff = report[i]-report[i-1]
            if 1 <= diff <= 3:
                increasing_no += 1
            elif 1 <= -diff <= 3:
                increasing_no += -1
        if increasing_no == len(report)-1 or increasing_no == -(len(report)-1):
            safe_reports += 1
        increasing_no = 0
    print(safe_reports)


if __name__ == "__main__":
    part1()






