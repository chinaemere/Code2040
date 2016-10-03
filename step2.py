##The first one is straightforward. You’re going to reverse a string.

##That is, if the API says “cupcake,” you’re going to send back “ekacpuc.”

##POST a JSON dictionary with the key token and your token value to this endpoint:

##http://challenge.code2040.org/api/reverse

##This endpoint will return a string that your code should then reverse, as in the example above.

##Once that string is reversed, send it back to us. POST some JSON to:

##http://challenge.code2040.org/api/reverse/validate

##Use the token for your token.

##Use the key string for your reversed string./

import requests

token = "dc12b6952158de030df0dea0a4d4b765"
data = {
    "token": token
}
url = "http://challenge.code2040.org/api/reverse"

##POSTing the string
response = requests.post(url=url, data=data)
string = response.content

##Reversing the string 
reversedString = string[::-1]
data["string"] = reversedString

##POSTing the reversed string
url = "http://challenge.code2040.org/api/reverse/validate"
response = requests.post(url=url, data=data)