# OLS for two independent variables 
n = int(input("Enter number of observations: "))

x1 = []
x2 = []
y = []

for i in range(n):
    x1.append(float(input(f"x1_{i+1}: ")))
    x2.append(float(input(f"x2_{i+1}: ")))
    y.append(float(input(f"y_{i+1}: ")))

x1_bar = sum(x1) / n
x2_bar = sum(x2) / n
y_bar = sum(y) / n

sum_x1y = sum(x1[i] * y[i] for i in range(n))
sum_x2y = sum(x2[i] * y[i] for i in range(n))
sum_x1x2 = sum(x1[i] * x2[i] for i in range(n))
sum_x1_sq = sum(x1[i] ** 2 for i in range(n))
sum_x2_sq = sum(x2[i] ** 2 for i in range(n))

D = (sum_x1_sq * sum_x2_sq) - (sum_x1x2 ** 2)

beta1 = (sum_x2_sq * sum_x1y - sum_x1x2 * sum_x2y) / D
beta2 = (sum_x1_sq * sum_x2y - sum_x1x2 * sum_x1y) / D
beta0 = y_bar - beta1 * x1_bar - beta2 * x2_bar

print("\nRegression Coefficients:")
print("β0 =", round(beta0, 2))
print("β1 =", round(beta1, 2))
print("β2 =", round(beta2, 2))

print("\nFinal Regression Equation:")
print(f"y = {round(beta0,2)} + {round(beta1,2)}x1 + {round(beta2,2)}x2")
