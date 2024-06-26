<h1>Input_Saver</h1>

<p><b>How to use:</b></p>
<ul>
   <li>Clone entire directory into any folder of your choice</li>
   <li>Inside the input_saver director, run <b>./input.sh {seconds}</b>, where seconds is the length of recording</li>
   <li>After the process finishes, check results/test.txt for the transcription of the recording</li>
   <li>To clean up the result and recording folders, run <b>./clean</b></li>
</ul>

Order of execution for input_saver ( FULL RELEASE, available in complete branch )

1) python3 inputaudio.py {duration of recording}
2) python3 voskhear.py {recording name}

Results
1) -> ./recordings gets a new .wav recording
   -> ./log/log_rec.txt gets a new entry for the newest recording

2) -> ./results gets a new test file with transcribed text
   -> ./log/log.txt gets a new entry for the newest test  
