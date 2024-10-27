from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace with the path to your Microsoft Edge WebDriver executable
driver_path = r'D:\Product Automation\msedgedriver.exe'  # Update the path as needed

# Initialize the WebDriver service for Edge
service = Service(driver_path)

# Initialize the WebDriver (for Edge)
driver = webdriver.Edge(service=service)

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
                search_box.clear()
                search_box.send_keys(query)
                search_box.send_keys(Keys.RETURN)

                # Wait for search results to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "search"))
                )
                
                # Log the iteration number and query
                print(f"Search '{query}' - Iteration {i + 1} completed")
            
            except Exception as e:
                print(f"An error occurred: {e}")
            
            # Wait before the next search
            time.sleep(2)  # Increase if you want to slow down the searches

# Define your search texts and number of repetitions
search_texts = ["Alfido Tech Internship", "www.alfidotech.com", "Alfido Tech"]
repeat_count = 500  # Set the desired number of repetitions

# Run the automated search
google_search(search_texts, repeat_count)

# Close the WebDriver
driver.quit()
