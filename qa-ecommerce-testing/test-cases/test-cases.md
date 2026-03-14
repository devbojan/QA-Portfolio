Login test cases

TC_LOGIN_01

Title: Login with valid credentials

Steps:

Open SauceDemo login page

Enter valid username

Enter valid password

Click Login

Expected result:
User is redirected to inventory page.

TC_LOGIN_02

Title: Login with invalid password

Expected result:
Error message displayed.

TC_LOGIN_03

Title: Login with empty username

Expected result:
Error message: username required.

TC_LOGIN_04

Title: Login with empty password

Expected result:
Error message displayed.

TC_LOGIN_05

Title: Login with both fields empty

Expected result:
Error message displayed.



Product page test cases

TC_PRODUCT_01

Verify product list loads successfully.

Expected result:
All products displayed.

TC_PRODUCT_02

Verify each product shows:

product name

image

price

Expected result:
All information visible.

TC_PRODUCT_03

Verify sorting products by price low to high.

Expected result:
Products sorted correctly.

TC_PRODUCT_04

Verify sorting by price high to low.

Expected result:
Products sorted correctly.

Cart test cases

TC_CART_01

Add product to cart.

Expected result:
Cart icon shows item count.

TC_CART_02

Remove product from cart.

Expected result:
Product removed from cart.

TC_CART_03

Add multiple products.

Expected result:
Cart shows correct quantity.

TC_CART_04

Open cart page.

Expected result:
Selected products displayed.



Checkout test cases

TC_CHECKOUT_01

Start checkout process.

Expected result:
Checkout form displayed.

TC_CHECKOUT_02

Checkout with valid information.

Expected result:
Order completed successfully.

TC_CHECKOUT_03

Checkout with empty first name.

Expected result:
Error message displayed.

TC_CHECKOUT_04

Checkout with empty postal code.

Expected result:
Validation error.


UI / usability tests

TC_UI_01
Verify cart icon visible.

Expected result:
Cart icon displayed.


TC_UI_02
Verify logout functionality.

Expected result:
User redirected to login page.

TC_UI_03
Verify menu button works.

Expected result:
Menu options visible.


TC_UI_04
Verify product details open.

Expected result:
Product page loads.


