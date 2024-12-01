data = open('input.txt').readlines()
list1 = []
list2 = []

for i in data:
    item1, item2 = i.split('   ')
    list1.append(int(item1.strip()))
    list2.append(int(item2.strip()))
    
def first():
    resultlist = []
    list1.sort()
    list2.sort()
    for index,value in enumerate(list1):
        resultlist.append(abs(value-list2[index]))
    print(sum(resultlist))

def second():
    count = 0
    valuedict = {}
    for i in set(list1):
        valuedict[i] = list2.count(i)*i
    for i in list1:
        count += valuedict[i]
    print(count)
    
if __name__ == '__main__':
    first()
    second()