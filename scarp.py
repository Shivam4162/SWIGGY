import bs4 as bs
import urllib.request
import time
six = 0
curr = 0
while True:
    sauce=urllib.request.urlopen('https://www.cricbuzz.com/live-cricket-scores/22402/bangalore-vs-mumbai-7th-match-indian-premier-league-2019').read()
    soup=bs.BeautifulSoup(sauce,'lxml')
    #print(soup.title.string)
    #print(soup.p)
    #print(soup.find_all('p'))
    #print(soup.get_text())
    #for url in soup.find_all('div class="cb-col cb-col-8 ab text-right"'):
      #  print(url)
    link="cb-col cb-col-8 ab text-right"
    div = soup.find_all('div', {"class" : link})
    try:
        print(div[1].get_text(),div[3].get_text())
    except Exception as e:
        print('gaya ')
        continue
    temp = int(div[1].get_text())+int(div[3].get_text()) - six
    if temp > 0:
        six += temp
        print('chakaaaa')
    elif temp < 0: six = 0
        
    
##    if int(text) - six > 0:
##        print('chakka pada h')
##        six =int(text)
##    
    time.sleep(6)
