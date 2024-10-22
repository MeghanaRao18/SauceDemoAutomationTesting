# Bug Report

## Summary
Multiple tests in the `tests/` folder are failing due to various issues. The failures affect the functionality of the application in different ways, including incorrect outputs, exceptions, and performance problems.

## Affected Tests

### 1. Test: **`test_cart_management.py::test_cart_item_removal `**

#### **Description**
This test fails when attempting to verify empty cart after removal of all items from the cart. The test looks for empty cart class in the shopping cart page.

#### **Steps to Reproduce**
1. Navigate to the login page.
2. Enter valid credentials (username: `standard_user`, password: `secret_sauce`).
3. Submit the login form.
4. Add multiple items to cart.
5. Goto shopping cart page and remove all the items.
6. Verify empty cart.

#### **Expected Results**
The user should be prompted with a message saying cart is empty.

#### **Actual Results**
The test fails with an assertion error indicating the unavailability of empty cart class in the cart page.Also no display of empty cart message.

#### **Error Logs**

#### **Environment**
- **Browser**: Chrome 114.0
- **OS**: macOS 11.5

## Attachments

- [Pytest HTML Report](reports/report.html)
- [Detailed Logs](reports/test_log.log)

## Severity/Priority
- **Severity**: Major
- **Priority**: Medium


**Reported By**: [Meghana Rao]  
**Date**: [2024-09-08]

---

### 2. Test: **` test_cart_management.py::test_cart_empty_message `**

#### **Description**
This test directly navigates to shopping cart page without adding any items and asserts as cart empty message is not displayed.

#### **Steps to Reproduce**
1. Navigate to the login page.
2. Enter valid credentials (username: `standard_user`, password: `secret_sauce`).
3. Submit the login form.
4. Navigate to shopping cart page. 
5. Verify empty cart message.

#### **Expected Results**
The user should be prompted with a message saying cart is empty.

#### **Actual Results**
The test fails with an assertion error for no display of empty cart message.

#### **Error Logs**
 AssertionError:No appropriate cart empty message

#### **Environment**
- **Browser**: Chrome 114.0
- **OS**: macOS 11.5

## Attachments

- [Pytest HTML Report](reports/report.html)
- [Detailed Logs](reports/test_log.log)

## Severity/Priority
- **Severity**: Minor
- **Priority**: Low


**Reported By**: [Meghana Rao]  
**Date**: [2024-09-08]

---

### 3. Test: **` test_cart_management.py::test_cart_icon_badge `**

#### **Description**
This test validates the shopping cart badge count with right number displayed as per the items in the cart. 

#### **Steps to Reproduce**
1. Navigate to the login page.
2. Enter valid credentials (username: `standard_user`, password: `secret_sauce`).
3. Submit the login form.
4. Add item to cart
5. Verify increment in the cart badge count
6. Remove item from cart
7. Verify badge count is 0


#### **Expected Results**
The badge count should be initialized to 0 and decremented to 0 when one item in the cart is removed.

#### **Actual Results**
The test fails with timeout error for not finding the count class from the badge header when no items in the cart.

#### **Error Logs**
 Failed: Failed to verify cart badge count. As cart badge class not present

#### **Environment**
- **Browser**: Chrome 114.0
- **OS**: macOS 11.5

## Attachments

- [Pytest HTML Report](reports/report.html)
- [Detailed Logs](reports/test_log.log)

## Severity/Priority
- **Severity**: Major
- **Priority**: Medium


**Reported By**: [Meghana Rao]  
**Date**: [2024-09-08]

---

### 4. Test: **` test_cart_management.py::test_update_item_quantity`**

#### **Description**
This test validates  if the user can update the quantity of each item before checkout.

#### **Steps to Reproduce**
1. Navigate to the login page.
2. Enter valid credentials (username: `standard_user`, password: `secret_sauce`).
3. Submit the login form.
4. Add item to cart.
5. Navigate to shopping cart page.
6. Check if the quantity field is modifiable.
7. If so update the quantity and validate the same.
8. If quantity field is not modifiable, fail the test.


#### **Expected Results**
The quantity field in the shopping cart should be an input field taking in new values.

#### **Actual Results**
The test fails with assertion error as the quantity of the item in cart is immutable.

#### **Error Logs**
 AssertionError: Failed to update item quantity. The quantity field is not an input element.

#### **Environment**
- **Browser**: Chrome 114.0
- **OS**: macOS 11.5

## Attachments

- [Pytest HTML Report](reports/report.html)
- [Detailed Logs](reports/test_log.log)

## Severity/Priority
- **Severity**: Critical
- **Priority**: High


**Reported By**: [Meghana Rao]  
**Date**: [2024-09-08]

---

### 5. Test: **` test_checkout.py::test_invalid_data`**

#### **Description**
This test validates checkout page when user enters invalid postal code ( anything other than digits)

#### **Steps to Reproduce**
1. Navigate to the login page.
2. Enter valid credentials (username: `standard_user`, password: `secret_sauce`).
3. Submit the login form.
4. Add item to cart.
5. Navigate to shopping cart page.
6. Navigate to Checkout.
7. Enter valid first name and last name.
8. Enter " " in postal code field.


#### **Expected Results**
Error message is displayed asking for valid postal code.

#### **Actual Results**
The application continues to order summary page with invalid postal code.

#### **Error Logs**
  Failed: Checkout was allowed even with invalid postal code !!

#### **Environment**
- **Browser**: Chrome 114.0
- **OS**: macOS 11.5

## Attachments

- [Pytest HTML Report](reports/report.html)
- [Detailed Logs](reports/test_log.log)

## Severity/Priority
- **Severity**: Critical
- **Priority**: High


**Reported By**: [Meghana Rao]  
**Date**: [2024-09-08]

---

### 6. Test: **` test_checkout.py::test_empty_cart_checkout`**

#### **Description**
This test validates the application checkout functionality when there are no items in the cart.

#### **Steps to Reproduce**
1. Navigate to the login page.
2. Enter valid credentials (username: `standard_user`, password: `secret_sauce`).
3. Submit the login form.
4. Do not add any item to cart.
5. Navigate to shopping cart page.
6. Checkout button is active even though no items in cart.


#### **Expected Results**
Inactive checkout button.

#### **Actual Results**
The checkout button is active and the application navigates to order summary and order placement page.

#### **Error Logs**
   AssertionError: Checkout button is enabled even though cart is empty

#### **Environment**
- **Browser**: Chrome 114.0
- **OS**: macOS 11.5

## Attachments

- [Pytest HTML Report](reports/report.html)
- [Detailed Logs](reports/test_log.log)

## Severity/Priority
- **Severity**: Critical
- **Priority**: High


**Reported By**: [Meghana Rao]  
**Date**: [2024-09-08]

---

### 7. Test: **` test_product_search.py::test_product_search`**

#### **Description**
This test validates the product search feature of the application.

#### **Steps to Reproduce**
1. Navigate to the login page.
2. Enter valid credentials (username: `standard_user`, password: `secret_sauce`).
3. Submit the login form.
4. Look for search field.


#### **Expected Results**
Search field anf button found in the product listing page.

#### **Actual Results**
The test fails as there is not search option.

#### **Error Logs**
   Failed: Search button is not found or not visible. 

#### **Environment**
- **Browser**: Chrome 114.0
- **OS**: macOS 11.5

## Attachments

- [Pytest HTML Report](reports/report.html)
- [Detailed Logs](reports/test_log.log)

## Severity/Priority
- **Severity**: Critical
- **Priority**: High


**Reported By**: [Meghana Rao]  
**Date**: [2024-09-08]

---

### 8. Test: **` test_product_search.py::test_search_no_results`**

#### **Description**
This test validates the search feature of the application by entering a value in search field resulting in no items.

#### **Steps to Reproduce**
1. Navigate to the login page.
2. Enter valid credentials (username: `standard_user`, password: `secret_sauce`).
3. Submit the login form.
4. In the product listing page look for search option.
5. Enter string :" hello" in the search field.


#### **Expected Results**
Search result shows - no items found. 

#### **Actual Results**
Test fails as search option is n or present in the product listing page.

#### **Error Logs**
   AssertionError: Checkout button is enabled even though cart is empty

#### **Environment**
- **Browser**: Chrome 114.0
- **OS**: macOS 11.5

## Attachments
- [Pytest HTML Report](reports/report.html)
- [Detailed Logs](reports/test_log.log)

## Severity/Priority
- **Severity**: Critical
- **Priority**: High


**Reported By**: [Meghana Rao]  
**Date**: [2024-09-08]

---