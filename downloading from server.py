from bs4 import BeautifulSoup
import requests
URL ="https://coddyschool.com/upload/Web-Scraping-with-Python_proglib.pdf"
response = requests.get(URL,stream=True)


with open(r"C:/Users/hp/Desktop/AI/w2eb1.pdf", "wb") as file:
    for char in response.iter_content(chunk_size=1024):
        file.write(char)
    else:
        print("download")
    