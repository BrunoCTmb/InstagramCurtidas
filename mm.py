from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Bot_instagram:
    def __init__(self):
        self.browser = Chrome()

    def browser_init(self):
        self.browser.get('https://instagram.com')

    def login(self):
        self.name_login = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
        self.password_login = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')))
        self.button_login = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')))
        self.name_login.send_keys('zazaduza10@gmail.com')
        self.password_login.send_keys('1234567890b')
        self.button_login.click()

        self.pu_button1 = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')))
        self.pu_button1.click()
        self.pu_button2 = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')))
        self.pu_button2.click()

    def get_profile(self):
        self.browser.get('https://instagram.com/fallen')
        
        self.all_photos = self.browser.find_elements_by_tag_name('a')

        self.links = []
        for pic in self.all_photos:
            href = pic.get_attribute('href')
            #print(href)
            if href.startswith('https://www.instagram.com/p/'):
                
                self.links.append(href)

        return self.links

    def like_all_photos(self):
        print(self.links)

    '''def like_all_photos(self):
        for link in todos_links:
            browser.get(link)
            botao_curtir = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')))
            botao_curtir.click()'''
        

bot = Bot_instagram()

bot.browser_init()
bot.login()
bot.get_profile()
