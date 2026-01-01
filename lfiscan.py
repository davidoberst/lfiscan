import pyfiglet
from colorama import Fore,Style
import requests
import argparse
import httpx
import sys
import time
import os 
 

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
          print(Fore.RED + f"[:] Site does not exist or is not available right now (HTTP {res.status_code}).")
          sys.exit(1)
    except httpx.RequestError:
        print(Fore.RED + "[:] The host appears to be down or unreachable. Please try again later." \
        "")

def CheckWordlist(): #CHECK IF THE WORDLIST PATH EXISTS BEFORE FUZZ 
   wpath = args.W
   if os.path.exists(wpath):
      pass
   else:
      print(Fore.RED + "[:] Wordlist path not founded.")


def Fuzz():
 #----check if the website has PHP and URL has -----
  
  r = requests.get(args.H) #request
  h = args.H.strip() #host 
  if ".php" in r.text.lower():
    print(Fore.GREEN + "[:] PHP found, may be vulnerable to LFI.")
  else:
    print(Fore.YELLOW + "[:] No PHP founded .")
  if "?page=" in h:
     print(Fore.GREEN + "[:] Vulnerable parameter founded! <?page=home>")
  



  

  #------INJECT PAYLOADS IN URL-----------
  
      
 
# ---------------BANNER---------------------
print(pyfiglet.figlet_format(text="lfiscan",font="larry3d"),end="")
print("            https://github.com/davidoberst",end="")
print("\n" + "-"*60 + "\n")

print(f"[:] HOST : {args.H}")
CheckHost()
CheckWordlist()
Fuzz()



