#reading HTML docs

from bs4 import BeautifulSoup
import requests

# -----------------------------------------------------

# with open("index.html", "r") as f:
#         doc = BeautifulSoup(f, "html.parser")
        
# print(doc)

# -----------------------------------------------------

# with open("index.html", "r") as f:
#         doc = BeautifulSoup(f, "html.parser")
        
# print(doc.prettify())
# adding .prettify will add indentation to the read file

# -----------------------------------------------------
# How to find things by the tag name

# with open("index.html", "r") as f:
#         doc = BeautifulSoup(f, "html.parser")
        
# tag = doc.p
# you can also modify the tag data by passing a string
# tag.string = "hello"
# print(tag.string)
# the .string allows you to access data within the tag

# with open("index.html", "r") as f:
#         doc = BeautifulSoup(f, "html.parser")
        
# tag = doc.find_all("p")[0]
# the doc.find_all will find all of the <p> tags in the html
# print(tag.find_all("b"))
# adding the find_all and "b" will find all of the b tags within the p tags

# -----------------------------------------------------

# How to read in html from a website

# request will send a get request to pull the data from the website

# url = "https://www.newegg.com/asus-geforce-rtx-3060-dual-rtx3060-o12g-white/p/N82E16814126634"

# result = requests.get(url)
# print(result.text)

# -----------------------------------------------------

# Pulling a particular piece of data from the website

# url = "https://www.newegg.com/asus-geforce-rtx-3060-dual-rtx3060-o12g-white/p/N82E16814126634"

# result = requests.get(url)
# doc = BeautifulSoup(result.text, "html.parser")

# prices = doc.find_all(string="$")
# parent = prices[0].parent
# strong = parent.find("strong")
# print(strong.string)