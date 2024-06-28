from pynput import keyboard

def on_press(key):
	try:
		if (key.char == 'r'):
			print(5)
			return False
		elif (key.char == 't'):
			print(10)
			return False
		elif (key.char == 'y'):
			print(20)
			return False
	except Exception as e:
		print(e)

# Collect events until released
with keyboard.Listener(
       	on_press=on_press) as listener:
    listener.join()
listener.start()