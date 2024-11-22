from selenium import webdriver
import time
import data
import helpers

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from data import ADDRESS_FROM, ADDRESS_TO, PHONE_NUMBER

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

    def __init__(self, driver: webdriver):
        self.driver = driver

    def enter_from_location(self, address_from: str):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(address_from)

    def enter_to_location(self, address_to: str):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(address_to)

    def call_a_taxi(self):
        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()

    def click_phone_number(self):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD).click()

    def fill_phone_number(self, phone_number: str):
        self.driver.find_element(*self.FILL_PHONE_FIELD).send_keys(phone_number)

    def click_next_phone(self):
        self.driver.find_element(*self.PHONE_NEXT).click()

    def click_phone_x(self):
        self.driver.find_element(*self.PHONE_CLOSE).click()

    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD).click()

    def click_add_card(self):
        self.driver.find_element(*self.ADD_CARD).click()

    def fill_card_details(self, card_number: str):
        self.driver.find_element(*self.CARD_DETAILS).send_keys(card_number)

    def click_card_x(self):
        self.driver.find_element(*self.CARD_CLOSE).click()

    def scroll_to_comment(self):
        comment_field = self.driver.find_element(*self.COMMENT_FIELD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", comment_field)

    def enter_comment(self, driver_comment: str):
        self.driver.find_element(*self.COMMENT_FIELD).send_keys(driver_comment)

    def select_supportive(self):
        self.driver.find_element(*self.SUPPORTIVE_TAXI).click()

    def order_blanket(self):
        self.driver.find_element(*self.BLANKET_BUTTON).click()

    def scroll_to_ice_cream(self):
        ice_cream = self.driver.find_element(*self.ADD_ICE_CREAM)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ice_cream)

    def add_ice_creams(self):
        self.driver.find_element(*self.ADD_ICE_CREAM).click()

    def enter_number_and_order(self):
        self.driver.find_element(*self.PLACE_ORDER).click()
