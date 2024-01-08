from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import requests

#API 
agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

#CHAVE    xgLNUFtZsAbhZZaxkRh5ofM6Z0YIXwwv
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/HLdCobSevIHAXs7LNpGNOxkOcHfh5Iiy" ,  headers=agent)
time.sleep(1)
api = api.text
api = api.split(".n.")
notification_ball = api[3].strip()
customer_contact = api[4].strip()
box_msg = api[5].strip()
msg_client = api[6].strip()
box_msg2 = api[7].strip()
box_search = api[8].strip()


user = 'victorlima.softwaredeveloper@gmail.com'
dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r'user-data-dir=' + dir_path + 'profile/session')
driver = webdriver.Chrome(options=chrome_options2)
driver.get("http://web.whatsapp.com/")
time.sleep(10)

def bot():
    try:

        #Capturar a bolinha
        ball = driver.find_element(By.CLASS_NAME, notification_ball)
        ball = driver.find_elements(By.CLASS_NAME, notification_ball)

        click_ball = ball[-1]
        action_click_ball = webdriver.common.action_chains.ActionChains(driver)

        action_click_ball.move_to_element_with_offset(click_ball, 0,-20)
        action_click_ball.click()
        action_click_ball.perform()
        action_click_ball.click()
        action_click_ball.perform()
        
        #Capturar o telefone
        customer_phone = driver.find_element(By.XPATH, customer_contact)
        end_phone = customer_phone.text
        print(end_phone)
        # time.sleep(2)

        #Capturar o mensagem
        all_messages = driver.find_elements(By.CLASS_NAME, msg_client)
        
        all_messages_text = [e.text for e in all_messages]
        msg = all_messages_text[-1]
        print(msg)

        #Respondendo cliente
        response = requests.get('http://localhost/bot/index.php?', params={'msg': msg, 'phone': end_phone, 'user': user}, headers=agent)
        response_text = response.text
        text_camp = driver.find_element(By.XPATH, box_msg)
        text_camp.click()

        text_camp.send_keys(response_text, Keys.ENTER)

        #Fechar contato
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    except:
        print('Aguardando novas mensagens')
        #Se não, faça isso

while True:
    bot()