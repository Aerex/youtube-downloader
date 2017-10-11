from gmusicapi import Musicmanager
from ..oauth import Oauth
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Google(object):
    def __init__(self, config={}):
        self.config = config
        self.mm = Musicmanager()

    def login(self):
        PHANTOM_JS_PATH = '/usr/local/bin/phantomjs'
        self.oauth = Oauth(self.config)
        self.oauth.createFlow()
        url = self.oauth.getAuthUrl()

        #1 Go to authorization URL
        driver = webdriver.PhantomJS(executable_path=PHANTOM_JS_PATH)
        driver.set_window_size(1920, 1080)
        driver.get(url)

        #2 Enter email
        wait = WebDriverWait(driver, 20)
        email = driver.find_element_by_xpath('//form//input[@id="Email"]')
        email.send_keys(self.config['email'])
        next = wait.until(EC.element_to_be_clickable((By.XPATH, '//form//input[@id="next"]')))
        next.click()

        #3 Enter Password
        password = wait.until(EC.element_to_be_clickable((By.XPATH,'//form//input[@id="Passwd"]')))
        password.send_keys(self.config['password'])
        signIn = wait.until(EC.element_to_be_clickable((By.XPATH, '//form//input[@id="signIn"]')))
        signIn.click()

        #5 Approve authorization
        approve = wait.until(EC.element_to_be_clickable((By.XPATH, '//form//button[@id="submit_approve_access"]')))
        approve.click()

        #6 Get code
        code = str(driver.title.strip('Success code='))

        driver.quit()
        print code
        credentials = self.oauth.getCredentials(code)

        if not self.mm.is_authenticated():
            self.mm.login(oauth_credentials=credentials)

    def upload(self, path, match):
        if not self.mm:
            raise StandardError('MusicManager is not defined')

        if not self.mm.is_authenticated():
            self.login()

        return self.mm.upload(path, enable_matching=match)

