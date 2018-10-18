# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import bleach
import yaml
from bs4 import BeautifulSoup
#import pdb; pdb.set_trace()
def result():
	page = requests.get('https://scotch.io/')
	soup = BeautifulSoup(page.text, 'html.parser')

	block_list = soup.find_all('a', {'class' : 'card-image'})

	with open("scotch.txt", "w") as file:
	  for block in block_list:
	    v_url = block.get('href')
	    print("url: ",v_url)

	    v_title = block.get('title')
	    print("title: ",v_title)

	    file.write("\n")
	    file.write("title: " + v_title)
	    file.write("\n")
	    file.write("url: " + v_url)

if __name__ == '__main__':
	result()

