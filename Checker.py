import io
import json
import subprocess
import sys
import tempfile
import time
import xlsxwriter
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# add new ids here
ids = {

    224348

}


def get_tor_session():
    session = requests.Session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http': 'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session


def renew_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)


def renew_connection_final():
    end_time = time.time() + 58
    while time.time() < end_time:
        print('Get new IP.')
        time.sleep(0.5)
        print('Get new IP..')
        time.sleep(0.5)
        print('Get new IP...')
        time.sleep(0.5)


def checkBanned(num_lines):
    if num_lines < 15:
        print('You are banned from FUTBIN')
        renew_connection_final()
        return True


def file_lengthy(checkBannedVar):
    length = len(checkBannedVar)
    return length


def startTor():
    subprocess.Popen('tor', shell=True)
    time.sleep(15)


def endTor():
    subprocess.Popen('Taskkill /IM tor.exe /F', shell=True)
    time.sleep(4)


endTor()  
startTor()
errorCounter = 0
console = 'ps'      # can be replaced with 'xbox' or 'pc', all three will work
ProfitValue = 300   # can be edited for personal preferences
for (id) in ids:
    session = get_tor_session()
    try:
        r = session.get('https://www.futbin.com/23/playerPrices?player=' + str(id)) # update the year inside the URL if needed
        r2 = session.get('https://www.futbin.com/')
    except requests.exceptions.Timeout:
        errorCounter += 1
        print('Connection ERROR1')
        if errorCounter > 3:
            sys.exit('Cant establish a valid connection! Check if TOR is running and try again')
        renew_connection_final()
        break
    except requests.exceptions.TooManyRedirects:
        errorCounter += 1
        print('Connection ERROR2')
        if errorCounter > 3:
            sys.exit('Cant establish a valid connection! Check if TOR is running and try again')
        renew_connection_final()
        break
    except requests.exceptions.RequestException as e:
        errorCounter += 1
        print('Connection ERROR3')
        if errorCounter > 3:
            sys.exit('Cant establish a valid connection! Check if TOR is running and try again')
        renew_connection_final()
        break
    else:
        checkBannedVar = r2.text
        num_lines = file_lengthy(checkBannedVar)
        if checkBanned(num_lines):
            break
        data = r.json()
        temp = tempfile.TemporaryFile()
        with open('temp', 'w', encoding='utf8') as outfile:
            str_ = json.dumps(data,
                              indent=4, sort_keys=True,
                              separators=(',', ': '), ensure_ascii=False)
            outfile.write(to_unicode(str_))
            for id in data:
                Preis1 = data[id]['prices'][str(console)]['LCPrice']
                Preis2 = data[id]['prices'][str(console)]['LCPrice2']
                Preis3 = data[id]['prices'][str(console)]['LCPrice3']
                Preis4 = data[id]['prices'][str(console)]['LCPrice4']
                Preis5 = data[id]['prices'][str(console)]['LCPrice5']

                MinPreis = data[id]['prices'][str(console)]['MinPrice']
                LastUpdated = data[id]['prices'][str(console)]['updated']
                LastUpdatedNumber = LastUpdated.split(" ")[0]
                HourOrMinute = LastUpdated.split(" ")[1]

                with open('output.txt', 'a+') as output:
                    for lines in data:
                        print(id)
                        dt = datetime.today()
                        TimeSeconds = dt.timestamp()

                        if HourOrMinute == "sec":
                            LastUpdatedSec = TimeSeconds
                        elif HourOrMinute == "secs":
                            LastUpdatedSec = TimeSeconds
                        elif HourOrMinute == "min":
                            LastUpdatedSec = LastUpdatedNumber * 60
                        elif HourOrMinute == "mins":
                            LastUpdatedSec = LastUpdatedNumber * 60
                        else:
                            LastUpdatedSec = 0

                        if LastUpdatedSec != 0:
                            TimeOfUpdateSec = TimeSeconds - str(LastUpdatedSec)
                            TimeOfUpdateTime = TimeOfUpdateSec * 60 * 60
                            print(TimeOfUpdateTime)
                        else:
                            print("Ergebnis zu ungenau")
