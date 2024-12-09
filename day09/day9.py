from aocd import get_data
dataset = get_data(day=9, year=2024)

# dataset = "2333133121414131402"

disk = [list(str(int(idx/2))*int(x)) if idx % 2 == 0 else list('.'*int(x)) for idx, x in enumerate(dataset)]
diskmap = [x for y in disk for x in y]
# print(diskmap)

def rearranger(disklist):
    tempdisk = disklist.copy()
    backindex = -1
    forwardindex = tempdisk.index('.')
    while abs(backindex) <= tempdisk.count('.'):
        if disklist[-1] != '.':
            lastspotvalue = disklist[backindex]
            tempdisk[forwardindex] = lastspotvalue
            tempdisk[backindex] = '.'
        backindex -= 1
        forwardindex = tempdisk.index('.')
    return tempdisk

def part1():
    total = 0
    calclist = rearranger(diskmap)
    print(diskmap)
    print(''.join(calclist))
    for ind, value in enumerate(calclist):
        if value != '.':
            # print(int(value)*ind)
            total += int(value)*ind
    return total

if __name__ == "__main__":
    print(f"Part 1: {part1()}")