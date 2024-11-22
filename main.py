import data
import helpers
from selenium import webdriver
import time
import pages

from data import URBAN_ROUTES_URL, PHONE_NUMBER
from pages import UrbanRoutesPage

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

    def test_set_route(self):
        # Fills "from" and "to" fields on Urban Routes main page
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        time.sleep(2)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        time.sleep(2)
        print("Function created for setting route")
        pass

    def test_select_route(self):
        # Assumes "from" and "to" fields were filled in the previous test
        # Selects route by clicking "Call a taxi" button
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.call_a_taxi()
        time.sleep(2)
        # Selects "Supportive" vehicle
        urban_routes_page.select_supportive()
        time.sleep(2)
        print("Function created for selecting route")
        pass

    def test_fill_phone_number(self):
        # Assumes previous tests have been run successfully
        # Selects phone number field on the left hand side of the screen
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_phone_number()
        time.sleep(2)
        # Phone field appears in center of page
        # Fills phone field in center of page with a test number
        urban_routes_page.fill_phone_number(data.PHONE_NUMBER)
        time.sleep(2)
        # Clicks "Next"
        urban_routes_page.click_next_phone()
        time.sleep(2)
        # Clicks 'X' to close phone field
        urban_routes_page.click_phone_x()
        time.sleep(2)
        print("Function created for filling phone number")
        pass

    def test_fill_card(self):
        # Assumes previous tests have been run successfully
        # Clicks "Payment method" on left side of screen
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_payment_method()
        time.sleep(2)
        # Clicks "Add card" in center of screen
        urban_routes_page.click_add_card()
        time.sleep(2)
        # Fills in card number field with test card number
        urban_routes_page.fill_card_details(data.CARD_NUMBER)
        time.sleep(2)
        # Closes credit card field
        urban_routes_page.click_card_x()
        time.sleep(2)
        print("Function created for filling card details")
        pass

    def test_comment_for_driver(self):
        # Assumes previous tests have been run successfully
        # Scrolls to the comment field (bottom of main page)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.scroll_to_comment()
        time.sleep(2)
        # Enters text in the comment field
        urban_routes_page.enter_comment(data.MESSAGE_FOR_DRIVER)
        time.sleep(2)
        print("Function created for leaving driver a comment")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Assumes previous tests have been run successfully
        # Selects "Blanket and Handkerchief"
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.order_blanket()
        time.sleep(2)
        print("Function created for ordering blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # Assumes previous tests have been run successfully
        # Scrolls to ice cream bucket (bottom of main page)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.scroll_to_ice_cream()
        time.sleep(2)
        # Selects "+" next to "ice cream" twice to add two ice creams
        # Loop to simulate ordering two ice creams
        number_of_ice_creams = 2
        for test_order in range(number_of_ice_creams):
            urban_routes_page.add_ice_creams()
            time.sleep(2)
            print(f"Function created for ordering ice cream #{test_order +1}")
        # Prints separately for ice cream #1 and ice cream #2
            pass

    def test_car_search_model_appears(self):
        # Assumes previous tests have been run successfully
        # Selects "Enter the number and order"
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_number_and_order()
        time.sleep(35)
        # Waits 35 seconds to ensure car model has appeared
        print("Function created for car search model appears")
        pass


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()