import numpy as np

def multiple_linear_regression(X, Y):
    X = np.insert(X, 0, 1, axis=1)
    XT = X.T

    beta = np.linalg.pinv(XT @ X) @ XT @ Y

    print("\nIntercept:", round(beta[0], 2))
    for i in range(1, len(beta)):
        print(f"b{i}:", round(beta[i], 2))

    print("\nFinal Regression Equation:")
    eq = "y = "
    for i in range(1, len(beta)):
        eq += f"{round(beta[i],2)}x{i} + "
    print(eq[:-3])  

n = int(input("Enter number of observations: "))
k = int(input("Enter number of independent variables: "))

X = []
Y = []

print("\nEnter X values:")
for i in range(n):
    row = []
    for j in range(k):
        row.append(float(input(f"X{i+1}{j+1}: ")))
    X.append(row)

print("\nEnter Y values:")
for i in range(n):
    Y.append(float(input(f"Y{i+1}: ")))

X = np.array(X)
Y = np.array(Y)

multiple_linear_regression(X, Y)
