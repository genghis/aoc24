from aocd import get_data
dataset = get_data(day=7, year=2024).splitlines()

def evaluate(preceding, numbers):
    results = []
    for i in preceding:
        results.append(i*numbers[0])
        results.append(i+numbers[0])
    if len(numbers) > 1:
        return evaluate(results, numbers[1:]) 
    return results

def evaluate_with_concats(preceding, numbers):
    results = []
    for i in preceding:
        results.append(i*numbers[0])
        results.append(i+numbers[0])
        results.append(int(str(i)+str(numbers[0])))
    if len(numbers) > 1:
        return evaluate_with_concats(results, numbers[1:]) 
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

def part2():
    count = 0
    for i in dataset:
        test_value, equation = i.split(": ")
        test_value = int(test_value)
        numbers = [int(x) for x in equation.split()]
        results = evaluate_with_concats([numbers[0]], numbers[1:])
        if test_value in results:
            count += test_value
    return count

if __name__ == "__main__":
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')