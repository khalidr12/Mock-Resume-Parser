# To Whom it may concern:
# This is just a MOCK parser, to illustrate how it should work in theory
# The real programm can not be displayed due to NDA
# The real programm would also have a code to import .csv files and arrange spread sheets into strings and lists when neccessary 

#import csv
#>>> with open('Candidates.csv', 'r') as csvfile:
#...     resumereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#...     for row in resumereader:
#...         print ', '.join(row)  

list1 = input("Please type in your resume") 
list1.split()
list2 = ["consultant", "skillsets", "experienced", "dedicated" , "motivated", "hardworking"] #example word bank
keywords = (set(list1.split()).intersection((list2))) #finding the words in the 'resume' that match the existing keywords 
list_common = []
list_common.append(keywords)
print (len(keywords))
print (len(list2))
score = (len(keywords) / (len(list2)) * 10)
print ("This is your matching score out of 10")
print (score)