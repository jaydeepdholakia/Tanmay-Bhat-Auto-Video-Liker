from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from getpass import getpass
import tkinter as tk
from tkinter import messagebox

class tanmay_bhat:
    def __init__(self, username, password, channel_addr):

        try:
            #Check for Chrome webdriver in Windows
            self.bot = webdriver.Chrome('driver/chromedriver.exe')
        except WebDriverException:
            try: 
                #Check for Chrome webdriver in Linux
                self.bot = webdriver.Chrome('/usr/bin/chromedriver') 
            except WebDriverException:
                print("Please set Chrome Webdriver path above")
                exit()

        self.username = username
        self.password = password
        self.channel_addr = channel_addr

    def login(self):
        bot = self.bot
        print("\nStarting Login process!\n")
        bot.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
        bot.implicitly_wait(10)
        self.bot.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.bot.find_element_by_xpath('//input[@type="email"]').send_keys(self.username)
        self.bot.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.bot.find_element_by_xpath('//input[@type="password"]').send_keys(self.password)
        self.bot.find_element_by_xpath('//*[@id="passwordNext"]').click()
        WebDriverWait(self.bot, 900).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div/div[1]/a[2]/span")))
        print("\nLoggedin Successfully!\n")
        sleep(2)
        self.bot.get(self.channel_addr + "/videos")

    def start_liking(self):
        bot = self.bot
        scroll_pause = 2
        last_height = bot.execute_script("return document.documentElement.scrollHeight")
        while True:
            bot.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            sleep(scroll_pause)

            new_height = bot.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                print("\nScrolling Finished!\n")
                break
            last_height = new_height
            print("\nScrolling")

        all_vids = bot.find_elements_by_id('thumbnail')
        links = [elm.get_attribute('href') for elm in all_vids]
        links.pop()
        for i in range(len(links)):
            bot.get(links[i])

            like_btn = bot.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a')
            check_liked = bot.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]')
            # Check if its already liked
            if check_liked.get_attribute("class") == 'style-scope ytd-menu-renderer force-icon-button style-text':
                like_btn.click()
                print("Liked video! Bot Army Zindabad!!!\n")
                sleep(0.5)
            elif check_liked.get_attribute("class") == 'style-scope ytd-menu-renderer force-icon-button style-default-active':
                print("Video already liked. You are a good Bot Army Member\n")




#**************************************************     GUI AREA     **********************************************

def start():
    if email_entry.get() and  password_entry.get() and url_entry.get():
        bot_army = tanmay_bhat(email_entry.get(), password_entry.get(), url_entry.get())
        root.destroy()
        bot_army.login()
        bot_army.start_liking()
    else:
        messagebox.showinfo('Notice', 'Please fill all the entries to proceed furthur')

def tanmay_url_inject():
    url_entry.delete(0, tk.END)
    url_entry.insert(0, "https://www.youtube.com/c/TanmayBhatYouTube")

root = tk.Tk()           
root.resizable(False, False)
root.geometry('%dx%d+%d+%d' % (760, 330, (root.winfo_screenwidth()/2) - (760/2), (root.winfo_screenheight()/2) - (330/2)))

frame = tk.Frame(root, height=330, width=760)
head_label = tk.Label(frame, text='Youtube Video Liker', font=('verdana', 25))
email_label = tk.Label(frame, text='Email: ', font=('verdana', 15))
password_label = tk.Label(frame, text='Password: ', font=('verdana', 15))
email_entry = tk.Entry(frame, font=('verdana', 15))
password_entry = tk.Entry(frame, font=('verdana', 15), show="*")
url_label = tk.Label(frame, text='Channel\nURL', font=('verdana', 15))
url_entry = tk.Entry(frame, font=('verdana', 15))
tanmay_button = tk.Button(frame, text='Tanmay\nBhatt', font=('verdana', 15), command=tanmay_url_inject)
start_button = tk.Button(frame, text='Start Liking', font=('verdana', 20), command=start)

frame.pack()
head_label.place(y=15, relx=0.32)
email_label.place(x=15, y=95, anchor='w')
password_label.place(x=15, y=130, anchor='w')
email_entry.place(x=140, y=78, width=600)
password_entry.place(x=140, y=115, width=600)
url_label.place(x=15, y=190, anchor='w')
url_entry.place(x=140, y=175, width=600)
tanmay_button.place(x=400, y=240)
start_button.place(x=550, y=250)
root.mainloop()


"""
Comment out the GUI area and uncomment the Console Area to use Console controls
**********************************************   Console Area    *******************************************

print("HI BOT ARMYYYYYYY! How you doing?\nToday is the time to make our PROVIDER (BOT LEADER) proud by liking all his videos!\n\nLet's make hime proud!!\n\n")

print("Enter the link of the channel or just hit [ENTER] key for default Tanmay's Channel")
channel_addr = str(input("Channel Link: "))

username = str(input("\nEnter your YouTube/Google Email ID: "))
password = str(getpass("Enter your password: "))

if not channel_addr:
    channel_addr = "https://www.youtube.com/c/TanmayBhatYouTube"


bot_army = tanmay_bhat(username, password, channel_addr)
bot_army.login()
bot_army.start_liking()
print("\n\nALL VIDEOS ARE LIKED!!! YOU CAN NOW OFFICIALLY CALL YOURSELF:\nA PROUD BOT ARMY MEMBERRRRR!!!!!!\n\n\nPress any key to end")
input()
"""