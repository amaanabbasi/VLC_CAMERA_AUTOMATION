from decouple import config
import pyautogui
import logging, time, os

path_to_vlc_executable = '/snap/bin/vlc'
log_file_name = 'vlc_automation.log'

logging.basicConfig(filename=log_file_name,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

logging.info("VLC Automation Started")

# Detaching the process, So that if the terminal is closed vlc player keeps running.
# os.system('/snap/bin/vlc & disown')
os.system(f'nohup {path_to_vlc_executable} &')
time.sleep(2)

logging.info("ctrl+n")
pyautogui.hotkey('ctrlleft', 'n')
time.sleep(1)


logging.info("Entering camera url")
pyautogui.typewrite(config('CAMERA_URL'))
pyautogui.hotkey('enter')
time.sleep(1)

logging.info("Entering credentials for camera account.")
pyautogui.typewrite(config('CAMERA_NAME'))
pyautogui.hotkey('tab')
pyautogui.typewrite(config('CAMERA_PASSWORD'))
pyautogui.hotkey('enter')

logging.info('Finished with love.')






