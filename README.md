# Authify Python API Wrapper


This is the official Python API Wrapper for [Authify](https://authify.biz).



### Login User

---

```python
from authify import api
import os


auth_instance = api("program version", "program key", "program api/encryption key")
auth_instance.init()

option = int(
    input('Press 1 to start')
)


if option == 1:

    _user = input('write your username >> ')

    _pass = input('now write your password >> ')

    if auth_instance.login(_user, _pass):
        user_data = auth_instance.user_data

        print(user_data.username)

        print(user_data.email)

        print(user_data.expires)

        print(user_data.var)

        print(user_data.rank)
    else:
        print('Error')
else:
    print('not available option')

```



### Register User

---

```python
from authify import api
import os


auth_instance = api("program version", "program key", "program api/encryption key")
auth_instance.init()

option = int(
    input('Press 1 to start')
)

if option == 1:

    _user = input('write your username >> ')

    _email = input('now write your email >> ')

    _pass = input('now write your password >> ')

    _token = input('now your token!! >> ')

    if auth_instance.register(_user, _email, _pass, _token):
        print('registered successfully!!')
    else:
        print('Error')
else:
    print('not available option')
```



### Activate User Sub

---

```python
from authify import api
import os


auth_instance = api("program version", "program key", "program api/encryption key")
auth_instance.init()

option = int(
    input('Press 1 to start')
)


if option == 1:

    _user = input('write your username >> ')
    _token = input('now, write your token >> ')


    if auth_instance.activate(_user, _token):
        print('activated successfully!!')
    else:
        print('Error')
else:
    print('not available option')


```



### All in one

---

```python
from authify import api
import os


auth_instance = api("program version", "program key", "program api/encryption key")
auth_instance.init()

option = int(
    input('Press 1 to start')
)

if option == 1:

    _token = input('write your token >> ')


    if auth_instance.all_in_one(_token):
        user_data = auth_instance.user_data

        print(user_data.username)

        print(user_data.email)

        print(user_data.expires)

        print(user_data.var)

        print(user_data.rank)
    else:
        print('Error')
else:
    print('not available option')
```

### Complete Setup
---

```python
#pip install Authify==0.0.2
from Authify import api

import os


def watermark():
    os.system('cls')
    print('--> Authify Example <--')


auth_instance = api("VERSION", "PROGRAM KEY", "API ENC KEY")

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
```
