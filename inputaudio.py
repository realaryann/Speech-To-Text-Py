'''
cmd-line args
arg1 = duration of recording
'''
import sys
import sounddevice as sd
import find_device as fd
import numpy
from scipy.io.wavfile import write

def write_audio(recording, freq_aud) -> None:
	storage = f"./recordings/recording.wav"
	write(storage, freq_aud, recording)

def record_audio(freq_aud: int, duration: int):
	recording = sdt.rec(int(duration*freq_aud), samplerate = freq_aud, channels=1)
	sd.wait()
	return recording

def main():
	# Frequency of audio
	freq_aud = 44100
	# Duration (in seconds) to record until 
	duration = int(sys.argv[1])
	try:
		sd.default.device = fd.find_device()
	except Exception as e:
		print(f"Finding {fd.DEVICE_NAME} failed: {e}\n")
	try:
		recording = record_audio(freq_aud, duration)
	except Exception as e:
		print(f"Recording audio failed: {e}\n")

	try:
		write_audio(recording, freq_aud)
	except Exception as e:
		print(f"Writing audio failed: {e}\n")

if __name__ == "__main__":
	main()