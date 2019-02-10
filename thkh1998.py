import requests

def send_message (chat_id,text,reply_id):
    bot_id='693605348:AAGNQ27QngVX8sVYPv-TfKY1tZI7nIQFnpg'
    url='https://api.telegram.org/bot%s/sendMessage'% bot_id
    answer=requests.post(url,data={'chat_id':chat_id,'text':text,'reply_to_message_id':reply_id})
    return(answer.json())

def set_chat_title (chat_id,title):
    bot_id='693605348:AAGNQ27QngVX8sVYPv-TfKY1tZI7nIQFnpg'
    url='https://api.telegram.org/bot%s/setChatTitle'% bot_id
    answer=requests.post(url,data={'chat_id':chat_id,'title':title})
    return(answer.json())

def pin_chat_message(chat_id,message_id):
    bot_id='693605348:AAGNQ27QngVX8sVYPv-TfKY1tZI7nIQFnpg'
    url='https://api.telegram.org/bot%s/pinChatMessage'% bot_id
    answer=requests.post(url,data={'chat_id':chat_id,'message_id':message_id})
    return(answer.json())

def get_chat(chat_id):
    bot_id='693605348:AAGNQ27QngVX8sVYPv-TfKY1tZI7nIQFnpg'
    url='https://api.telegram.org/bot%s/getChat'% bot_id
    answer=requests.post(url,data={'chat_id':chat_id})
    return(answer.json())

def get_chat_member(chat_id,user_id) :
    bot_id='693605348:AAGNQ27QngVX8sVYPv-TfKY1tZI7nIQFnpg'
    url='https://api.telegram.org/bot%s/getChatMember'% bot_id
    answer=requests.post(url,data={'chat_id':chat_id,'user_id':user_id})
    return(answer.json())

def get_update(offset) :
    bot_id='693605348:AAGNQ27QngVX8sVYPv-TfKY1tZI7nIQFnpg'
    url='https://api.telegram.org/bot%s/getUpdates'% bot_id
    answer=requests.post(url,data={'offset':-1})
    return(answer.json())

def get_bot_user():
    
    username_id=[]
    for i in range (0,20):
        answer=get_update(i)
        username_id.append([answer['result'][0]['message']['from']['username'],answer['result'][0]['message']['from']['id']])
    return username_id

#print(send_message('@thkh1998_ch','even the function is working',0))
#print(set_chat_title('@thkh1998_ch','title has changed !'))
#print(pin_chat_message('@thkh1998_ch',5))
#print(get_chat('@thkh1998_ch'))
#print(get_chat_member('@thkh1998_ch',?))
#print (answer['result'][1])
#print (answer['result'][1]['message']['from']['username'])
#print (answer)
#print (get_updates())
#print (len(answer['result']))
#print(get_bot_users())

user_id=get_bot_user()
print(user_id)
bot_id='693605348:AAGNQ27QngVX8sVYPv-TfKY1tZI7nIQFnpg'
url='https://api.telegram.org/bot%s/getUpdates'% bot_id
answer=requests.post(url)
print (answer)