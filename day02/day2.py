from aocd import get_data
dataset = get_data(day=2, year=2024).splitlines()

def handler(part):
    safe = 0
    for i in dataset:
        report = [int(x) for x in i.split()]
        addition = safecheck(report)
        if addition:
            safe += addition
        elif part == 2:
            for i in range(len(report)):
                newreport = list(report)
                del newreport[i]
                if safecheck(newreport):
                    safe += 1
                    break
    return safe
    
def safecheck(report):
    safechecklist = [x[0]-x[1] for x in zip(report[0::],report[1::])]
    if all(4 > x > 0 for x in safechecklist) or all(0 > x > -4 for x in safechecklist):
        return 1
    else:
        return 0

if __name__ == "__main__":
    print("Part One: " + str(handler(1))) #runs part 1
    print("Part Two: " + str(handler(2))) #runs part 2