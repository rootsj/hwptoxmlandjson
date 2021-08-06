import os 
import win32com.client as win32 
import win32gui 


hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwp.XHwpWindows.Item(0).Visible = True  # 숨김해제


# 아래부터 페이지 여백 설정하는 코드
hwp.HAction.GetDefault("PageSetup", hwp.HParameterSet.HSecDef.HSet)  # 초기화

hwp.HParameterSet.HSecDef.PageDef.LeftMargin = hwp.MiliToHwpUnit(0.0)  # 좌측여백
hwp.HParameterSet.HSecDef.PageDef.RightMargin = hwp.MiliToHwpUnit(0.0)  # 우측여백
hwp.HParameterSet.HSecDef.PageDef.TopMargin = hwp.MiliToHwpUnit(0.0)  # 상단여백
hwp.HParameterSet.HSecDef.PageDef.BottomMargin = hwp.MiliToHwpUnit(0.0)  # 하단여백
hwp.HParameterSet.HSecDef.PageDef.HeaderLen = hwp.MiliToHwpUnit(0.0)  # 머릿말
hwp.HParameterSet.HSecDef.PageDef.FooterLen = hwp.MiliToHwpUnit(0.0)  # 꼬릿말
hwp.HParameterSet.HSecDef.HSet.SetItem("ApplyClass", 24)  # 적용범위 분류
hwp.HParameterSet.HSecDef.HSet.SetItem("ApplyTo", 3)  # 적용범위

hwp.HAction.Execute("PageSetup", hwp.HParameterSet.HSecDef.HSet)  # 실행