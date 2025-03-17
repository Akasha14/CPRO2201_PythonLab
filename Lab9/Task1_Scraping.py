# Step 2: Import Libraries.
import requests  
from bs4 import BeautifulSoup 

# Step 3: Send HTTP GET request.
url = "http://quotes.toscrape.com/"  
quoteResponse = requests.get(url)  
# Print message, code 200 = success.  
if quoteResponse.status_code == 200:  
    print("Fetch successful!")  
else:  
    print(f"Failed. Status code: {quoteResponse.status_code}") 

# Step 4: Parse with beautiful soup.
bSoup = BeautifulSoup(quoteResponse.text, "html.parser")

# Step 5: Find All Quotes.
# Example quote from website: <span class="text" itemprop="text">“The world as we have created it is a process of our thinking....”</span>
# All Quotes are inside span class="text".
allQuotes = bSoup.find_all("span", class_="text") 

# Step 6: Display the First 3 Quotes.  
for i in range(3):  
    print(f"Quote {i + 1}: {allQuotes[i].text}")  