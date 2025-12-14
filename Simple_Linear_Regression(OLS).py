# Ordinary Least Squares (Simple Linear Regression) 
n = int(input("Enter number of data points: "))

x = []
y = []

for i in range(n):
    x.append(float(input(f"Enter x{i+1}: ")))
    y.append(float(input(f"Enter y{i+1}: ")))

x_mean = sum(x) / n
y_mean = sum(y) / n

numerator = 0
denominator = 0

for i in range(n):
    numerator += (x[i] - x_mean) * (y[i] - y_mean)
    denominator += (x[i] - x_mean) ** 2

m = numerator / denominator
b = y_mean - m * x_mean

print("\nSlope (m):", m)
print("Intercept (b):", b)
print("Final OLS Regression Equation:")
print(f"ŷ = {round(m,2)}x + {round(b,2)}")
