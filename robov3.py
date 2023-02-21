import os
import re
import clipboard as c
import time
import pyautogui

print("------------Inicio do Programa--------")
# o set é um conjunto(lista []) que tem como propriedade não possuir elementos iguais
listXmls = set(os.listdir("xmls/"))


# essa função (extractCodeXml) serve pra limpar todos
# os caracteres do nome do xml e deixar
# só os digitos


def extractCodeXml(code):
    return re.sub("\D", "", re.sub(
        "[a-z]", "", code))


setXmls = set(map(extractCodeXml, listXmls))

os.system('pause')
for xml in setXmls:
    time.sleep(3)
    print(xml)
    c.copy(xml)
    xmlCopied = c.paste()
    # o while é pra forçar que seja copiado o xml da vez
    while xmlCopied != xml:
        c.copy(xml)
        time.sleep(1)
        xmlCopied = c.paste()
    pyautogui.keyDown('f4')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('f8')

print("------------Fim do Programa--------")
