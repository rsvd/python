import requests
import time
f = open('inputfile.txt', 'r')

log= {}

hostname=''
url=''
for line in f:
    
    keyvalue = line.split('=')
     
    if(keyvalue[0]=="hostname"):
        hostname=keyvalue[1].rstrip()
        hostname=hostname[1:-1]
    if(keyvalue[0]=='url'):
        url=keyvalue[1].rstrip()
        url=url[1:-1]
        
    
print(hostname)
print(url)    

params = {'apikey': '-YOUR API KEY HERE-', 'url':hostname + url}
response = requests.post('https://www.virustotal.com/vtapi/v2/url/scan', data=params)
json_response = response.json()
print(json_response)

time.sleep(1)


headers = {
  "Accept-Encoding": "gzip, deflate",
  "User-Agent" : "gzip,  My Python requests library example client or username"
  }
params = {'apikey': '-YOUR API KEY HERE-', 'resource':hostname + url}
response = requests.post('https://www.virustotal.com/vtapi/v2/url/report',
  params=params, headers=headers)
json_response = response.json()
print(json_response)




