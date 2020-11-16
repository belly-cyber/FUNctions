#!/usr/bin/env python3
# coding: utf-8

# In[1]:


def likes(names):
    '''
    returns who has like a post 
    '''
    if len(names)>=1:
        if len(names)==1:
            place_holder=names[0]
        else:
            place_holder="no one"
        likes_str="{} likes this".format(place_holder)
        
    elif len(names)==2:
        place_holder=' and '.join(names)
    
    elif len(names)==3:
        place_holder="{}, {} and {}".format(names[0],names[1],names[2])
    
    elif len(names)>3:
        place_holder="{},{} and {} others ".format(names[0],names[1],len(names)-2)
    
    else:
        place_holder="no one"

    likes_str="{} like this".format(place_holder)
    return(likes_str)


# In[ ]:





# In[2]:


def alphabet_position(text):
    '''
    outputs number of the character in association with the ascii aphabet
    '''
    index=[]
    for x in text.lower():
        if x in string.ascii_lowercase:
            index.append(str(string.ascii_lowercase.index(x)+1))
    return(index)


# In[ ]:





# In[193]:


def row_sum_odd_numbers(n):
    '''
    over complicated n to the 3rd power sum 
    '''
    
    result=[x for x in range(n*(n+1)) if x%2!=0][-n:]
    the_sum=sum(result)
    return(the_sum)


# In[ ]:





# In[3]:


def get_middle(s):
    '''
    get the middle element of a str if not even get the middle two
    '''
    len_of_s=len(s)
        
    if len_of_s<=2:
        result=s
    elif len_of_s%2==0:
        index=len_of_s//2-1
        result=s[index:-index]
        
    else:
        result=s[len_of_s//2]
    return(result)


# In[ ]:





# In[125]:


def tower_builder(n_floors):
    '''
    builds a triangle tower 
    '''
    tower=[]
    for x in range(n_floors):
        floor='*'*(x*2+1)
        total_white_spaces=(n_floors)*2-len(floor)
        outer_spaces=' '*(total_white_spaces//2)
        floor=outer_spaces+floor+outer_spaces
        tower.append(floor)
    return(tower)


# In[ ]:





# In[239]:


def sort_array(source_array):
    '''
    sorts ascending odd numbers but leaves even numbers on their place.
    '''
    if len(source_array)==0:
        return(source_array)
    
    odd_list=sorted([item for item in source_array if item%2!=0])
    [odd_list.insert(index,item) for index,item in enumerate(source_array) if item%2==0]
    return(odd_list)


# In[ ]:





# In[267]:


def count_smileys(arr):
    import re
    '''
    counts the number of smiley with a unique set of parameters
    '''
    result=re.findall(r'(:|;){1}(-|~)?(\)|D)',''.join(arr))
    return(len(result))


# In[278]:


def find_uniq(arr):
    '''
    finds the unique element not repeted in side a list
    '''
    return([x for x in set(arr) if arr.count(x)==1][0])


# In[ ]:





# In[345]:


def zero(value='0'): 
    if value!='0':
        value=eval('0'+value)
    return(value)

def one(value='1'):
    if value!='1':
        value=eval('1'+value)
    return(value)

def two(value='2'):
    if value!='2':
        value=eval('2'+value)
    return(value)

def three(value='3'): 
    if value!='3':
        value=eval('3'+value)
    return(value)

def four(value='4'): 
    if value!='4':
        value=eval('4'+value)
    return(value)

def five(value='5'):
    if value!='5':
        value=eval('5'+value)
    return(value)

def six(value='6'): 
    if value!='6':
        value=eval('6'+value)
    return(value)

def seven(value='7'):
    if value!='7':
        value=eval('7'+value)
    return(value)

def eight(value='8'): 
    if value!='8':
        value=eval('8'+value)
    return(value)

def nine(value='9'): 
    if value!='9':
        value=eval('9'+value)
    return(value)

def plus(digit):
    return('+'+digit)
def minus(digit):
    return('-'+digit)
def times(digit): 
    return('*'+digit)
def divided_by(digit):
    return('//'+digit)


# In[346]:





# In[414]:


def decodeMorse(morse_code):
    MORSE_CODE= {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS', '  ': ' '}
    readable=' '.join([''.join([MORSE_CODE[word] for word in morse.split() if word in MORSE_CODE.keys()]) for morse in morse_code.strip().split('  ')])
    return(readable)


# In[ ]:





# In[427]:


def song_decoder(song,keyword='WUB'):
    import re 
    song=re.sub('({})+'.format(keyword),' ',song,)
    return(song.strip())


# In[ ]:





# In[448]:


def find_outlier(integers):
    print(integers[:2])
    if (integers[0]+integers[3])%2==0 and (integers[1]+integers[3])%2==0:
        return [x for x in integers if x%2==0][0]
    else:
        return [x for x in integers if x%2!=0][0]


def order_weight(strng):
    w={sum([int(y) for y in x]):x for x in strng.split()} 
    for x in sorted(w.items())
    
    print(w)


def inthisweek(date):
    from datetime import *
    """
    input = str of 'year-month-day'
    returns wether a given date falls in the current work week"
    """       
    date=datetime.strptime(date,"%Y-%m-%d").date()
    today = datetime.today().date()
    days = timedelta(today.weekday())
    monday=today-days
    
    if monday <= date:
        return True
    else:
        return False





# In[ ]:




