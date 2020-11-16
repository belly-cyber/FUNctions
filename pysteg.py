#!/usr/bin/env python3
# coding: utf-8

# In[1]:


import os,re,random,requests


# In[2]:


def crypto(message):
    """this is the function that will ofuscate the message"""
    new_message=b''
    for letter in message:
        num = ord(letter)
        hex_num = hex(num)[2:]
        new_message+=b'\\x'+bytes(hex_num,'utf-8')
    return new_message


def decrypto(cryt_message):
    """this one will return the ofusacated message to plain text"""
    message=''
    for x in cryt_message.split(b'\\x'):
        x =str(x,'utf-8')
        letter = bytes.fromhex(x)
        letter = str(letter,'utf-8')
        message+=letter
    return message


# In[7]:


description = "type in name of image.\nif you dont have an image type 'random' for random image pulled from reddit."
earthporn="https://www.reddit.com/r/EarthPorn/.rss"
reddit_friendly_header = {"User-Agent" : "pysego:com.example.myredditapp:v1",}
#https://github.com/reddit-archive/reddit/wiki/API


# In[4]:


user_input = input(description)


# In[8]:


if "random" in user_input.lower():
    metadata       = requests.get(earthporn,reddit_friendly_header).text
    image_list     = re.findall("https://i\.redd\.it.*?\&",metadata)
    image_list     = [x[:-1] for x in image_list]
    image_url      = random.choice(image_list)
    filename       = 'stock_img.jpg'
    original_image = requests.get(image_url).content

else:
    with open(user_input,'rb') as f:
            original_image = f.read()
    filename = user_input
    
new_image='new_'+filename

# In[10]:


hidden_message = input('what do you want to hide?')
crypto_message = crypto(hidden_message)
print(hidden_message,crypto_message)


# In[11]:


original_image+=crypto_message


# In[13]:


with open(new_image,'wb') as f:
    f.write(original_image)


# In[14]:


print('completed hiding your dirty secret to {}'.format(filename))


# In[ ]:




