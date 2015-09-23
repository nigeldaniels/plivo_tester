#!/usr/bin/python2
import requests

def make_call():
    payload = {'From':from_phone,
               'To':to_phone,
               'AnswerUrl':answer_url,
               'Gateways':gateway
    }
    request = requests.post(plivo_base_url,payload)

def get_auth():
    auth_data=[]
    authfile = open('auth','r')
    auth_data.append(authfile.readline())
    auth_data.append(authfile.readline())
    return auth_data

def main():
    auth = get_auth

    auth_id = auth[0]
    auth_token = auth[1]
    to_phone = '+14157697098'
    answer_url =  'http://10.100.20.41/answer/'
    from_phone = '1111111111'
    gateway = 'sofia/gateway/flowroute/'
    plivo_base_url = 'http://'+auth_id+':'+auth_token+'@10.0.255.9:8088/v0.1/Call/'

    make_call()

if __name__== '__main__':
    main()

