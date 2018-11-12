#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file name: ")
if len(fname) < 1 : 
    fname = "Sample data.txt"
fh = open(fname)

import re

numlist = list()

for line in fh:
    line = line.rstrip()
    if len(line) < 1:
        continue
    stuff = re.findall('[0-9]+', line)
    if len(stuff) == 0 :
        continue #skip all the lines that do not match
    numlist = numlist + stuff

total = 0
for n in numlist:
    total = total + float(n)
print('Sum:', total)
