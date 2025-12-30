import pyfiglet
import argparse

parser = argparse.ArgumentParser() #Create parser
parser.add_argument("-H",required=True,metavar="HOST",help="Host = http://examplehost.co")
args = parser.parse_args() #read user argument

# BANNER
print(pyfiglet.figlet_format(text="lfiscan",font="larry3d"),end="")
print("            https://github.com/davidoberst",end="")
print("\n" + "-"*60 + "\n")
print(f"[:] HOST :{args.H}")

