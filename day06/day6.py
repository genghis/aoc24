from aocd import get_data
from pprint import pprint

dataset = get_data(day=6, year=2024).splitlines()
# pprint(dataset)
# dataset = '''....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...'''.splitlines()

firstgrid = [list(x) for x in dataset]

for index, value in enumerate(dataset):
    if '^' in value:
        ycoord = index
        xcoord = value.index('^')
        startingpoint = (ycoord,xcoord)

xboundary = len(dataset[0])-1
yboundary = len(dataset)-1

def next_loc(currenty, currentx, direction, grid):
    currenty, currentx = currenty, currentx
    match direction:
            case "u":
                nextloc = (currenty-1, currentx)
                nextdir = "r"
            case "r":
                nextloc = (currenty, currentx+1)
                nextdir = "d"
            case "d":
                nextloc = (currenty+1, currentx)
                nextdir = "l"
            case "l":
                nextloc = (currenty, currentx-1)
                nextdir = "u"

    if 0 <= nextloc[0] <= xboundary and 0 <= nextloc[1] <= yboundary and grid[nextloc[0]][nextloc[1]] == "#":
        return(next_loc(currenty, currentx, nextdir, grid))
    return(nextloc[0], nextloc[1], direction)

def run_grid(grid):
    locs = set()
    currenty = startingpoint[0]
    currentx = startingpoint[1]
    direction = "u"
    while 0 <= currentx <= xboundary and 0 <= currenty <= yboundary:
        locs.add((currenty,currentx))
        currenty, currentx, direction = next_loc(currenty, currentx, direction, grid)
    return(locs)

def find_loop(grid):
    currenty = startingpoint[0]
    currentx = startingpoint[1]
    direction = "u"
    locs = []
    while 0 <= currentx <= xboundary and 0 <= currenty <= yboundary:
        locs.append((currenty, currentx, direction))
        currenty, currentx, direction = next_loc(currenty, currentx, direction, grid)
        if (currenty, currentx, direction) in locs:
            return True
    return False

def part1():
    return len(run_grid(firstgrid))
    
def part2():
    loops = 0
    locs = [x for x in run_grid(firstgrid) if x != (startingpoint)]

    for i in locs:
        newgrid = [list(x) for x in dataset]
        newgrid[i[0]][i[1]] = "#"
        loop = find_loop(newgrid)
        if loop:
            loops += 1
    return loops
    
if __name__ == "__main__":
    pprint(f"Part 1: {part1()}")
    pprint(f"Part 2: {part2()}")