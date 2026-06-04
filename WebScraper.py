'''
This script is a web scraper that extracts quotes, their authors, and associated tags from the website "https://quotes.toscrape.com". 
It uses the requests library to make HTTP requests and BeautifulSoup to parse the HTML content of the pages. 
The extracted data is then written to a CSV file named 'quotes.csv'. 
The script also includes error handling for failed HTTP requests and implements a delay between processing each quote to avoid overwhelming the server with requests.
'''

import requests 
from bs4 import BeautifulSoup
import csv
import time 

response = requests.get("https://quotes.toscrape.com") # page 1 of the quotes website to start scraping from

print("Successfully retrieved the webpage.")
print("Quotes and their authors:")
print("-----------------------------------")
with open('quotes.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f) # create a CSV writer object to write data to the CSV file
    writer.writerow(["Quote", "Author", "Tags"]) # write the header row to the CSV file

    while True: 
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser') # parse the HTML content of the page using BeautifulSoup
            quotes = soup.find_all('div', class_='quote') # find all the div elements with the class 'quote'
            print(f"Found {len(quotes)} quotes on the page.")

        else: 
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            break

        for quote in quotes:
            text = quote.find('span', class_='text') # extract the text of the quote  
            author = quote.find('small', class_='author') # extract the author's name from the quote
            tags = quote.find_all('a', class_='tag') # extract the tags associated with the quote
            clean_tags = [] # convert the tag elements to a list of tag texts
            for tag in tags:
                clean_tags.append(tag.text)

            time.sleep(1) # add a delay of 1 second between processing each quote to avoid overwhelming the server with requests

            # tags = [tag.text for tag in tags] # alternative way to extract the tag texts using a list comprehension
            
            print(f"{author.text}: {text.text} - Tags: {clean_tags}")
            print()
            writer.writerow([text.text, author.text, ';'.join(clean_tags)]) # write the quote data to a CSV file, separating the tags with a semicolon

        next_page = soup.find('li', class_='next') # find the 'next' button to navigate to the next page of quotes
        if next_page is None:
            break # if there is no 'next' button, we have reached the last page and can exit the loop
        else:
            next_url = next_page.find('a')['href'] # extract the URL for the next page
            response = requests.get(f"https://quotes.toscrape.com{next_url}") # make a request to the next page and update the soup object to parse the new page


