#This script product by : erfan4lx - M4nifest0 Cyber Security Team
#Special tnx to : hack4lx
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv
print ('''




            \nThis script product by erfan4lx - M4nifest0 Cyber Security Team
            Special tnx to : hack4lx\n''')
# please disable the two verification code if this enable in your telegram account before using this software

api_id = input("Enter the API ID: ") # go to the my.telegram.org and API DEVEPLOMENT then copy the apt id and paste here
api_hash = str(input("Enter the API HASH: ")) # go to the my.telegram.org and API DEVEPLOMENT then copy the apt hash and paste here
phone = str(input("Enter the Phone: ")) # enter the your account phone number + Countery code example:+989124444444
client = TelegramClient(phone, api_id, api_hash)
 
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
 
 
chats = []
last_date = None
chunk_size = 200
groups=[]
 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
 
for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue
 
print('Choose a group to scrape members from:')
i=0
for g in groups:
    print(str(i) + '- ' + g.title)
    i+=1
 
g_index = input("Enter a Number: ")
target_group=groups[int(g_index)]
 
print('Fetching Members...')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)
 
print('Saving In file...')
with open("erfan4lx.csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
    for user in all_participants:
        if user.username:
            username= user.username
        else:
            username= ""
        if user.first_name:
            first_name= user.first_name
        else:
            first_name= ""
        if user.last_name:
            last_name= user.last_name
        else:
            last_name= ""
        name= (first_name + ' ' + last_name).strip()
        writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])      
print('Members scraped successfully.')
print ('''



            \nThis script product by erfan4lx - M4nifest0 Cyber Security Team
            Special tnx to : hack4lx\n''')
#This script product by : erfan4lx - M4nifest0 Cyber Security Team
#Special tnx to : hack4lx
