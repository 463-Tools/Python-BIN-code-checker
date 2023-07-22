# Path: app.py
import re
from os import path
from sys import argv
from checker import check_bin

def arg_check(arg):
    # arg = List
    binlist = []
    arg.pop(0)
    # Split each item on comma or pipe, remove leading/trailing whitespace, and flatten the list
    arg = [x.strip() for temp in arg for x in re.split(',|\|', temp) if x.strip()]
    print(arg)
    for x in arg:
        if path.isfile(x):
            with open(x, 'r') as f:
                # There have three ways to write the list file
                line = f.read()
                try:
                    if "," in line:
                        binlist.extend(line.replace(' ', '').split(','))
                    elif "|" in line:
                        binlist.extend(line.replace(' ', '').split('|'))
                    elif "\n" in line:
                        binlist.extend(line.replace(' ', '').split('\n'))
                except: pass
        elif x.isdigit() and len(x) == 6:
            binlist.append(x)
        else:
            print(f'Item {x} is not a valid BIN or file.')
    return binlist

if __name__ == '__main__':
    # Import data from text or txt file
    try:
        if len(argv)>=2: # If the user enters the bin number or list file, etc. 457173 or list.txt
            binlist = arg_check(argv)
            check_bin(binlist)
        else: # If no bin number or list file is entered
            bins = input("[•] PLEASE PUT THE FIRST 6 DIGITS OF YOUR CARD OR BIN LIST FILE> ").replace(" ", "")
            binlist = arg_check(bins)
            check_bin(binlist)
    except KeyboardInterrupt: print("\nGOODBYE!"); exit()
    except EOFError: print("\nGOODBYE!"); exit()