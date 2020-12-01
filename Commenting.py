from selenium import webdriver
from time import sleep

class tanmay_bhat:
    def __init__(self, username, password, comment):
        self.bot = webdriver.Firefox()
        self.username = username
        self.password = password
        self.comment = comment

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
        print("\nLoggedin Successfully!\n")
        sleep(2)
        self.bot.get('https://www.youtube.com/c/TanmayBhatYouTube/videos')

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

    def start_liking_and_commenting(self):
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
            
            comment_box = bot.find_element_by_xpath('//*[@id="simplebox-placeholder"]')
            comment_box.click()
            textbox = bot.find_element_by_xpath('//*[@id="contenteditable-root"]')
            textbox.send_keys(comment)
          
            submit_button = bot.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[3]/ytd-comment-dialog-renderer/ytd-commentbox/div/div[4]/div[5]/ytd-button-renderer[2]/a')            
            submit_button.click()

print("HI BOT ARMYYYYYYY! How you doing?\nToday is the time to make our PROVIDER (BOT LEADER) proud by liking and commenting all his videos!\n\nLet's make hime proud!!\n\n")
username = str(input("Enter your YouTube/Google Email ID: "))
password = str(input("Enter your password: "))
comment = str(input("Enter the text you want to comment: "))

bot_army = tanmay_bhat(username,password,comment)
bot_army.login()
bot_army.start_liking_and_commenting()
print("\n\nALL VIDEOS ARE LIKED!!! YOU CAN NOW OFFICIALLY CALL YOURSELF:\nA PROUD BOT ARMY MEMBERRRRR!!!!!!\n\n\nPress any key to end")
input()

# Hey Jaydeep, bro my discord is BishBoi#1715 plis contect <3
