import math

data = [
    [5.1,3.5,'Setosa'],
    [4.9,3.0,'Setosa'],
    [6.2,3.4,'Versicolor'],
    [6.5,3.0,'Virginica']
]

test = [5.0,3.4]

distances = []

for row in data:
    d = math.sqrt((row[0]-test[0])**2 +
                  (row[1]-test[1])**2)
    distances.append((d,row[2]))

distances.sort()

print("Predicted Class:", distances[0][1])
