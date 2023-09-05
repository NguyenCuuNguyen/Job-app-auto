import requests
from bs4 import BeautifulSoup
import csv
# Making a GET request
r = requests.get('https://h1b.io/blog/list-h1b-cap-exempt-employers/')

# check status code for response received
# success code - 200
#print(r)

# print content of request
#print(r.content)
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('div', class_='entry-content')
uni_name_link = s.find_all('p')
result = {"Organizations": [], "Link": [], "Visa sponsored": [], "Current Job Openings": [], "Original_link": []} 
lst = []
for paragraph in s.find_all('p'):
    lst.append(paragraph.text)

#https://h1b.io/blog/list-h1b-cap-exempt-employers/
for l in lst[3:]:
    try:
        new_l = l.split(" – ")
        # print(new_l)
        result["Organizations"].append(new_l[0])
    except IndexError as e:
        print(e)
        result["Organizations"].append('')

    try:
        link = str(new_l[0]).replace(" ", "+")
        new_link = f"https://www.google.com/search?q={link}+career&sca_esv=562779362&sxsrf=AB5stBjHvyJVrVY_5CPydAO6JTdXR84QWA%3A1693934756084&ei=pGT3ZK_IBLet5NoPjrS7sAM&ved=0ahUKEwivqqLb_pOBAxW3FlkFHQ7aDjYQ4dUDCBA&uact=5&oq=center+for+global+development+career&gs_lp=Egxnd3Mtd2l6LXNlcnAiJGNlbnRlciBmb3IgZ2xvYmFsIGRldmVsb3BtZW50IGNhcmVlcjIIEAAYigUYkQIyBhAAGBYYHjIIEAAYigUYhgMyCBAAGIoFGIYDMggQABiKBRiGAzIIEAAYigUYhgNIsD9Q0ylY7jpwBXgBkAEAmAGPAaAB9gaqAQM4LjK4AQPIAQD4AQHCAgoQABhHGNYEGLADwgIQEC4YigUYxwEY0QMYsAMYQ8ICBxAjGIoFGCfCAgUQABiABMICCxAuGIAEGMcBGK8B4gMEGAAgQYgGAZAGCQ&sclient=gws-wiz-serp&bshm=rimc/1"
        result["Link"].append(new_link)
    except IndexError as e:
        print(e)
        result["Link"].append('')

    try:
        v = new_l[1].split('Visas sponsored: ')[1]
        result["Visa sponsored"].append(v)
    except IndexError as e:
        print(e)
        result["Visa sponsored"].append('')
    try:
        j = new_l[2].split('Current job openings: ')[1]
        result["Current Job Openings"].append(j)
    except IndexError as e:
        print(e)
        result["Current Job Openings"].append('')
    try:
        result["Original_link"].append("https://h1b.io/blog/list-h1b-cap-exempt-employers/")
    except IndexError as e:
        print(e)
        result["Original_link"].append('')
    # except IndexError as e:
    #     print(e)

print(result["Organizations"])


with open("H1B Cap-exempt Job Database.csv", "w") as outfile:
   writer = csv.writer(outfile)
   writer.writerow(result.keys())
   writer.writerows(zip(*result.values()))



