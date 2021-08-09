import os 
import win32com.client as win32 


hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")

hwp.Open("C:/Users/rootsj/Desktop/hiconcy/static/test.hwp")
hwp.SaveAs("C:/Users/rootsj/Desktop/hiconcy/static/test.pdf", "PDF")


hwp.Quit()