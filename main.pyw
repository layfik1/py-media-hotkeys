# sorry for bad english
import pyautogui #load pyautogui lib
import keyboard # load keyboard lib
import json

config = open("config.json","r") #open config.json as file object
configJson = json.load(config) # load config 

ver = configJson.get("ver") # get the version number
playpause = str(configJson.get("playpause")) # get the play/pause keybind
nexttrack = str(configJson.get("nexttrack")) # get the next track keybind
prevtrack = str(configJson.get("prevtrack")) # get the previous track keybind
volumeup = str(configJson.get("volumeup")) # get the volume up keybind
volumedown = str(configJson.get("volumedown")) # get the volume down keybind

print("PyMediaHotkeys V",ver) #print version number

while True:
	if keyboard.is_pressed(playpause): #emulate play/pause button press
		pyautogui.press("playpause")

	if keyboard.is_pressed(nexttrack): #emulate next track button press
		pyautogui.press("nexttrack")

	if keyboard.is_pressed(prevtrack): #emulate previous track button press
		pyautogui.press("prevtrack")

	if keyboard.is_pressed(volumeup): #emulate volume up button press
		pyautogui.press("volumeup")

	if keyboard.is_pressed(volumedown): #emulate volume down button press
		pyautogui.press("volumedown")

