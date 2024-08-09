<h1><ins>Speech-To-Text-Py</ins></h1>

<h2><ins>Python package to record input audio from a sound device and transcribe it into text for further operations</ins></h2>


<h3><ins>Installation and Usage</ins></h3>
<ul>
   <li>Clone entire directory into any folder of your choice</li>
   <li>Manually go through each file and change the absolute paths based on your file structure</li>
   <li>Inside the input_saver directory, run ./input.sh</li>
   <li>After the process finishes, check results/test.txt for the transcription of the recording</li>
   <li>the voskcall.py file is used for working with the vosk-transcriber and must be carefully altered</li>
   <li>This package is supposed to work with https://github.com/realaryann/Keyword-Select-Service (service to extract keywords)</li>
</ul>

![demo-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/dfde0522-dcb1-4e02-808e-352a528e27d5)

<br>Working pipeline of recording, transcribing, and storing

<h3><ins>Required Python Libraries</ins></h3>
<ul>
   <li>sounddevice</li>
   <li>numpy</li>
   <li>scipy</li>
   <li>vosk</li>
</ul>

<h3><ins>Changing Sound Device</ins></h3>
<ul>
   <li>Navigate to input_saver/find_device.py</li>
   <li>In a terminal, check the name of your sounddevice by running python3 -m sounddevice</li>
   <li>Replace the DEVICE_NAME variable with the name of the device</li>
</ul>

<h3><ins>Program Input</ins></h3>
<ul>
   <li>Input_Saver currently takes string input from the command line</li>
   <li>Input Mapping</li>
   <ol>
      <li>R: Record for 5 seconds</li>
      <li>T: Record for 10 seconds</li>
      <li>Y: Record for 20 seconds</li>
      <li>Z: Exit program</li>
   </ol>
   <li>The program will continue looping until valid input is entered</li>
</ul>

<h3><ins>Configuring Output</ins></h3>
<ul>
   <li>Navigate to input_saver/voskhear.py</li>
   <li>Replace the newf and filesrc variables (WARNING, could break everything!)</li>
</ul>

<h3><ins>Cleaning Results</ins></h3>
<ul>
   <li>Run ./clean.sh in ~/input_saver to clear out previous recordings and results</li>
</ul>

<h3><ins>Full Release with tracking capabilities</ins></h3>
<b>(Check complete branch)</b> Order of execution for input_saver

1) python3 inputaudio.py
2) python3 voskhear.py
