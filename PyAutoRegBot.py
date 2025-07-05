import pyautogui, sys
import time
import pyperclip

#Deve ser aberto no EDGE, com um grupo de 3 abas
#em sequencia: citsmart, registro chat(-75% de zoom), 
#planilha escolhendo a celula acima do protocolo do bot desejado

nome_de_usuario = input ('Qual usuario deseja usar?')

try:
    quantidade_bots = int(input('Quantos bots deseja fazer?'))

except ValueError:
    print('INSIRA UM NÚMERO')
    exit()

def aba_planilha():
    pyautogui.moveTo(93, 234), pyautogui.click()

def protocolo_bot():
    pyautogui.press('down'), time.sleep(1)
    pyautogui.hotkey('ctrl', 'c'), time.sleep(1)
    pyautogui.moveTo(83, 202), pyautogui.click(), time.sleep(1)
    pyautogui.moveTo(316, 417), time.sleep(0.5)
    pyautogui.scroll(200)
    pyautogui.moveTo(292, 429), pyautogui.click(), time.sleep(0.5)
    pyautogui.moveTo(296, 494), pyautogui.click(), time.sleep(0.5)
    pyautogui.hotkey('ctrl', "v"), time.sleep(1)


def verifica_envio ():
    pyautogui.moveTo(335, 660), pyautogui.click(clicks=2), pyautogui.hotkey('ctrl', 'c') #verifica
    texto = pyperclip.paste()
    return "Agradecemos" in texto

def enviado_ou_nao():
    tentativas = 0
    tentativas_maximo = 10
    while not verifica_envio():
        tentativas+=1
        pyautogui.scroll(400), time.sleep(0.4)
        pyautogui.moveTo(377, 603), pyautogui.click(), pyautogui.press('enter'), time.sleep(8)
        if tentativas >= tentativas_maximo:
            return False
    return True
        

def aba_ist():
    pyautogui.moveTo(70, 167), pyautogui.click(), time.sleep(1)
    pyautogui.moveTo(316, 417), time.sleep(0.5)
    pyautogui.scroll(500), time.sleep(1)

def verifica_roteiro():
    roteiro_usado = pyperclip.paste()
    return "CTA-002" in roteiro_usado


def roteiro_utilizado():
    pyautogui.press('right')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    aba_ist()
    pyautogui.moveTo(1235, 224)
    time.sleep(0.5)
    pyautogui.scroll(300)
    time.sleep(0.5)
    pyautogui.moveTo(1289, 650)
    pyautogui.moveTo(1289, 593, 0.25)
    pyautogui.click()
    time.sleep(1)
    pyautogui.scroll(300)
    time.sleep(1)
    pyautogui.moveTo(300, 269, 1.5)
    pyautogui.click()
    pyautogui.write(nome_de_usuario)
    time.sleep(3)
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('c')
    time.sleep(3)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(3)
    pyautogui.write('informacao sem tramite', interval = 0.25)
    time.sleep(3)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.scroll(300)
    time.sleep(0.5) #sobe pagina pra clicar na aba de pesquisa de roteiro
    pyautogui.moveTo(1314, 224)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1235, 224)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(421, 213)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', "v")
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.moveTo(489, 507)
    pyautogui.click()
    time.sleep(2)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('tab', presses=11)
    if verifica_roteiro():
        pyautogui.write('chat abandonado')
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('c')
        time.sleep(2)
        pyautogui.press('tab')

    else:
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('d')
        time.sleep(2)
        pyautogui.press('tab')
    aba_planilha()
    pyautogui.press('right')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pyautogui.press('left')
    time.sleep(0.5)
    pyautogui.press('left')
    time.sleep(0.5)
    aba_ist()
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('tab', presses=3)
    pyautogui.press('enter')
    time.sleep(9)
    #pyautogui.moveTo(1271, 691), pyautogui.click(), time.sleep(6)
    pyautogui.moveTo(757, 187)
    pyautogui.click(clicks=2)
    time.sleep(1) #copiar ist, monitor original
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pyautogui.press('esc')
    pyautogui.moveTo(83, 202)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(284, 540)
    pyautogui.click()
    time.sleep(1) #clica no botao ist no registro
    pyautogui.moveTo(377, 603)
    pyautogui.click()
    time.sleep(1) #clica na barra de pesquisa ist
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(6)


#Copia o roteiro utilizado, cria a IST do zero, registra todas as informacoes, copia
#o codigo e registra o bot






for _ in range(quantidade_bots):
    aba_planilha() 
    protocolo_bot() 
    aba_planilha()
    roteiro_utilizado()
    if enviado_ou_nao() == False:
        print ("Máximo de tentativas, tente novamente mais tarde")
        input()
        break        
    time.sleep(2)

print("Bot finalizado com sucesso, aperte alguma tecla para sair :)")
input()

