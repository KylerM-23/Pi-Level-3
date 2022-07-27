import os, sys

print("If the code stops, enter y in the temrinal.")

os.system("cd /usr/bin && sudo rm python && sudo ln -s python3 python")

success = 0
failed = []

modules = {
    'Update': "sudo apt-get update",
    "Upgrade": 'sudo apt-get upgrade',
    "Libport Audio": "sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev",
    "Pyaudio Method": "sudo apt-get install python-pyaudio",
    "Pyaudio Pip Method": "sudo pip3 install pyaudio",
    "Espeak" : "sudo apt install espeak",
    "Pyttsx3": "sudo pip3 install pyttsx3",
    "Matplotlib": "sudo apt install python3-matplotlib",
    "Vosk": "sudo pip3 install vosk",
    "Sounddevice": "sudo pip3 install sounddevice",
    "Numpy": "sudo pip3 install numpy"
    }

for act, cmd in modules.items():
    print("Installing", act)
    for x in range(1,4):
        if os.system(cmd) == 0:
            success += 1
            break
        if x == 3:
            failed.append(act)
            
if success == len(modules.keys()):
    print("\nInstallation Success.")
else:
    print ("These modules failed to install. Try running the command in the terminal.")
    print(failed)



