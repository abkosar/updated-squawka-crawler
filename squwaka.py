import requests
import time
from bs4 import BeautifulSoup
import re
from time import sleep

prog_start=time.time()

team_list=["Manchester United","Chelsea","Liverpool","Southampton","Manchester City","Real Madrid","Barcelona","Tottenham Hotspur","Arsenal"]
def crawl(url):
	while True:
		try:
			r=requests.get(url)
			return r.content
			break
		except Exception as e:
			print (e)
			sleep(2)
			print ("Retrying!!")
base_url = "http://www.squawka.com/teams/"

def makeMyURL(teamname):
	teamname=teamname.lower()
	teamname=teamname.replace(" ","-")
	return base_url+teamname+"/squad"

for team in team_list:
	fetch_team=time.time()
	url=makeMyURL(team)
	print ("Starting to crawl "+team+" from "+url)
	html = crawl(url)
	print ("Crawled page!")
	soup=BeautifulSoup(html)
	player_names=soup.find_all("td", { "class" : "squad_playerphoto" })
	#print (player_names)
	player_links=soup.find_all("a", { "class" : "teamstatinfo" })
	#print (player_links)
	print ("-----------------------------------------------")
	print ("         PLAYERS   FROM    "+team)
	print ("-----------------------------------------------") 
	i=0
	for player in player_links:
		start="<div>"
		end="</div>"
		print (re.search('%s(.*)%s' % (start, end),str(player_names[i])).group(1))
		start="players/"
		end="/stats/../stats\">"
		print (re.search('%s(.*)%s' % (start, end),str(player)).group(0))
		i+=1
	print ("")
	print ("Time taken is"+str(time.time()-fetch_team)+" s")
"Tottenham Hotspur",
