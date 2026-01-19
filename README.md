# ML_CLASS_WORK

This repository contains **implementations of supervised learning regression algorithms** in Python.  
All algorithms are implemented using their **original mathematical formulas**, without using machine learning libraries such as `scikit-learn`.

---

## 📘 Algorithms Implemented

---

## 1️⃣ Simple Linear Regression (Ordinary Least Squares – OLS)

**File:** `Simple_Linear_Regression(OLS).py`

### 📌 Model
\[
\hat{y} = mx + b
\]

### 📐 OLS Formulas
\[
m = \frac{\sum (x - \bar{x})(y - \bar{y})}{\sum (x - \bar{x})^2}
\]

\[
b = \bar{y} - m\bar{x}
\]

### 🎯 Objective
Minimize the **sum of squared errors**:
\[
\sum (y - \hat{y})^2
\]

---

## 2️⃣ Multiple Linear Regression (OLS – Formula Method)

**File:** `Multiple_Linear_Regression(OLS).py`

### 📌 Model
\[
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2
\]

### 📐 OLS Coefficient Formulas

\[
\beta_1 =
\frac{
(\sum x_2^2)(\sum x_1 y) - (\sum x_1 x_2)(\sum x_2 y)
}{
(\sum x_1^2)(\sum x_2^2) - (\sum x_1 x_2)^2
}
\]

\[
\beta_2 =
\frac{
(\sum x_1^2)(\sum x_2 y) - (\sum x_1 x_2)(\sum x_1 y)
}{
(\sum x_1^2)(\sum x_2^2) - (\sum x_1 x_2)^2
}
\]

\[
\beta_0 = \bar{y} - \beta_1 \bar{x}_1 - \beta_2 \bar{x}_2
\]

---

## 3️⃣ Multiple Linear Regression (Matrix / Normal Equation Method)

**File:** `Multiple_Linear_Regression(Matrix).py`

### 📌 Model
\[
y = X\beta
\]

### 📐 Normal Equation
\[
\beta = (X^T X)^{-1} X^T y
\]

### ⚠️ Note
To avoid singular matrix errors, the **Moore–Penrose Pseudoinverse** is used:
\[
\beta = (X^T X)^{+} X^T y
\]

---

## 4️⃣ Gradient Descent for Linear Regression

**File:** `Gradient_Descent.py`

### 📌 Model
\[
\hat{y} = mx + b
\]

### 📉 Cost Function (Mean Squared Error)
\[
J(m,b) = \frac{1}{n}\sum (y - \hat{y})^2
\]

### 🔁 Update Rules
\[
m = m - \alpha \left(-\frac{2}{n}\sum x(y - \hat{y})\right)
\]

\[
b = b - \alpha \left(-\frac{2}{n}\sum (y - \hat{y})\right)
\]

Where:
- \(\alpha\) = learning rate  
- \(n\) = number of data points  

---
