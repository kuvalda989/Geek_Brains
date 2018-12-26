from socket import *
import time
import json
import pickle


def connect_to_server(addr, port):
    # create connnection and return it
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addr, port))
    print('Connect to server on port %s' % port)
    return s


def ask_for_status(connection):
    # asking for status use connect_to_server
    json_ask_stat = pickle.dumps(presense)
    connection.sendall(json_ask_stat)


def take_status_from_server(connection):
    # take status from server and return in json
    data = connection.recv(10000)
    pickle_data = pickle.loads(data, encoding="utf-8")
    json_data = json.dumps(pickle_data, ensure_ascii=False)
    return json_data


timestamp = int(time.time())
account = "DiManchiK"
presense = {
    "action": "presence",
    "time": timestamp,
    "type": "status",
    "user": {
        "account_name": account,
        "status": "Yep, I am here!"
    }
}


if '__main__' == __name__:
    connection = connect_to_server('localhost', 8888)
    ask_stat = ask_for_status(connection)
    status = take_status_from_server(connection)
    print(status)
