from bs4 import BeautifulSoup
import urllib2, re, time

def mrhinkydink_com():
    print ">Scrapping of Mrhinkydink.com started"
    #start = time.time()
    try:
        data = []
        for x in range (1, 21):
            if x == 1:
                x = ""
            url = 'http://www.mrhinkydink.com/proxies%s.htm' % (x)
            page = urllib2.urlopen(url)
            soup = BeautifulSoup(page.read(), "html.parser")
            bs_proxy = soup.find_all("tr", class_="text", height="10")
            for proxx in bs_proxy:
                sopola = proxx.find_all("td")
                cols = [ele.text.strip() for ele in sopola] #data.append([ele for ele in cols if ele]) #Get rid of empty values
                data.append(cols[0]+":"+cols[1])
    except:
        pass
    print data
    for item in data:
        file_location = "bases/mrhinkydink_com.txt"
        export = open(file_location, "a")
        export.write(item.encode('utf-8') + "\n")

if __name__ == "__main__":
    mrhinkydink_com() 