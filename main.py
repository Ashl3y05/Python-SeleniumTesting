from selenium import webdriver
from selenium.webdriver.common.by import By
import
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get("https://www.python.org/")

upcoming_dates = driver.find_elements(By.CSS_SELECTOR, value='.event-widget .shrubbery ul li time' )
upcoming_event = driver.find_elements(By.CSS_SELECTOR, value='.event-widget .shrubbery ul li a' )
table = {}
count = 0
dates = [item.text for item in upcoming_dates]
events = [item.text for item in upcoming_event]

for num in range(0, len(dates)-1):
    table["2025-"+dates[num]]= events[num]

print(table)


driver.quit()