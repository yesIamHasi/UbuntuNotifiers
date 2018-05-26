'''
Notfies about important news table from NUST website.
'''

from bs4 import BeautifulSoup
import urllib.request
import subprocess

def APsplit(li):
    '''
    Splits a list into odd indexed and even indexed list.
    Not a good algorithm though.
    '''
    odd = []
    even = []
    for i in range(len(li)):
        if i%2 == 0:
            even.append(li[i])
        else:
            odd.append(li[i])
    return even, odd

def fetch():
    sauce = urllib.request.urlopen('https://ugadmissions.nust.edu.pk/')
    soup = BeautifulSoup(sauce, 'lxml')

    for div in soup.findAll('div', {'class':'Notice-box'}):
        notice = div.text.split('\n')
        while '' in notice:
            notice.remove('')
        title, body = APsplit(notice)
        for i in range(len(title)):
            print(title[i], body[i])
            subprocess.Popen(['notify-send', title[i], body[i]])
            
if __name__ == '__main__':
    fetch()
