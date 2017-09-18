intro = input("Hey there! I am Alexa, your assistant for the day. Welcome to WITS Consulting! Would you like to (1) View all job openings; (2) Apply for a specific job? (3) Ask some questions? Please reply by entering 1, 2, or 3 ")
if intro == 1 or 2 :
  print ("Here are all the positions that are open in WITS Consulting:")
  redirect = input ("We are currently in need of (1) Android Developers and (2) Web developers. If you would like to apply for a job please type in 'yes'")
  if redirect == 1 or 2 :
    q1 = input("Are you applying for our Web Developer or android Developer role? Answer 1 for Android and 2 for Web Developer ")
    if q1 == "1" :
      list1 = input("Please input your resume at the end of this line: ")
      list1.split()
      print (list1)
      android = ["object orient programming","OPP", "android", "java", "API", "experienced"]
      #finding the words in the 'resume' that match the existing keywords 
      if len(list1) < len(android):
        keywords2 = (set(android).intersection(list1.split()))
        print (keywords2)
        print ("You matched "+(str(len(keywords2)))+ " word(s) in the Web Developer Wordbank")
        score2 = (len(keywords2) / (len(android)) * 100)
        print ("This is your matching score for the Android Developer position --> " + str(score2) + "%")
        if score2 <= 60:
          print ("We think this job may not be the right fit for you")
        elif score2 > 60 and score2 <= 80:
          print ("We seem to meet most of our criteras but not all. We will keep you in mind")
        else :
           print ("Great! We think you will be a great fit!")
      else :
        keywords2 = set(list1.split()).intersection(webdev)
        print (keywords2)
        print ("You matched "+(str(len(keywords2)))+ " word(s) in the Web Developer Wordbank")
        score2 = (len(keywords2) / (len(webdev)) )
        print ("This is your matching score out of 10 for Android --> " + str(score2))
        if score2 <= 30:
          print ("We think this job may not be the right fit for you")
        elif score2 > 30 and score2 <= 60:
          print ("Great! We think you will be a great fit!")
    elif q1 == 2:
      list1 = input("Please input your resume at the end of this line: ")
      list1.split()
      print (list1)
      webdev = [ "html", "HTML", "CSS", "css", "PHP", "php", "website", "websites", "webpage", "frontend", "front", "Front", "end", "back", "backend", "web developer", "web", "developer"]
      #finding the words in the 'resume' that match the existing keywords 
      if len(list1) < len(webdev):
        keywords2 = (set(webdev).intersection(list1.split()))
        print (keywords2)
        print ("You matched "+(str(len(keywords2)))+ " word(s) in the Web Developer Wordbank")
        score2 = (len(keywords2) / (len(webdev)) * 100)
        print ("This is your matching score out of 10 for Android --> " + str(score2))
        if score2 <= 30:
          print ("We think this job may not be the right fit for you")
        elif score2 > 30 and score2 <= 60:
          print ("Great! We think you will be a great fit!")
      else :
        keywords2 = set(list1.split()).intersection(webdev)
        print (keywords2)
        print ("You matched "+(str(len(keywords2)))+ " word(s) in the Web Developer Wordbank")
        score2 = (len(keywords2) / (len(webdev)) )
        print ("This is your matching score out of 10 for Android --> " + str(score2))
        if score2 <= 30:
          print ("We think this job may not be the right fit for you")
        elif score2 > 30 and score2 <= 60:
          print ("Great! We think you will be a great fit!")
elif intro == 3 :
  print ("Which question would you like me to answer?")
  selection = input ( "(1) What are recruiters looking for in a resume? (2) How soon will I know if I got a job or not? (3) How will I know if I got a job or not?")
  if selection == 1:
    print (" Recruiters want to fill a job opening as quickly as possible and get on to the next assignment. Hiring managers similarly want to hire someone as quickly as possible and get back to their work. Your resume is the tool that gets you in the door.What recruiters and hiring managers despise is an overabundance of self-praising descriptors: superior, excellent, team player, detail-oriented, thought leader, self-motivated, hard worker, and the like. When recruiters see a resume filled with adjectives unsupported by skills and achievements, they read a phrase like, 'Excellent Accounts Receivable skills; detail-oriented' and mutter, 'I'll be the judge of that!'")
