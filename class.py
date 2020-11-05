from selenium import webdriver
import time
import selenium
from discord import Webhook, RequestsWebhookAdapter, Embed
import requests
import sys

user_name = ""
password = ""
login_url = "https://studybase.in/login"
live_stream_url = "https://studybase.in/student/live-stream"
gecko_location = r""
webhook_url = ""
content = "<@355658987372281856>"

driver = webdriver.Firefox(executable_path=gecko_location)

driver.get(url=login_url)

time.sleep(5.0)

mobile_element = driver.find_element_by_id(id_="Mobile")
password_element = driver.find_element_by_id(id_="Password")
login_button = driver.find_element_by_id(id_="submitForm")
mobile_element.send_keys(user_name)
password_element.send_keys(password)
driver.find_elements_by_class_name
login_button.click()

time.sleep(5.0)


driver.get(url=live_stream_url)
time.sleep(5.0) # Random delay for Table to get rendered

try:
    stream = driver.find_element_by_xpath("//table[@id='studentsTable']/tbody/tr[1]")
except selenium.common.exceptions.NoSuchElementException:
    exit()
else:
    pass



classtime = stream.find_element_by_xpath("//td[1]").text
date = stream.find_element_by_xpath("//td[2]").text
duration = stream.find_element_by_xpath("//td[3]").text
subject = stream.find_element_by_xpath("//td[5]").text
by = stream.find_element_by_xpath("//td[6]").text
join = stream.find_element_by_xpath("//td[7]/span/a")

join.click()

def success():
    webhook = Webhook.from_url(webhook_url, adapter=RequestsWebhookAdapter())
    embed = Embed(
        color = 0x00ff00,
        title= "Success"
    )
    embed.add_field(name="ClassTime", value=classtime)
    embed.add_field(name="Date", value=date)
    embed.add_field(name="Duration", value=duration)
    embed.add_field(name="Subject", value=subject)
    embed.add_field(name="By", value=by)
    
    webhook.send(content= me_mention, embed=embed)
    sys.exit()



time.sleep(15) # 15 seconds delay cuz why not ?

try:
    audio = driver.find_elements_by_class_name("join-audio-by-voip") 
    if not audio:
        raise selenium.common.exceptions.NoSuchElementException()
except selenium.common.exceptions.NoSuchElementException:
    print("Couldn't find the button will retry soon.")
else:
    print("Found the button. so joined succedeed.")
    success()


for x in range(15):
    #Try refreshing to try getting in class for 15 minute
    print(f"{x} Retries done")
    time.sleep(60)
    driver.refresh()
    time.sleep(15)
    try:
        audio = driver.find_elements_by_class_name("join-audio-by-voip") 
        if not audio:
            raise selenium.common.exceptions.NoSuchElementException()
    except selenium.common.exceptions.NoSuchElementException:
        continue
    else:
        success()



def failed():
    webhook = Webhook.from_url(webhook_url, adapter=RequestsWebhookAdapter())
    embed = Embed(
        color = 0xff0000,
        title= title,
        description= content
    )
    embed.add_field(name="ClassTime", value=classtime)
    embed.add_field(name="Date", value=date)
    embed.add_field(name="Duration", value=duration)
    embed.add_field(name="Subject", value=subject)
    embed.add_field(name="By", value=by)
    
    webhook.send(content= me_mention, embed=embed)
    sys.exit()

try:
    content = driver.find_elements_by_class_name("zm-modal-body-content")
    if type(content) == list:
        content = content[0].text
    else:
        content = content.text

    title = driver.find_element_by_class_name("zm-modal-body-title")
    if type(title) == list:
        title = title[0].text
    else:
        title = title.text
except selenium.common.exceptions.NoSuchElementException:
    content = "Unknown Error"
    title= "Unknown Error"
else:
    failed()
failed()

