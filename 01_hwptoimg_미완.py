import os 
import win32com.client as win32 
import win32gui 

BASE_DIR = "C:\\Users\\rootsj\\Desktop\\hiconcy\\static\\" 
os.chdir(BASE_DIR)

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject") 
hwnd = win32gui.FindWindow(None, "빈 문서 1 - 한글")

print(hwnd) 
print(hwp)

win32gui.ShowWindow(hwnd, 0) 

file_list = [file for file in os.listdir() if file != "result"] 
print(file_list) 

for i in file_list: 
    hwp.Open(os.path.join(BASE_DIR, i)) 
    true_false = hwp.CreatePageImage(BASE_DIR + "\\" + i , 0, resolution=600) 
    if true_false == True: 
        print("Success") 
    else: 
        print("Fail") 
        
hwp.Quit()