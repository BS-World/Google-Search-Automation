from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Replace with the path to your Microsoft Edge WebDriver executable
driver_path = r'D:\Product Automation\msedgedriver.exe'  # Update the path as needed

# Initialize the WebDriver service for Edge
service = Service(driver_path)

# Initialize the WebDriver (for Edge)
driver = webdriver.Edge(service=service)

def human_like_sleep(min_seconds=1, max_seconds=3):
    """Pause execution for a random duration to mimic human behavior."""
    time.sleep(random.uniform(min_seconds, max_seconds))

def scroll_down_page(scroll_time=3):
    """Scroll down the page to mimic human scrolling behavior."""
    end_time = time.time() + scroll_time
    while time.time() < end_time:
        # Scroll down by a random amount
        driver.execute_script("window.scrollBy(0, window.innerHeight * 0.5);")  # Scroll down by half the viewport height
        human_like_sleep(0.5, 1.5)  # Wait between scrolls

def google_search(queries, repeat_count):
    for query in queries:
        for i in range(repeat_count):
            # Open Google
            driver.get("https://www.google.com")
            
            try:
                # Wait until the search box is loaded and visible
                search_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "q"))
                )

                # Mimic human typing speed
                for char in query:
                    search_box.send_keys(char)
                    human_like_sleep(0.1, 0.3)  # Random delay between keystrokes

                human_like_sleep(0.5, 1.0)  # Wait before hitting Enter
                search_box.send_keys(Keys.RETURN)

                # Wait for search results to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "search"))
                )

                # Log the iteration number and query
                print(f"Search '{query}' - Iteration {i + 1} completed")

                # Randomly wait before considering a link click
                human_like_sleep(2, 5)

                # Click on a random search result link
                try:
                    links = driver.find_elements(By.XPATH, '//h3')
                    if links:
                        random_link = random.choice(links)
                        random_link.click()
                        
                        # Scroll down the page
                        scroll_down_page(scroll_time=random.randint(5, 10))  # Scroll for a random duration
                        
                        # Go back to search results
                        driver.back()
                        human_like_sleep(2, 4)  # Wait before the next search
                except Exception as e:
                    print(f"An error occurred when clicking a link: {e}")

            except Exception as e:
                print(f"An error occurred during the search process: {e}")

# Define your search texts and number of repetitions
search_texts = ["Alfido Tech Internship", "Alfido Tech"]
repeat_count = 19  # Set the desired number of repetitions (Lower for demonstration)

# Run the automated search
google_search(search_texts, repeat_count)

# Close the WebDriver
driver.quit()
