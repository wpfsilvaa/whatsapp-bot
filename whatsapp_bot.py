from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import os

def config():
    EDGE_DRIVER_PATH = "msedgedriver.exe"
    usuario_dir = "C:/Users/SEU_USUARIO/AppData/Local/Microsoft/Edge/User Data/NOVO_PERFIL_CRIADO"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    options = webdriver.EdgeOptions()
    options.add_argument(f"--user-data-dir={usuario_dir}")
    options.add_argument(f"--user-agent={user_agent}")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--log-level=3")
    service = Service(EDGE_DRIVER_PATH)
    return webdriver.Edge(service=service, options=options)

def abrir_arquivo(nome_do_arquivo):
    if not os.path.exists(nome_do_arquivo):
        raise FileNotFoundError(f"Arquivo '{nome_do_arquivo}' não encontrado.")
    
    with open(nome_do_arquivo, 'r', encoding="UTF-8") as arquivo:
        linhas = [linha.strip() for linha in arquivo.readlines() if linha.strip()]
    if not linhas:
        raise ValueError(f"O arquivo '{nome_do_arquivo}' está vazio.")
    return linhas

def abrir_whatsapp(driver):
    driver.get("https://web.whatsapp.com")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[contenteditable="true"]')))
    print("Login realizado com sucesso no WhatsApp Web.")

def enviar_mensagem(driver, numero, mensagem):
    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
    driver.get(link)
    try:
        send_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Enviar"]'))
        )
        send_button.click()
        print(f"Mensagem enviada para {numero}: {mensagem}")
    except Exception as e:
        print(f"Erro ao enviar mensagem para {numero}: {e}")

def disparo_modo_1(driver):
    mensagem = input("Digite a mensagem a ser enviada em massa: ")
    try:
        telefones = abrir_arquivo("numeros.txt")
        for numero in telefones:
            enviar_mensagem(driver, numero, mensagem)
            time.sleep(random.uniform(3.0, 15.0))
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        driver.quit()

def disparo_modo_2(driver):
    try:
        linhas = abrir_arquivo("numeros_mensagem.txt")
        mensagens = [dict(numero=linha.split(';')[0], mensagem=linha.split(';')[1]) for linha in linhas]
        for contato in mensagens:
            enviar_mensagem(driver, contato["numero"], contato["mensagem"])
            time.sleep(random.uniform(3.0, 15.0))
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        driver.quit()

if __name__ == '__main__':
    driver = config()
    with driver:
        try:
            print("Logue no WhatsApp para acessar as opções.")
            abrir_whatsapp(driver)
            print("Selecione uma opção:")
            print("(1) Disparo em massa (mensagem única para vários números)")
            print("(2) Disparo em massa (mensagens personalizadas)")
            escolha = int(input(":: "))
            if escolha == 1:
                disparo_modo_1(driver)
            elif escolha == 2:
                disparo_modo_2(driver)
            else:
                print("Opção inválida.")
        except Exception as e:
            print(f"Erro geral: {e}")
        finally:
            driver.quit()
