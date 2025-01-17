# my-calculator
# JSON History Calculator

This is a calculator program that saves and manages calculation history using a JSON file. It allows users to perform basic mathematical operations and store the results for future reference. You can clear the history, read past calculations, or continue calculations using previous results.

## Features

- Save calculation history to a JSON file
- Read the calculation history from a JSON file
- Clear the calculation history
- Support for basic mathematical operations including addition, subtraction, multiplication, division, modulus, power, square root, and Euclidean division
- The ability to continue a calculation using the result of the previous calculation

## Functions

### 1. `save_history_log(nb1, nb2, ope, result)`

This function saves the calculation history to a JSON file.

- **Arguments**:
    - `nb1`: First number in the calculation
    - `nb2`: Second number in the calculation
    - `ope`: Operator used in the calculation (represented by a number)
    - `result`: Result of the calculation

### 2. `read_history_log()`

This function reads and displays the calculation history from the JSON file.

### 3. `clear_history_log()`

This function clears the calculation history stored in the JSON file.

### 4. `calculator_menu()`

The main menu function that allows users to choose between:
- Clearing the history
- Reading the history
- Performing calculations

### 5. `operator(flag, int_and_float)`

This function prompts the user to choose an operator and provides an option to calculate with integers or floating-point numbers.

### 6. `calc(nb1, nb2, ope, result, flag3, flag, int_and_float)`

The function that performs the calculation and allows the user to continue with further calculations using the result of the previous one.

## Installation

1. Download or clone this repository to your local machine.
2. Ensure that Python 3.x is installed on your machine.
3. Run the script using a Python interpreter:
   ```bash
   python calculator.py
  ```
---

