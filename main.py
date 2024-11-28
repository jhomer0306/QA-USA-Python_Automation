import data
import helpers
from selenium import webdriver
import time
import pages

from pages import UrbanRoutesPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUrbanRoutes:

# setup_class is used to establish a single connection to Urban Routes server
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        # Check if the URL is reachable
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server.")
        else:
            print("Cannot connect to the Urban Routes. Check if the server is running.")
# URL is specified in data.py.
# If the Urban Routes server is reachable, print "Connected...".  Otherwise, print "cannot connect..."
# Check server connection before proceeding with other tests.  Other tests will fail if server has expired.

    def test_set_route_from(self):
        # Navigate to Urban Routes main page
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Wait for the "From" field to be clickable
        urban_routes_page.wait_for_from_field()

        # Fill the "From" field
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)

        # Check that the From field is correctly filled
        assert urban_routes_page.get_from_location() == data.ADDRESS_FROM, \
            "The 'from' field did not contain the expected address"

    def test_set_route_to(self):
        # Navigate to Urban Routes main page
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Wait for the "From" field to be clickable
        urban_routes_page.wait_for_from_field()

        # Fill the "From" field
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)

        # Wait for the "To" field to be clickable
        urban_routes_page.wait_for_to_field()

        # Fill "To" field
        urban_routes_page.enter_to_location(data.ADDRESS_TO)

        # Check that the field is correctly filled
        assert urban_routes_page.get_to_location() == data.ADDRESS_TO, \
            "The 'to' field did not contain the expected address"

    def test_select_call_taxi(self):
        # Navigate to Urban Routes main page
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Wait for the "From" field to be clickable
        urban_routes_page.wait_for_from_field()

        # Fill the "From" field
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)

        # Wait for the "To" field to be clickable
        urban_routes_page.wait_for_to_field()

        # Fill "To" field
        urban_routes_page.enter_to_location(data.ADDRESS_TO)

        # Wait for "Call a taxi" button to be clickable
        urban_routes_page.wait_for_call_taxi_button()

        # Select "Call a taxi" button
        urban_routes_page.call_a_taxi()

        # Wait until the "Supportive Taxi" element is visible
        supportive_taxi = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(urban_routes_page.SUPPORTIVE_TAXI)
        )

        # Assert that the "Supportive" taxi is displayed
        assert supportive_taxi.is_displayed(), \
            "'Supportive' taxi is not displayed on the screen"

    def test_select_supportive_taxi(self):
        # Navigate to Urban Routes main page
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Wait for the "From" field to be clickable
        urban_routes_page.wait_for_from_field()

        # Fill the "From" field
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)

        # Wait for the "To" field to be clickable
        urban_routes_page.wait_for_to_field()

        # Fill "To" field
        urban_routes_page.enter_to_location(data.ADDRESS_TO)

        # Wait for "Call a taxi" button to be clickable
        urban_routes_page.wait_for_call_taxi_button()

        # Select "Call a taxi" button
        urban_routes_page.call_a_taxi()

        # Wait until the "Supportive Taxi" element is visible
        supportive_taxi = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(urban_routes_page.SUPPORTIVE_TAXI)
        )

        # Select "Supportive" vehicle
        urban_routes_page.select_supportive()

        # Scroll to "Blanket and Handkerchief" element
        urban_routes_page.scroll_to_blanket_button()

        # Wait for "Blanket and Handkerchief" element to be visible
        urban_routes_page.wait_for_blanket_button()

        # Assert that "Blanket and Handkerchief" element is visible
        assert urban_routes_page.is_blanket_button_visible(), \
            "'Blanket and Handkerchief' element is not visible on the screen"

    def test_fill_phone_number(self):
        # Navigate to Urban Routes main page
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Wait for the "From" field to be clickable
        urban_routes_page.wait_for_from_field()

        # Fill the "From" field
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)

        # Wait for the "To" field to be clickable
        urban_routes_page.wait_for_to_field()

        # Fill "To" field
        urban_routes_page.enter_to_location(data.ADDRESS_TO)

        # Wait for "Call a taxi" button to be clickable
        urban_routes_page.wait_for_call_taxi_button()

        # Select "Call a taxi" button
        urban_routes_page.call_a_taxi()

        # Wait until the "Supportive Taxi" element is visible
        supportive_taxi = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(urban_routes_page.SUPPORTIVE_TAXI)
        )

        # Select "Supportive" vehicle
        urban_routes_page.select_supportive()

        # Scroll to phone number field on the main page
        urban_routes_page.scroll_to_phone_number()

        # Wait for phone number field to be clickable
        urban_routes_page.wait_for_phone_number_field()

        # Click phone number field
        urban_routes_page.click_phone_number()

        # Wait for phone number modal (FILL_PHONE_FIELD) to be fillable
        urban_routes_page.wait_for_fill_phone_field()

        # Fill phone field in modal with a test number
        urban_routes_page.fill_phone_number(data.PHONE_NUMBER)

        # Assert that phone field is filled with the correct value
        assert urban_routes_page.get_phone_number() == data.PHONE_NUMBER, \
            "The phone field did not contain the expected value"

    def test_phone_next_and_close(self):
        # Navigate to Urban Routes main page
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Wait for the "From" field to be clickable
        urban_routes_page.wait_for_from_field()

        # Fill the "From" field
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)

        # Wait for the "To" field to be clickable
        urban_routes_page.wait_for_to_field()

        # Fill "To" field
        urban_routes_page.enter_to_location(data.ADDRESS_TO)

        # Wait for "Call a taxi" button to be clickable
        urban_routes_page.wait_for_call_taxi_button()

        # Select "Call a taxi" button
        urban_routes_page.call_a_taxi()

        # Wait until the "Supportive Taxi" element is visible
        supportive_taxi = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(urban_routes_page.SUPPORTIVE_TAXI)
        )

        # Select "Supportive" vehicle
        urban_routes_page.select_supportive()

        # Scroll to phone number field on the main page
        urban_routes_page.scroll_to_phone_number()

        # Wait for phone number field to be clickable
        urban_routes_page.wait_for_phone_number_field()

        # Click phone number field
        urban_routes_page.click_phone_number()

        # Wait for phone number modal (FILL_PHONE_FIELD) to be fillable
        urban_routes_page.wait_for_fill_phone_field()

        # Fill phone field in modal with a test number
        urban_routes_page.fill_phone_number(data.PHONE_NUMBER)

        # Wait for "Next" (PHONE_NEXT) in modal to be clickable
        urban_routes_page.wait_for_next_button()

        # Click "Next" to move to second modal
        urban_routes_page.click_next_phone()

        # Assert that "X" (PHONE_CLOSE) in second modal is visible
        assert urban_routes_page.is_phone_close_visible(), \
            "'X' button in the phone modal is not visible"

    def test_fill_card(self):
        # Navigate to Urban Routes main page
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Wait for the "From" field to be clickable
        urban_routes_page.wait_for_from_field()

        # Fill the "From" field
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)

        # Wait for the "To" field to be clickable
        urban_routes_page.wait_for_to_field()

        # Fill "To" field
        urban_routes_page.enter_to_location(data.ADDRESS_TO)

        # Wait for "Call a taxi" button to be clickable
        urban_routes_page.wait_for_call_taxi_button()

        # Select "Call a taxi" button
        urban_routes_page.call_a_taxi()

        # Wait until the "Supportive Taxi" element is visible
        supportive_taxi = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(urban_routes_page.SUPPORTIVE_TAXI)
        )

        # Select "Supportive" vehicle
        urban_routes_page.select_supportive()

        # Scroll to phone number field on the main page
        urban_routes_page.scroll_to_phone_number()

        # Wait for phone number field to be clickable
        urban_routes_page.wait_for_phone_number_field()

        # Click phone number field
        urban_routes_page.click_phone_number()

        # Wait for phone number modal (FILL_PHONE_FIELD) to be fillable
        urban_routes_page.wait_for_fill_phone_field()

        # Fill phone field in modal with a test number
        urban_routes_page.fill_phone_number(data.PHONE_NUMBER)

        # Wait for "Next" (PHONE_NEXT) in modal to be clickable
        urban_routes_page.wait_for_next_button()

        # Click "Next" to move to second modal
        urban_routes_page.click_next_phone()

        # Wait for "X" in second modal to be clickable
        urban_routes_page.wait_for_phone_close_button()

        # Click "X" to close phone modal
        urban_routes_page.click_phone_x()

        # Wait until "Payment Method" on main page is clickable
        urban_routes_page.wait_for_payment_method()

        # Click "Payment Method" on left side of screen
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_payment_method()

        # Wait until "Add card" in payment modal is clickable
        urban_routes_page.wait_for_add_card()

        # Click "Add card" in payment modal
        urban_routes_page.click_add_card()

        # Wait until card number modal is fillable
        urban_routes_page.wait_for_card_details_field()

        # Fill "card details" field with credit card number
        urban_routes_page.fill_card_details(data.CARD_NUMBER)

        # Assert that card details have been entered correctly
        assert urban_routes_page.get_card_details() == data.CARD_NUMBER, \
            "The card details field did not contain the expected value"

    def test_comment_for_driver(self):
        # Navigate to Urban Routes main page
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Wait for the "From" field to be clickable
        urban_routes_page.wait_for_from_field()

        # Fill the "From" field
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)

        # Wait for the "To" field to be clickable
        urban_routes_page.wait_for_to_field()

        # Fill "To" field
        urban_routes_page.enter_to_location(data.ADDRESS_TO)

        # Wait for "Call a taxi" button to be clickable
        urban_routes_page.wait_for_call_taxi_button()

        # Select "Call a taxi" button
        urban_routes_page.call_a_taxi()

        # Wait until the "Supportive Taxi" element is visible
        supportive_taxi = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(urban_routes_page.SUPPORTIVE_TAXI)
        )

        # Select "Supportive" vehicle
        urban_routes_page.select_supportive()

        # Scroll to phone number field on the main page
        urban_routes_page.scroll_to_phone_number()

        # Wait for phone number field to be clickable
        urban_routes_page.wait_for_phone_number_field()

        # Click phone number field
        urban_routes_page.click_phone_number()

        # Wait for phone number modal (FILL_PHONE_FIELD) to be fillable
        urban_routes_page.wait_for_fill_phone_field()

        # Fill phone field in modal with a test number
        urban_routes_page.fill_phone_number(data.PHONE_NUMBER)

        # Wait for "Next" (PHONE_NEXT) in modal to be clickable
        urban_routes_page.wait_for_next_button()

        # Click "Next" to move to second modal
        urban_routes_page.click_next_phone()

        # Wait for "X" in second modal to be clickable
        urban_routes_page.wait_for_phone_close_button()

        # Click "X" to close phone modal
        urban_routes_page.click_phone_x()

        # Wait until "Payment Method" on main page is clickable
        urban_routes_page.wait_for_payment_method()

        # Click "Payment Method" on left side of screen
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_payment_method()

        # Wait until "Add card" in payment modal is clickable
        urban_routes_page.wait_for_add_card()

        # Click "Add card" in payment modal
        urban_routes_page.click_add_card()

        # Wait until card number modal is fillable
        urban_routes_page.wait_for_card_details_field()

        # Fill "card details" field with credit card number
        urban_routes_page.fill_card_details(data.CARD_NUMBER)

        # Wait until credit card close button is clickable
        urban_routes_page.wait_for_card_close_button()

        # Close credit card field
        urban_routes_page.click_card_x()

        # Scroll to the comment field (bottom of main page)
        urban_routes_page.scroll_to_comment()

        # Wait until the comment field is fillable
        urban_routes_page.wait_for_comment_field()

        # Enter text in the comment field
        urban_routes_page.enter_comment(data.MESSAGE_FOR_DRIVER)

        # Assert that the correct text has been entered in the comment field
        assert urban_routes_page.get_comment() == data.MESSAGE_FOR_DRIVER, \
            "The comment field did not contain the expected message"

    def test_order_blanket_and_handkerchiefs(self):
        # Navigate to Urban Routes main page
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Wait for the "From" field to be clickable
        urban_routes_page.wait_for_from_field()

        # Fill the "From" field
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)

        # Wait for the "To" field to be clickable
        urban_routes_page.wait_for_to_field()

        # Fill "To" field
        urban_routes_page.enter_to_location(data.ADDRESS_TO)

        # Wait for "Call a taxi" button to be clickable
        urban_routes_page.wait_for_call_taxi_button()

        # Select "Call a taxi" button
        urban_routes_page.call_a_taxi()

        # Wait until the "Supportive Taxi" element is visible
        supportive_taxi = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(urban_routes_page.SUPPORTIVE_TAXI)
        )

        # Select "Supportive" vehicle
        urban_routes_page.select_supportive()

        # Scroll to phone number field on the main page
        urban_routes_page.scroll_to_phone_number()

        # Wait for phone number field to be clickable
        urban_routes_page.wait_for_phone_number_field()

        # Click phone number field
        urban_routes_page.click_phone_number()

        # Wait for phone number modal (FILL_PHONE_FIELD) to be fillable
        urban_routes_page.wait_for_fill_phone_field()

        # Fill phone field in modal with a test number
        urban_routes_page.fill_phone_number(data.PHONE_NUMBER)

        # Wait for "Next" (PHONE_NEXT) in modal to be clickable
        urban_routes_page.wait_for_next_button()

        # Click "Next" to move to second modal
        urban_routes_page.click_next_phone()

        # Wait for "X" in second modal to be clickable
        urban_routes_page.wait_for_phone_close_button()

        # Click "X" to close phone modal
        urban_routes_page.click_phone_x()

        # Wait until "Payment Method" on main page is clickable
        urban_routes_page.wait_for_payment_method()

        # Click "Payment Method" on left side of screen
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_payment_method()

        # Wait until "Add card" in payment modal is clickable
        urban_routes_page.wait_for_add_card()

        # Click "Add card" in payment modal
        urban_routes_page.click_add_card()

        # Wait until card number modal is fillable
        urban_routes_page.wait_for_card_details_field()

        # Fill "card details" field with credit card number
        urban_routes_page.fill_card_details(data.CARD_NUMBER)

        # Wait until credit card close button is clickable
        urban_routes_page.wait_for_card_close_button()

        # Close credit card field
        urban_routes_page.click_card_x()

        # Scroll to the comment field (bottom of main page)
        urban_routes_page.scroll_to_comment()

        # Wait until the comment field is fillable
        urban_routes_page.wait_for_comment_field()

        # Enter text in the comment field
        urban_routes_page.enter_comment(data.MESSAGE_FOR_DRIVER)

        # Scroll to the "blanket and handkerchiefs" toggle switch
        urban_routes_page.scroll_to_blanket_button()

        # Click the toggle switch
        urban_routes_page.order_blanket()

        # Check that the toggle switch is checked
        assert urban_routes_page.get_blanket_and_handkerchiefs_option_checked(), \
            "Blanket toggle switch is not checked as expected"

    def test_order_2_ice_creams(self):
        # Navigate to Urban Routes main page
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Wait for the "From" field to be clickable
        urban_routes_page.wait_for_from_field()

        # Fill the "From" field
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)

        # Wait for the "To" field to be clickable
        urban_routes_page.wait_for_to_field()

        # Fill "To" field
        urban_routes_page.enter_to_location(data.ADDRESS_TO)

        # Wait for "Call a taxi" button to be clickable
        urban_routes_page.wait_for_call_taxi_button()

        # Select "Call a taxi" button
        urban_routes_page.call_a_taxi()

        # Wait until the "Supportive Taxi" element is visible
        supportive_taxi = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(urban_routes_page.SUPPORTIVE_TAXI)
        )

        # Select "Supportive" vehicle
        urban_routes_page.select_supportive()

        # Scroll to phone number field on the main page
        urban_routes_page.scroll_to_phone_number()

        # Wait for phone number field to be clickable
        urban_routes_page.wait_for_phone_number_field()

        # Click phone number field
        urban_routes_page.click_phone_number()

        # Wait for phone number modal (FILL_PHONE_FIELD) to be fillable
        urban_routes_page.wait_for_fill_phone_field()

        # Fill phone field in modal with a test number
        urban_routes_page.fill_phone_number(data.PHONE_NUMBER)

        # Wait for "Next" (PHONE_NEXT) in modal to be clickable
        urban_routes_page.wait_for_next_button()

        # Click "Next" to move to second modal
        urban_routes_page.click_next_phone()

        # Wait for "X" in second modal to be clickable
        urban_routes_page.wait_for_phone_close_button()

        # Click "X" to close phone modal
        urban_routes_page.click_phone_x()

        # Wait until "Payment Method" on main page is clickable
        urban_routes_page.wait_for_payment_method()

        # Click "Payment Method" on left side of screen
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_payment_method()

        # Wait until "Add card" in payment modal is clickable
        urban_routes_page.wait_for_add_card()

        # Click "Add card" in payment modal
        urban_routes_page.click_add_card()

        # Wait until card number modal is fillable
        urban_routes_page.wait_for_card_details_field()

        # Fill "card details" field with credit card number
        urban_routes_page.fill_card_details(data.CARD_NUMBER)

        # Wait until credit card close button is clickable
        urban_routes_page.wait_for_card_close_button()

        # Close credit card field
        urban_routes_page.click_card_x()

        # Scroll to the comment field (bottom of main page)
        urban_routes_page.scroll_to_comment()

        # Wait until the comment field is fillable
        urban_routes_page.wait_for_comment_field()

        # Enter text in the comment field
        urban_routes_page.enter_comment(data.MESSAGE_FOR_DRIVER)

        # Scroll to the "blanket and handkerchiefs" toggle switch
        urban_routes_page.scroll_to_blanket_button()

        # Click the toggle switch
        urban_routes_page.order_blanket()

        # Scroll to ice cream bucket (bottom of main page)
        urban_routes_page.scroll_to_ice_cream()

        # Wait for "+ ice cream" element to be clickable (ADD_ICE_CREAM)
        urban_routes_page.wait_for_add_ice_cream_clickable()

        # Select "+" next to "ice cream" twice to add two ice creams
        # Loop to simulate ordering two ice creams
        number_of_ice_creams = 2
        for test_order in range(number_of_ice_creams):
            urban_routes_page.add_ice_creams()

        # Check that two ice creams have been added
        assert urban_routes_page.get_amount_of_ice_cream() == 2, \
            "Two ice creams have not been added as expected"

    def test_car_search_modal_appears(self):
        # Navigate to Urban Routes main page
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Wait for the "From" field to be clickable
        urban_routes_page.wait_for_from_field()

        # Fill the "From" field
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)

        # Wait for the "To" field to be clickable
        urban_routes_page.wait_for_to_field()

        # Fill "To" field
        urban_routes_page.enter_to_location(data.ADDRESS_TO)

        # Wait for "Call a taxi" button to be clickable
        urban_routes_page.wait_for_call_taxi_button()

        # Select "Call a taxi" button
        urban_routes_page.call_a_taxi()

        # Wait until the "Supportive Taxi" element is visible
        supportive_taxi = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(urban_routes_page.SUPPORTIVE_TAXI)
        )

        # Select "Supportive" vehicle
        urban_routes_page.select_supportive()

        # Scroll to phone number field on the main page
        urban_routes_page.scroll_to_phone_number()

        # Wait for phone number field to be clickable
        urban_routes_page.wait_for_phone_number_field()

        # Click phone number field
        urban_routes_page.click_phone_number()

        # Wait for phone number modal (FILL_PHONE_FIELD) to be fillable
        urban_routes_page.wait_for_fill_phone_field()

        # Fill phone field in modal with a test number
        urban_routes_page.fill_phone_number(data.PHONE_NUMBER)

        # Wait for "Next" (PHONE_NEXT) in modal to be clickable
        urban_routes_page.wait_for_next_button()

        # Click "Next" to move to second modal
        urban_routes_page.click_next_phone()

        # Wait for "X" in second modal to be clickable
        urban_routes_page.wait_for_phone_close_button()

        # Click "X" to close phone modal
        urban_routes_page.click_phone_x()

        # Wait until "Payment Method" on main page is clickable
        urban_routes_page.wait_for_payment_method()

        # Click "Payment Method" on left side of screen
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_payment_method()

        # Wait until "Add card" in payment modal is clickable
        urban_routes_page.wait_for_add_card()

        # Click "Add card" in payment modal
        urban_routes_page.click_add_card()

        # Wait until card number modal is fillable
        urban_routes_page.wait_for_card_details_field()

        # Fill "card details" field with credit card number
        urban_routes_page.fill_card_details(data.CARD_NUMBER)

        # Wait until credit card close button is clickable
        urban_routes_page.wait_for_card_close_button()

        # Close credit card field
        urban_routes_page.click_card_x()

        # Scroll to the comment field (bottom of main page)
        urban_routes_page.scroll_to_comment()

        # Wait until the comment field is fillable
        urban_routes_page.wait_for_comment_field()

        # Enter text in the comment field
        urban_routes_page.enter_comment(data.MESSAGE_FOR_DRIVER)

        # Scroll to the "blanket and handkerchiefs" toggle switch
        urban_routes_page.scroll_to_blanket_button()

        # Click the toggle switch
        urban_routes_page.order_blanket()

        # Scroll to ice cream bucket (bottom of main page)
        urban_routes_page.scroll_to_ice_cream()

        # Wait for "+ ice cream" element to be clickable (ADD_ICE_CREAM)
        urban_routes_page.wait_for_add_ice_cream_clickable()

        # Select "+" next to "ice cream" twice to add two ice creams
        # Loop to simulate ordering two ice creams
        number_of_ice_creams = 2
        for test_order in range(number_of_ice_creams):
            urban_routes_page.add_ice_creams()

        # Wait for "Enter the number and order" button to be clickable
        urban_routes_page.wait_for_place_order()

        # Select "Enter the number and order"
        urban_routes_page.enter_number_and_order()

        # Wait for car search modal to appear (CAR_SEARCH_MODAL)
        urban_routes_page.wait_for_car_search()

        # Check for presence of car search modal
        assert urban_routes_page.is_car_search_modal_present()

    def test_driver_will_arrive_appears(self):
        # Navigate to Urban Routes main page
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Wait for the "From" field to be clickable
        urban_routes_page.wait_for_from_field()

        # Fill the "From" field
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)

        # Wait for the "To" field to be clickable
        urban_routes_page.wait_for_to_field()

        # Fill "To" field
        urban_routes_page.enter_to_location(data.ADDRESS_TO)

        # Wait for "Call a taxi" button to be clickable
        urban_routes_page.wait_for_call_taxi_button()

        # Select "Call a taxi" button
        urban_routes_page.call_a_taxi()

        # Wait until the "Supportive Taxi" element is visible
        supportive_taxi = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(urban_routes_page.SUPPORTIVE_TAXI)
        )

        # Select "Supportive" vehicle
        urban_routes_page.select_supportive()

        # Scroll to phone number field on the main page
        urban_routes_page.scroll_to_phone_number()

        # Wait for phone number field to be clickable
        urban_routes_page.wait_for_phone_number_field()

        # Click phone number field
        urban_routes_page.click_phone_number()

        # Wait for phone number modal (FILL_PHONE_FIELD) to be fillable
        urban_routes_page.wait_for_fill_phone_field()

        # Fill phone field in modal with a test number
        urban_routes_page.fill_phone_number(data.PHONE_NUMBER)

        # Wait for "Next" (PHONE_NEXT) in modal to be clickable
        urban_routes_page.wait_for_next_button()

        # Click "Next" to move to second modal
        urban_routes_page.click_next_phone()

        # Wait for "X" in second modal to be clickable
        urban_routes_page.wait_for_phone_close_button()

        # Click "X" to close phone modal
        urban_routes_page.click_phone_x()

        # Wait until "Payment Method" on main page is clickable
        urban_routes_page.wait_for_payment_method()

        # Click "Payment Method" on left side of screen
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_payment_method()

        # Wait until "Add card" in payment modal is clickable
        urban_routes_page.wait_for_add_card()

        # Click "Add card" in payment modal
        urban_routes_page.click_add_card()

        # Wait until card number modal is fillable
        urban_routes_page.wait_for_card_details_field()

        # Fill "card details" field with credit card number
        urban_routes_page.fill_card_details(data.CARD_NUMBER)

        # Wait until credit card close button is clickable
        urban_routes_page.wait_for_card_close_button()

        # Close credit card field
        urban_routes_page.click_card_x()

        # Scroll to the comment field (bottom of main page)
        urban_routes_page.scroll_to_comment()

        # Wait until the comment field is fillable
        urban_routes_page.wait_for_comment_field()

        # Enter text in the comment field
        urban_routes_page.enter_comment(data.MESSAGE_FOR_DRIVER)

        # Scroll to the "blanket and handkerchiefs" toggle switch
        urban_routes_page.scroll_to_blanket_button()

        # Click the toggle switch
        urban_routes_page.order_blanket()

        # Scroll to ice cream bucket (bottom of main page)
        urban_routes_page.scroll_to_ice_cream()

        # Wait for "+ ice cream" element to be clickable (ADD_ICE_CREAM)
        urban_routes_page.wait_for_add_ice_cream_clickable()

        # Select "+" next to "ice cream" twice to add two ice creams
        # Loop to simulate ordering two ice creams
        number_of_ice_creams = 2
        for test_order in range(number_of_ice_creams):
            urban_routes_page.add_ice_creams()

        # Wait for "Enter the number and order" button to be clickable
        urban_routes_page.wait_for_place_order()

        # Select "Enter the number and order"
        urban_routes_page.enter_number_and_order()

        # Wait for car search modal to appear (CAR_SEARCH_MODAL)
        urban_routes_page.wait_for_car_search()

        # Wait up to 60 seconds for "The driver will arrive" modal
        urban_routes_page.wait_for_driver_will_arrive()

        # Check for presence of "The driver will arrive" modal
        assert urban_routes_page.is_driver_will_arrive_present()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()