"""Module used for converting wav recording to a transcribed textfile"""

import voskcall as v

FILENAME = "recordings/recording.wav"
MODEL_PATH = "/home/csrobot/vosktest/models/vosk-model-en-us-0.22"

transcriber = v.Transcriber(MODEL_PATH)
transcription = transcriber.transcribe(FILENAME)

NEWF = "test.txt"

filesrc = f"./results/{NEWF}"
with open(filesrc, "w") as tf:
    for i in transcription:
        tf.write(i+'\n')
