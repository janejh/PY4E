#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
#Convert the extracted value to a floating point number and print it out.

#text = "X-DSPAM-Confidence:    0.8475";
#numtxt = text[23]+text[24]+text[25]+text[26]+text[27]+text[28]
#num = float(numtxt)
#print(num)

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
numtxt1 = text[pos+1:]
numtxt2 = numtxt1.replace(' ','')
num = float(numtxt2)
print(num)
