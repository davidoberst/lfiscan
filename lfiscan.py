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
        sys.exit(1)

def CheckWordlist(): #CHECK IF THE WORDLIST PATH EXISTS BEFORE FUZZ 
   wpath = args.W
   if os.path.exists(wpath):
      pass
   else:
      print(Fore.RED + "[:] Wordlist path not founded.")


def Fuzz():
  #----scan fot website vulnerable parameters-----
  r = requests.get(args.H) #request
  h = args.H.strip() #host 
  if ".php" in r.text.lower():
    time.sleep(1)
    print(Fore.GREEN + "[:] PHP found, may be vulnerable to LFI."  + Style.RESET_ALL)
  else:
    time.sleep(1)
    print(Fore.YELLOW + "[:] No PHP founded."  + Style.RESET_ALL)
 
  #------INJECT PAYLOADS IN URL-----------

  with open(args.W, "r", encoding="utf-8") as f: #OPEN WORDLIST : (f = file)  
   time.sleep(1)
   print("\n" + "-"*60 + "\n")
   print("[:] Sending URL payload requests")
   print("")
   for line in f:
      payload = line.strip()
      newURL = args.H +"?page="+ payload #create URL with the wordlist
      r = requests.get(newURL) #r = response
      if r.status_code == 200:
         print(f"{r.status_code} OK = {Fore.GREEN + newURL + Style.RESET_ALL}")
      else:
         print((f"{r.status_code} = {Fore.RED + newURL + Style.RESET_ALL}"))

# ---------------BANNER---------------------
print(pyfiglet.figlet_format(text="lfiscan",font="larry3d"),end="")
print("            https://github.com/davidoberst",end="")
print("\n" + "-"*60 + "\n")

print(f"[:] HOST : {args.H}")
CheckHost()
CheckWordlist()
Fuzz()



