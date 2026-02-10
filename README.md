# Calculator Project (Python)

A simple calculator application built in Python with full unit test coverage and CI/CD pipeline using GitHub Actions.

##  Features
- Add, subtract, multiply, and divide operations
- Command-line REPL interface
- Exception handling (division by zero, invalid input)
- 100% test coverage with pytest
- Automated CI/CD using GitHub Actions

## Project Structure
week3_calculator/
├── calculator/
│ ├── init.py
│ ├── operations.py
│ └── repl.py
├── tests/
│ ├── test_operations.py
│ └── test_repl.py
├── .github/
│ └── workflows/
│ └── python-app.yml
├── README.md
└── requirements.txt
