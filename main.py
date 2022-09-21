import internetSpeedTwitterBot

# Parameters
PROMISED_DOWN = 50
PROMISED_UP = 25
CHROME_DRIVER = r"C:\Users\MBmah\OneDrive\Documents\chromedriver_win32\chromedriver.exe"
TWITTER_EMAIL = "webmail@gmail.com"
TWITTER_PASSWORD = "************"

# Creating a TwitterNot object
speed_test = internetSpeedTwitterBot.TwitterBot(CHROME_DRIVER)

# Calling the function to get the internet speed and the function to tweet the speed
speed_test.get_internet_speed()
speed_test.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD, PROMISED_DOWN, PROMISED_UP)

