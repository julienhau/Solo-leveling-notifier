#! python3

import requests
import bs4
import sys
from currentchap import currentchap

res = requests.get(f'https://sololeveling.net/manga/solo-leveling-chapter-{currentchap}/')
bs = bs4.BeautifulSoup(res.text, 'html.parser')

if bs.find(string = 'Next Chapter') == None:
	sys.exit()

from twilio.rest import Client

YOUR_NUMBER = 

account_sid = YOUR_SID
auth_token = YOUR_AUTH_TOKEN
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body=f'Your chapter code is https://sololeveling.net/manga/solo-leveling-chapter-{currentchap+1}/',
                              from_='whatsapp:+14155238886',
                              to='whatsapp: YOUR_NUMBER'
                          )

print(message.sid)

f = open('currentchap.py', 'w')
f.write(f'currentchap={currentchap+1}')
f.close()
