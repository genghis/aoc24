from aocd import get_data
import re
dataset = get_data(day=3, year=2024)
multmatch = re.compile(r'(?:mul\()\d{1,3}[,]\d{1,3}\)')

def part1():
    instructions = multmatch.findall(dataset)
    count = 0
    count += chop_and_mult(instructions)
    return count

def part2():
    count = 0
    dos = dataset.split("do()")
    for i in dos:
        realdos = i.split("don't()")
        instructions = multmatch.findall(realdos[0])
        count += chop_and_mult(instructions)
    return count

def chop_and_mult(instructions):
    count = 0
    for i in instructions:
        nums = i[4:-1]
        num1,num2 = nums.split(',')
        count += int(num1)*int(num2)
    return count

if __name__ == '__main__':
    print("Part 1: " + str(part1()))
    print("Part 2: " + str(part2()))