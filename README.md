# Assignment 2: Module 3 - Control Structures in Python

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

## 📚 Overview

This repository contains Python programs demonstrating fundamental **control structures** — the building blocks of programming logic. These examples are designed for beginners learning Python.

---

## 📋 Assignment Tasks

### Task 1: Check if a Number is Even or Odd
**File:** `even_odd_checker.py`

**Problem Statement:**
1. Takes an integer input from the user
2. Checks whether the number is even or odd using an if-else statement
3. Displays the result accordingly

### Task 2: Sum of Integers from 1 to 50 Using a Loop
**File:** `sum_calculator.py`

**Problem Statement:**
1. Uses a for loop to iterate over numbers from 1 to 50
2. Calculates the sum of all integers in this range
3. Displays the final sum

---

## 🎯 Learning Objectives

After completing these exercises, you will understand:

- ✅ How to use `if-else` statements for decision making
- ✅ How to use `for` loops for iteration
- ✅ How to handle user input with error checking
- ✅ How to use the modulo operator (`%`) for mathematical operations

---

## 📁 Project Structure

```
python-control-structures-assignment2/
│
├── even_odd_checker.py    # Task 1: Check if a number is even or odd
├── sum_calculator.py      # Task 2: Calculate sum of numbers 1 to 50
└── README.md              # This documentation file
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your computer
- A terminal or command prompt
- A text editor or IDE (VS Code recommended)

### Running the Programs

#### Task 1: Even or Odd Checker

```bash
python even_odd_checker.py
```

**Sample Output:**
```
========================================
    EVEN OR ODD CHECKER
========================================

Please enter an integer: 7

✓ The number 7 is ODD.
  Explanation: 7 ÷ 2 = 3 with remainder 1

========================================
Program finished. Thank you!
========================================
```

#### Task 2: Sum Calculator

```bash
python sum_calculator.py
```

**Sample Output:**
```
==================================================
    SUM CALCULATOR: Numbers from 1 to 50
==================================================

Calculating the sum step by step:
--------------------------------------------------
  After adding 10: Running total = 55
  After adding 20: Running total = 210
  After adding 30: Running total = 465
  After adding 40: Running total = 820
  After adding 50: Running total = 1275
--------------------------------------------------

✓ RESULT: The sum of numbers from 1 to 50 is: 1275

📝 Verification using formula: n×(n+1)/2 = 50×51/2 = 1275
   ✓ Both methods give the same answer!

==================================================
Program finished. Thank you!
==================================================
```

---

## 📖 Concepts Explained

### 1. If-Else Statements

```python
if condition:
    # Code runs if condition is TRUE
else:
    # Code runs if condition is FALSE
```

**Used in:** `even_odd_checker.py` to determine if a number is even or odd.

### 2. For Loops

```python
for variable in range(start, end):
    # Code repeats for each value
```

**Used in:** `sum_calculator.py` to iterate through numbers 1 to 50.

### 3. Modulo Operator (%)

The `%` operator returns the remainder of division:
- `10 % 2 = 0` (10 is even)
- `7 % 2 = 1` (7 is odd)

### 4. Error Handling

```python
try:
    # Code that might cause an error
except ValueError:
    # Code to handle the error gracefully
```

---

## ✅ Features

- Clean, beginner-friendly code with meaningful comments
- Error handling for invalid user input
- Clear output formatting
- Mathematical verification in sum calculator

---

## 📝 Reference

Python Course - Module 3: Control Structures in Python

---

## 👤 Author

**Student Assignment**  
Module 3: Control Structures in Python

---

*Happy Coding! 🐍*
