import requests
import pandas as pd
import time
api_url = 'https://api.celebrityninjas.com/v1/search?name='
names=pd.read_csv('name1.txt',sep='\n',header=None)
# print(names.values)
error_flag=False
file = open('test.json','a',encoding="utf-8")
for name in names.values[1091:]:
    count=0
    time_out=0
    # print(name)
    while(True):
        time.sleep(10)
        count+=1
        response = requests.get(api_url + str(name[0]), headers={'X-Api-Key': 'c8FAgopguMiQbBS0W9naxA==bx1I5vjX2fCFDHLZ'})
        if response.status_code == requests.codes.ok:
            break
        if count>3:
            time_out+=1
            time.sleep(180)
            if time_out>1:
                break
            else:
                count=0
    print(count)
    if count>3:
        print(str(name)+"Error:"+str(response.status_code)+str(response.text))
        break
    file.write(response.text)
    file.write('\n')
    # else:
    #     print(str(name)+"Error:"+str(response.status_code)+str(response.text))
    #     file.write('\n')
file.close()