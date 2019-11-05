


import requests
from bs4 import BeautifulSoup
import time
import datetime
import zmq
import sys


base_url = 'http://dart.fss.or.kr/dsaf001/main.do?rcpNo='


def consumer():
    context = zmq.Context()
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://10.146.0.2:"+sys.argv[1])
    i= 0
    while True:
        i+=1
        work = consumer_receiver.recv_json()
        data = work["data"]
        f = open(str(i) + "data","w")
        f.close()

consumer()



