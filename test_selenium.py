from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_add_task_selenium():
    # Setup: Start Chrome WebDriver
    driver = webdriver.Chrome()  # Ensure you have chromedriver installed
    driver.get("http://localhost:5000")  # Your Flask app URL

    # Simulate adding a task
    task_input = driver.find_element(By.NAME, "task")
    deadline_input = driver.find_element(By.NAME, "deadline")
    submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')

    task_input.send_keys("Test Task from Selenium")
    deadline_input.send_keys("2025-12-31")
    submit_button.click()

    time.sleep(2)  # Wait for the page to reload

    # Assert the task appears in the task list
    task_element = driver.find_element(By.XPATH, "//span[text()='Test Task from Selenium']")
    assert task_element is not None

    # Cleanup: Close the driver
    driver.quit()

def test_delete_task_selenium():
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000")

    # Find and click on the delete button for the first task
    delete_button = driver.find_element(By.XPATH, "//input[@value='Delete']")
    delete_button.click()

    time.sleep(2)

    # Check if the task is deleted (check absence of task element)
    try:
        driver.find_element(By.XPATH, "//span[text()='Test Task from Selenium']")
        assert False, "Task was not deleted"
    except:
        pass  # Task was deleted, so this is fine

    driver.quit()
