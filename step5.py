# Step V: The dating game

# Great job so far. The last challenge is a little different. You’re going to work with dates and times.

# The API will again give you a dictionary. The value for datestamp is a string, formatted as an ISO 8601 datestamp. The value for interval is a number of seconds.

# You’re going to add the interval to the date, then return the resulting date to the API. POST your token here:

# http://challenge.code2040.org/api/dating

# Then POST a dictionary with your results here:

# http://challenge.code2040.org/api/dating/validate

# Use the key token for your token.

# Use the key datestamp for an ISO 8601 datestamp string.

# Hints:

# Make sure your datestamp is formatted the same way as the one the API gives you.
# Dates are hard! Don’t feel badly if you’re scratching your head on this one. Most platforms have libraries to help with date and time tasks. 
# Don’t be afraid of using one to solve this challenge.

import requests
import dateutil.parser
import datetime

token = "dc12b6952158de030df0dea0a4d4b765"
data = {
    "token": token
}
url = "http://challenge.code2040.org/api/dating"
response = requests.post(url=url, data=data)
dictionary = response.json()

#grabbing datestamp and interval from the dictionary
datestamp = dictionary.get("datestamp")
interval = dictionary.get("interval")


dateObject = dateutil.parser.parse(datestamp)


newDateObject = dateObject + datetime.timedelta(seconds=interval)

#Converting the Date Object into ISO String format
newDateString = newDateObject.isoformat()

#Making sure it's formated correctly
data['datestamp'] = newDateString.replace('+00:00', 'Z')


#POSTing the solution to the endpoint
url = "http://challenge.code2040.org/api/dating/validate"
requests.post(url=url, data=data)
