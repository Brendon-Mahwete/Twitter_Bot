from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:

    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.down = "0"
        self.up = "0"

# This gets the download and upload internet speed
    def get_internet_speed(self):
        driver = webdriver.Chrome(executable_path=self.driver_path)
        driver.get("https://www.speedtest.net/")

        time.sleep(5)

        close_cookies = driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button')
        close_cookies.click()

        time.sleep(5)

        go_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                  '1]/a/span[4]')
        time.sleep(5)
        go_button.click()

        time.sleep(60)

        self.down = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                  '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        return f"download Mbps {self.down}, upload Mbps {self.up}"

    #This will tweet the message detail the promised speed vs the actual speed
    def tweet_at_provider(self, email, password, promised_down, promised_up):
        driver = webdriver.Chrome(executable_path=self.driver_path)
        driver.get("https://twitter.com/")

        time.sleep(10)

        # Loggin in to twitter
        while True:
            try:
                login_button = driver.find_element(By.XPATH,
                                                   '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div['
                                                   '1]/div/div[3]/div[5]/a/div/span/span')
                login_button.click()
                break
            except selenium.common.exceptions.NoSuchElementException:
                pass

        time.sleep(10)

        # Entering the email
        while True:
            try:
                input_email = driver.find_element(By.NAME, 'text')
                input_email.send_keys(email)
                input_email.send_keys(Keys.ENTER)
                break
            except selenium.common.exceptions.NoSuchElementException:
                print("Cant find email input tag")

        time.sleep(10)

        # Entering the password
        while True:
            try:
                input_password = driver.find_element(By.NAME, 'password')
                input_password.send_keys(password)
                input_password.send_keys(Keys.ENTER)
                break
            except selenium.common.exceptions.NoSuchElementException:
                try:
                    # When using the program to login titter sets up a section to input your user name
                    username = driver.find_element(By.NAME, "text")
                    username.send_keys("username")
                    username.send_keys(Keys.ENTER)
                except selenium.common.exceptions.NoSuchElementException:
                    print("Cant log in")

        time.sleep(5)

        # Tweeting the message
        while True:
            try:
                # In order to access the input section I'll have to click the 'open_tweet_input' then the input dive
                # will appear
                open_tweet_input = driver.find_element(By.XPATH,
                                                       '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                       '1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                       '1]/div/div/div/div/div/div/div/div/div/div/label/div['
                                                       '1]/div/div/div/div/div/div[2]/div/div/div/div')
                open_tweet_input.click()
                time.sleep(5)
                tweets = driver.find_element(By.XPATH,
                                             '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div['
                                             '2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                             '1]/div/div/div/div/div/div[2]/div/div/div/div/label/div['
                                             '1]/div/div/div/div/div/div[2]/div/div/div/div')
                tweets.send_keys(f"Hey Internet Provider, why is my internet speed {self.down} mbps download /{self.up} "
                                 f"mbps upload when I pay for {promised_down} mbps download /{promised_up} mbps upload?")
                print(f"Hey Internet Provider, why is my internet speed {self.down} mbps download /{self.up} "
                      f"mbps upload when I pay for {promised_down} mbps download /{promised_up} mbps upload?")
                tweet = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                      '1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                      '3]/div/div/div[2]/div')
                tweet.click()
                break
            except selenium.common.exceptions.NoSuchElementException:
                print("Unable to find the input section")
