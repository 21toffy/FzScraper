from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import Search

import mechanize
from bs4 import BeautifulSoup
import requests



def home (request):
    divs = ''
    links = ''
    details = ''
    rows = ''
    perf_list = ''
    detail_link = ''
    mylist = ''
    if request.method == "POST":
        searchword = request.POST.get('searchword')
        print(searchword)
        
        #to initialize the browser
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        #to open fzmovies homepage
        br.open("https://www.fzmovies.net/")
        #initialize form i think
        br.select_form(nr=0)

        br.form['searchname'] = str(searchword)

        #submitting form
        br.submit()

        # saves page source
        orders_html = br.response().read()

        #initializing bs4 for scraping
        soup = BeautifulSoup(orders_html,'html.parser')


        #picking the closest div to the link we want to pick by class name
        divs = soup.find_all("div", {"class": "mainbox"})
    
        details = []
        links = []
        #iterating through all available divs produces by the search
        for div in divs:
            
            #reavealing the href property inother get link
            rows = div.find_all('a', href=True)
            for row in rows:               
                links.append(row['href'])
            for tes in divs:
                details.append(tes.find_all(text=True))
        #This eliminates all double links in the list
        mylist = list(dict.fromkeys(links))

        perf_list = []
        det = []

        #this deletes the empty strings and any movie tag link in the list of links and appends the remaining to a new list
        for i in mylist:
            if i=='' or 'movietags' in i:
                del i
            else:
                perf_list.append(i)

        # for link,ident in zip(perf_list, details):
        #     print('LINK:::  https://fzmovies.net/{}  :::     TITLE:{}    YEAR:{}    QUALITY:{}'.format(link, ident[1], ident[3], ident[5]))
        #     print('\n')

    else:
        searchword = Search()
    return render(request, 'index.html', {'data':zip(perf_list, detail_link), 'searchword':searchword, 'links':links})


