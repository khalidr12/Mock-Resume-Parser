# Mock-Resume-Parser
Please understand that this is a MOCK parser, simply demostrarting the concept behind it                                                    
list1 = input("You are applying for the position of Android Developer, please type in your resume") 
list1.split()
list2 = ["consultant", "android", "java", "skillsets", "experienced", "dedicated" , "motivated", "hardworking"] #example word bank
keywords = (set(list1.split()).intersection((list2))) #finding the words in the 'resume' that match the existing keywords 
list_common = []
list_common.append(keywords)
print ("You matched "+(str(len(keywords)))+ " word(s)")
score = (len(keywords) / (len(list2)) * 10)
print ("This is your matching score out of 10 --> " + str(score))
if score <= 3:
    print ("We think this job may not be the right fit for you")
elif score > 3 and score <= 6:
    print ("Great! We think you will be a great fit!")
 
