import requests
import os 
from PIL import Image
from IPython.display import IFrame
url='https://www.ibm.com/'
r=requests.get(url)
print("status: ",r.status_code)
print("headers: ",r.request.headers)
print("body: ",r.request.body)
response_header=r.headers
print("response headers: ",response_header)
print("date of obtaining: ",response_header["Date"])
print("Content Data Type: ",response_header["Content-Type"])
print("encoding : ",r.encoding)
#As the content type is text so we use attribute text
print("text content: ",r.text[0:100])
# Use single quotation marks for defining string like images
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r=requests.get(url)
print(r.headers)
print(r.headers['Content-Type'])
path=os.path.join(os.getcwd(),'image.png')
print(path)
with open(path,'wb') as f:
    f.write(r.content)
print(Image.open(path).show())
url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"
path=os.path.join(os.getcwd(),"example.txt")
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)
url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}
r=requests.get(url_get,params=payload)
print(r.url)
print("request body:", r.request.body)
print(r.status_code)
print(r.text)
print(r.headers['Content-Type'])
print(r.json())
print(r.json()['args'])
url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)
print("POST request URL:",r_post.url )
print("GET request URL:",r.url)
#print("POST request body:",r_post.request.body)
#print("GET request body:",r.request.body)
print("POST request URL:", r_post.url)  # Use r_post instead of response
print(r_post.json()['form'])


