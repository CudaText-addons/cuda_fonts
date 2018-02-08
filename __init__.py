import os
#import win32api
#import win32con
import ctypes
from cudatext import *

#def notify_os():
    #win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_FONTCHANGE)

def load_font(fontpath):
    FR_PRIVATE  = 0x10
    FR_NOT_ENUM = 0x20
    pathbuf = ctypes.create_unicode_buffer(fontpath)
    AddFontResourceEx = ctypes.windll.gdi32.AddFontResourceExW
    num = AddFontResourceEx(ctypes.byref(pathbuf), FR_PRIVATE, 0)
    return bool(num)

class Command:
    def on_start(self, ed_self):
        if os.name!='nt': return
    
        dir = os.path.join(app_path(APP_DIR_DATA), 'fonts')
        if not os.path.isdir(dir): return
        
        names = os.listdir(dir)
        for name in names:
            if name.endswith('.ttf') \
            or name.endswith('.ttc') \
            or name.endswith('.otf') \
            or name.endswith('.fon'):
                ok = load_font(os.path.join(dir, name))
                msg = '' if ok else '... failed' 
                print('Loading font:', name, msg)
