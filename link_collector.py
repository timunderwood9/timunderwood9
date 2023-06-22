

from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import random
from fake_useragent import UserAgent 
import shutil
from datetime import datetime
import os



# Helper function to get a BeautifulSoup object from a URL
def get_soup_selenium(url): #just going to leave this here for the moment as an example of a selenium function
    driver = webdriver.Chrome() #the link does work when I use requests.Sessions, the reason that it didn't when I initially tried to use sessions
    #is that I hadn't also set up the user agent to work correctly at that point
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_soup_ua(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

#the Amazon search pages only work when I use sessions, not with the standadrd request.
def get_soup_ua_session(url):
    ua = UserAgent()
    with requests.Session() as session: #do this so that it automatically closes sess preventing res leaks
        session.headers = {'User-Agent': ua.random} #the . operator can both let you modify an attribute or call on a method
        #in this case we are modifying the headers attribute. The headers attribute is a dictionary key value pair
        #User-Agent is the key, and ua.random is the value that is specified when the key is called on
        response = session.get(url)
        response.raise_for_status() #this is raises an error specifically if you return an http error code, and ends program then
        return BeautifulSoup(response.content, 'html.parser')

#function to check if a links.txt already exists, and to archive it if it does
#the archived file will have a name that includes the date it was made
#I only care about archiving one file per calendar date
def links_check():
    if os.path.exists('links.txt'):
        creation_time = os.path.getctime('links.txt')
        creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')
        #create the archive folder
        if not os.path.exists('old_link_lists'):
            os.makedirs('old_link_lists')
            
        #note how this renaming also moves the location
        dst = f'old_link_lists/links-{creation_date}.txt'
        if not os.path.exists(dst):
            shutil.move('links.txt', dst)
        else: os.remove('links.txt')


#function to create a list of links
def get_links(soup):
    #use the links check function to make sure that we do not have an existing links.txt when the program runs

    div_tags = soup.find_all('div', {'data-component-type': 's-search-result'}) 

    links = []
    for div in div_tags:
        # Get the data-index attribute
        data_index = int(div.get('data-index', 0))  # if data-index attribute doesn't exist, it defaults to 0
        if 0 <= data_index <= 50:
            a_tag = div.find('a', {'class': 'a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold'})
            if a_tag:
                Kindle_check = a_tag.text
                if Kindle_check == 'Kindle':
                    dirty_link = a_tag.get('href')
                    #I'm getting rid of all the cookie stuff in the link
                    clean_link = dirty_link.split('/ref')[0]
                    #and since the links are relative, we need to add amazon.com, etc
                    link = 'https://www.amazon.com' + clean_link 
                    links.append(link)
    return links




def collect_links():

    url_list = ['https://www.amazon.com/s?k=pride+and+prejudice+variations&s=exact-aware-popularity-rank',
                'https://www.amazon.com/s?k=pride+and+prejudice+variations&s=exact-aware-popularity-rank&page=2',
                'https://www.amazon.com/s?k=pride+and+prejudice+variations&s=exact-aware-popularity-rank&page=3',
                'https://www.amazon.com/s?k=pride+and+prejudice+variations&s=exact-aware-popularity-rank&page=4',
                'https://www.amazon.com/s?k=pride+and+prejudice+variations&s=exact-aware-popularity-rank&page=5',
                'https://www.amazon.com/s?k=pride+and+prejudice+variations&s=exact-aware-popularity-rank&page=6',
                'https://www.amazon.com/s?k=pride+and+prejudice+variations&s=exact-aware-popularity-rank&page=7',
                'https://www.amazon.com/s?k=pride+and+prejudice+variations&s=exact-aware-popularity-rank&page=8']

    links_check()

    links = []
    for url in url_list:
        soup = get_soup_ua_session(url)
        url_links = get_links(soup)
        #links = links.append(url_links) #links.append() bc it is a method called on links modifying its attribute, not links = links.append()
        #also links links.append adds the new thing as a sub list, what you actually want is to use links links.extend(url_links)
        links.extend(url_links)


#remove duplicates -- ideally I'd figure out why the duplicates where showing up there at all :/

    links_set = set (links)
    links = list(links_set)
        
    with open ('links.txt', 'a') as f:
        for link in links:
            f.write(link + '\n')


if __name__ == "__main__":
    collect_links()