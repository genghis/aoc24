from aocd import get_data

dataset = get_data(day=8, year=2024).splitlines()

locations = {}
ybound = len(dataset)-1
xbound = len(dataset[0])-1

for indy, row in enumerate(dataset):
    for indx, cha in enumerate(row):
        position = (indy, indx)
        if cha != '.':
            if cha not in locations:
                locations[cha] = [position,]
            else: 
                locations[cha].append(position)

def get_antinodes(locs, part):
    antinodes = set()
    for loc1 in locs:
        for loc2 in [x for x in locs if x != loc1]:
            ychange = loc1[0]-loc2[0]
            xchange = loc1[1]-loc2[1]
            currenty = loc1[0]
            currentx = loc1[1]
            if part == 2:
                while 0 <= currenty <= ybound and 0 <= currentx <= xbound:
                    antinodes.add((currenty, currentx))
                    currenty += ychange
                    currentx += xchange
            else:
                currenty += ychange
                currentx += xchange
                if 0 <= currenty <= ybound and 0 <= currentx <= xbound:
                    antinodes.add((currenty, currentx))
    return antinodes

def handler(part):
    antinodes = set()
    for frequency in locations:
        antinodes.update(get_antinodes(locations[frequency], part))
    return len(antinodes)

if __name__ == "__main__":
    print(f'Part 1: {handler(1)}')
    print(f'Part 2: {handler(2)}')