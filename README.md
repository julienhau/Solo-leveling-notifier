# Solo-leveling-notifier
A python script which notifies when a new chapter of solo leveling is released 

This script uses BeautifulSoup to parse the html page and check if there is a next button on the last chapter checked.
The last chapter is saved in a python file called currentchap.
The script then uses a messaging API (Twilio) to send a notifying message.
