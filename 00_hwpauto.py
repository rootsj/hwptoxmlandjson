import win32com.client as win32 
import win32gui 
import win32con

# 아래아한글 실행하기
hwp = win32.Dispatch("HWPFrame.HwpObject")

# 아래아한글의 핸들값 찾기
hwnd = win32gui.FindWindow(None, "빈 문서 1 - 한글")
print(hwnd)

# 아래아한글 백그라운드로 숨기기
win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

# 아래아한글이 실행중인지 확인하기
hwp.InitScan()
hwp.GetText()
hwp.GetText()
hwp.GetText()
hwp.GetText()

# 아래아한글 숨기기 해제
win32gui.ShowWindow(hwnd, win32con.SW_SHOW)

# 아래아한글 종료
hwp.Quit()