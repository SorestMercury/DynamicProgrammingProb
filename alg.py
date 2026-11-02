numbers = [[0 for i in range(100)] for j in range(100)]
pathSums = [[0 for i in range(100)] for j in range(100)]

with open("numbers.txt") as file:
    text = file.read().split()
    for x in range(len(numbers)):
        for y in range(len(numbers[0])):
            num = int(text[(x*len(numbers[0]))+y])
            numbers[x][y] = num
            pathSums[x][y] = num

#print(numbers)

for x in range(len(numbers)-2, -1, -1):
    for y in range(len(numbers[0])-1, -1, -1):
        choices = [pathSums[x+1][y]]
        if y != 0:
            choices.append(pathSums[x+1][y-1])
        if y != len(pathSums[0]) - 1:
            choices.append(pathSums[x+1][y+1])

        pathSums[x][y] = numbers[x][y] + max(choices)

print(pathSums)
        
print("\nthe maximum possible sum is " + str(max(pathSums[0])))