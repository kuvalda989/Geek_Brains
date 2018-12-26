from socket import *
import time
import pickle
import json


def server_start(host, port):
    # starting server and return conn and addr
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)
    conn, addr = sock.accept()
    return {'conn': conn, 'addr': addr}


def take_information_from_client(connnection, addr):
    # take information from client and return in json
    print('Connect established with %s' % str(addr))
    data = connnection.recv(10000)
    pickle_data = pickle.loads(data, encoding="utf-8")
    json_data = json.dumps(pickle_data)
    return json_data


def response_status(connection, response):
    # send status to client
    pickle_data = pickle.dumps(response)
    connection.sendall(pickle_data)


def close_server(connection):
    connection.close()


response_200 = {
    "response": 200,
    "alert": "Необязательное сообщение/уведомление"
}


if '__main__' == __name__:
    while True:
        con = server_start('localhost', 8888)
        inf = take_information_from_client(con['conn'], con['addr'])
        response_status(con['conn'], response_200)
        print(inf)
        close_server(con['conn'])
