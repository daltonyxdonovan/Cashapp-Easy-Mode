import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'opencv-python', 'colorama', 'datetime', 'pyautogui', 'PyQt5', 'qdarkstyle', 'PySimpleGUI', 'qtpy'])
reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

