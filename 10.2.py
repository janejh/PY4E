#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file name: ")
if len(fname) < 1 : 
    fname = "mbox-short.txt"
fh = open(fname)

counts = dict()
time = None
hour = None
hourlist = list()
timelist = list()

for line in fh:
    line = line.rstrip()
    if len(line) < 1:
        continue
    wordlist = line.split()
    if len(wordlist) < 2:
        continue
    if wordlist[0] == 'From:':
        continue
    if wordlist[0] != 'From':
        continue
    time = wordlist[5]
    timelist = time.split(':')
    hour = timelist[0]
    if hourlist is None:
        hourlist = hour #TypeError: unsupported operand type(s) for Add: 'NoneType' and 'str' on line 27
    else: 
        hourlist.append(hour)
        
for hr in hourlist:
    counts[hr] = counts.get(hr,0) + 1

lst = list()
for k,v in counts.items():
    part = (k,v)
    lst.append(part)

lst = sorted(lst)

for k,v in lst:
    print(k, v)
