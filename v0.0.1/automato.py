
# Importações das bibliotecas
import pyautogui
from time import sleep, localtime

#Declaração de váriaveis

ctab = 0
cposto = 0
c = 0
data = localtime()

dia = data[2]

ano = data[0]

if data[1] >= 10:
    mes = data[1]
else:
    mes = f'0{data[1]}'

postos = [1,2,5,6,7,8,9,10,11,279]

# Abrir o navegador, logar no sistema e selecionar a opção desejada

pyautogui.press('win')
sleep(1)
pyautogui.write('chrome')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.hotkey('ctrl', 't')
pyautogui.write('lis.humanizalab.com.br')
pyautogui.press('enter')
sleep(50)
pyautogui.press('tab')
pyautogui.press('enter')
sleep(1)
pyautogui.write('emissao de previa')
sleep(1)
pyautogui.press('enter')

while True:
    if ctab < 26:
        pyautogui.press('tab')
        ctab += 1
    else:
        ctab = 0
        break
    
sleep(1)
              
# Inicio do loop para emitir o espelho de cada posto do dia desejado            
                                
while True:
    if c < 10:
        pyautogui.write(f'{dia-1}{mes}{ano}')
        pyautogui.press('tab')
        sleep(1)
        pyautogui.write(f'{dia-1}{mes}{ano}')
        pyautogui.press('tab')
        pyautogui.write('10')
        sleep(1)
        pyautogui.press('down')
        pyautogui.press('enter')

        while True:
            if ctab < 5:
                pyautogui.press('tab')
                ctab += 1
            else:
                ctab = 0
                break                               
        sleep(1)
        
        pyautogui.write(f'{postos[c]}')
        
        sleep(1)
        
        if c == 0:
            while True:
                if ctab < 4:
                    pyautogui.press('down')
                    ctab += 1
                else:
                    ctab = 0
                    break
            pyautogui.press('enter')
            sleep(1)
        else:
            pyautogui.press('down')
            pyautogui.press('enter')
            sleep(1)
        
        while True:
                if ctab < 6:
                    pyautogui.press('tab')
                    ctab += 1
                else:
                    ctab = 0
                    break                               
        sleep(1)
        pyautogui.write('25')
        sleep(1)
        pyautogui.press('down')
        pyautogui.press('enter')
        sleep(1)
        
        while True:
                if ctab < 22:
                    pyautogui.hotkey('shift', 'tab')
                    ctab += 1
                else:
                    ctab = 0
                    break       
        sleep(1)
        pyautogui.press('enter')
        sleep(1)
        
        while True:
                if ctab < 9:
                    pyautogui.press('tab')
                    ctab += 1
                else:
                    ctab = 0
                    break
        
        c += 1
        cposto +=1
        
         
            
    else: 
        break
    
# Visualiza os relatórios gerados    

while True:
    if ctab < 8:
        pyautogui.hotkey('shift', 'tab')
        ctab += 1
    else:
        ctab = 0
        break
sleep(1)
pyautogui.press('enter')