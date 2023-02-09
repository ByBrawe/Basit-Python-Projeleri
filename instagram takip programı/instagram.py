from user import username,password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#oto takip listesi,
#oto takip ettirme,
#takipten çıkartma,
#takipe takip var mı kontrol,
#scroll bar değiştir
#kaydetme işlemi
# önceki takip ettiklerini takip etmeme


class Instagram:
    def __init__(self,username,password):
        self.browserProile = webdriver.ChromeOptions()
        self.browserProile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/')
        time.sleep(3)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(4)
        #self.browser.find_element_by_css_selector('.div.publisher.a')

    def getFollowers(self):

        # document.documentelement.scrollheight

        # window.scrollTo(0,document.documentelement.scrollheight)

        # last_height = self.browser.execute_script("return document.documentelement.scrollheight")

        # while True:
        #     self.browser.execute_script("window.scrollTo(0,document.documentelement.scrollheight)")
        #     time.sleep(2)
        #     new_height = self.browser.execute_script("return document.documentelement.scrollheight")
        #     if last_height == new_height:
        #         break
        #     new_height = last_height

        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")

        self.browser.maximize_window()
        followersCount = len(dialog.find_elements_by_css_selector("li"))
        print(f"first count: {followersCount}")
        action = webdriver.ActionChains(self.browser)

        i = 0
        while i < 10:

            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followersCount != newCount:
                followersCount = newCount
                print(f"Second Count: {newCount}")
                time.sleep(1)
            else:
                break
            i += 1
        followers = dialog.find_elements_by_css_selector("li")


        followerList = []
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followerList.append(link)
        with open("followers.txt","w", encoding= "UTF-8") as file:
            for item in followerList:
                file.writelines(item + "\n")

    def getLikingUser(self):

        self.browser.get(f"https://www.instagram.com/p/CJQRdr0Bk31/")
        time.sleep(2)
        self.browser.find_element_by_xpath("//section/div/div/button").click()
        time.sleep(2)
        self.browser.maximize_window()

        dialog = self.browser.find_element_by_xpath("//div/div/div/div/div/div/div[2]/div[2]")
        #dialog = self.browser.find_element_by_css_selector("div[aria-labelledby]")


        followersCount = len(self.browser.find_elements_by_xpath("//div/div/span/a"))
        print(f"first count: {followersCount}")
        action = webdriver.ActionChains(self.browser)


        i = 0
        while i < 100:

            dialog.click()

            action.key_down(Keys.SPACE).key_up(Keys.SPACE).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            i += 1

            time.sleep(1)
            newCount = len(self.browser.find_elements_by_xpath("//div/div/span/a"))

            if followersCount != newCount:
                followersCount = newCount
                print(f"Second Count: {newCount}")
                time.sleep(1)
            else:
                break
            i += 1
                
        followers = self.browser.find_elements_by_xpath("//div/div/span/a")

        followerList = []
        for user in followers:
            link = user.get_attribute("href")
            followerList.append(link)
        with open("liking.txt", "w", encoding="UTF-8") as file:
            for item in followerList:
                file.writelines(item + "\n")

    def followUser(self, username):


            self.browser.get("https://www.instagram.com/"+ username)
            followButton = self.browser.find_element_by_tag_name("button")
            if followButton.text != "Following":
                followButton.click()
                time.sleep(2)
            else:
                print("Zaten takiptesin")

    def followUsers(self):

        with open('followers.txt') as f:
            mylist = f.read().splitlines()


        for user in mylist:
            self.browser.get(user)
            followButton = self.browser.find_element_by_tag_name("button")
            time.sleep(2)
            print(followButton.text)
            if followButton.text != "Following":
                time.sleep(1)
                followButton.click()
                print(str(user) + " 'i takip ettin.")
                time.sleep(2)
            else:
                print(str(user) +" için Zaten takiptesin.")
                time.sleep(2)

    def unFollowUser(self,username):
        self.browser.get("https://www.instagram.com/" + username)
        time.sleep(2)

        followButton = self.browser.find_element_by_xpath("//span[@aria-label='Following']")


        if followButton.get_attribute("aria-label") == "Following":
            followButton.click()
            time.sleep(2)
            confirmButton = self.browser.find_element_by_xpath('//button[text()="Unfollow"]')
            confirmButton.click()
        else:
            print("zaten takip etmiyorsun")

        #pass
    def unFollowUsers(self):

        with open('followers.txt') as f:
            mylist = f.read().splitlines()

        for user in mylist:

            self.browser.get(user)
            time.sleep(1)

            followButton = self.browser.find_element_by_tag_name("button")
            if followButton.text == "Follow":
                print(user + " " + followButton.text)

            elif followButton.text == "Follow Back":
                print(user + " " + followButton.text)
            elif followButton.text == "Message":
                followButton = self.browser.find_element_by_xpath("//span[@aria-label='Following']")
                followButton.click()
                time.sleep(2)
                confirmButton = self.browser.find_element_by_xpath('//button[text()="Unfollow"]')
                time.sleep(0.5)
                confirmButton.click()
                print(str(user) + " 'i takipden çıktın.")
            else:
                print("farklı bir problem var")




        #pass

instagram = Instagram(username,password)
instagram.signIn()
instagram.getLikingUser()

#instagram.getFollowers()
#instagram.followUser("kod_evreni")
#instagram.unFollowUser("kod_evreni")
#instagram.followUsers()
#instagram.unFollowUsers()