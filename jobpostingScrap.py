import requests
from bs4 import BeautifulSoup
import csv 


jobsType = "data+science+internship"
location = "Toronto"
URL = f"https://ca.indeed.com/jobs?q={jobsType}&l={location}"
res = requests.get(URL)  # now we got the HTML page


# pass the response to a parse, arrange it with a tree 
soup = BeautifulSoup (res.content, 'html5lib')

jobs = []

table = soup.find('td' , attrs = {'id': 'resultsCol'})

for row in table.findAll('div',attrs ={'class': 'jobsearch-SerpJobCard unifiedRow row result'}):
    job ={}
    job['id'] = row['data-jk']
    job_link = URL + f"&vjk={row['data-jk']}"
    job['link'] = job_link
    job['title'] = row.h2.a['title']
    sjcl = row.find('div' , attrs = {'class' : 'sjcl'}) 
    company_div = sjcl.find('span' , attrs={'class': 'company'})
    job['company'] = company_div.text.strip()
    jobs.append(job)

filename = f'job_{jobsType}_result.csv'
with open(filename,'w',newline='') as f : 
    w = csv.DictWriter(f,['id','title','company','link'])
    w.writeheader()
    for job in jobs:
        w.writerow(job)

    






