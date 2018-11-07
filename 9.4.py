#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file name: ")
if len(fname) < 1 : 
    fname = "mbox-short.txt"

fh = open(fname)
counts = dict()
countsmax = None
wordmax = None
addresslist = list()

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
    addresslist.append(wordlist[1])

for address in addresslist:
    counts[address] = counts.get(address,0) + 1

for word,count in counts.items():
    if countsmax is None or count > countsmax:
        wordmax = word
        countsmax = count

print(wordmax,countsmax)
    
    
