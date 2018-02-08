import os
import ctypes
from cudatext import *

FR_PRIVATE  = 0x10
FR_NOT_ENUM = 0x20

def load_font(fontpath):
    pathbuf = ctypes.create_unicode_buffer(fontpath)
    AddFontResourceEx = ctypes.windll.gdi32.AddFontResourceExW
    num = AddFontResourceEx(ctypes.byref(pathbuf), FR_PRIVATE, 0)
    return bool(num)

class Command:
    def on_start(self, ed_self):
        if os.name!='nt': return

        dir = os.path.join(app_path(APP_DIR_DATA), 'fonts')
        if not os.path.isdir(dir): return

        count = 0
        for name in os.listdir(dir):
            if name.endswith('.ttf') \
            or name.endswith('.ttc') \
            or name.endswith('.otf') \
            or name.endswith('.fon'):
                count += 1
                ok = load_font(os.path.join(dir, name))
                msg = '' if ok else '... failed'
                print('Loading font:', name, msg)
