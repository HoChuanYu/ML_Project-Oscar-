import re
from typing import Text
import numpy as np
import pandas as pd
#&nbsp;<\/span><a class="tileLink" href="\/\/www.thefamouspeople.com\/profiles\/.*?.php">(.*?)<\/a><\/h2><div   <span class="number">&nbsp;(.*?)\("fa-thumbs-up"\)
profile_regex = re.compile(r'"number">&nbsp;(.*?)<\/div><div class="clear"><\/div>')
name_regex = re.compile(r'&nbsp;<\/span><a class="tileLink" href="\/\/www.thefamouspeople.com\/profiles\/.*?.php">(.*?)<\/a><\/h2><div')
birthday_regex = re.compile(r'Birthdate: <\/b>(.*?)<\/div><div')
sign_regex = re.compile(r'Sun Sign: <\/b>(.*?)<\/div><div')
place_regex = re.compile(r'Birthplace: <\/b>(.*?)<\/div><div')
job_regex = re.compile(r'Famous As: <\/b>(.*?)<\/div><div')
count=0

f = open('mess/actor_mess.txt',encoding="utf-8")
text = f.read()
f.close()

f = open('country.txt',encoding="utf-8")
country_list = f.read().splitlines()
f.close()

file = open('actor_info.csv','w',encoding="utf-8")
file.write('name\tb_date\tb_month\tb_year\tsun_sign\tb_country\tjob\n')
match = profile_regex.findall(text)
print(len(match))
for t in match:
    name = name_regex.findall(t)
    birthday = birthday_regex.findall(t)
    sign = sign_regex.findall(t)
    a=place_regex.findall(t)
    job=job_regex.findall(t)
    if not name or not sign or not birthday or not a or not job:
        continue
    else:
        places=a[0].split(',')
        country=places[len(places)-1].strip()
        if country not in country_list:
            continue
        else:
            count+=1
            job[0]=job[0].replace(' ','_')
            b_year=birthday[0].split(',')[1].strip()
            b_date=(birthday[0].split(',')[0].strip()).split(' ')[1]
            b_month=(birthday[0].split(',')[0].strip()).split(' ')[0]
            arr=[name[0],b_date,b_month,b_year,sign[0],country,str(job[0].lower())]
            file.write(('\t'.join(arr)) +'\n')

f = open('mess/actress_mess.txt',encoding="utf-8")
text = f.read()
f.close()
match = profile_regex.findall(text)
print(len(match))
for t in match:
    name = name_regex.findall(t)
    birthday = birthday_regex.findall(t)
    sign = sign_regex.findall(t)
    a=place_regex.findall(t)
    job=job_regex.findall(t)
    if not name or not sign or not birthday or not a or not job:
        continue
    else:
        places=a[0].split(',')
        country=places[len(places)-1].strip()
        if country not in country_list:
            continue
        else:
            count+=1
            job[0]=job[0].replace(' ','_')
            b_year=birthday[0].split(',')[1].strip()
            b_date=(birthday[0].split(',')[0].strip()).split(' ')[1]
            b_month=(birthday[0].split(',')[0].strip()).split(' ')[0]
            arr=[name[0],b_date,b_month,b_year,sign[0],country,str(job[0].lower())]
            file.write(('\t'.join(arr)) +'\n')

file.close()