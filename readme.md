Simple Arithmetic Unit Testing Demo
This project demonstrates clean, effective unit testing for basic arithmetic operations — add() and subtract() — using Python's built-in unittest framework.

Project Structure
text
calculator.py        # Core logic (add & subtract functions)
test_calculator.py   # Comprehensive unit tests
Setup & Run
Clone or copy the project files

Ensure you have Python 3.6+ installed

Run the tests:

bash
python -m unittest test_calculator.py -v
Note: The -v flag enables verbose output to see each test result clearly.

Tests Covered
add(a, b)
Handles positive, negative, and zero values

Supports large integers (10¹⁸) and floating-point numbers

Raises TypeError for invalid inputs:

Strings ("3")

None values

Mixed types (int + str)

➖ subtract(a, b)
Covers normal, zero, and negative scenarios

Validates large number cancellation and extreme differences

Enforces input validation with TypeError on invalid types

Ques:-Why Unit Tests Matter?
Answer:-
Risk of Skipping Tests	Consequence
Undetected Bugs	Logic errors (e.g., off-by-one) go unnoticed until production
Regression Issues	Future changes silently break working code
Slower Debugging	Bugs found late cost 10x more to fix
Security Vulnerabilities	Unchecked edge cases can lead to exploits (e.g., overflow)
Loss of Confidence	Harder to refactor, scale, or deploy reliably
Unit tests = safety net for your code
