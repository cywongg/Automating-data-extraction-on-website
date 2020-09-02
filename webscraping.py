from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from time import sleep
import pandas as pd

'''Create new instance of Chrome in Incognito mode'''
##Adding the incognito argument to our webdriver
option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
##create a new instance of Chrome
browser = webdriver.Chrome('/Users/joeywong/chromedriver')

##desired website url
browser.get("https://www.crunchbase.com/")
sleep(5)
browser.find_element_by_xpath('/html/body/chrome/div/app-header/mat-toolbar[1]/span[3]/session-controls/div/a/span').click()
sleep(2)
browser.find_element_by_xpath('/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/authentication-page/page-layout/div/div/authentication/mat-card/mat-tab-group/div/mat-tab-body[1]/div/login/form/mat-form-field[1]/div/div[1]/div/input').send_keys("username")
sleep(2)
browser.find_element_by_xpath('/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/authentication-page/page-layout/div/div/authentication/mat-card/mat-tab-group/div/mat-tab-body[1]/div/login/form/mat-form-field[2]/div/div[1]/div/input').send_keys("password")
sleep(2)
browser.find_element_by_xpath('/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/authentication-page/page-layout/div/div/authentication/mat-card/mat-tab-group/div/mat-tab-body[1]/div/login/form/div/button[2]/span').click()
sleep(5)
browser.find_element_by_xpath('/html/body/chrome/div/new-app-header/mat-toolbar/multi-search/form/mat-form-field/div/div[1]/div[2]/input').click()
sleep(5)
browser.find_element_by_xpath('/html/body/chrome/div/new-app-header/mat-toolbar/multi-search/form/mat-form-field/div/div[1]/div[2]/input').send_keys("no broker")
sleep(5)
browser.find_element_by_xpath('/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/multi-search-results/page-layout/div/div/div/div[2]/search-results-section[1]/mat-card/a[1]/span/span[2]').click()

'''Scrape Basic Info'''
from parsel import Selector
url = 'https://www.crunchbase.com/organization/nobroker#section-overview'
browser.get(url)
selector = Selector(text=browser.page_source)

##Name of the company
name = browser.find_elements_by_xpath('//*[@id="section-overview"]/mat-card/div[2]/image-with-fields-card/image-with-text-card/div/div/div[2]/div[1]/field-formatter/blob-formatter/span')
for i in name:
    name = i.text
print(name)

#Intro of the company
intro_element = browser.find_elements_by_xpath('//*[@id="section-overview"]/mat-card/div[2]/description-card/div/p')
for i in intro_element:
    intro = i.text
print(intro)

##total funding amount 
fundingtotal = browser.find_elements_by_xpath('//*[@id="section-overview"]/mat-card/div[2]/big-values-card/div/div[1]/mat-card/span[2]/field-formatter/a')
for i in fundingtotal:
    fundingtotal = i.text
print(fundingtotal)

#Location
location = browser.find_elements_by_xpath('//*[@id="section-overview"]/mat-card/div[2]/image-with-fields-card/image-with-text-card/div/div/div[2]/div[3]/field-formatter/identifier-multi-formatter')
for i in location:
    location = i.text
print(location)

##Categories
categories = browser.find_elements_by_xpath('//*[@id="section-overview"]/mat-card/div[2]/fields-card[1]/div/span[2]/field-formatter/identifier-multi-formatter/span')
for i in categories:
    categories = i.text
print(categories)

##Headquarter
headquarter = browser.find_elements_by_xpath('//a[contains(@href,"organizations/location_group_identifiers")]')
for i in headquarter:
    headquarter = i.text
print(headquarter)

##Founded Date
foundeddate = browser.find_elements_by_xpath('//span[contains(@class,"component--field-formatter field-type-date_precision ng-star-inserted")]')
for i in foundeddate:
    foundeddate = i.text
print(foundeddate)  
    
##Founders
founders = browser.find_elements_by_xpath('//*[@id="section-overview"]/mat-card/div[2]/fields-card[1]/div/span[8]/field-formatter/identifier-multi-formatter')
for i in founders:
    founders = i.text
print(founders)  

##Number of Employees
numofemployees = browser.find_elements_by_xpath('//a[contains(@href,"organizations/num_employees_enum/")]')
for i in numofemployees:
    numofemployees = i.text
print(numofemployees)

#Legal Name
legalname = browser.find_elements_by_xpath('//*[@id="section-overview"]/mat-card/div[2]/fields-card[1]/div/span[18]/field-formatter/blob-formatter/span')
for i in legalname:
    legalname = i.text
print(legalname)

##IPO Status
IPOstatus = browser.find_elements_by_xpath('//*[@id="section-overview"]/mat-card/div[2]/fields-card[2]/div/span[2]/field-formatter/span')
for i in IPOstatus:
    IPOstatus = i.text
print(IPOstatus)

##Company Type
companytype = browser.find_elements_by_xpath('//*[@id="section-overview"]/mat-card/div[2]/fields-card[2]/div/span[4]/field-formatter/span')
for i in companytype:
    companytype = i.text
print(companytype)

##Website
website = browser.find_elements_by_xpath('//*[@id="section-overview"]/mat-card/div[2]/fields-card[3]/div/span[2]/field-formatter/link-formatter/a')
for i in website:
    website = i.text
print(website)
    
##Facebookurl
facebook = browser.find_elements_by_xpath('//*[@id="section-overview"]/mat-card/div[2]/fields-card[3]/div/span[4]/field-formatter/link-formatter/a')
for i in facebook:
    facebook = i.get_attribute('href')
print(facebook)

##LinkedInurl
linkedin = browser.find_elements_by_xpath('//*[@id="section-overview"]/mat-card/div[2]/fields-card[3]/div/span[6]/field-formatter/link-formatter/a')
for i in linkedin:
    linkedin = i.get_attribute('href')
print(linkedin)

##Twitterurl
twitter = browser.find_elements_by_xpath('//*[@id="section-overview"]/mat-card/div[2]/fields-card[3]/div/span[8]/field-formatter/link-formatter/a')
for i in twitter:
    twitter = i.get_attribute('href')
print(twitter)
    
##Contact Email
contactemail = browser.find_elements_by_xpath('//*[@id="section-overview"]/mat-card/div[2]/fields-card[3]/div/span[10]/field-formatter/blob-formatter/span')
for i in contactemail:
    contactemail= i.text
print(contactemail)
    
##Phone Number 
phonenumber = browser.find_elements_by_xpath('//*[@id="section-overview"]/mat-card/div[2]/fields-card[3]/div/span[12]/field-formatter/blob-formatter/span')
for i in phonenumber:
    phonenumber = i.text
print(phonenumber)
    
'''Automation''' 
browser.find_element_by_xpath('//*[@id="section-overview"]/mat-card/div[2]/big-values-card/div/div[1]/mat-card/span[2]/field-formatter/a').click()
sleep(2)
browser.find_element_by_xpath('/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/search/page-layout/div/div/form/div[2]/results/div/div/div[1]/div/div/div/button[1]/span/span/span').click()
sleep(2)
browser.find_element_by_xpath('//*[@id="mat-checkbox-11"]/label/div').click()
sleep(2)
browser.find_element_by_xpath('//*[@id="mat-dialog-0"]/column-panel/div/dialog-layout/div/mat-dialog-content/div/div/div[1]/div/div[1]/mat-nav-list/mat-list-item[3]/div/div[3]/label-with-info/div/span[1]').click()
sleep(2)
browser.find_element_by_xpath('//*[@id="mat-checkbox-16"]/label/div').click()
sleep(2)
browser.find_element_by_xpath('//*[@id="mat-checkbox-17"]/label/div').click()
sleep(2)
browser.find_element_by_xpath('//*[@id="mat-checkbox-18"]/label/div').click()
sleep(2)
browser.find_element_by_xpath('//*[@id="mat-dialog-0"]/column-panel/div/dialog-layout/div/mat-dialog-actions/div/button/span').click()
sleep(2)

'''List'''
name_list =[]
fundingstage_list = []
moneyraised_list = []
numofinvestors_list = []
leadinvestors_list = []
investorsnames_list = []

'''iteration''' 
investors = browser.find_elements_by_xpath('//div[contains(@class,"component--grid-row")]')
for row in investors:
    name = browser.find_elements_by_xpath('//div[contains(@class,"flex-no-grow cb-overflow-ellipsis identifier-label")]')
    for i in name:
        name = i.text
    fundingstage = browser.find_elements_by_xpath('//div[contains(@class,"flex-no-grow cb-overflow-ellipsis identifier-label")]')
    for i in fundingstage:
        fundingstage = i.text
    moneyraised = browser.find_elements_by_xpath('//span[contains(@class,"component--field-formatter field-type-money ng-star-inserted")]')
    for i in moneyraised:
        moneyraised = i.text
    numofinvestors = browser.find_elements_by_xpath('//a[contains(@class,"cb-link component--field-formatter field-type-integer ng-star-inserted")]')
    for i in numofinvestors:
        numofinvestors = i.text
    leadinvestors = browser.find_elements_by_xpath('//grid-cell[contains(@class,"column-id-lead_investor_identifiers ng-star-inserted")]')
    for i in leadinvestors:
        naleadinvestorsme = i.text
    investorsnames = browser.find_elements_by_xpath('//grid-cell[contains(@class,"column-id-investor_identifiers ng-star-inserted")]')
    for i in investorsnames:
        investorsnames = i.text
    name_list.append(name)
    fundingstage_list.append(fundingstage)
    moneyraised_list.append(moneyraised)
    numofinvestors_list.append(numofinvestors)
    leadinvestors_list.append(leadinvestors)
    investorsnames_list.append(investorsnames)


name = browser.find_elements_by_xpath('//div[contains(@class,"flex-no-grow cb-overflow-ellipsis identifier-label")]')
for i in name:
    name = i.text
print(name)



'''Export to dataframe'''
df = pd.DataFrame(list(zip(name_list,fundingstage_list, moneyraised_list, numofinvestors_list, leadinvestors_list, investorsnames_list)), columns=['Transaction Name','Funding Stage', 'Money Raised','Number of Investors','Lead Investors','Investor Names'])
seleniumtesting = df.to_csv('Selenium_fundinginvestors.csv', index=False)

##a timeout period and the Try/Except
# Wait 20 seconds for page to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class=’avatar width-full rounded-2']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
    
'''Get The Response'''
##getting all titles for the pinned repositories
# find_elements_by_xpath returns an array of selenium objects.
titles_element = browser.find_elements_by_xpath("//a[@class=’text-bold’]")
# use list comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]
# print out all the titles.
print('titles:')
print(titles, '\n')

##get all the languages for the pinned repositories
language_element = browser.find_elements_by_xpath("//p[@class=’mb-0 f6 text-gray’]")
# same concept as for list-comprehension above.
languages = [x.text for x in language_element]
print("languages:")
print(languages, '\n')

'''Combine the responses using zip function'''
for title, language in zip(titles, languages):
    print("RepoName : Language")
    print(title + ": " + language, '\n')

