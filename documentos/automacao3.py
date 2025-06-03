import pyautogui
import time

def espera(segundos=2):
    time.sleep(segundos)

def clique(x,y,delay=2):
    espera(delay)
    pyautogui.click(x = x, y =y)

def dois_cliques(x,y,delay=2):
    espera(delay)
    pyautogui.doubleClick(x = x, y = y)

def abrir_site(nome_site, delay=2):
    espera(delay)
    pyautogui.write(nome_site)
    espera(delay)
    pyautogui.press('enter')
    espera(1)

#verificar cursos senac em taquaraqlto


clique(1809, 22)
dois_cliques(104, 729)
abrir_site('https://www.to.senac.br/')
clique(1184, 254)
clique(1244, 423)
