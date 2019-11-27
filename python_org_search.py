from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://vehicleenquiry.service.gov.uk/")

elem = driver.find_element_by_id('wizard_vehicle_enquiry_capture_vrn_vrn')
elem.clear()
elem.send_keys("SL05OAC")
elem.send_keys(Keys.RETURN)
if 'There has been a problem' in driver.page_source:
    driver.close()

elem = driver.find_element_by_id('yes-vehicle-confirm')
elem.click()

elem = driver.find_element_by_id('capture_confirm_button')

elem.click()

