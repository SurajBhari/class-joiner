# class-joiner
This is a script that I use to join my online class automatically. 
It works in this manner
- It goes to the website
- Goes to login page
- login in
- go to live stream page
- join the class
- retry for sometime in case of a failure 
- In end. send a discord webhook with information

# How to use it ?
Make this clear. This is not made for everyone to use. nor can everyone use this. you must have a account in studybase.in provided by the school.

- Download this program
- Edit the variable inside the class.py
  - Fill up your username ------ for login
  - Fill up your password ------ for login
  
  - Geckodriver location . the .exe file provided. ex (` gecko_location = r"D:\geckodriver"` ) ... don't add `.exe` to end.
  - Webhook location where the message should be sent (example - https://discord.com/api/webhooks/747216354813149364/90Lnzc4xHggKYeD5tjO2Zn0NvnXs8tYK8psIJp8BB-9UFzl8kMqK4usP9KTJTDUOiyYW)
  - Content - additional message that must be sent with the webhook. can be anything can also be empty can be a mention
- Set up auto execution of script
  - Read this https://www.jcchouinard.com/python-automation-using-task-scheduler/
  
# Requirments 
- Python
  - Selenium
  - discord.py
  - requests
  
  
