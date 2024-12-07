from aocd import get_data
dataset = get_data(day=7, year=2024).splitlines()

def evaluate(preceding, numbers, concats):
    results = []
    for i in preceding:
        results.append(i*numbers[0])
        results.append(i+numbers[0])
        if concats:
            results.append(int(str(i)+str(numbers[0])))
    if len(numbers) > 1:
        return evaluate(results, numbers[1:], concats) 
    return results

def handler(concats):
    count = 0
    for i in dataset:
        test_value, equation = [int(x) if i == 0 else x for i, x in enumerate(i.split(": "))]
        numbers = [int(x) for x in equation.split()]
        results = evaluate([numbers[0]], numbers[1:], concats)
        if test_value in results:
            count += test_value
    return count

if __name__ == "__main__":
    print(f'Part 1: {handler(False)}')
    print(f'Part 2: {handler(True)}')