# Problem Set 0 – MIT 6.0001: Introduction to Computer Science and Programming in Python 

## 📄 Assignment Overview
**Completed:** [8/1/25]
**Source:** https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps0/

This problem set introduces:
- The programming environment **Spyder** from the Anaconda distribution of Python
- Python basics: printing, reading user input, variables
- Simple math operations including exponentiation and logarithms
- The general **MIT 6.0001 problem set structure**

---

## 📝 Original Assignment Summary

You will:
1. Confirm your Python and Spyder installation (Python 3.5+).
2. Familiarize yourself with Spyder using exercises from the *Getting Started* handout.
3. Write a Python program (`ps0.py`) that:
   - Prompts the user to enter a number `x`
   - Prompts the user to enter a number `y`
   - Prints `x` raised to the power `y`
   - Prints the base-2 logarithm of `x`

**Example interaction:**
  Enter number x: 2
  Enter number y: 3
  X**y = 8
  log(x) = 1
  
---

## 💡 Hints from the Assignment
- Use the `print()` function to display results.
- Use the `input()` function to read values from the user.
- Convert inputs to integers with `int()` (or floats with `float()`).
- Use `numpy.log2()` for the base-2 logarithm (after importing numpy).
- Store results in variables to reuse values.
- Remember that in Python 3 you should use `input()` instead of `raw_input()`.

---

## ✅ What I Did
- Created `ps0.py` in Spyder.
- Imported `numpy` to use the `log2()` function.
- Converted input strings to numbers using `float()`.
- Stored intermediate results in variables for clarity.
- Tested with multiple values of `x` and `y` to confirm outputs match expectations.

---

## 📂 Files in This Folder
- **`ps0.py`** – My solution code for Problem Set 0.
- **`README.md`** – This file, summarizing the problem set and my approach.

---

## 🖥️ How to Run
1. Open a terminal (or use Spyder’s console).
2. Navigate to the `ps0` folder:
   ```bash
     cd ps0
3. Run the program
   ```bash
     python ps0.py
4. Follow the prompts to enter numbers.


---


   
