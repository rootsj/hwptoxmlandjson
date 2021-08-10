import os 
import win32com.client as win32 

BASE_DIR = "C:\\Users\\rootsj\\Desktop\\hiconsy\\static\\" 
os.chdir(BASE_DIR)

print(os.listdir())

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")

for i in os.listdir():
    hwp.Open(os.path.join(BASE_DIR, i))
    hwp.SaveAs(BASE_DIR+"\\"+i+".pdf", "PDF")

hwp.Quit()