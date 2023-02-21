import os
import clipboard as c
import time
import pyautogui
print("------------Inicio do Programa--------")
os.system('pause')
for arq in os.listdir("xmls/"):
    time.sleep(4)
    print(arq)
    codigo = arq.replace("-nfe.xml","")
    c.copy(codigo)
    pyautogui.keyDown('f4')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('f8')

print("------------Fim do Programa--------")