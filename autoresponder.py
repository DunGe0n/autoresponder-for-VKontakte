#imports
import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType

#main
session = requests.Session()
login, password = 'Ваш логин, email или телефон / Your login, email or phone', 'Ваш пароль / Your password'
vk_session = vk_api.VkApi(login, password)
try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)
    return


longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.from_user: 
                    vk.messages.send(
                    user_id=event.user_id,
                    message='Ваше сообщение / Your message'
		)
            #elif event.from_chat:
                #vk.messages.send( 
                    #chat_id=event.chat_id,
                    #message='Ваш текст'
		#)    
