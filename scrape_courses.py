import requests
from bs4 import BeautifulSoup
import csv
from datetime import date

url = "https://dattakala.edu.in/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

today = date.today()

courses = []

# COMMON TAGS USED FOR COURSE / PROGRAM NAMES
for tag in soup.find_all(["h2", "h3", "li"]):
    text = tag.get_text(strip=True)

    if any(word in text.lower() for word in [
        "engineering", "computer", "be", "b.tech", "mba",
        "pharmacy", "polytechnic", "management", "diploma"
    ]):
        courses.append(text)

# Remove duplicates
courses = list(set(courses))

with open("dattakala_courses.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Course / Program Name", "Date"])

    for course in courses:
        writer.writerow([course, today])

print("Courses extracted successfully!")
