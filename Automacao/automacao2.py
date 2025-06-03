import pyautogui
import time

pyautogui.press('win')
time.sleep(3)
pyautogui.write('chrome')

time.sleep(3)

pyautogui.press('enter')

pyautogui.hotkey('alt', 'f4') # combina duas teclas
time.sleep(3)

pyautogui.click(x=1809, y=22)

time.sleep(2)

pyautogui.doubleClick(x=104, y=729)
time.sleep(1)
pyautogui.write('https://www.to.senac.br/')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=1862, y=32)
time.sleep(1)
pyautogui.click(x=1183, y=256)
time.sleep(1)
pyautogui.click(x=1185, y=253)
time.sleep(1)
pyautogui.click(x=1212, y=435)
                
time.sleep(1)
pyautogui.press('enter')

# import pyautogui
# import time

# pyautogui.doubleClick(x=104, y=729)

# import webbrowser

# Substitua pelo seu provedor de email, por exemplo, Gmail
# email_url = 'https://accounts.google.com/v3/signin/challenge/pwd?TL=AArrULS_MYUd4gZajzq6oXLe7-8MbuWKfideVhyeaScKdLEvQpVxUZLmX-walhzf&checkConnection=youtube%3A446&checkedDomains=youtube&cid=2&continue=https%3A%2F%2Fwww.google.com.br%2F&dsh=S874708198%3A1747182264110784&ec=futura_ctr_og_so_72776761_p&flowEntry=ServiceLogin&flowName=GlifWebSignIn&hl=pt-BR&ifkv=ASKV5Mi1hMLYcEk_o8bAaJZhz-naExZb9e1wDgomrJLo69kSaAn4DsC2zsRfb3O7Etdlb-TiF5tT&pstMsg=1'

# # Abre o email no navegador padrão
# webbrowser.open(email_url)
# import pyautogui
# import time
# time.sleep(2)

# time.sleep(1)
# pyautogui.write('www.gmail.com.br')
# time.sleep(1)
# pyautogui.press('enter')

