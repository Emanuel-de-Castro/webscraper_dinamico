import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


produto = input("Digite o nome do produto que deseja procurar: ")


driver = webdriver.Chrome()
driver.get('https://www.enjoei.com.br/')

with open("enjoei.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"\n--- ITEM: {produto.upper()} ---\n")

produtos_salvos = set()



time.sleep(random.uniform(3, 5))
botao_sair = driver.find_element(By.XPATH, "//button[@class='c-modal__close']")
botao_sair.click()

campo_pesquisa = driver.find_element(By.XPATH, "//input[@class='search-input__input']")
campo_pesquisa.click()
time.sleep(random.uniform(3, 5))
campo_pesquisa.send_keys(produto)
time.sleep(random.uniform(1, 3))
campo_pesquisa.send_keys(Keys.ENTER)
time.sleep(random.uniform(1, 4))

try:
    while True:
        time.sleep(random.uniform(3, 5))
        cards = driver.find_elements(By.XPATH, "//div[contains(@class,'c-product-card')]")

        for card in cards:
            try:
                nome = card.find_element(By.XPATH, ".//h2[contains(@class,'c-product-card__title')]").text
                preco = card.find_element(By.XPATH, ".//span[contains(@class,'c-product-card__price')]/span[1]").text
                link = card.find_element(By.XPATH, ".//a[contains(@href, '/p/')]").get_attribute("href")
                item = f"{nome} - {preco} - {link}"
                # print(item)

                if item not in produtos_salvos:
                    produtos_salvos.add(item)
                    with open("enjoei.txt", "a", encoding="utf-8") as arquivo:
                        arquivo.write(item + os.linesep)
                        
            except:
                # Se este elemento não tiver nome/preco/link, ele ignora e segue
                continue

        try:
            time.sleep(random.uniform(3, 5))
            driver.execute_script("""let altura = document.documentElement.scrollHeight;window.scrollTo(0, altura * 0.9);""")
            botao_proximo = driver.find_element(By.XPATH, "//a[@data-test='button-proxima']")
            time.sleep(random.uniform(2,3))
            botao_proximo.click()
        except:
            print("Robô interrompido")
            break
except KeyboardInterrupt:
    print("Robô interrompido pelo usuário.")
finally:
    driver.quit() 