import rpa
import os
import clipboard as c
import time

rpa.init(visual_automation = True,chrome_browser = False)

for arq in os.listdir("xmls/"):
    print(arq)
    rpa.click("btn1.png")
    # rpa.click("campo1.png")
    # rpa.type("campo1.png",arq.replace("-nfe.xml",""))
    # rpa.keyboard(arq.replace("-nfe.xml",""))
    codigo = arq.replace("-nfe.xml","")
    time.sleep(2)
    rpa.keyboard(codigo)
    # c.copy("123456")
    # c.paste()
    time.sleep(2)
    rpa.keyboard("[F8]")
    time.sleep(2)
    rpa.click("btn2.png")
    os.system('pause')
