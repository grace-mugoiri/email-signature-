"""import necessary modules"""
from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

from qotd import qotd
DATA = {'signature': qotd.qotd()}   # quote source up-to-you!

SCOPES = 'https://www.googleapis.com/auth/gmail.settings.basic'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))
# this entire block optional if you only have one sender address
addresses = GMAIL.users().settings().sendAs().list(userId='me',
        fields='sendAs(isPrimary,sendAsEmail)').execute().get('sendAs')
for address in addresses:
    if address.get('isPrimary'):
        break
rsp = GMAIL.users().settings().sendAs().patch(userId='me',
        sendAsEmail=address['sendAsEmail'], body=DATA).execute()
print("Signature changed to '%s'" % rsp['signature'])

