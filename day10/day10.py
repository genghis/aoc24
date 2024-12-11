from aocd import get_data
dataset = get_data(day=10, year=2024).splitlines()

trailheads = {}
trailheads2 = {}
trailends = []

for ycoord, row in enumerate(dataset):
    for xcoord, value in enumerate(row):
        if int(value) == 0:
            trailheads[(ycoord,xcoord)] = set()
            trailheads2[(ycoord,xcoord)] = []
        elif int(value) == 9:
            trailends.append((ycoord,xcoord))

def check_surrounding(starting, coordinates, value):
    if value == 0:
        trailheads[coordinates].add(starting)
        trailheads2[coordinates].append(starting)
    surrounding = {}
    ycoord,xcoord = coordinates
    if xcoord > 0:
        surrounding['left'] = (ycoord, xcoord-1)
    if xcoord < len(dataset[0])-1:
        surrounding['right'] = (ycoord, xcoord+1)
    if ycoord > 0:
        surrounding['up'] = (ycoord-1, xcoord)
    if ycoord < len(dataset)-1:
        surrounding['down'] = (ycoord+1, xcoord)
    for i in surrounding:
        yc, xc = surrounding[i]
        if int(dataset[yc][xc]) == value-1:
            check_surrounding(starting, (yc,xc), value-1)

def part1():
    count = 0
    for i in trailends:
        check_surrounding(i,i,9)
    for j in trailheads.values():
        count += len(j)
    return count

def part2():
    count = 0
    for i in trailheads2.values():
        count += len(i)
    return count

if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')