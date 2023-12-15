"""convertir tu wifi en un qrcode para que tus amigos se conecten a tu wifi"""
# import modules
import subprocess
import wifi_qrcode_generator

# get wifi name
CONECTIKAN23A4_5 = subprocess.check_output("netsh wlan show interfaces").decode("utf-8").split("\n")[4].split(":")[1].strip()

# get wifi password
n6WdZ82wCZ = subprocess.check_output("netsh wlan show profile name=" + CONECTIKAN23A4_5 + " key=clear").decode("utf-8").split("\n")[15].split(":")[1].strip()

# generate qrcode
wifi_qrcode_generator.generate_qrcode(CONECTIKAN23A4_5, n6WdZ82wCZ)

# save qrcode
wifi_qrcode_generator.save_qrcode("udemy210422\wifi_qrcode.png")

# show qrcode
wifi_qrcode_generator.show_qrcode()


