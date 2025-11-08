This project demonstrates simple unit testing for add() and subtract() functions using Python’s built-in unittest framework.

Project Structure
calculator.py          # Core logic
test_calculator.py     # Unit tests

Setup & Run

Clone or copy the project.

Run the tests using:

python -m unittest test_calculator.py

Tests Covered

add()

Handles positive, negative, and float values.

Raises TypeError for invalid inputs (e.g., strings, None).

subtract()

Handles normal and edge cases.

Validates input types.

Why Unit Tests Matter

Skipping tests can cause:

Undetected logic or validation bugs.

Unexpected failures after future code changes.

Loss of confidence in refactoring and deployment.