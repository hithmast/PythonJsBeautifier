import requests #IMPORT PyLIBRARY
import jsbeautifier

url = input("Enter URL : ")
url_ = str(url)
param1 = input("Enter Param: ") #ADD more Parameters if you need 
param1_value = input("Enter Param. VALUE : ") #MORe Values TOO ^_^ 
r = requests.get(url_,data = {param1:param1_value}) #MAKING HTTP GET REQUEST 

code =r.status_code #RESPONSE CODE :
headers = r.headers 
encodeing =r.encoding
text = r.text
print("Code: ",code)
print("headers : ",headers)
print("encoding : ",encodeing)
print("Text : ",text)

print("BEAUTIFY ")

res = jsbeautifier.beautify(text)
if True:
	print("DONE++")	
	print(res,file=open("beautified.txt","x")) #cat TEXT File for Results

else:
	print("FAILED")

