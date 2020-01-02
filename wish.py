import selenium
from selenium import webdriver
import os
import logging
import getpass
from time import sleep
import time
from bs4 import *
import tkinter as tk
from tkinter import *
from selenium.webdriver.common.keys import Keys

class AutoFB:

    def __init__(self):

        logging.basicConfig(level=logging.INFO)
        logging.info('Bot Launched at {}'.format(time.strftime("%H:%M:%S")))

        self.root = Tk()
        self.root.title('Enter credentials')
        self.root.geometry('300x250')
        self.root.resizable(False,False)

        frame = Frame(self.root,bg = 'DodgerBlue2')
        frame.pack(fill = 'both',expand = 'yes')

        label1 = Label(frame,text = 'Enter Username' ,bg = 'DodgerBlue2' , fg = 'white')
        label1.pack()

        label2 = Label(frame)
        label2.pack()

        self.t1 = tk.Text(label2 , height = 1 ,width = 30)
        self.t1.pack()

        label3 = Label(frame,text = 'Enter Password', bg = 'DodgerBlue2', fg = 'white')
        label3.pack()

        label4 = Label(frame)
        label4.pack()

        self.t2 = tk.Entry(label4 , show = '*', width = 30)
        self.t2.pack()

        label5 = Label(frame, bg = 'DodgerBlue2', fg = 'white')
        label5.pack()

        button_submit = Button(label5, text = 'Submit' , command = self.login)
        button_submit.pack( pady = 20)

        self.root.mainloop()

        
        

        

        
        
        
        

    def login(self):
        
        username = str(self.t1.get("1.0",END))
        pw = str(self.t2.get())
        self.root.destroy()
        
        self.driver = webdriver.Chrome(os.getcwd()+'/chromedriver.exe')
        self.driver.get('https://www.facebook.com/')
        self.driver.implicitly_wait(2)

        
       
        self.driver.find_element_by_id('email').send_keys(username)
        self.driver.find_element_by_id('pass').send_keys(pw)
        self.driver.find_element_by_id('loginbutton').click()

        logging.info('Logged in successfully as {}'.format(username))

        self.birthdays()


    def birthdays(self):

        self.driver.get('https://www.facebook.com/events/birthdays/')
        logging.info('Redirected to the Birthdays section')
        sleep(3)

        soup = BeautifulSoup(self.driver.page_source,'lxml')
        b_container = soup.find('div',{'id':'birthdays_recent_card'}).parent

        logging.info('{} people have their birthdays today'.format(len(b_container.findAll('textarea'))))
        logging.info('Commence posting birthday wishes')
        text_areas = [i.get('id') for i in b_container.findAll('textarea')]

        for ID in text_areas:
            self.driver.find_element_by_id(ID).send_keys('Wish you a very happy birthday!'+ Keys.ENTER)
            sleep(3)

        logging.info('Posted all the wishes')
        
        logging.info('Bot run successful!')    

        
        



if __name__ == '__main__':

    obj = AutoFB()
    #obj.login()
    #obj.birthdays()
    
