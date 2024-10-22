# SauceDemo Test

This project contains an automated test scenario for the SauceDemo website using Selenium and Python.

## Prerequisites

- Python 3.x installed
- Selenium WebDriver library installed (`pip install selenium`)
- Chrome WebDriver executable installed and in the system PATH

## Setup

1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command:pip install -r requirements.txt
3. Activate the virtual environment: source venv/bin/activate  # On Windows: venv\Scripts\activate
4. Download the WebDriver:For Chrome, download from ChromeDriver. 
5. Place the chromedriver executable in the drivers/ directory.
6. Navigate to tests directory and update the reports path in pytest.ini file
7. Run the tests from tests directory


## Test Scenarios

The various test scenarios covering critical features of the web application are as below: 

1. Create a browser instance and set up the test environment as part of precondition in all the tests.
2. Open the login page and verify the Swag Labs logo.
3. Login with valid credentials.
4. Login with invalid credentials.
5. Login from locked out user.
6. Logout functionality.
7. Product listing checks.
8. Product filtering options verification.
9. Product search verification.
10. Navigate to the product detail page and verify the product name.
11. Add the item to the cart and verify the "Remove" button.
12. Navigate to the shopping cart page and verify the item in the cart.
13. Validate empty shopping cart navigation.
14. Continue with the checkout process and verify the checkout page.
15. Enter valid checkout information.
16. Validate with invalid checkout field values.
17. Confirmation of product total price in summary matches the cart total price.
18. Proceed to the confirmation page and verify the item in the overview.
19. Logout from the website.
20. Tear down the test environment.

## Running all the Tests
 pytest 

## Running individual Test
 pytest <test_name.py>

- The test will be executed with the provided test data (username and password). Entire test results are store in reports/ directory