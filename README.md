# A01796556_A5.2

Activity 5.2 – Programming Exercise 2 and Static Analysis  
Course: Software Testing and Quality Assurance  

Author: Israel Agustin Vargas Monroy
Student ID: A01796556  

---

## Project Description

This project implements the program `computeSales.py`, which:

1. Reads a JSON file containing a product price catalogue (`title`, `price`).
2. Reads a JSON file containing sales records (`Product`, `Quantity`).
3. Computes the total sales cost.
4. Handles invalid or missing data by reporting errors and continuing execution.
5. Prints the results to the console.
6. Saves the results to `SalesResults.txt`.
7. Reports execution time.
8. Follows the PEP-8 coding standard.
9. Produces no errors with flake8 or pylint.
10. Includes automated test cases using pytest.

---

## Project Structure


A01796556_A5.2/
│
├── computeSales.py
├── requirements.txt
├── README.md
├── .gitignore
├── .flake8
├── .pylintrc
│
├── data/
│ ├── TC1.ProductList.json
│ ├── TC1.Sales.json
│ ├── TC2.Sales.json
│ └── TC3.Sales.json
│
├── tests/
│ └── test_compute_sales.py
│
└── evidence/
├── flake8.txt
├── pylint.txt
└── run_tc1_tc2_tc3.txt


---

## Requirements

- Python 3.10 or higher
- pip

---

## Environment Setup (Mac)

### 1. Create virtual environment


python3 -m venv .venv


### 2. Activate virtual environment


source .venv/bin/activate


### 3. Install dependencies


pip install -r requirements.txt


---

## Program Execution

Example using TC1:


python computeSales.py data/TC1.ProductList.json data/TC1.Sales.json


The program will:

- Print the total cost to the console.
- Generate the file `SalesResults.txt`.

---

## Running Tests


pytest -q


All three test cases must pass successfully:

- TC1
- TC2
- TC3

---

## Static Analysis

### Flake8


flake8 .


### Pylint


pylint computeSales.py


The project must produce no errors.

Static analysis and execution logs are documented in the `evidence/` folder.

---

## Expected Results

| Test Case | Expected Total |
|-----------|----------------|
| TC1       | 2481.86        |
| TC2       | 166568.23      |
| TC3       | 165235.37      |

---

## Concepts Applied

- Dynamic testing (pytest)
- Static testing (flake8, pylint)
- PEP-8 coding standard
- Exception handling
- Modular design and separation of concerns
- Execution time measurement

---

## Commit History

The repository contains multiple commits demonstrating development history:

- Project initialization
- Core implementation
- Test implementation
- Static analysis configuration
- Style corrections
- Final documentation and evidence