'''
cmd-line args
arg1 = duration of recording
'''
import sys
import sounddevice as sd
import find_device as fd
import numpy
from pynput import keyboard
from scipy.io.wavfile import write

duration = 0

def write_audio(recording, freq_aud) -> None:
	storage = f"./recordings/recording.wav"
	write(storage, freq_aud, recording)

def record_audio(freq_aud: int, duration: int):
	recording = sd.rec(int(duration*freq_aud), samplerate = freq_aud, channels=1)
	sd.wait()
	return recording

def decide() -> int:
	print("R: 5 Seconds")
	print("T: 10 Seconds")
	print("Y: 20 Seconds")
	inp = input()
	while (inp not in "rRtTyY"):
		inp = input()
	if (inp in "rR" and len(inp) == 1):
		return 5
	elif (inp in 'tT' and len(inp) == 1):
		return 10
	elif (inp in 'yY' and len(inp) == 1):
		return 20 

def main():
	# Frequency of audio
	freq_aud = 44100
	duration = decide()
	try:
		sd.default.device = fd.find_device()
	except Exception as e:
		print(f"Finding {fd.DEVICE_NAME} failed: {e}\n")
	try:
		print(f"INFO: Recording now, for {duration} seconds")
		recording = record_audio(freq_aud, duration)
	except Exception as e:
		print(f"Recording audio failed: {e}\n")
	try:
		write_audio(recording, freq_aud)
	except Exception as e:
		print(f"Writing audio failed: {e}\n")

if __name__ == "__main__":
	main()