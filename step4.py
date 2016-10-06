#Great job -- but we’re not done with collections.

#In this challenge, the API is going to give you another dictionary. The first value, prefix, is a string. The second value, array, is an array of strings. 
#Your job is to return an array containing only the strings that do not start with that prefix.

#Note: The strings in your array should be in the same order as in the original array.

#POST your token here:

#http://challenge.code2040.org/api/prefix

#Once you’ve built your array, POST a dictionary here:

#http://challenge.code2040.org/api/prefix/validate

#Use the key token for your token.

#Use the key array for your array.

#Hint: You’ll need a little string-fu to complete this challenge. But rest assured: comparing the beginnings of strings is a common task. 
#Your platform’s standard libraries might even have some code to help you do this.


import requests
import json

token = "dc12b6952158de030df0dea0a4d4b765"
data = {
    "token": token
}
url = "http://challenge.code2040.org/api/prefix"
response = requests.post(url=url, data=data)
dictionary = response.json()

#Grabbing the words array and prefix from the dictionary
array = dictionary.get("array")
prefix = dictionary.get("prefix")

#A for loop that grabs words that do not start with the prefix and adds them to the array
result = [word for word in array if not word.startswith(prefix)]

data['array'] = result

#The data has converted into json format
url = "http://challenge.code2040.org/api/prefix/validate"
response = requests.post(url=url, json=data)
