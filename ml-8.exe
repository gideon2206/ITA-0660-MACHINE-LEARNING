x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

n = len(x)

mx = sum(x)/n
my = sum(y)/n

num = sum((x[i]-mx)*(y[i]-my) for i in range(n))
den = sum((x[i]-mx)**2 for i in range(n))

m = num/den
c = my - m*mx

print("Slope =", m)
print("Intercept =", c)

x_new = 6
y_pred = m*x_new + c

print("Predicted Value =", y_pred)
