from bs4 import BeautifulSoup
import requests

#Get description of ticker

def get_desc(ticker):
    url = f'https://www.google.com/finance/quote/{ticker}:NASDAQ'
    
    # Get web page data from url
    response = requests.get(url)
    
    # Get html document from web page data
    html_doc = response.text
    
    #print the content
    #print(html_doc)
    soup = BeautifulSoup(html_doc, 'lxml')
    tags = soup.find_all('div', class_='bLLb2d')
    print(tags[0].text,'\n')

#Get current stock price for ticker

def get_stock_price(ticker):
    url = f'https://www.marketwatch.com/investing/stock/{ticker}'
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'lxml')
    tags = soup.find_all('h2', class_='intraday__price')  
    stock_price = tags[0].text
    stock_price = stock_price.replace("\n","")
    stock_price = stock_price.replace("$","")
    stock_price = stock_price.replace(" ","")
    print(f"Stock Price = {stock_price}", "\n")
    return stock_price

#Get daily range of ticker for the current day

def get_day_range(ticker):
    url = f'https://www.google.com/finance/quote/{ticker}:NASDAQ'
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'lxml')
    tags = soup.find_all('div', class_='P6K39c')
    
    daily_range = tags[1] 
    daily_range = daily_range.text
    daily_range = daily_range.replace("$","")
    daily_range = daily_range.replace(" - ",",")
    daily_range = daily_range.split(',')
    low, high = float(daily_range[0]), float(daily_range[1])
    print(f"Low = {low}, High = {high}", '\n')
    return low,high

#Get volume of ticker for the current day

def get_volume(ticker):
    url = f'https://www.google.com/finance/quote/{ticker}:NASDAQ'
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'lxml')
    tags = soup.find_all('div', class_='P6K39c') 
    volume = tags[4]
    volume = volume.text
    print(f"Volume = {volume}", '\n')
    return volume
