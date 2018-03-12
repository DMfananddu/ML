
# coding: utf-8

# In[1]:


print ('hello')


# In[33]:


import json

import requests

#print (r)
vacancies = [] # Список всех вакансий
page = 0 # Текущая считываемая страница
pages = 1 # Всего страниц в выдаче
params = ""

# Борьба с возможной "пагинацией"
while page != pages:
    params = '?text=machine+learning+Russia&area=113&per_page=100&no_magic=true&only_with_salary=true&page=' + str(page)
    res = requests.get('http://api.hh.ru/vacancies' + params)
    if res.status_code != requests.codes.ok:
        print('FATAL: API return ' + str(res.status_code) + ' code!' + color.END)
        break
    r = res.json()
    vacancies += r['items']
    pages = r['pages']
    page += 1
    print('Считываем страницу: %s / %s (%3s элементов)' % (page, r['pages'], len(r['items'])))

#res = requests.get('http://api.hh.ru/vacancies?text=machine+learning+Russia&per_page=100&only_with_salary=true')
#r = res.json()

#for key in r:
#    print(key, '---', r[key], '\n')
items = vacancies
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
sal=list(cisal.values())
for i in cisal.keys():
    if len(cisal[i])==1:
        cisal[i]=cisal[i][0]
    else:
        cisal[i].sort()
        salary=cisal[i][len(cisal[i])//2]
        cisal[i]=salary
print(sal)
#cities=cisal.keys()
#print(type(cities))
    #if items[i]['area']['name'] not in city:
    #    city.append(items[i]['area']['name'])
    #cisal.fromkeys(items[i]['area']['name'])
#dict = r.text
#print(dict)


# In[3]:


allsal=[[40000, 0], [80000, 0], [120000, 0], [160000, 0], [200000, 0], [240000, 0], [280000, 0], [320000, 0]]
sal100=[]
for i in range(len(sal)):
    if type(sal[i]) is list:
        for j in range(len(sal[i])):
            sal100.append(sal[i][j])
    else:
        sal100.append(sal[i])
ma=max(sal100)
#print(sal100)
allsal.append([ma, 0])
for i in sal100:
    for j in range(9):
        if i<=allsal[j][0]:
            allsal[j][1]+=1
            break
print(allsal)


# In[29]:


import matplotlib.pyplot as plt
import numpy as np

bins = range(0, 450000, 40000)

#ax = plt.subplot(111)
x = np.arange(0, 450000, 80000)
plt.xticks(x)


l, bins = np.histogram(sal100, bins = bins)
plt.hist(sal100, bins)
plt.grid(True)
plt.show()

#print(l, bins)
#plt.fill_between(color='green')
#plt.bar(y, x, align='center')
#plt.xticks(y, l)
#plt.show()


# In[28]:


v, k = [], []
for i in cisal.keys():
    v.append(cisal[i])
    k.append(i)

fig, ax = plt.subplots()

c = np.arange(len(k))
#print(c)
ax.grid(True)
ax.barh(c, v, align='center', color='green')
ax.set_yticks(c)
ax.set_yticklabels(k)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_title('Зарплаты по городам России')

plt.show()

