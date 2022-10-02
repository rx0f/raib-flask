import sys
from bs4 import BeautifulSoup 
import requests

urlll = sys.argv[1]
fff = requests.get(urlll)
soup = BeautifulSoup(fff.text, 'lxml')
tg = soup.find_all(class_="download_zip")
meta = tg[0]['href']
image = tg[1]['href']
meta = 'https://www.missionjuno.swri.edu' + meta
image = 'https://www.missionjuno.swri.edu/' + image


req = requests.get(meta)
req1 = requests.get(image)

# Split URL to get the file name
filename = "DATA.zip"
 
# Writing the file to the local file system
with open(filename,'wb') as output_file:
    output_file.write(req.content)
print('Downloading Completed')
with open('images.zip','wb') as output_file:
    output_file.write(req1.content)
print('Downloading Completed')

from zipfile import ZipFile 
import os  
# specifying the name of the zip file
file = "DATA.zip"
  
# open the zip file in read mode
with ZipFile(file, 'r') as zip: 
    # list all the contents of the zip file
    # extract all files
    zip.extractall() 
with ZipFile('images.zip', 'r') as zip: 
    # list all the contents of the zip file
    # extract all files
    zip.extractall() 
#link = sys.args[1]
import shutil
name = ''
for i in os.listdir(os.getcwd() +  '/ImageSet'):
    if i.__contains__('-raw.png'):
        name = i
shutil.move('ImageSet/' + name, 'raw.png')

shutil.move('DataSet/' + os.listdir(os.getcwd() +  '/DataSet')[0], 'raw.json')

exec(open('deploy.py').read())
