#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
from splinter import Browser
from pprint import pprint
import pymongo
import pandas as pd
import requests


# In[3]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


url = ('https://mars.nasa.gov/news/')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())


# In[5]:


# pull titles from website
titles = soup.find_all('div', class_="content_title")
#print(titles)


# In[6]:


# pull body from website
body = soup.find_all('div', class_="rollover_description")
#print(body)


# In[7]:


# pull titles and body from website
results = soup.find_all('div', class_="slide")
for result in results:
    titles = result.find('div', class_="content_title")
    title = titles.find('a').text
    bodies = result.find('div', class_="rollover_description")
    body = bodies.find('div', class_="rollover_description_inner").text
   # print('----------------')
  #  print(title)
 #   print(body)


# In[29]:


url = ('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())


# In[11]:


# pull images from website
images = soup.find_all('a', class_="fancybox")
#print(images)


# In[12]:


# pull image link
pic_src = []
for image in images:
    pic = image['data-fancybox-href']
    pic_src.append(pic)

featured_image_url = 'https://www.jpl.nasa.gov' + pic
featured_image_url


# In[13]:


mars_facts_url = "https://space-facts.com/mars/"
table = pd.read_html(mars_facts_url)
table[0]


# In[14]:


df = table[0]
df.columns = ["Facts", "Value"]
df.set_index(["Facts"])
df


# In[15]:


facts_html = df.to_html()
facts_html = facts_html.replace("\n","")
facts_html


# In[16]:


hemisphere_image_urls = []


# In[18]:


url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())


# In[19]:


cerberus_img = soup.find_all('div', class_="wide-image-wrapper")
#print(cerberus_img)


# In[20]:


for img in cerberus_img:
    pic = img.find('li')
    full_img = pic.find('a')['href']
 #   print(full_img)
cerberus_title = soup.find('h2', class_='title').text
#print(cerberus_title)
cerberus_hem = {"Title": cerberus_title, "url": full_img}
#print(cerberus_hem)


# In[21]:


url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())


# In[22]:


shiaparelli_img = soup.find_all('div', class_="wide-image-wrapper")
#print(shiaparelli_img)


# In[23]:


for img in shiaparelli_img:
    pic = img.find('li')
    full_img = pic.find('a')['href']
    print(full_img)
shiaparelli_title = soup.find('h2', class_='title').text
#print(shiaparelli_title)
shiaparelli_hem = {"Title": shiaparelli_title, "url": full_img}
#print(shiaparelli_hem)


# In[ ]:


url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())


# In[24]:


syrtris_img = soup.find_all('div', class_="wide-image-wrapper")
#print(syrtris_img)


# In[25]:


for img in syrtris_img:
    pic = img.find('li')
    full_img = pic.find('a')['href']
 #   print(full_img)
syrtris_title = soup.find('h2', class_='title').text
#print(syrtris_title)
syrtris_hem = {"Title": syrtris_title, "url": full_img}
#print(syrtris_hem)


# In[27]:


url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[26]:


valles_marineris_img = soup.find_all('div', class_="wide-image-wrapper")
#print(valles_marineris_img)


# In[28]:


for img in valles_marineris_img:
    pic = img.find('li')
    full_img = pic.find('a')['href']
 #   print(full_img)
valles_marineris_title = soup.find('h2', class_='title').text
#print(valles_marineris_title)
valles_marineris_hem = {"Title": valles_marineris_title, "url": full_img}
#print(valles_marineris_hem)


# In[ ]:




