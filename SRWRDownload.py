# -*- coding: utf-8 -*-
"""
Download daily zip file from Scottish Road Works Register

@author: NMacEwan
"""
import zipfile
import json
import requests


# url for request to get url for actual download
# https://downloads.srwr.scot//export/api/v1/daily

url = 'https://downloads.srwr.scot//export/api/v1/daily'


geturl = requests.get(url, allow_redirects=True)

# convert response into dictionary and extract url for zip download

downloadurl = json.loads(geturl.content.decode('utf-8'))['url']

print(downloadurl)

# request daily file
getzip = requests.get(downloadurl, allow_redirects=True)


# write data to zip file
with open('Daily.zip', 'wb') as file:
    file.write(getzip.content)

# unzip downloaded file

with zipfile.ZipFile('Daily.zip', 'r') as zip_file:
    zip_file.extractall()
    