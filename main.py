import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import datetime
import time
appmail = Flask(__name__)
CORS(appmail)
# def pngr():
#     while True:
#         a = requests.get('')
#         if a.status_code == 200:
#             pass
#         else:
#             pass
#         time.sleep(600)
users = {}
plox = {}
@appmail.route('/')
def apr():
    a = f'''
    MAIN
--------------------------
BIG.mail - Your Python-AI Mail!
You need to help? Visit t.me/BIGmail_AI.
Our mail adress - @bigmail.BM
--------------------------
    MORE
--------------------------
Mail BM - A high-tech mail systemt. Suitable for production. Sometimes the database may be reset.
You search help? - Request to write a letter - /mail/action/send, request to check mail: /mail/action/check, request to clear mail: /mail/action/clear, request for help - /, REGISTER - /mail/registr.
Our community is FUNNY! Step into a world of letters and friendship!
--------------------------

Request: 200
Time: {datetime.datetime.now().hour}h : {datetime.datetime.now().minute}m
Fun :)
'''
    return a, 200
@appmail.route('/mail/registr', methods=['POST'])
def reg():
    try:
        data = request.get_json()
        if data:

            try:
                parol = data.get('password')
            except:
                return 'Oops... Please, write a your password. Password can"t be a "None". Key: "parol"', 400
            try:
                email = data.get('email')
                if email not in users:
                    try:
                        a = email.split('@')
                        if a[1] != 'bigmail.BM':
                            email = f'{a[0]}@bigmail.BM'
                        else:
                            pass
                    except:
                        return 'Enter a valid email address. Example: mymail@bigmail.BM', 403
                else:
                    return 'This email adress is already exists. Key: "email"',403
            except:
                return 'Oops... Please, write a your email adress. Email adress can"t be a "None". Key: "email"', 400
            if email not in plox:
                users[email] = {
                    'password': parol,
                    'attBLOK': 0,
                    'messages': []
                }
                return f'Registered your email! Password: {parol}, email address: {email}. Make a request to /mail/action/send and provide your password and email address. You can see examples at t.me/BIGmail_AI', 200
            else:
                plox[email]['deystvie'].append('Attempt to register at this address.')
                return f'This email address has been blocked due to suspicious activity and has been identified and added to the block database. All your actions associated with the extremist address {email} have been recorded in the block database.', 403
        else:
            return 'Your post-data can"t be a "None"... Please, visit t.me/BIGmail_AI to view the registration request!', 400

    except:
        return 'Oops... visit t.me/BIGmail_AI to view problems.', 504
@appmail.route('/mail/action/send', methods=['POST'])
def send():
    try:
        data = request.get_json()
        if data:
            try:
                email = data.get('email')
                if email in users:
                    pass
                else:
                    return 'There is no such email. Please register this address.', 403
            except:
                return 'Oops... Your data dont"t have a "email" key. Please, visit a t.me/BIGmail_AI to view POST - request.', 400
            try:
                message = data.get('message')
                if message:
                    try:
                        messges = message.split(' ')
                        for i in messges:
                            for x in ['bomb','terrorism', 'sex', 'porn', 'arson', 'murder', 'kill', 'violence']:
                                if x in i.lower():
                                    if email not in plox:
                                        plox[email] = {
                                            'deystvie': []
                                        }
                                    else:
                                        pass
                                    plox[email]['deystvie'].append(f'Suspected of Terrorism. Text: {message}')
                                    del users[email]
                                    return 'You have violated our policy. We do not support criminal activity. Your address has been blocked, and all activity has been recorded in our database.', 403
                                else:
                                    pass
                    except:
                        pass
                else:
                    pass
            except:
                return 'Oops... Your data dont"t have a "message" key. Please, visit a t.me/BIGmail_AI to view POST - request.', 400
            try:
                parol = data.get('password')
                if users[email]['password'] == parol:
                    users[email]['attBLOK'] = 0
                else:
                    if users[email]['attBLOK'] < 10:
                        users[email]['attBLOK'] += 1
                        if users[email]['attBLOK'] == 5:
                            users[email]['messages'] = ['HACK [5]: Urgent situation - your address has been attempted to be hacked 5 times. We have deleted all the emails, but we advise you to pay attention to this and warn everyone. If you continue attempts to hack, your address will be deleted. The message is not translated by AI for security and urgent reading.']
                            return 'BLOCKING: All emails from this email address have been removed from the database to ensure user security. All hacking attempts have been recorded and taken into account.', 403

                        return 'ANTI-FRAUD SYSTEM: We have detected an attempt to hack an email, which is prohibited by BIGmail policy. For security reasons, if further attempts occur, the email receiving multiple requests will be blocked.', 403
                    else:
                        del users[email]
                        return 'BLOCK: The address was permanently deleted.', 403
            except:
                return 'Oops... Please, write a your password. Password can"t be a "None". Key: "password"', 400
            try:
                sendto = data.get('to_email')
                if sendto in users:
                    pass
                else:
                    return 'There is no such contact. Most likely, he is not registered on the BIGmail network or his email was deleted due to fraud...', 404
            except:
                return 'Oops... Please, check a send to email-adress. Key: "to_email"', 400
            users[sendto]['messages'].append(f'{message} - FROM {email} | {datetime.datetime.now().day}d {datetime.datetime.now().month}m ]')
            return f'Message sent successfully! Sent to email {sendto}. BIGmail | 2026 ©', 200
        else:
            return 'Your post-data can"t be a "None"... Please, visit t.me/BIGmail_AI to view the registration request!', 400
    except:
        return 'Oops... visit t.me/BIGmail_AI to view problems.', 504
@appmail.route('/mail/action/check', methods=['POST'])
def mail():
    try:
        data = request.get_json()
        if data:
            try:
                email = data.get('email')
                if email in users:
                    pass
                else:
                    return 'This email does not exist. Please register a new one or check its validity...', 400
            except:
                return 'Oops... Please, write a your email adress. Email adress can"t be a "None". Key: "email"', 400
            try:
                parol = data.get('password')
                if users[email]['password'] == parol:
                    users[email]['attBLOK'] = 0
                else:
                    if users[email]['attBLOK'] < 10:
                        users[email]['attBLOK'] += 1
                        if users[email]['attBLOK'] == 5:
                            users[email]['messages'] = ['HACK [5]: Urgent situation - your address has been attempted to be hacked 5 times. We have deleted all the emails, but we advise you to pay attention to this and warn everyone. If you continue attempts to hack, your address will be deleted. The message is not translated by AI for security and urgent reading.']
                            return 'BLOCKING: All emails from this email address have been removed from the database to ensure user security. All hacking attempts have been recorded and taken into account.', 403

                        return 'ANTI-FRAUD SYSTEM: We have detected an attempt to hack an email, which is prohibited by BIGmail policy. For security reasons, if further attempts occur, the email receiving multiple requests will be blocked.', 403
                    else:
                        del users[email]
                        return 'BLOCK: The address was permanently deleted.', 403
            except:
                return 'Oops... Please, write a your password. Password can"t be a "None". Key: "password"', 400
            return users[email]['messages'], 200
        else:
            return 'Your post-data can"t be a "None"... Please, visit t.me/BIGmail_AI to view the registration request!', 400
    except:
        return 'Oops... visit t.me/BIGmail_AI to view problems.', 504
@appmail.route('/mail/action/clear', methods=['POST'])
def psnfj():
    try:
        data = request.get_json()
        if data:
            try:
                email = data.get('email')
                if email in users:
                    pass
                else:
                    return 'This email does not exist. Please register a new one or check its validity...', 400
            except:
                return 'Oops... Please, write a your email adress. Email adress can"t be a "None". Key: "email"', 400
            try:
                parol = data.get('password')
                if users[email]['password'] == parol:
                    users[email]['attBLOK'] = 0
                else:
                    if users[email]['attBLOK'] < 10:
                        users[email]['attBLOK'] += 1
                        if users[email]['attBLOK'] == 5:
                            users[email]['messages'] = ['HACK [5]: Urgent situation - your address has been attempted to be hacked 5 times. We have deleted all the emails, but we advise you to pay attention to this and warn everyone. If you continue attempts to hack, your address will be deleted. The message is not translated by AI for security and urgent reading.']
                            return 'BLOCKING: All emails from this email address have been removed from the database to ensure user security. All hacking attempts have been recorded and taken into account.', 403

                        return 'ANTI-FRAUD SYSTEM: We have detected an attempt to hack an email, which is prohibited by BIGmail policy. For security reasons, if further attempts occur, the email receiving multiple requests will be blocked.', 403
                    else:
                        del users[email]
                        return 'BLOCK: The address was permanently deleted.', 403
            except:
                return 'Oops... Please, write a your password. Password can"t be a "None". Key: "password"', 400
            users[email]['messages'] = []
            return 'Your messages is clear.', 200
        else:
            return 'Your post-data can"t be a "None"... Please, visit t.me/BIGmail_AI to view the registration request!', 400
    except:
        return 'Oops... visit t.me/BIGmail_AI to view problems.', 504
if __name__ == '__main__':
    # th1 = threading.Thread(target=appmail.run, args=('0.0.0.0', 10000))
    # th1.daemon = True
    # th1.start()
    appmail.run(host='0.0.0.0', port=10000)
