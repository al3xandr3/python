
import win32api, win32con

def click(x,y):
    h_x, h_y = win32api.GetCursorPos() #Get position
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    win32api.Sleep(500)
    win32api.SetCursorPos((h_x,h_y)) # go back to previous position

for x in range(0, 10):
    click(2600,500)
    win32api.Sleep(500)
    click(2400,300)
    print("click")
    win32api.Sleep(20000)