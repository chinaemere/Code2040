#Next, let’s check your skills for working with collections.

#We’re going to send you a dictionary with two values and keys. The first value, needle, is a string. The second value, haystack, is an array of strings. You’re going to tell the API where the needle is in the array.

#Grab that dictionary from here, again by POSTing your token:

#http://challenge.code2040.org/api/haystack

#Locate the needle in the haystack array. You’re going to send back the position, or “index,” of the needle string. The API expects indexes to start counting at 0.

#POST your results to:

#http://challenge.code2040.org/api/haystack/validate

#Use the key token for your token.

#Use the key needle for the integer representing where the needle was in the array.

#Hint: You’ll probably use a loop to solve this one.


import requests

token = "dc12b6952158de030df0dea0a4d4b765"
data = {
    "token": token
}
url = "http://challenge.code2040.org/api/haystack"
response = requests.post(url=url, data=data)
dictionary = response.json()

# grab haystack from dictionary 
needle = dictionary.get("needle")
haystack = dictionary.get("haystack")


for i in range(len(haystack)):
    if needle == haystack[i]:
        index = i
        break

# POSTing solution to the endpoint
data["needle"] = index
url = "http://challenge.code2040.org/api/haystack/validate"
requests.post(url=url, data=data)

