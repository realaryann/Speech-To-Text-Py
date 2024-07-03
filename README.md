<h1>Input_Saver</h1>

<p><b>How to use:</b></p>
<ul>
   <li>Clone entire directory into any folder of your choice</li>
   <li>Inside the input_saver director, run <b>sudo ./input.sh</li>
   <li> <b>sudo privilages are required because the keyboard python module requires them to operate </b></li>
   <li>After the process finishes, check results/test.txt for the transcription of the recording</li>
   <li>To clean up the result and recording folders, run <b>./clean</b></li>
</ul>

<h2> Full Release with tracking capabilities </h2>
<b>(Check complete branch)</b> Order of execution for input_saver

1) python3 inputaudio.py
2) python3 voskhear.py

Results
1) -> ./recordings gets a new .wav recording
   -> ./log/log_rec.txt gets a new entry for the newest recording

2) -> ./results gets a new test file with transcribed text
   -> ./log/log.txt gets a new entry for the newest test  
