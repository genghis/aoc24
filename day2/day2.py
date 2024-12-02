from aocd import get_data
dataset = get_data(day=2, year=2024).splitlines()

def handler(part):
    safe = 0
    for i in dataset:
        report = [int(x) for x in i.split()]
        safe += safecheck(report, part)
    print(safe)
    
def safecheck(report,rerun):
    safechecklist = [x[0]-x[1] for x in zip(report[0::],report[1::])]
    if all(4 > x > 0 for x in safechecklist) or all(0 > x > -4 for x in safechecklist):
        return 1
    elif rerun == False:
        for i in range(len(report)):
            newreport = list(report)
            del newreport[i]
            if safecheck(newreport, True):
                return 1
        return 0
    else:
        return 0

if __name__ == "__main__":
    handler(True) #runs part 1
    handler(False) #runs part 2