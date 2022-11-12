
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import requests
from lxml import etree


start_time = datetime.now()
columns_list = ["url", "product_title", "price", 'Size Available']
result = pd.DataFrame(columns=columns_list)

'''Define the path to your input file'''
Links = pd.read_excel(r'input_1.xlsx')


candidates = input("Please input your name here : ")

'''Creating the driver'''

'''Uncomment this when using Mozilla'''
# driver = webdriver.Firefox(executable_path=r"geckodriver.exe")
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

'''Uncomment this when using Chrome'''

# driver = webdriver.Chrome(executable_path=r'chromedriver.exe')


'''Function to extract different informations of the product'''


def do_task(iteration):
    url = Links.iloc[iteration, 0]
    print("Current URL is: ", url)
    driver.get(url)
    time.sleep(1)

    '''You can either use Selenium to scrape or use Beautifulsoup'''

    '''Variable soup below are used when scraping using Beautifulsoup'''
    source = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(source, 'lxml')

    '''This is the example on how to fetch the data using the Beautifulsoup'''
    # delivery_time = soup.find("span", class_  = "variant-liefer").get_text().strip()

    '''This is the example on how to fetch the data using the Selenium'''
    # delivery_time = driver.find_element(By.CLASS_NAME, "variant-liefer").get_text().strip()

    '''Try to fulfill the output required by fetching the data and save it in a variable'''

    url1 = url
    product_title = soup.find('h1', class_='product-title').text.strip()
    price =soup.find('div',  class_ = "price--main").text.strip()
    # size1 = soup.find('select',selected='selected',  class_ = 'form-field-input form-field-select form-field-filled')
    # size = soup.find('select', select="selected", id="data-product-option-0")
    # size1 = soup.select('option', selected='selected', id='data-product-option-0')
    # datatag = '<select id="data-product-option-0" class="form-field-input form-field-select form-field-filled" data-product-option="0"><option><selected="selected"></option></select>'
    # dom = etree.HTML(datatag)
    # size = dom.xpath("//*[@id='data-product-option-0']/text()")

    size1 = soup.find('div', 'selected', class_ = "form-field-select-wrapper")
    # size2= size1.select('option', selected = 'selected')
    size2 = size1.select("option[value]")
    size3 = [item.get('value') for item in size2]


    '''These are the output requirement.'''
    output = [url1, product_title, price, size3]

    print(output)
    return output


'''Use the function above to crawl for all links'''

# Running the loop to crawl links in file import
print("Starting with links in excel")
for iteration in range(len(Links)):
    print('on the {} link (total: {})'.format(iteration + 1, len(Links)))
    output = do_task(iteration)
    result.loc[len(result)] = output

'''Exporting result to target folder'''
end_time = datetime.now()
timestr = time.strftime("%d.%m.%Y-%H%M%S")
print('Duration: {}'.format(end_time - start_time))
name = "Webshop_" + timestr + "_" + candidates
result.to_excel(r'{}.xlsx'.format(name), index=False)
