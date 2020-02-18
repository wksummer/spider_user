import requests
from bs4 import BeautifulSoup


def outTxt(html):
    data = open("C:\\Users\Only\Desktop\data.txt",'w+')
    print(html,file=data)
    data.close()

'''
dict['Age'] = 8; # update existing entry 
dict['School'] = "DPS School"; # Add new entry
 
print "dict['Age']: ", dict['Age'];
print "dict['School']: ", dict['School'];
'''
def getInfo():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.87 Safari/537.36",
        "Cookie": "acw_tc=76b20f7015795746067147930e727e1b1b99a9dcd646d672ecb951b9a7037a;"
                  " PHPSESSID=uqhismobvkiq1ggfut4b53c7d7;"
                  " EjI9_fe95_lastvisit=1580879703;"
                  " EjI9_fe95_saltkey=a24B2i2a; EjI9_fe95_sendmail=1;"
                  " EjI9_fe95_it618_loginpreurl=https%3A%2F%2Fbbs.hcbbs.com%2F;"
                  " _fmdata=GHEYJX6TvBfgc%2Brv6j1u2nzRolLHsx7mV5wGsufsqJA%2Fx8O6AoOfmXHut7qaqnQJRBe1Q%2FR61kIVtcDkMZMaEKCl6EeUC4mExWsCYn2z6vM%3D;"
                  " EjI9_fe95_lastact=1580883323%09plugin.php%09; EjI9_fe95_ulastactivity=1580883323%7C0;"
                  " EjI9_fe95_auth=c878Kuu6VmAcJxH3M67Sv%2FwqDhwD1NjwO6SaMTW10SELeMbmVaDRuq%2FP%2Bw",
    }

    userInfo={
    }
    requests.packages.urllib3.disable_warnings()
    url = "https://bbs.hcbbs.com/home.php"  # ?mod=space&uid=743301
    for i in range(743301,750000):
        html = requests.get(url,params={'mod':'space','uid':i}, headers=headers,verify=False).text
        soup = BeautifulSoup(html, "html.parser")
        name = soup.select('#spacename')
        for name in name:
            print(name.get_text()[2:-5])


if __name__ == '__main__':
    getInfo()
