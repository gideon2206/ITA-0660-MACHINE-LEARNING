import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

x1 = 2
x2 = 3

w1 = 0.5
w2 = 0.8
bias = -1

z = (x1 * w1) + (x2 * w2) + bias

output = sigmoid(z)

print("Sigmoid Output =", output)

if output >= 0.5:
    print("Class = 1")
else:
    print("Class = 0")
