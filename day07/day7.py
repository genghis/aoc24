from aocd import get_data
dataset = get_data(day=7, year=2024).splitlines()

# dataset = '''190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20'''.splitlines()

def evaluate(preceding, numbers):
    results = []
    print(len(numbers))
    for i in preceding:
        results.append(i*numbers[0])
        results.append(i+numbers[0])
    if len(numbers) > 1:
        return evaluate(results, numbers[1:]) 
    return results

def part1():
    count = 0
    for i in dataset:
        test_value, equation = i.split(": ")
        test_value = int(test_value)
        numbers = [int(x) for x in equation.split()]
        results = evaluate([numbers[0]], numbers[1:])
        if test_value in results:
            count += test_value
    return count

if __name__ == "__main__":
    print(f'Part 1: {part1()}')