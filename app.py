from selenium import webdriver
from selenium.webdriver.common.by import By
import json

PATH = "E:\scraping selenium\selenium webdriver\chromedriver.exe"  # path to chromedriver.exe make sure you have Chrome downloaded to version 104

driver = webdriver.Chrome(PATH)

driver.get(
    "https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99")  # the site that is being scraped

# getting all of the data
product_name = driver.find_element(By.CLASS_NAME, "product-name")
product_price = driver.find_element(By.CLASS_NAME, "product-sale--cross")
product_price_on_sale = driver.find_element(By.CLASS_NAME, "product-sale--discount")
product_color = driver.find_element(By.CLASS_NAME, "colors-info-name")
product_size = driver.find_element(By.CLASS_NAME, "selector-trigger")

# making the data into text
product_name = product_name.get_attribute("textContent")
product_price = product_price.get_attribute("textContent")
product_price_on_sale = product_price_on_sale.get_attribute("textContent")
product_color = product_color.get_attribute("textContent")
product_size = product_size.get_attribute("textContent")


# a function for getting the numbers from a string and making them into float type. Example lv.23.54 -> 23.54
def get_pricing(price):
    price = price.split('.')
    final = f"{price[1]}.{price[2]}"
    final = float(final)
    return final


product_price = get_pricing(product_price)
product_price_on_sale = get_pricing(product_price_on_sale)
product_size = [product_size]

obj = {'name': product_name,
       'price': product_price,
       'price_on_sale': product_price_on_sale,
       'color': product_color,
       'size': product_size
       }

# making the json file
json_data = json.dumps(obj)
with open("data.json", "w") as f:
    f.write(json_data)

driver.quit()  # close the browser window after the scraping is done
