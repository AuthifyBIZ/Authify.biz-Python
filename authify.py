import json  # json

import binascii  # hex encoding

import requests  # https requests

from uuid import uuid4  # gen random guid

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
# aes + padding, sha256

import webbrowser, platform, subprocess, datetime

from requests_toolbelt.adapters.fingerprint import FingerprintAdapter

# doesn't output the responses in a message box

class api:
    program_version = program_key = api_key = ""

    is_initialized = show_messages = logged_in = False

    def __init__(self, version, program_key, api_key, show_messages=True):
        self.program_version = version

        self.program_key = program_key

        self.api_key = api_key

        self.show_messages = show_messages

    session_id = session_iv = ""

    def init(self):
        self.session_iv = str(uuid4())[:8]

        init_iv = SHA256.new(self.session_iv.encode()).hexdigest()

        post_data = {
            "version": encryption.encrypt(self.program_version, self.api_key, init_iv),
            "session_iv": encryption.encrypt(self.session_iv, self.api_key, init_iv),
            "api_version": encryption.encrypt("1.2", self.api_key, init_iv),

            "program_key": binascii.hexlify(self.program_key.encode()),
            "init_iv": init_iv
        }

        response = self.__do_request("init", post_data)

        if response == "program_doesnt_exist":
            print("The program key you tried to use doesn't exist")
            return

        response = encryption.decrypt(response, self.api_key, init_iv)

        decoded_response = json.loads(response)

        if not decoded_response["success"]:
            print(decoded_response["message"])

        response_data = decoded_response["response"].split("|")

        if response_data[0] == "wrong_version":
            webbrowser.open(response_data[1])
            return

        self.is_initialized = True

        self.session_iv += response_data[1]

        self.session_id = response_data[2]

    def login(self, username, password, hwid=None):
        if hwid is None: hwid = others.get_hwid()

        if not self.is_initialized:
            print("The program wasn't initialized")
            return False

        post_data = {
            "username": encryption.encrypt(username, self.api_key, self.session_iv),
            "password": encryption.encrypt(password, self.api_key, self.session_iv),
            "hwid": encryption.encrypt(hwid, self.api_key, self.session_iv),

            "sessid": binascii.hexlify(self.session_id.encode())
        }

        response = self.__do_request("login", post_data)

        response = encryption.decrypt(response, self.api_key, self.session_iv)

        decoded_response = json.loads(response)

        self.logged_in = decoded_response["success"]

        if not self.logged_in and self.show_messages:
            print(decoded_response["message"])
        elif self.logged_in:
            self.__load_user_data(decoded_response["user_data"])

        return self.logged_in

    def register(self, username, email, password, token, hwid=None):
        if hwid is None: hwid = others.get_hwid()

        if not self.is_initialized:
            print("The program wasn't initialized")
            return False

        post_data = {
            "username": encryption.encrypt(username, self.api_key, self.session_iv),
            "email": encryption.encrypt(email, self.api_key, self.session_iv),
            "password": encryption.encrypt(password, self.api_key, self.session_iv),
            "token": encryption.encrypt(token, self.api_key, self.session_iv),
            "hwid": encryption.encrypt(hwid, self.api_key, self.session_iv),

            "sessid": binascii.hexlify(self.session_id.encode())
        }

        response = self.__do_request("register", post_data)

        response = encryption.decrypt(response, self.api_key, self.session_iv)

        decoded_response = json.loads(response)

        if not decoded_response["success"] and self.show_messages:
            print(decoded_response["message"])

        return decoded_response["success"]

    def activate(self, username, token):
        if not self.is_initialized:
            print("The program wasn't initialized")
            return False

        post_data = {
            "username": encryption.encrypt(username, self.api_key, self.session_iv),
            "token": encryption.encrypt(token, self.api_key, self.session_iv),

            "sessid": binascii.hexlify(self.session_id.encode())
        }

        response = self.__do_request("activate", post_data)

        response = encryption.decrypt(response, self.api_key, self.session_iv)

        decoded_response = json.loads(response)

        if not decoded_response["success"] and self.show_messages:
            print(decoded_response["message"])

        return decoded_response["success"]

    def all_in_one(self, token, hwid=None):
        if hwid is None: hwid = others.get_hwid()

        if self.login(token, token, hwid):
            return True

        elif self.register(token, token + "@email.com", token, token, hwid):
            exit()
            return True

        return False

    def file(self, file_name, hwid=None):
        if hwid is None: hwid = others.get_hwid()

        if not self.is_initialized:
            print("The program wasn't initialized")
            return "not_initialized".encode()

        if not self.logged_in:
            print("You can only grab server sided files after being logged in.")
            return "not_logged_in".encode()

        post_data = {
            "file_name": encryption.encrypt(file_name, self.api_key, self.session_iv),
            "sessid": binascii.hexlify(self.session_id.encode())
        }
        
        response = self.__do_request("file", post_data)

        response = encryption.decrypt(response, self.api_key, self.session_iv)

        decoded_response = json.loads(response)

        if not decoded_response["success"] and self.show_messages:
            print(decoded_response["message"])

        return binascii.unhexlify(decoded_response["response"])

    def var(self, var_name, hwid=None):
        if hwid is None: hwid = others.get_hwid()

        if not self.is_initialized:
            print("The program wasn't initialized")
            return "not_initialized"

        if not self.logged_in:
            print("You can only grab server sided variables after being logged in.")
            return "not_logged_in"

        post_data = {
            "var_name": encryption.encrypt(var_name, self.api_key, self.session_iv),
            "sessid": binascii.hexlify(self.session_id.encode())
        }

        response = self.__do_request("var", post_data)

        response = encryption.decrypt(response, self.api_key, self.session_iv)

        decoded_response = json.loads(response)

        if not decoded_response["success"] and self.show_messages:
            print(decoded_response["message"])

        return decoded_response["response"]

    def log(self, message):
        if self.user_data.username == "": self.user_data.username = "NONE"

        if not self.is_initialized:
            print("The program wasn't initialized")
            return "not_initialized"

        post_data = {
            "username": encryption.encrypt(self.user_data.username, self.api_key, self.session_iv),
            "message": encryption.encrypt(message, self.api_key, self.session_iv),

            "sessid": binascii.hexlify(self.session_id.encode())
        }

        self.__do_request("log", post_data)

    def __do_request(self, type, post_data):
        headers = {"User-Agent": self.__user_agent}

        rq = requests.Session()

        rq.mount(
            self.__api_endpoint,
            FingerprintAdapter('ac94e131a7aee8bfec3b856fcc3aaa19a1af9dca1f886d85456e4a26ca1e83dc')
        )

        rq_out = rq.post(
            self.__api_endpoint + "?type=" + type, data=post_data, headers=headers, verify=False
        )

        return rq_out.text

    # region user_data
    class user_data_class:
        username = email = var = ""
        expires = datetime.datetime.now()
        rank = 0

    user_data = user_data_class()

    def __load_user_data(self, data):
        self.user_data.username = data["username"]

        self.user_data.email = data["email"]

        self.user_data.expires = datetime.datetime.fromtimestamp(int(data["expires"]))

        self.user_data.var = data["var"]

        self.user_data.rank = data["rank"]

    # endregion

    __api_endpoint = "https://authify.biz/api/handler.php"

    __user_agent = "Mozilla Authify"


class others:
    @staticmethod
    def get_hwid():
        if platform.system() != "Windows":
            return "None"

        cmd = subprocess.Popen("wmic useraccount where name='%username%' get sid", stdout=subprocess.PIPE, shell=True)

        (suppost_sid, error) = cmd.communicate()

        suppost_sid = suppost_sid.split(b'\n')[1].strip()

        return suppost_sid.decode()


class encryption:
    @staticmethod
    def encrypt_string(plain_text, key, iv):
        plain_text = pad(plain_text, 16)

        aes_instance = AES.new(key, AES.MODE_CBC, iv)

        raw_out = aes_instance.encrypt(plain_text)

        return binascii.hexlify(raw_out)

    @staticmethod
    def decrypt_string(cipher_text, key, iv):
        cipher_text = binascii.unhexlify(cipher_text)

        aes_instance = AES.new(key, AES.MODE_CBC, iv)

        cipher_text = aes_instance.decrypt(cipher_text)

        return unpad(cipher_text, 16)

    @staticmethod
    def encrypt(message, enc_key, iv):
        try:
            _key = SHA256.new(enc_key.encode()).hexdigest()[:32]

            _iv = SHA256.new(iv.encode()).hexdigest()[:16]

            return encryption.encrypt_string(message.encode(), _key.encode(), _iv.encode()).decode()
        except:
            print("Invalid API/Encryption key")
            return ""

    @staticmethod
    def decrypt(message, enc_key, iv):
        try:
            _key = SHA256.new(enc_key.encode()).hexdigest()[:32]

            _iv = SHA256.new(iv.encode()).hexdigest()[:16]

            return encryption.decrypt_string(message.encode(), _key.encode(), _iv.encode()).decode()
        except:
            print("Invalid API/Encryption key")
            return ""
