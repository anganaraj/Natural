from bs4 import BeautifulSoup
import requests

File = open("out.csv", "a")


URL="https://www.amazon.com/Maya-Kaimal-Masala-Indian-Simmer/dp/B003GDNM4O/ref=sr_1_2?crid=2IK9UT58HPWBW&keywords=masala&qid=1648709543&sprefix=%2Caps%2C1535&sr=8-2"
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")
print("hi")
# Outer Tag Object
title = soup.find("span", attrs={"id":'productTitle'})
print(title.string)














































# ------------------

def get_title(soup):
     
    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})
 
        # Inner NavigableString Object
        title_value = title.string
 
        # Title as a string value
        title_string = title_value.strip()
 
        # # Printing types of values for efficient understanding
        # print(type(title))
        # print(type(title_value))
        # print(type(title_string))
        # print()
 
    except AttributeError:
        title_string = ""   
 
    return title_string
 
# Function to extract Product Price
def get_price(soup):
 
    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
 
    except AttributeError:
        price = ""  
 
    return price
 
# Function to extract Product Rating
def get_rating(soup):
 
    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
         
    except AttributeError:
         
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = "" 
 
    return rating
 
# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
         
    except AttributeError:
        review_count = ""   
 
    return review_count
 
# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available = available.find("span").string.strip()
 
    except AttributeError:
        available = ""  
 
    return available    
 
if __name__ == '__main__':
 
    # Headers for request
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
 
    # The webpage URL
   
 
    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)
 
    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")
 
    # Function calls to display all necessary product information
    print("Product Title =", get_title(soup))
    print("Product Price =", get_price(soup))
    print("Product Rating =", get_rating(soup))
    print("Number of Product Reviews =", get_review_count(soup))
    print("Availability =", get_availability(soup))
    print()
    print()