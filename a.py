import numpy as np
import re
profile_regex = re.compile(r'"number">&nbsp;(.*?)<\/div><div class="clear"><\/div>')
place_regex = re.compile(r'Birthplace: <\/b>(.*?)<\/div><div')

f = open('mess/actor_mess.txt',encoding="utf-8")
text = f.read()
f.close()
arr=[]
match = profile_regex.findall(text)
for t in match:
    a=place_regex.findall(t)
    if not a:
        continue
    places=a[0].split(',')
    country=places[len(places)-1].strip()
    arr.append(country)
arr=np.unique(arr)
print(len(arr))   