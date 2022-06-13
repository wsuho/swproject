#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys
import urllib.request
import pandas as pd
import json
import re
client_id = "cHD9pPY6pssTuar5LXwc"
client_secret = "yOJryxOkyp"

query = urllib.parse.quote(input("검색어 입력: "))
idx = 0
display = 5
start = 1
end = 10

web_df = pd.DataFrame(columns=("Title", "LInk", "Description")) 

for start_index in range(start,end,display):

    url = "https://openapi.naver.com/v1/search/webkr?query=" + query    + "&display=" + str(display)    + "&start=" + str(start_index)

    request = urllib. request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib. request.urlopen(request)
    rescode = response. getcode()
    if(rescode==200):
        response_body = response.read()
        response_dict = json. loads(response_body.decode('utf-8'))
        items =  response_dict['items']
        for item_index in range(0, len(items)):
            remove_tag = re. compile('<.*?>')
            title = re. sub(remove_tag,'',items[item_index]['title'])
            link = items[item_index]['link']
            description = re. sub(remove_tag,'',items[item_index]['description'])
            web_df. loc[idx] = [title, link, description]
            idx += 1
    else:
        print("Error Code:" + rescode)

web_df


# In[7]:


import os
import sys
import urllib.request
import pandas as pd
import json
import re
client_id = "cHD9pPY6pssTuar5LXwc"
client_secret = "yOJryxOkyp"

query = urllib.parse.quote(input("검색어 입력: "))
idx = 0
display = 5
start = 1
end = 10
sort = "sim"

news_df = pd.DataFrame(columns=("Title", "LInk","Original Link", "Description","Publication Date")) 

for start_index in range(start,end,display):

    url = "https://openapi.naver.com/v1/search/news?query=" + query    + "&display=" + str(display)    + "&start=" + str(start_index)    +"&sort=" +sort

    request = urllib. request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib. request.urlopen(request)
    rescode = response. getcode()
    if(rescode==200):
        response_body = response.read()
        response_dict = json. loads(response_body.decode('utf-8'))
        items =  response_dict['items']
        for item_index in range(0, len(items)):
            remove_tag = re. compile('<.*?>')
            title = re. sub(remove_tag,'',items[item_index]['title'])
            link = items[item_index]['link']
            original_link = items[item_index]['originallink']
            description = re. sub(remove_tag,'',items[item_index]['description'])
            pub_date = items[item_index]['pubDate']
            news_df. loc[idx] = [title, original_link, link, description, pub_date]
            idx += 1
    else:
        print("Error Code:" + rescode)

news_df