from bs4 import BeautifulSoup
import urllib2, re, time

def proxy_list_org():
    print ">Scrapping of Proxy-list.org started"
    start = time.time()
    for x in range(1, 11):
        url = 'https://proxy-list.org/english/index.php?p=%s' % (x)
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page.read(), "html.parser")
        bs_proxy = soup.find_all("li", class_="proxy")
        for prx in bs_proxy:
            p_base = str(prx)
            address = re.search("(?<=\').*?(?=\')", p_base) #Para anular o que houver entre html tags; re.sub("<.*?>", "", p_base)
            if address:
                address = address.group(0)
                address = address.decode('base64')
                file_location = "bases/proxy_list_org.txt"
                export = open(file_location, "a")
                export.write(address + "\n")
    end = "%.0f" % (time.time() - start)
    print ">Proxy-list.org scrapped in %s seconds \n>Scrap saved in '%s'" % (end, file_location)

if __name__ == "__main__":
    proxy_list_org()