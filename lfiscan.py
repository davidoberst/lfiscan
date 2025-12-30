import pyfiglet
import argparse
import httpx
import sys
import time
from colorama import init, Fore, Style; init(autoreset=True) 

# PARSER / ARGUMENTS
parser = argparse.ArgumentParser() #Create parser
parser.add_argument("-H",required=True,metavar="HOST",help="Host = http://examplehost.co") #host
parser.add_argument("-W",required=True,metavar="WORDLIST",help="Wordlist") #wordlist
args = parser.parse_args() #read user argument

def CheckHost(): # CHECK IF THE HOST EXIST OR IS ACTIVE BEFORE FUZZING
 h = args.H.strip()
 if not h.startswith(("https://","http://")):
    time.sleep(1)
    print("Unable to reach the host. Please provide a full URL (http:// or https://)")
    sys.exit(1)
 else:
    try:
       res = httpx.get(args.H, timeout=3.0, follow_redirects=True)
       if res.status_code == 200:
          print("[:] Host is up!")
       else :
          print("[:] Site does not exist or is not available (HTTP {res.status_code}).")
    except httpx.RequestError:
        print("[:] The host appears to be down or unreachable. Please try again later.")
 
# ---------------BANNER---------------------
print(pyfiglet.figlet_format(text="lfiscan",font="larry3d"),end="")
print("            https://github.com/davidoberst",end="")
print("\n" + "-"*60 + "\n")

print(f"[:] HOST : {args.H}")
CheckHost()


