from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from re import sub
from decimal import Decimal

class Instabot:
	def __init__(self,username,password,OtherUserId,comment):
		self.driver=webdriver.Chrome("chromedriver.exe")
		self.driver.maximize_window()
		self.driver.get("https://www.instagram.com/")
		sleep(2)
		self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
		self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
		self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
		sleep(5)
		self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
		sleep(5)
		self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
		sleep(5)
		self.driver.get("https://www.instagram.com/"+OtherUserId)
		posts = self.driver.find_element_by_xpath("/html/body/div/section/main/div/header/section/ul/li/span/span").text
		posts = Decimal(sub(r'[^\d.]', '', posts))
		print(posts)
		pic = self.driver.find_element_by_class_name("_9AhH0")    
		pic.click()
		sleep(2)
		like = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
		like.click()
		cmt = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[2]/button')
		cmt.click()
		sleep(1)
		self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(comment)
		self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(Keys.ENTER)
		nextPic = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
		nextPic.click()
		print("success") 
		sleep(2)
		for i in range(int(posts-1)):
			like = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
			sleep(2)
			like.click()
			sleep(2)
			cmt = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[2]/button')
			cmt.click()
			sleep(1)
			self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(comment)
			self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(Keys.ENTER)
			nextPic = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
			nextPic.click()
			print("success") 
			sleep(2)
	sleep(20)
Instabot('yourusername','yourpassword','otheruser','your comment')