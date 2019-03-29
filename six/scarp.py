import bs4 as bs
import urllib.request
import time
import pygame
six = 0
curr = 0
upgrade = str(input('enter crikbuzz url of the match'))
while True:
    sauce=urllib.request.urlopen(upgrade).read()
    soup=bs.BeautifulSoup(sauce,'lxml')
    link="cb-col cb-col-8 ab text-right"
    div = soup.find_all('div', {"class" : link})
    try:
        print(div[1].get_text(),div[3].get_text())
    except Exception as e:
        print('out, waiting for new player info')
        time.sleep(10)
        continue
    temp = int(div[1].get_text())+int(div[3].get_text()) - six
    if temp > 0:
        six += temp
        pygame.mixer.init()
        pygame.mixer.music.load("six.mp3")
        pygame.mixer.music.play()
        time.sleep(6)
        print('chakaaaa')
    elif temp < 0: six = 0
        
    
  
    time.sleep(6)
