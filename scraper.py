from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Edge('msedgedriver.exe')
browser.get(START_URL)

time.sleep(10)

scraped_data = []

# Define Exoplanet Data Scrapping Method
def scrape():
        print(f'Scrapping page {i+1} ...' )
        
        # BeautifulSoup Object     
        soup = BeautifulSoup(browser.page_source, "html.parser")

        bright_star_table = soup.find('table',attrs = {'class','wikitable'})

        table_body = bright_star_table.find('tbody')

        table_rows = table_body.find('tr')

        for rows in table_rows:
            table_columns = rows.find_all('td')

            temp_list = []

            for col_data in table_columns:  

                data = col_data.text.strip()

                temp_list.append(data)

            scraped_data.append(temp_list)

        # Find all elements on the page and click to move to the next page
stars_data  = []

for i in range(0,len(scraped_data)):

    Star_name = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]

    req_data = [Star_name,Distance,Mass,Radius,Lum]
    stars_data.append(req_data)
scrape()

# Define Header
headers = ['Star_name','Distance','Mass','Radius','Lum']

# Define pandas DataFrame   
stars_df_1 = pd.DataFrame(stars_data, columns=headers)

# Convert to CSV
stars_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
