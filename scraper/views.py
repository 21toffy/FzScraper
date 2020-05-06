from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import Search
import mechanize
import requests
import urllib
import re
import mechanize
from bs4 import BeautifulSoup


br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
from django.http import HttpResponse


#Exceptions error 500 , 503 , Backend Error

def home (request):
    all_texts = ''
    perf_links = ''
    if request.method == "POST":
        searchword = request.POST.get('searchword')
        br.open("https://www.fzmovies.net/")
        #initialize form i think
        br.select_form(nr=0)
        #this picks the forms search valur and fills it in Fzmovies search form
        br.form['searchname'] = str(searchword)

        #submitting form
        br.submit()

        # saves page source
        orders_html = br.response().read()

        #initializing bs4 for scraping
        soup = BeautifulSoup(orders_html,'html.parser')


        #picking the closest div to the link we want to pick by class name
        divs = soup.find_all("div", {"class": "mainbox"})

        #this empty array would be used to store all thhe texts in that mainbox div
        all_texts = []

        #this empty array would be used to store all the a tags in the mainbox div
        links = []

        #iterating through all available divs produces by the search
        for div in divs:

            #reavealing the href property in other get links
            a_tags = div.find_all('a', href=True)

            #this for loop appends all the links in mainbox div into the links array
            for row in a_tags:
                links.append(row['href'])
            #this for loop appends all the texts in mainbox div into the all_texts array
            for texts in divs:
                all_texts.append(texts.find_all(text=True))

        '''
        there would be two of each link in the links array so this eliminates all double links in the list
        '''
        all_links = list(dict.fromkeys(links))

        '''
        there would be some unwanted strings in the links array called movie tags
        so we initialized an empty array to delete them and save the main links to a perfect array called perf_array
        '''

        perf_links = []


        #this deletes the empty strings and any movie tag link in the list of links and appends the remaining to a new array
        for i in all_links:
            if i=='' or 'movietags' in i:
                del i
            else:
                perf_links.append(i)

        searchword = Search()

    else:
        searchword = Search()
        #the zip function is used to loop over each list and make thier values appear right ontop of each other and data would be used as a key in the template
    return render(request, 'index.html', {'data':zip(all_texts, perf_links), 'searchword':searchword})


import urllib

def generate_download_link(request):
    download_url = request.POST.get('movie_to_download')
    detail = urllib.parse.unquote(str(download_url))

    #for opening detail page
    r = br.open(detail)

    #to read and save the page
    orders_html = br.response().read()

    soup = BeautifulSoup(orders_html,'html.parser')

    #filltering ul
    divs = soup.find_all("ul", {"class": "moviesfiles"})

    #initializing an empty array
    li = []

    #  this for loop is for filltering all a tags in the ul tag fillltered before and appending the results to a new array
    for d in divs:
        ul = d.find_all('a', href=True)
        for u in ul:
            li.append(u['href'])

    #initializing a new array
    down_page = []


    #this for loop is to remove the media.php in the link array and form the download page link
    for i in li:
        if 'mediainfo.php' in i:
            del i
        else:
            down_page.append('fzmovies.net/'+str(i))

    #raw url for download page1
    down_conf = down_page[0]
    #action to open url for downoad page 1, with http appended to it
    r = br.open('https://'+down_conf)

    orders_html = br.response().read()

    soup = BeautifulSoup(orders_html,'html.parser')

    divs = soup.find_all("a", {"id": "downloadlink"})

    nexts = []
    for d in divs:
        nexts.append(d['href'])
        maybe = d['href']
        down_page_2 = 'https://fzmovies.net/'+maybe


    ######Entering the last Download page#####

    #opening the page
    r = br.open(down_page_2)

    #reading the page
    orders_html = br.response().read()


    soup = BeautifulSoup(orders_html,'html.parser')

    down_link = soup.find_all("input", {"name": "download1"})
    real_links = []

    #download links generated

    label = ['link 1', 'link 2', 'link 3', 'link 4', 'link 5']

    for i in down_link:
        real_links.append(i['value'])

    data = real_links

    return render(request, 'generated.html', {'data':data} )


def about(request):
    return render(request,'about.html')    