
# Calculator Project (Python)

A simple command-line calculator application built in Python with full unit test coverage and an automated CI/CD pipeline using GitHub Actions.

---

## 🚀 Features

* Supports basic arithmetic operations:

  * Addition
  * Subtraction
  * Multiplication
  * Division
* Interactive command-line REPL (Read–Eval–Print Loop)
* Handles exceptions:

  * Division by zero
  * Invalid user input
* 100% unit test coverage using **pytest**
* Continuous Integration (CI) with **GitHub Actions**

---

## 🛠️ Technologies Used

* Python 3.12
* Pytest
* Pytest-Cov
* GitHub Actions (CI/CD)

---

## 📁 Project Structure

```
week3_calculator/
├── calculator/
│   ├── __init__.py
│   ├── operations.py
│   └── repl.py
├── tests/
│   ├── test_operations.py
│   └── test_repl.py
├── .github/
│   └── workflows/
│       └── python-app.yml
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd week3_calculator
```

2. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Calculator

```bash
python -m calculator.repl
```

Example:

```
Welcome to Calculator
Operations: add, sub, mul, div, exit
Enter operation: add
Enter first number: 10
Enter second number: 5
Result: 15
```

---

## 🧪 Run Tests with Coverage

```bash
pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100
```

This ensures:

* All tests pass
* 100% code coverage is maintained

---

## 🔁 CI/CD Pipeline (GitHub Actions)

This project uses GitHub Actions to automatically:

* Install dependencies
* Run all tests
* Enforce 100% test coverage on every push and pull request

Workflow file:

```
.github/workflows/python-app.yml
```

---

## 📌 Requirements

Listed in `requirements.txt`:

* pytest
* pytest-cov

---

## 📄 License

This project is for educational purposes.

---

## 👨‍💻 Author

**Lohiteesh Reddy Bommareddy**
Master’s Student in Data Science
New Jersey Institute of Technology (NJIT)
