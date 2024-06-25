import voskcall as v

filename = "recordings/recording0.wav"
model_path = "/home/csrobot/vosktest/models/vosk-model-en-us-0.22"

transcriber = v.Transcriber(model_path)
transcription = transcriber.transcribe(filename)

newf = "test.txt"

with open("./log/log.txt", "r+") as logfile:
	loglines = logfile.readlines()
	if len(loglines) == 0:
		newf = f"test0.txt"
		logfile.write("0\n")
	else:
		num = int(loglines[-1][0:-1:]) + 1
		newf = f"test{num}.txt"
		logfile.write(str(num)+'\n')

filesrc = f"./results/{newf}"
with open(filesrc, "w") as tf:
	for i in transcription:
		tf.write(i+'\n')