
# coding: utf-8

# In[1]:


# Send yourself an email with as much information as possible from the site, such as:

# The title of the thing (the sale, the article, whatever)
# A URL for it
# Upvotes/thumbs ups/subreddits/prices/links to images/etc


# In[54]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[56]:


response = requests.get('https://slickdeals.net')
doc = BeautifulSoup(response.text, 'html.parser')


# In[57]:


products = doc.find_all(class_='fpItem')
len(products)


# In[92]:


list_of_products = []

for product in products:
    
    product_dict = {}
    
    try:
        title = product.find(class_='itemTitle')
        product_dict['title'] = title.text
        store = product.find(class_='itemStore')
        product_dict['store'] = store.text
        price = product.find(class_='itemPrice')
        product_dict['price'] = price.text
        url = "https://slickdeals.net"
        product_dict['link'] = url+product.find(class_='itemTitle').attrs['href']
    except:
        print(" ")
        
        
    list_of_products.append(product_dict)
    
list_of_products
    


# In[98]:


df = pd.DataFrame(list_of_products)
df['price'] = df['price'].str.replace("\n", " ")
df.head()


# In[99]:


import datetime
right_now = datetime.datetime.now()
right_now = str(right_now.strftime("%Y-%m-%d-%I%p"))
str(right_now)
right_now_header = datetime.datetime.now()
right_now_header = str(right_now_header.strftime("%I%p"))
right_now_header


# In[100]:


df.to_csv('slick-deals-products-'+ right_now +'.csv' , index=False)


# In[101]:


filename = 'slick-deals-products-'+ right_now +'.csv'
filename


# In[102]:


response = requests.post(
        "https://api.mailgun.net/v3/sandboxf739b30cd9aa47bf9fb818fc4c6883da.mailgun.org/messages",
        auth=("api", mailgun_key),
        files=[("attachment", open(filename))],
        data={"from": "Excited User <mailgun@sandbox69f4b1683cf340f1b876b47ae74e0d74.mailgun.org>",
              "to": "Excited User <mailgun@sandbox69f4b1683cf340f1b876b47ae74e0d74.mailgun.org>",
              "subject": "Here is your "+ right_now_header+" briefing",
              "text": " "})

