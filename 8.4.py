#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    wordlist = line.split()
    if len(wordlist) == 0:
        continue
    for word in wordlist:
        if word in lst: #lst=lst.append(word) TypeError: argument of type 'NoneType' is not iterable on line 9
            continue
        lst.append(word)
lst.sort()
print(lst)
#print(lst.sort()) #this does not work, and just print None
