# from aocd import get_data
# ruleslist,updateslist = get_data(day=5, year=2024).split("\n\n")

ruleslist, updateslist = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''.split("\n\n")

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

def makevalid(numberlist):
    newline = numberlist.copy()
    for index, value in enumerate(numberlist):
            if value in rulesorder:
                for i in rulesorder[value]:
                    if i in numberlist[0:index]:
                        if value in newline:
                            newline.remove(value)
                        offenderlocation = numberlist.index(i)
                        newline.insert(offenderlocation-1, value)
            else:
                if value not in newline:
                    newline.insert(-1, value)
    print(newline)
    return newline

def part1():
    count = 0

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
        if valid:
            middle = int((len(numberlist)+1)/2)-1
            count += numberlist[middle]

    return count

def part2():
    count = 0
    invalidlines = []
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
        if not valid:
            middle = int((len(numberlist)+1)/2)-1
            count += makevalid(numberlist)[middle]
    return count
                    
            
if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")