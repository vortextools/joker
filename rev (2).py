import re
import requests
import os
from colorama import Fore, init, Style
import concurrent.futures

# Initialize colorama for colored output
init()
yl = Fore.YELLOW
red = Fore.RED
gr = Fore.GREEN
res = Style.RESET_ALL

# Display banner
def banner():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print(red + "××××××××××××××××××××××××××××××××××××××××××××××××××××××××")
    print(gr + "×                                                      ×")
    print(gr + "×                        REVERSE IP                    ×")
    print(gr + "×                     IMPROVE BY SAGA                  ×")
    print(gr + "×                   TG- @@updateteams                    ×")
    print(gr + "×                                                      ×")
    print(red + "××××××××××××××××××××××××××××××××××××××××××××××××××××××××")
    print(gr + f"       -MASS FIND WEBSITE HOSTED ON SAME IP-\n  {res}      ")

# Worker function to process each IP
def worker(site):
    try:
        site = site.strip()
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}
        resp = requests.get(f'https://rapiddns.io/sameip/{site}?full=1', headers=headers)
        if ">0</span></div>" not in resp.text:
            ext = re.findall('</th>\n<td>(.*?)</td>', resp.text)
            with open("reverse.txt", 'a') as f:
                for i in ext:
                    print(i)
                    f.write(i + '\n')
        else:
            print(f"{yl}Dead IP: {site}{res}")
    except Exception as e:
        print(f"{red}Error processing {site}: {e}{res}")

# Main function to read input file and start the thread pool
def grab():
    sites = input("ENTER FILE OF IPS: ")
    with open(sites) as file:
        lines = [line.strip() for line in file]

    # Using ThreadPoolExecutor with 100 threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(worker, lines)

if __name__ == '__main__':
    banner()
    grab()
