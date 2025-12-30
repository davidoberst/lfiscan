import pyfiglet
import argparse
from icmplib import ping 

# PARSER / ARGUMENTS
parser = argparse.ArgumentParser() #Create parser
parser.add_argument("-H",required=True,metavar="HOST",help="Host = http://examplehost.co") #host
parser.add_argument("-W",required=True,metavar="WORDLIST",help="Wordlist") #wordlist
args = parser.parse_args() #read user argument

def CheckHost(): #check if the host is active before fuzz
 #OPTION 1 : Try with ICMP first
 host = args.H
 r = ping(host,count=2,timeout=2) #(r = result), count sends two packets, timeout waits 2 seconds 
 if(r.is_alive):
  print("Host is up")
 else:
  print("The host appears to be down or unreachable. Please try again later.")

# BANNER
print(pyfiglet.figlet_format(text="lfiscan",font="larry3d"),end="")
print("            https://github.com/davidoberst",end="")
print("\n" + "-"*60 + "\n")


print(f"[:] HOST :{args.H}")

