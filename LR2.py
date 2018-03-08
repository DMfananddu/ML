
# coding: utf-8

# In[1]:


print ('hello')


# In[134]:


import json

import requests
res = requests.get('http://api.hh.ru/vacancies?text=machine+learning+Russia&per_page=100&only_with_salary=true&salary!=None&currency=RUR')
r = res.json()
#print (r)

#for key in r:
#    print(key, '---', r[key], '\n')
items = r['items']
print(len(items))
city=[]
cisal={}
salary=0
koef=0
for i in range(len(items)):
    #print(i)
    #print(items[i]['salary'])
    if items[i]['salary']['currency']=='EUR':
        koef=70
    elif items[i]['salary']['currency']=='USD':
        koef=60
    else:
        koef=1
    if items[i]['salary']['to']==None:
           salary=items[i]['salary']['from']*koef
    elif items[i]['salary']['from']==None:
        salary=items[i]['salary']['to']*koef
    else:
        salary=(items[i]['salary']['to']+items[i]['salary']['from'])*koef//2
    if items[i]['area']['name'] not in cisal.keys():
        cisal[items[i]['area']['name']]=[salary]
    else:
        cisal[items[i]['area']['name']].append(salary)
for i in cisal.keys():
    if len(cisal[i])==1:
        cisal[i]=cisal[i][0]
    else:
        cisal[i].sort()
        salary=cisal[i][len(cisal[i])//2]
        cisal[i]=salary
print(cisal)
    #if items[i]['area']['name'] not in city:
    #    city.append(items[i]['area']['name'])
    #cisal.fromkeys(items[i]['area']['name'])
#dict = r.text
#print(dict)


# In[107]:


for value in r:
    print(value)

