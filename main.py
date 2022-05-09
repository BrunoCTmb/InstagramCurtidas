from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


browser = Chrome()

browser.get('https://instagram.com')

def login():
    login_nome = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
    login_senha = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')))
    login_botao = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')))
    login_nome.send_keys('zazaduza10@gmail.com')
    login_senha.send_keys('1234567890b')
    login_botao.click()

    pu_botao1 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')))
    pu_botao1.click()

    pu_botao2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')))
    pu_botao2.click()

def profile():
    browser.get('https://instagram.com/fallen')

def pegar_fotos():
    todas_fotos = browser.find_elements_by_tag_name('a')
    
    links = []
    for fotos in todas_fotos:
        href = fotos.get_attribute('href')
        #print(href)
        if href.startswith('https://www.instagram.com/p/'):
            
            links.append(href)

    print(links)

    return links

def curtir_foto(todos_links):
    for link in todos_links:
        browser.get(link)
        botao_curtir = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')))
        botao_curtir.click()

login()
profile()
link_fotos = pegar_fotos()
curtir_foto(link_fotos)
