#!/usr/bin/python2
import requests
import psycopg2

phone_data = {'from_phone':'1111111111',
             'phone_to':55551212,
             'plivo_request_uuid':'1111111111',
             'sf_task_id':'1111111111',
             'user_id':'111111',
             'org-id':'load-test'
             }

def make_call(auth,dial_id):

    auth_id = auth[0].rstrip()
    auth_token = auth[1].rstrip()
    answer_url =  'http://127.0.0.1/answer/'
    gateway = 'sofia/gateway/load-test/'
    plivo_base_url = 'http://'+auth_id+':'+auth_token+'@127.0.0.1:8088/v0.1/Call/'

    payload = {'From':phone_data['from_data'],
               'To':phone_data['phone_to'],
               'AnswerUrl':answer_url,
               'Gateways':gateway,
               'ExtraDialString':'sip_h_Accuvit-Dial-ID='+dial_id[0][0]+',sip_h_Accuvit-Dial-Side=0'
    }
    request = requests.post(plivo_base_url,payload)

def get_auth():
    auth_data=[]
    authfile = open('auth','r')
    auth_data.append(authfile.readline())
    auth_data.append(authfile.readline())
    return auth_data

def database_auth():
    database_params=[]
    database = open('db','r')
    for line in database:
        database_params.append(line.rstrip())
    return database_params

def database_setup(database_params):
    conn_string = " host="+database_params[0] + " dbname="+database_params[1] + " user="+database_params[2] + " password="+ database_params[3] + " port=5802"
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    return cur

def get_dial_id(db_cursor,phone_data):
    I_query = """INSERT INTO dials (phone_from, phone_to, plivo_request_uuid, sf_task_id, user_id, org_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING dial_id;"""
    db_cursor.execute(I_query,(phone_data['from_phone'],phone_data['phone_to'],phone_data['plivo_request_uuid'],phone_data['sf_task_id'],phone_data['user_id'],phone_data['org-id']))
    return db_cursor.fetchall()

def main():
    test = database_auth()
    db_cursor = database_setup(test)
    dial_id  = get_dial_id(db_cursor,phone_data)
    make_call(get_auth(),dial_id[0][0])

if __name__== '__main__':
    main()
