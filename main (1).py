#Same problem with this console so I had to include the input()
#Press enter to begin the program
input("Press enter to begin")

#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Facebook data breach!")

#Introduces breach
print("Would you like to learn about the 2019 facebook data breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("The 2019 data breach of Facebook affected 533 million users in 106 countries, resulting in the leak of their personal data. The information stolen included phone numbers, full names, locations, email addresses, and other details from users’ profiles. Facebook chose not to notify the affected users, which damaged its reputation as it failed to maintain safety and transparency.")
  
  elif topic.lower() == "b":
    print("Facebook stated that the issue with their platform was resolved in 2019, and no data scraping could occur. They did not recommend any actions for users to take, claiming that users wouldn’t be able to resolve the situation.")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to CIA Triad, (b) my reaction, (c) my advice, or (d) none")
  topic = input()

  if topic.lower() == "a":
    print("This data breach violates confidentiality by leaking users’ personal information like phone numbers, names, emails, and locations. This shows how Facebook failed to protect the confidentiality of its users' data.")

  elif topic.lower() == "b":
    print("I disagree with the organization's response because they actively chose not to notify the 533 million users that had their data stolen. This prevented them with the opportunity to take down their personal information if they knew there were breaches going on, and by handling this the way they did, Facebook failed to provide safety for their users and full transparency.")

  elif topic.lower() == "c":
    print("I would convince victims to take action by spreading awareness about the issue in order to connect with other victims to show the true dangers of this breach and hold the platform accountable.")

  elif topic.lower() == "d":
    break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

  input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")