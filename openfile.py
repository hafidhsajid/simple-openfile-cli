import argparse
import json
import os.path
import sys

parser = argparse.ArgumentParser()

parser.add_argument( "input", help="Input file location")
parser.add_argument("-o", "--outputfile", help="Output file location")
parser.add_argument("-t", "--type", help="Type file output")
args = parser.parse_args()

fileinput = sys.argv[1]
if args.outputfile!=None: 
    fileoutput = args.outputfile
else: 
    fileoutput = "output.txt"

if os.path.exists(fileinput):
    if args.type=="json": 
        f = open(fileinput, "r")
        arrayoutput = []
        for baris in f:
            baris = baris.strip()
            words = baris.split(' \n')
            for w in words:
                if any(c.isdigit() for c in w):
                    arrayoutput.append(w)

        
        if args.outputfile!=None: 
            fileoutput = args.outputfile
        else: 
            fileoutput = "output.json"
        newfile = open(fileoutput, "w")

        newfile.write(json.dumps(arrayoutput))
        f.close()

    else:
        f = open(fileinput, "r")
        if args.outputfile!=None: 
            fileoutput = args.outputfile
        else: 
            fileoutput = "output.txt"
        newfile = open(fileoutput, "w")
        newfile.write(f.read())

else:
    print("File Not Found")


