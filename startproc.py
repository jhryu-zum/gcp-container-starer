

import time
import requests
import datetime
import sys

#f = open('','w')



i = 0

while True:

    i+= 1

    f = open(str(i)+'test'+sys.argv[1],'w')


    resp = requests.get('http://dart.fss.or.kr/dsaf001/main.do?rcpNo=20191104900049')
    f.write(str(datetime.datetime.now())+'\n')
    f.write(str(resp.text)+'\n')
    f.close()

    time.sleep(10)


