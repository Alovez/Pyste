import pyperclip
import time
from paste_manager import PasteManager

if __name__ == '__main__':
    pm = PasteManager()
    latest = pm.get_latest()
    while True:
        if pyperclip.paste() != latest:
            latest = pyperclip.paste()
            pm.save_value(pyperclip.paste())
        time.sleep(1)