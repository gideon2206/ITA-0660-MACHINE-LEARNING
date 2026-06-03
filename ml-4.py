import numpy as np

X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

Y = np.array([[0],[1],[1],[0]])

weights = np.random.rand(2,1)

for i in range(1000):
    output = 1/(1+np.exp(-np.dot(X,weights)))

    error = Y - output

    weights += np.dot(X.T,error)*0.1

print("Output:")
print(output)
