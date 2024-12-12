from aocd import get_data
dataset = get_data(day=11, year=2024).split(' ')

def rules(val):
    if int(val) == 0:
        return ['1']
    elif int(len(val))%2 == 0:
        midpoint = len(val)//2
        left = str(int(val[:midpoint]))
        right = str(int(val[midpoint:]))
        return [left,right]
    else:
        return [str(int(val)*2024)]

def blink(blinks):
    stones = {}
    for blink in range(blinks+1):
        stones[blink] = {}
    
    for i in dataset:
        stones[0][i] = 1
    
    for blink in range(blinks+1)[1:]:
        for i in stones[blink-1]:
            for j in rules(i):
                if stones[blink].get(j):
                    stones[blink][j] += 1*stones[blink-1][i]
                else:
                    stones[blink][j] = 1*stones[blink-1][i]
    return sum(stones[blinks].values())

    
if __name__ == '__main__':
    print(f'Part 1: {blink(25)}')
    print(f'Part 2: {blink(75)}')