Tests end-to-end functionality of the Urban Routes website, automating the process of entering a route, ordering a taxi, adding payment, selecting options, and placing an order.  

The following tests are included: 

- Set route with addresses
- Select the "Supportive" taxi mode
- Add a phone number to the order
- Add a card payment method
- Add a message to the driver
- Add a blanket and handkerchiefs to the order
- Add 2 ice creams to the order
- Place the order

main.py contains test cases that orchestrate interactions with the application and perform assertions to validate expected behavior.

pages.py contains page object methods and locators that abstract and encapsulate interactions with specific UI elements of the application.

data.py contains configuration values, constants, and test data used across the test suite for consistency and reusability.