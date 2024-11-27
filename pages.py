from selenium import webdriver
import time
import data
import helpers

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:

    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_BUTTON = (By.XPATH, '//button[@class="button round"]')
    PHONE_NUMBER_FIELD = (By.XPATH, "//div[@class='np-text' and text()='Phone number']")
    FILL_PHONE_FIELD = (By.XPATH, "//input[@name='phone']")
    PHONE_NEXT = (By.XPATH, '//button[@class="button full"]')
    PHONE_CLOSE = (By.XPATH, '//div[@class="section active"]/button[@class="close-button section-close"]')
    PAYMENT_METHOD = (By.XPATH, '//div[@class="pp-button filled"]/div[@class="pp-text"]')
    ADD_CARD = (By.XPATH, '//div[@class="pp-row disabled"]/div[@class="pp-title"]')
    CARD_DETAILS = (By.XPATH, '//input[@id="number"]')
    CARD_CLOSE = (By.XPATH, '//div[@class="section active unusual"]/button[@class="close-button section-close"]')
    COMMENT_FIELD = (By.XPATH, '//*[@id="comment"]')
    SUPPORTIVE_TAXI = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')
    BLANKET_BUTTON = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    ADD_ICE_CREAM = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    PLACE_ORDER = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button/span[1]')
    CAR_SEARCH_MODAL = (By.XPATH, "//div[@class='order-header-title' and text()='Car search']")
    DRIVER_WILL_ARRIVE = (By.XPATH, "//div[contains(text(), 'driver will arrive')]")

    def __init__(self, driver: webdriver):
        self.driver = driver

    def enter_from_location(self, address_from: str):
        # Enter address in the "From" field
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(address_from)

    def enter_to_location(self, address_to: str):
        # Enter address in the "To" field
        self.driver.find_element(*self.TO_LOCATOR).send_keys(address_to)

    def call_a_taxi(self):
        # Select "Call a taxi" button
        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()

    def click_phone_number(self):
        # Select phone number field on main page
        self.driver.find_element(*self.PHONE_NUMBER_FIELD).click()

    def fill_phone_number(self, phone_number: str):
        # Fill phone number in modal
        self.driver.find_element(*self.FILL_PHONE_FIELD).send_keys(phone_number)

    def click_next_phone(self):
        # Select "next" in phone number modal
        self.driver.find_element(*self.PHONE_NEXT).click()

    def click_phone_x(self):
        # Select "X" to close out of phone number modal
        self.driver.find_element(*self.PHONE_CLOSE).click()

    def click_payment_method(self):
        # Select payment method field on main page
        self.driver.find_element(*self.PAYMENT_METHOD).click()

    def click_add_card(self):
        # Select "add a card" on payment method modal
        self.driver.find_element(*self.ADD_CARD).click()

    def fill_card_details(self, card_number: str):
        # Fill credit card details field
        self.driver.find_element(*self.CARD_DETAILS).send_keys(card_number)

    def click_card_x(self):
        # Select "X" to close out of credit card modal
        self.driver.find_element(*self.CARD_CLOSE).click()

    def scroll_to_comment(self):
        # Scroll to "Leave driver a comment" field on main page
        comment_field = self.driver.find_element(*self.COMMENT_FIELD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", comment_field)

    def enter_comment(self, driver_comment: str):
        # Enter a comment in "leave a comment" field
        self.driver.find_element(*self.COMMENT_FIELD).send_keys(driver_comment)

    def select_supportive(self):
        # Select 'Supportive' taxi option
        self.driver.find_element(*self.SUPPORTIVE_TAXI).click()

    def order_blanket(self):
        # Click slider switch to order a blanket and handkerchief
        self.driver.find_element(*self.BLANKET_BUTTON).click()

    def scroll_to_ice_cream(self):
        # Scroll to 'add ice cream' element
        ice_cream = self.driver.find_element(*self.ADD_ICE_CREAM)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ice_cream)

    def add_ice_creams(self):
        # Add an ice cream to the order (no flavor indicated)
        self.driver.find_element(*self.ADD_ICE_CREAM).click()

    def enter_number_and_order(self):
        # Select "enter number and order" to place the order
        self.driver.find_element(*self.PLACE_ORDER).click()

    def get_from_location(self):
        # Check to see what text is entered in the "From" field
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute("value")

    def get_to_location(self):
        # Check to see what text is entered in the "To" field
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute("value")

    def wait_for_from_field(self):
        # Wait until the 'From' field is clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FROM_LOCATOR)
        )

    def wait_for_to_field(self):
        # Wait until the 'To' field is clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TO_LOCATOR)
        )

    def wait_for_call_taxi_button(self):
        # Wait until "Call taxi" button is clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CALL_TAXI_BUTTON)
        )

    def scroll_to_blanket_button(self):
        # Scroll to the "Blanket and Handkerchief" element
        blanket_button = self.driver.find_element(*self.BLANKET_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", blanket_button)

    def wait_for_blanket_button(self):
        # Wait until the 'Blanket and Handkerchief' button is visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.BLANKET_BUTTON)
        )

    def is_blanket_button_visible(self):
        # Check if the "Blanket and Handkerchief" element is visible
        blanket_button = self.driver.find_element(*self.BLANKET_BUTTON)
        return blanket_button.is_displayed()

    def scroll_to_phone_number(self):
        # Scrolls to the phone number field on the main page
        phone_field = self.driver.find_element(*self.PHONE_NUMBER_FIELD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", phone_field)

    def wait_for_phone_number_field(self):
        # Wait until the phone number field on the main page is clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PHONE_NUMBER_FIELD)
        )

    def wait_for_fill_phone_field(self):
        # Wait until the phone modal field is fillable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FILL_PHONE_FIELD)
        )

    def get_phone_number(self):
        # Check the value in the phone modal field
        phone_field = self.driver.find_element(*self.FILL_PHONE_FIELD)
        return phone_field.get_attribute("value")

    def wait_for_next_button(self):
        # Wait until the "Next" button in the phone number modal is clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PHONE_NEXT)
        )

    def is_phone_close_visible(self):
        # Check if the "X" button in the second phone modal is visible
        phone_close = self.driver.find_element(*self.PHONE_CLOSE)
        return phone_close.is_displayed()

    def wait_for_phone_close_button(self):
        # Wait until the "X" button in the second phone modal is clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PHONE_CLOSE)
        )

    def wait_for_payment_method(self):
        # Wait until the 'Payment Method' button is clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PAYMENT_METHOD)
        )

    def wait_for_add_card(self):
        # Wait until the 'Add Card' button is clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_CARD)
        )

    def wait_for_card_details_field(self):
        # Wait until the card details field is fillable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CARD_DETAILS)
        )

    def get_card_details(self):
        # Get the value from the card details field.
        card_field = self.driver.find_element(*self.CARD_DETAILS)
        return card_field.get_attribute("value")

    def wait_for_card_close_button(self):
        # Wait until the card close button is clickable.
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CARD_CLOSE)
        )

    def wait_for_comment_field(self):
        # Wait until the comment field is fillable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.COMMENT_FIELD)
        )

    def get_comment(self):
        # Get the text currently entered in the comment field
        comment_field = self.driver.find_element(*self.COMMENT_FIELD)
        return comment_field.get_attribute("value")

    def blanket_button_clickable(self):
        # Wait until the 'Blanket and Handkerchief' button is clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BLANKET_BUTTON)
        )

    def is_blanket_button_clickable(self):
        # Check if the "blanket and handkerchiefs" toggle switch is clickable
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.BLANKET_BUTTON)
            )
            return True
        except:
            return False

    def wait_for_add_ice_cream_clickable(self):
        # Wait until the '+ ice cream' element is clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_ICE_CREAM)
        )

    def is_counter_plus_disabled(self):
        # Check if the '+ ice cream' button is disabled
        button = self.driver.find_element(*self.ADD_ICE_CREAM)
        return "disabled" in button.get_attribute("class")

    def wait_for_car_search(self):
        # Wait until the car search modal appears
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CAR_SEARCH_MODAL)
        )

    def wait_for_place_order(self):
        # Wait for the 'Place Order' button to be clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PLACE_ORDER),
        )

    def is_car_search_modal_present(self):
        # Check if the 'Car Search' modal is visible
        try:
            self.driver.find_element(*self.CAR_SEARCH_MODAL)
            return True
        except:
            return False

    def wait_for_driver_will_arrive(self):
        # Wait up to 30 seconds for "The driver will arrive" modal to appear
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.DRIVER_WILL_ARRIVE)
        )

    def is_driver_will_arrive_present(self):
        # Check if 'The driver will arrive...' modal is visible
        try:
            self.driver.find_element(*self.DRIVER_WILL_ARRIVE)
            return True
        except:
            return False



    # def is_blanket_ordered(self):
        #"""Checks if the 'Blanket and Handkerchief' slider has been clicked."""
        #blanket_button = self.driver.find_element(*self.BLANKET_BUTTON)
        #return "active" in blanket_button.get_attribute("class")

    #def is_blanket_toggled(self):
        # """Checks if the 'Blanket and Handkerchiefs' toggle switch is activated."""
        #toggle_input = self.driver.find_element(*self.BLANKET_TOGGLE_INPUT)
        #return toggle_input.is_selected()

    # def wait_for_blanket_toggle_state_change(self, initial_state):
        # """Waits for the state of the toggle switch to change."""
        # WebDriverWait(self.driver, 10).until(
        #    lambda driver: self.is_blanket_toggled() != initial_state
        # )
