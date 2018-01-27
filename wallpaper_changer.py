from bs4 import BeautifulSoup
import requests
import urllib
import os
import re
import commands

def beta(keyword):
	keyword = keyword.replace(" ","%20")
	target = urllib.urlopen("https://www.hdwallpapers.in/search.html?q="+keyword)

	#Scaping the Image URL................................................................
	soup = BeautifulSoup(target,"html.parser")

	sauce = soup.prettify().encode("utf-8")
	li = soup.find("div",{"class":"thumb"})
	div = li.find("a")
	lip = str(div).split('"')
	target1 = lip[1]

	destination = urllib.urlopen("https://www.hdwallpapers.in/"+target1)
	soup2 = BeautifulSoup(destination,"html.parser")

	sauce2 = soup2.prettify().encode("utf-8")
	item = soup2.find("a",{"class":"wallpaper-thumb"}) 
	div2 = item.find("img") 
	lip2 = str(div2).split('"')
	target2 = lip2[3]
	target_url = "https://www.hdwallpapers.in/"+target2
	#Downloading the image..................................................................

	filename = "ImageWallpaper" + ".jpeg"
	urllib.urlretrieve(target_url,filename)
	
	#setting wallpaper......................................................................
	
	command = "gsettings set org.gnome.desktop.background picture-uri file:///home/shivam/Desktop"+filename
	status, output = commands.getstatusoutput(command)
	print("Process Completed, Wallpaper is set")

	
query = raw_input("Enter the search keywords here:")
beta(query)