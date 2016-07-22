import requests, time, sys
from threading import Thread

#After turning on the pump, wait at least ten seconds for the pressure to stabilize before opening the feed valve'

def proxiando(p, i):
    proxies = {}
    proxies['http'] = p
    try:
        start = time.time() #Response timer start
        r = requests.get('http://www.bing.com/', proxies=proxies, timeout=(2, 3)) #request bing using the last proxy on proxies 
        z = float("%.3f" % ((time.time() - start))) #Response timer finish / Use float to compare results in miliseconds
        #Dividing proxies acording to their reponse time
        if z < 0.1:
            with open("results/A_Class.txt", "a") as a:
                a.write(p + "\n")
        elif 0.1 <= z < 0.5:
            with open("results/B_Class.txt", "a") as b:
                b.write(p + "\n")
        elif 0.5 <= z < 1.0:
            with open("results/C_Class.txt", "a") as c:
                c.write(p + "\n")
        elif 1.0 <= z < 2.0:
            with open("results/D_Class.txt", "a") as d:
                d.write(p + "\n")
        elif 2.0 <= z <= 5.0:
            with open("results/E_Class.txt", "a") as e:
                e.write(p + "\n")
        if z < 1:
            with open("results/Under_1_sex.txt", "a") as und:
                und.write(p + "\n")
    except:
        pass

def main():
    plit = [line.rstrip('\n') for line in open('bases/mrhinkydink_com.txt')]
    tam = len(plit)
    print "Testing %s proxies" % (tam)
    i = 1
    for p in plit:
        t = Thread(target=proxiando, args=(p, i))
        t.start()
        i = i + 1
        if i % 100 == 0:
            print "%s requests sent" % (i)
        if i > tam:
            print "Awaiting the last responses"

if __name__ == '__main__':
    main()