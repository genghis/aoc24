from aocd import get_data
dataset = get_data(day=4, year=2024).splitlines()

def get_up(ycoord, xcoord):
    return ("up", ycoord-1, xcoord, dataset[ycoord-1][xcoord])

def get_down(ycoord,xcoord):
    return ("down", ycoord+1, xcoord, dataset[ycoord+1][xcoord])

def get_left(ycoord,xcoord):
    return ("left", ycoord, xcoord-1, dataset[ycoord][xcoord-1])

def get_right(ycoord,xcoord):
    return ("right", ycoord, xcoord+1, dataset[ycoord][xcoord+1])

def get_up_left(ycoord,xcoord):
    return ("up_left", ycoord-1, xcoord-1, dataset[ycoord-1][xcoord-1])

def get_up_right(ycoord,xcoord):
    return ("up_right", ycoord-1, xcoord+1, dataset[ycoord-1][xcoord+1])

def get_down_left(ycoord,xcoord):
    return ("down_left", ycoord+1, xcoord-1, dataset[ycoord+1][xcoord-1])

def get_down_right(ycoord,xcoord):
    return ("down_right", ycoord+1, xcoord+1, dataset[ycoord+1][xcoord+1])

def get_surrounding(ycoord,xcoord):
    results = []
    if ycoord == 0 and xcoord == 0:
        results.extend([get_right(0,0), get_down(0,0), get_down_right(0,0)])
    elif ycoord == 0 and xcoord == len(dataset[0])-1:
        results.extend([get_left(ycoord,xcoord), get_down_left(ycoord, xcoord), get_down(ycoord, xcoord)])
    elif ycoord == len(dataset)-1 and xcoord == 0:
        results.extend([get_up(ycoord,xcoord), get_up_right(ycoord,xcoord), get_right(ycoord, xcoord)])
    elif ycoord == len(dataset)-1 and xcoord == len(dataset[0])-1:
        results.extend([get_left(ycoord, xcoord), get_up_left(ycoord, xcoord), get_up(ycoord,xcoord)])
    elif ycoord == 0:
        results.extend([get_left(ycoord,xcoord), get_down_left(ycoord, xcoord), get_down(ycoord, xcoord), get_down_right(ycoord,xcoord), get_right(ycoord,xcoord)])
    elif ycoord == len(dataset)-1:
        results.extend([get_left(ycoord,xcoord), get_up_left(ycoord, xcoord), get_up(ycoord, xcoord), get_up_right(ycoord,xcoord), get_right(ycoord,xcoord)])
    elif xcoord == 0:
        results.extend([get_up(ycoord,xcoord), get_up_right(ycoord,xcoord), get_down(ycoord, xcoord), get_down_right(ycoord,xcoord), get_right(ycoord,xcoord)])
    elif xcoord == len(dataset[0])-1:
        results.extend([get_up(ycoord,xcoord), get_up_left(ycoord,xcoord), get_down(ycoord, xcoord), get_down_left(ycoord,xcoord), get_left(ycoord,xcoord)])
    else:
        results.extend([get_up(ycoord,xcoord), get_up_right(ycoord,xcoord), get_down(ycoord, xcoord), get_down_right(ycoord,xcoord), get_right(ycoord,xcoord), get_left(ycoord,xcoord), get_up_left(ycoord,xcoord), get_down_left(ycoord,xcoord)])
    return results

def check_direction(payload):
    match payload[0]:
        case "left":
            if payload[2] != 0:
                return get_left(payload[1],payload[2])
        case "right":
            if payload[2] != len(dataset[0])-1:
                return get_right(payload[1],payload[2])
        case "up":
            if payload[1] != 0:
                return get_up(payload[1],payload[2])
        case "down":
            if payload[1] != len(dataset)-1:
                return get_down(payload[1],payload[2])
        case "up_left":
            if payload[1] != 0 and payload[2] != 0:
                return get_up_left(payload[1],payload[2])
        case "up_right":
            if payload[1] != 0 and payload[2] != len(dataset[0])-1:
                return get_up_right(payload[1],payload[2])
        case "down_right":
            if payload[1] != len(dataset)-1 and payload[2] != len(dataset[0])-1:
                return get_down_right(payload[1],payload[2])
        case "down_left":
            if payload[1] != len(dataset)-1 and payload[2] != 0:
                return get_down_left(payload[1],payload[2])
    return ("Nope", "Nope", "Nope", "Nope")

def get_x(ycoord, xcoord):
    up_left = get_up_left(ycoord,xcoord)[3]
    up_right = get_up_right(ycoord,xcoord)[3]
    down_left = get_down_left(ycoord,xcoord)[3]
    down_right = get_down_right(ycoord,xcoord)[3]
    if up_left == "M" and down_right == "S":
        if (up_right == "S" and down_left == "M") or (up_right == "M" and down_left == "S"):
            return True
    if up_left == "S" and down_right == "M":
        if (up_right == "S" and down_left == "M") or (up_right == "M" and down_left == "S"):
            return True
    else:
        return False
    

def part1():
    count = 0
    for ycoord, row in enumerate(dataset):
        for xcoord, character in enumerate(row):
            if character == "X":
                surrounding = get_surrounding(ycoord, xcoord)
                for i in surrounding:
                    if i[3] == "M":
                        j = check_direction(i)
                        if j[3] == "A":
                            k=check_direction(j)
                            if k[3] == "S":
                                count+=1
    return count
                        
def part2():
    count = 0
    for ycoord, row in enumerate(dataset):
        for xcoord, character in enumerate(row):
            if character == "A" and ycoord != 0 and ycoord != len(dataset)-1 and xcoord != 0 and xcoord != len(dataset[0])-1:
                if get_x(ycoord,xcoord):
                    count += 1
    return count
                

if __name__ == "__main__":
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')