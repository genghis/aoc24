from aocd import get_data
dataset = get_data(day=9, year=2024)

# dataset = "2333133121414131402"

diskmap = [int(idx / 2) if idx % 2 == 0 else '.' for idx, val in enumerate(dataset) for _ in range(int(val))]

def rearranger(disklist):
    count = 0
    tempdisk = disklist.copy()
    for i, v in enumerate(tempdisk):
            if v == '.':
                while tempdisk[-1] == '.':
                    tempdisk.pop()
                if i >= len(tempdisk):
                    break
                tempdisk[i] = tempdisk[-1]
                tempdisk.pop()
            count+=int(tempdisk[i])*i
        
    return count

def file_rearranger(disklist):
    count = 0
    tempdisk = disklist.copy()
    for i, v in enumerate(tempdisk):
            if v == '.':
                while tempdisk[-1] == '.':
                    tempdisk.pop()
                if i >= len(tempdisk):
                    break
                tempdisk[i] = tempdisk[-1]
                tempdisk.pop()
            count+=int(tempdisk[i])*i
        
    return count

def part1():
    return rearranger(diskmap)

def part2():
    return file_rearranger(diskmap)

if __name__ == "__main__":
    print(f"Part 1: {part1()}")