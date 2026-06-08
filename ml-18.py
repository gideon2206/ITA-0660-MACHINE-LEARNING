x1 = 5.1
x2 = 3.5

w1 = 0.5
w2 = 0.3
bias = -2

net = (x1*w1) + (x2*w2) + bias

if net > 0:
    print("Iris Setosa")
else:
    print("Other Iris")
