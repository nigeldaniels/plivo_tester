#!/usr/bin/python2
import requests

def make_call(auth):
    
    auth_id = auth[0].rstrip()
    auth_token = auth[1].rstrip()
    to_phone = '5551212'
    answer_url =  'http://127.0.0.1/answer/'
    from_phone = '1111111111'
    gateway = 'sofia/gateway/load-test/'
    plivo_base_url = 'http://'+auth_id+':'+auth_token+'@127.0.0.1:8088/v0.1/Call/'

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
    auth = get_auth()

    print auth
    make_call(auth)

if __name__== '__main__':
    main()

