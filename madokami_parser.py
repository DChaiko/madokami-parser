'''
Программа для выкачивания всех файлов со страницы сайта manga.madokami.al
'''

from requests_html import HTML, HTMLSession
import requests
import pickle
session = HTMLSession()
input_link = str(input('Вставьте ссылку на страницу с которой хотите скачать файлы: '))
input_login = str(input('Введите логин: '))
input_pass = str(input('Введите пароль: '))
r = session.get(input_link, auth=(input_login,input_pass))

file_l = open('links.txt', 'w')
link = r.html.find('body ', first=True)
get = link.find('.mobile-files-table', first=True)
tbody = get.find('tbody', first=True)
data = tbody.find('tr')


#берем название файла
#name = data[1].text.split('\n')



for d in data:
    try:
        link = d.find('a', first=True)
        link_text = str(link.absolute_links)
        name = d.text.split('\n')
        req = requests.get(link_text[2:(len(link_text)-2)], auth=(input_login,input_pass))
        with open (name[0] , 'wb') as f:
            f.write(req.content)
    
    except:
        pass




