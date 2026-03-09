''' Extracting Data from XML '''
''' url: https://py4e-data.dr-chuck.net/comments_2203406.xml '''

import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

sum = 0

# ignore certificate verification
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter url here: ').strip()
# fetch data
response = urllib.request.urlopen(url, context=ctx)
data = response.read().decode() # bytes to string 
root = ET.fromstring(data)    # string to xml 

comments_lst_tags = root.findall('comments/comment')
# print(comments_lst_tags)
for count_tags in comments_lst_tags:
    num = count_tags.find('count').text
    num = int(num)
    sum = sum + num

print(sum)