# Exercise: Testing Sauce Demo Application

## Objective

The goal of this exercise is to set up a test environment for the Sauce Demo web application, run a series of automated tests, and analyze the results. The tests will cover functionalities such as login, product search, cart management, and checkout.

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

## Test Coverage

### 1. Login Functionality
#### Test: test_login_valid
- **Objective:** Verify that users can log in with valid credentials.
- **Expected Result:** Successful login redirects to the product page.

#### Test: test_login_invalid
- **Objective:** Verify that users cannot log in with invalid credentials.
- **Expected Result:** Error message displayed in the login page.

#### Test: test_login_empty_credentials
- **Objective:** Verify that users cannot log in with empty credentials.
- **Expected Result:** Error message displayed in the login page.

#### Test: test_login_locked_out_user
- **Objective:** Verify that users who are locker cannot log in.
- **Expected Result:** Failed login with appropriate error message on login page.

### 2. Logout Functionality
#### Test: test_logout
- **Objective:** Verify that users can log out by section logout menu options.
- **Expected Result:** Successful logout.

#### Test: test_logout_redirection
- **Objective:** Verify that users can logout by selection log out option from menu and redirected to login page.
- **Expected Result:** Post logout redirected to login page.


### 3. Product Search
#### Test: test_product_search
- **Objective:** Test to validate search feature.
- **Expected Result:** presence of search option and getting the right result of the product.

#### Test: test_product_no_result
- **Objective:** Verify search such that no product is listed.
- **Expected Result:** presence of search option and getting no result.


### 4. cart management
#### Test: test_add_to_cart_inventory
- **Objective:** This test add items to cart from product listing page and check the cart.
- **Expected Result:** Item found in the shopping cart page.

#### Test: test_add_to_cart_product_detail
- **Objective:** Verify  This test adds the items to card from individual product detail page and verifies the cart contents.
- **Expected Result:** Item found in the shopping cart page with remove option.

#### Test: test_cart_item_removal
- **Objective:** This test verifies item removal from the cart.
- **Expected Result:** cart empty after removal of one added item.

#### Test: test_cart_empty_message
- **Objective:** This test checks appropriate messaging in the cart page when there are no items in the cart.
- **Expected Result:** Display cart is empty message when no items added to cart and navigated to shopping cart.

#### Test: test_cart_icon_badge
- **Objective:** This test validates the item in cart count from the shopping cart badge.
- **Expected Result:** Cart badge count updated as per the item count in cart.

#### Test: test_update_item_quantity
- **Objective:**  This test validates the quantity update feature in the cart page.
- **Expected Result:** The quantity field in shopping cart page should be modifiable and update the total price based on the count

### 5. Checkout Process
#### Test: test_checkout
- **Objective:** Test checkout feature with valid input values.
- **Expected Result:** Successful checkout with confirmation message.

#### Test: test_invalid_data
- **Objective:** est checkout feature with invalid input values.
- **Expected Result:** Failed checkout with error message.
- 
#### Test: test_total_summary
- **Objective:** Test to check the total cost of all the items in cart matches with the summary in checkout page.
- **Expected Result:** Total summary matches with all the prices of the items in cart added.

#### Test: test_empty_cart_checkout
- **Objective:** Test to verify the checkout process when no items in the cart.
- **Expected Result:** Failed checkout with checkout button being inactive/disabled.

### 6. Product listing and details
#### Test: test_product_listing_page
- **Objective:** Verify that after login there are products listed in the product catalog page.
- **Expected Result:** More than one product listed in the page.

#### Test: test_product_details_page
- **Objective:** Test to verify each product detail page content.
- **Expected Result:** After product selection, product detail page displays the same item details.

#### Test: test_product_list_count
- **Objective:** Verify if all the products from inventory is listed.
- **Expected Result:** Product list count matches the expected value.

#### Test: test_product_description
- **Objective:** Test to verify the product description in product detail page.
- **Expected Result:** Description of product matches the product selected.

### 7. Product filtering 
#### Test: test_filtering_name
- **Objective:** Test to validate filtering functionality by name both options a-z and z-a.
- **Expected Result:** products listed as per the sort option selected.

#### Test: test_filtering_by_price
- **Objective:** Test to validate filtering by price option, both low-to-high and high-to-low.
- **Expected Result:** products listed as per the sort option selected.

## Analyzing Test Results
- **Console Output:** Review the console output for immediate feedback on test execution.
- **Log File:** Inspect reports/test_log.log for detailed logs on test activities and issues.
- **HTML Report:** View reports/report.html for a graphical representation of test results, including passed, failed, and skipped tests.
Troubleshooting
- **Test Failures:** If a test fails, examine the error message in the console output or log file to diagnose the issue. Common issues might include incorrect test data, application state problems, or environment configuration issues.
- **Missing Dependencies:** Ensure all required packages are installed correctly by checking requirements.txt.

## Submission
- **After completing the exercise:** Ensure that all tests pass or document any failed tests with details on the issues encountered.
Submit a summary report of your findings, including any problems or observations.

## Additional Notes
- **Environment:** Make sure your test environment mirrors the application’s expected configuration as closely as possible.
- **Support:** Reach out if you encounter any issues or have questions regarding the test setup or execution. [mvmeghana@gmail.com](mvmeghana@gmail.com)
## Running all the Tests to log into console
 pytest -v

## Running all the Tests with html report 
pytest --html=/reports/report.html
Open report.html in your web browser to view a detailed report of the test results.

## Running individual Test
 pytest <test_name.py>

- The test will be executed with the provided test data (username and password). Entire test results are store in reports/ directory