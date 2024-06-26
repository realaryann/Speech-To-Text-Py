import voskcall as v

filename = "recordings/recording.wav"
model_path = "/home/csrobot/vosktest/models/vosk-model-en-us-0.22"

transcriber = v.Transcriber(model_path)
transcription = transcriber.transcribe(filename)

newf = "test.txt"

filesrc = f"./results/{newf}"
with open(filesrc, "w") as tf:
	for i in transcription:
		tf.write(i+'\n')