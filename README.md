Order of execution for input_saver

1) python3 inputaudio.py {duration of recording}
2) python3 voskhear.py {recording name}

Results
1) -> ./recordings gets a new .wav recording
   -> ./log/log_rec.txt gets a new entry for the newest recording

2) -> ./results gets a new test file with transcribed text
   -> ./log/log.txt gets a new entry for the newest test  