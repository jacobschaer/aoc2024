

def part_1(input):
    count = 0
    for report in input:
        levels = [int(x) for x in report.strip().split(' ')]
        level = None
        sign = None
        is_valid = True
        for i in range(len(levels)):
            if level is not None:
                diff = levels[i] - level
                if diff == 0:
                    is_valid = False
                    break
                new_sign = diff / abs(diff)
                diff = abs(diff)
                if sign is not None and new_sign != sign:
                    is_valid = False
                    break
                if diff >3 or diff < 1:
                    is_valid = False
                    break
                sign = new_sign
            level = levels[i]

        print(is_valid)
        if is_valid:
            count += 1

    print(count)

def check_line(levels):
    level = None
    sign = None
    is_valid = True
    for i in range(len(levels)):
        if level is not None:
            diff = levels[i] - level
            if diff == 0:
                is_valid = False
                break
            new_sign = diff / abs(diff)
            diff = abs(diff)
            if sign is not None and new_sign != sign:
                is_valid = False
                break
            if diff >3:
                is_valid = False
                break
            sign = new_sign
        level = levels[i]
    return is_valid


def part_2(input):
    count = 0
    for report in input:
        levels = [int(x) for x in report.strip().split(' ')]
        for i in range(len(levels)):
            candidate = levels[:i] + levels[i + 1:]
            print(candidate)
            if check_line(candidate):
                print("good")
                count += 1
                break
    print(count)



if __name__ == "__main__":
    with open('input.txt') as inputfile:
        part_2(inputfile)
