import csv
import time
start=time.time()
#values of find_words stored in array x2
f2 = open("C:/Users/dhand/Desktop/DP/Translate_Words_Challenge/find_words.txt" , "rt")
a2=f2.read()
x2=a2.split()
# storing the lines of sonnet in a
file=open("C:/Users/dhand/Desktop/DP/Translate_Words_Challenge/t8.shakespeare.txt")
a=file.readline()
dict={}
splchar=",'_-!@.\\\;<<:?*"
#creating a output file
fileout=open("C:/Users/dhand/Desktop/DP/Translate_Words_Challenge/frequency.csv","w")
#creating a dictionary to store the words in french dictionary
with open("C:/Users/dhand/Desktop/DP/Translate_Words_Challenge/french_dictionary.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        dict[row[0]] = row[1]

l1=[]
l2=[]
print(file)
for i in file:
    l1.append(i)
l1=str(l1).split()
for i in range(len(l1)):
    for j in splchar:
        l1[i]=l1[i].replace(j,"")
lout=[]
ltemp=[]
for i in dict:
    if i in l1:
        ltemp.append(i)
        ltemp.append(dict[i])
        ltemp.append(l1.count(i))
        lout.append(ltemp)
        ltemp=[]
# writing the output values in frequency.csv file
for i in lout:
    fileout.write(str(i))
    fileout.write("\n")

#To replace the strings in Sonnet file
for i in range(len(lout)):
    fin = open("C:/Users/dhand/Desktop/DP/Translate_Words_Challenge/t8.shakespeare.txt","rt")
    data=fin.read()
    data=data.replace(lout[i][0],lout[i][1])
    fin.close()
    fin=open("C:/Users/dhand/Desktop/DP/Translate_Words_Challenge/t8.shakespeare.txt","wt")
    fin.write(data)
    fin.close()
end=time.time()
#To create a file performance and add the processed time to it.
textout=open("C:/Users/dhand/Desktop/DP/Translate_Words_Challenge/performance.txt","w")
textout.write("Time to process...")
textout.write(str(end-start))

#End of program.