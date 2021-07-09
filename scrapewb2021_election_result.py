from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unicodedata
from bs4 import BeautifulSoup
import pandas as pd
import csv

def remove_accented_chars(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

def seleniumBrowser():
    browser.get("https://results.eci.gov.in/Result2021/ConstituencywiseS25190.htm?ac=190")
    html = browser.page_source
    soup = BeautifulSoup(html,"html.parser")
    print(soup)
    startPoint = soup.findAll('table', attrs={'align': 'center'})
    #print(startPoint)
    # scrapeWebPage(startPoint)

def scrapeWebPage(startPoint):
    for tRows in startPoint[0].findAll('tr'):
        count = 0
        csvRows = []

        if (tRows.find('td')):
            #print(tRows)

            csvRows.append("https://www.troublecodes.net/freightlinercodes/")
            csvRows.append("Powertrain")
            for tData in tRows.findAll('td'):
                #print(tData)
                count=count+1
                if(count==1):
                    csvRows.append(remove_accented_chars(tData.text))
                    specific_code=tData.text[-2:]
                elif(count==2):
                    csvRows.append(remove_accented_chars(tData.text.replace(",","; ")))
                    csvRows.append("Freightliner")
                else:
                    csvRows.append(remove_accented_chars(tData.text.replace(",","; ")))
                    csvRows.append(specific_code)
            print(csvRows)
            writer.writerow(csvRows)

if __name__=='__main__':
    options = Options()
    options.add_argument("--diable-infobars")

    outfile = open("Freightliner_PCodes.csv", "a+")
    writer = csv.writer(outfile)
    writer.writerow(
        ["Source_url", "SubSystem", "OBD_Code", "Description", "Type", "AffectedSubSystem", "SpecificCode"])

    chromedriver = "/Users/rajeshpyne/Documents/chromedriver"
    browser = webdriver.Chrome(chromedriver, chrome_options=options)
    seleniumBrowser()
    browser.close()