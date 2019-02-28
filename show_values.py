import sqlite3
import datetime
import pyperclip

from paste_manager import PasteManager


if __name__ == '__main__':
    latest = ''
    pm = PasteManager()
    print pm.get_value()