from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
from datetime import date
import time

# Chrome options
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# Open website
driver.get("https://dattakala.edu.in/")
time.sleep(5)  # wait for page to load fully

today = date.today()
courses = []

# Collect visible text from headings & list items
elements = driver.find_elements(By.XPATH, "//h1 | //h2 | //h3 | //li")

for el in elements:
    text = el.text.strip().lower()
    if any(word in text for word in [
        "engineering", "computer", "be", "b.e", "b.tech",
        "mba", "pharmacy", "polytechnic", "diploma"
    ]):
        courses.append(el.text.strip())

driver.quit()

# Remove duplicates
courses = list(set(courses))

# Save to CSV
with open("dattakala_courses.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Course / Program Name", "Date"])

    for course in courses:
        writer.writerow([course, today])

print("✅ Courses extracted successfully!")
