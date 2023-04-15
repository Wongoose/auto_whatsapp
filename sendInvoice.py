import pandas as pd
import sys
import pywhatkit as pwk
import pyautogui
import re
import time
from pynput.keyboard import Key, Controller
keyboard = Controller();


def sendMessage(phone: str, imgPath: str, msg: str):
	print("Sending...\n");
	pwk.sendwhats_image(
		receiver = phone,
		img_path = imgPath,
		caption = msg,
		wait_time = 15,
		tab_close = False,
		close_time = 3
		)
	print("Loaded contents!\n");
	# pyautogui.click();
	# time.sleep(2);
	# keyboard.press(Key.enter);
	# keyboard.release(Key.enter);
	print("Message sent!");

# main function
if len(sys.argv) < 2:
	sys.exit();
file = pd.read_csv(sys.argv[1], header = None);
units = file[0].values.tolist();
names = file[1].values.tolist();
whatsapp = file[4].values.tolist();
count = len(units);
i = 1; #index 1 to skip the headers

while i < count:
	print("item: " + units[i] + "\n");
	final_phone =  "+6" + re.sub("[Ww-]", "", whatsapp[i]);
	print("wa: " + final_phone + "\n");
	sendMessage(final_phone, "img/" + units[i] + ".jpg", "Dear " + names[i] + ",\n\nhere is your invoice testing.");
	i += 1;
