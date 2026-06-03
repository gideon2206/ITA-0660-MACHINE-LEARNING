import math

data = [
    [2,4,'A'],
    [4,6,'A'],
    [4,4,'B'],
    [6,2,'B']
]

test = [5,3]
k = 3

distances = []

for row in data:
    dist = math.sqrt((row[0]-test[0])**2 +
                     (row[1]-test[1])**2)
    distances.append((dist,row[2]))

distances.sort()

neighbors = distances[:k]

countA = 0
countB = 0

for n in neighbors:
    if n[1] == 'A':
        countA += 1
    else:
        countB += 1

if countA > countB:
    result = 'A'
else:
    result = 'B'

print("Classified as:", result)
