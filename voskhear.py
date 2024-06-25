import voskcall as v

filename = "recording0.wav"
model_path = "/home/csrobot/vosktest/models/vosk-model-en-us-0.22"

transcriber = v.Transcriber(model_path)
transcription = transcriber.transcribe(filename)

newf = "test.txt"

with open("./log/log.txt", "a+") as logfile:
	loglines = logfile.readlines()
	if loglines == []:
		newf = f"test{0}.txt"
		logfile.write("0\n")
	else:
		num = int(loglines[-1]) + 1
		newf = f"test{num}.txt"
		logfile.write(str(num))

filesrc = f"./results/{newf}"
with open(filesrc, "w") as tf:
	for i in transcription:
		tf.write(i+'\n')