import pyautogui
import time

def espera(segundos=2):
    time.sleep(segundos)

def clique(x,y,delay=3):
    espera(delay)
    pyautogui.click(x = x, y =y)

def dois_cliques(x,y,delay=3):
    espera(delay)
    pyautogui.doubleClick(x = x, y =y)


def abrir_site(nome_site, delay=3):
    espera(delay)
    pyautogui.write(nome_site)
    espera(delay)
    pyautogui.press('enter')
    espera(2)
   
  

def senha(senha,delay=3):
    espera(delay)
    pyautogui.write(senha)
    espera(5)
    pyautogui.press('enter')
    espera(2)


def escrever(delay =3):
    espera(delay)
    pyautogui.press('tab')
    espera(2)
    pyautogui.write('Atividade Pyautogui')
    espera(delay)
    pyautogui.press('tab')
    espera(delay)


#verificar cursos senac em taquaraqlto


clique(1211, 1051)
clique(1779, 127)
abrir_site('bevenutoportuga@gmail.com')
senha("573802Chpw")
clique(1730, 118)
clique(87, 193)
abrir_site('mateusgn@to.senac.br')
escrever()
clique(1422, 996)
clique(127, 200)
dois_cliques(568, 160)
clique(536, 304)
clique(800, 510)
clique(1303, 998)
