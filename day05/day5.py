from aocd import get_data
ruleslist,updateslist = get_data(day=5, year=2024).split("\n\n")

rules = ruleslist.splitlines()
updates = updateslist.splitlines()

rulesorder = {}

for rule in rules:
    before, after = rule.split('|')
    before, after = int(before), int(after)
    if before in rulesorder:
        rulesorder[before].append(after)
    else:
        rulesorder[before] = [after]

def makevalid(numberlist, newline):
    if not numberlist:
        return newline
    for i in numberlist:
        workinglist = [x for x in numberlist if x != i]
        if i in rulesorder:
            if all(x in rulesorder[i] for x in workinglist):
                newline.append(i)
                return(makevalid(workinglist,newline))
        elif len(numberlist) == 1:
            newline.append(i)
            return(makevalid(workinglist,newline))
  
def handler():
    validcount = 0
    invalidcount = 0
    for update in updates:
        numberlist = [int(x) for x in update.split(',')]
        valid = True
        for index, value in enumerate(numberlist):
            if value in rulesorder:
                for i in rulesorder[value]:
                    if i not in numberlist[0:index]:    
                        pass
                    else:
                        valid = False
                        break
        middle = int((len(numberlist)+1)/2)-1
        if valid:
            validcount += numberlist[middle]
        if not valid:
            invalidcount += makevalid(numberlist,[])[middle]
    return (validcount,invalidcount)

if __name__ == "__main__":
    results = handler()
    print(f"Part 1: {results[0]}")
    print(f"Part 2: {results[1]}")