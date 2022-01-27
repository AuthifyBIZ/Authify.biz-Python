# import via file or pip install Authify
from authify import api

import os


def watermark():
    os.system('cls')
    print('--> Authify Example <--')


auth_instance = api("program version", "program key", "program api/encryption key")

auth_instance.init()

watermark()

option = int(
    input('write your option : \n1) Login\n2) Register\n3) Activate\n4) All In One\n')
)

if option == 1:
    watermark()

    _user = input('write your username : ')

    watermark()

    _pass = input('now write your password : ')

    watermark()

    if auth_instance.login(_user, _pass):
        user_data = auth_instance.user_data

        print(user_data.username)

        print(user_data.email)

        print(user_data.expires)

        print(user_data.var)

        print(user_data.rank)
    else:
        print(':ddd !!!')

elif option == 2:
    watermark()

    _user = input('write your username : ')

    watermark()

    _email = input('now write your email : ')

    watermark()

    _pass = input('now write your password : ')

    watermark()

    _token = input('now your token!! : ')

    watermark()

    if auth_instance.register(_user, _email, _pass, _token):
        print('registered successfully!!')
    else:
        print(':(((')

elif option == 3:
    watermark()

    _user = input('write your username : ')

    watermark()

    _token = input('now, write your token : ')

    watermark()

    if auth_instance.activate(_user, _token):
        print('activated successfully!!')
    else:
        print(':(((')

elif option == 4:
    watermark()

    _token = input('write your token : ')

    watermark()

    if auth_instance.all_in_one(_token):
        user_data = auth_instance.user_data

        print(user_data.username)

        print(user_data.email)

        print(user_data.expires)

        print(user_data.var)

        print(user_data.rank)
    else:
        print(':ddd !!!')
else:
    print('not available option')
