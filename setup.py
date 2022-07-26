import os, sys

os.system("cd /usr/bin && sudo rm python && sudo ln -s python3 python")

success = 0

modules = {
    'Update': "sudo apt-get update",
    "Upgrade": 'sudo apt-get upgrade',
    "Libport Audio": "sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev",
    "Pyaudio Method": "sudo apt-get install python-pyaudio",
    "Pyaudio Pip Method": "sudo pip3 install pyaudio",
    "Espeak" : "sudo apt install espeak",
    "Pyttsx3": "sudo pip3 install pyttsx3",
    "Matplotlib": "sudo apt install python3-matplotlib"
    }

for act, cmd in modules.items():
    print("Installing", act)
    for x in range(1,4):
        if os.system(cmd) == 0:
            success += 1
            break
        
if success == len(modules.keys()):
    print("\nInstallation Success.")
else:
    print ("\nSome libraries were not installed. Try again.")


