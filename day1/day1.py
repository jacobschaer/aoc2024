from collections import defaultdict


def part_1(input):
    l = []
    r = []
    for line in input:
        splitted = line.split(' ')
        a, b = splitted[0], splitted[-1]
        print(a,b)
        l.append(int(a))
        r.append(int(b))
    l.sort()
    r.sort()
    d = 0
    while l:
        a = l.pop()
        b = r.pop()
        d += abs(b - a)
    print(d)

def part_2(input):
    l = []
    r = defaultdict(int) 
    for line in input:
        splitted = line.split(' ')
        a, b = splitted[0], splitted[-1]
        print(a,b)
        l.append(int(a))
        r[int(b)] += 1
    d = 0
    while l:
        a = l.pop()
        b = r[a]
        print(a,b)
        d += a * b
    print(d)



if __name__ == "__main__":
    with open('example.txt') as inputfile:
        #part_1(inputfile)
        part_2(inputfile)

    with open('input.txt') as inputfile:
        #part_1(inputfile)
        part_2(inputfile)
