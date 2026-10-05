```markdown id="02yn2v"
# Playwright QA Automation

UI automation project built with **Python**, **Pytest**, and **Playwright**.

The project is based on the SauceDemo test website and is used to practice and demonstrate QA Automation skills.

## Tech Stack

- Python
- Pytest
- Playwright
- Page Object Model
- Parametrization
- Pytest Fixtures

## Project Structure

```text
project_QA/
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── pytest.ini
├── requirements.txt
└── README.md
```

## Covered Scenarios

### Login
- Successful login
- Invalid password
- Locked out user

### Inventory
- Inventory page validation
- Product card validation
- Add product to cart

### Cart
- Open cart
- Verify product in cart
- Remove product from cart
- Verify empty cart

### Checkout
- Successful checkout
- Checkout form validation
- Missing first name
- Missing last name
- Missing postal code
- Verify checkout overview
- Complete order

## Installation

Clone the repository:

```bash
git clone https://github.com/DiabloDonych/playwright-qa.git
cd playwright-qa
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browser:

```bash
playwright install chromium
```

## Running Tests

Run all tests:

```bash
pytest
```

Run tests with detailed output:

```bash
pytest -v
```

Run tests in headed mode:

```bash
pytest --headed
```

Run a specific test:

```bash
pytest tests/test_cart.py::test_cart -v
```

## Test Website

SauceDemo:

```text
https://www.saucedemo.com/
```

## Project Goal

The goal of this project is to build practical QA Automation skills and gradually develop a clean and maintainable Playwright test framework using the Page Object Model.
```
