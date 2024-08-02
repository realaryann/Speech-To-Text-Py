<h1>Input_Saver</h1>

<h2>Python package to record input audio from a sound device and transcribe it into text for further operations</h2>

<h3>Installation and Usage</h3>
<ul>
   <li>Clone entire directory into any folder of your choice</li>
   <li>Manually go through each file and change the absolute paths based on your file structure</li>
   <li>Inside the input_saver directory, run ./input.sh</li>
   <li>After the process finishes, check results/test.txt for the transcription of the recording</li>
   <li>This package is supposed to work with https://github.com/realaryann/Keyword-Select-Service (service to extract keywords)</li>
</ul>

<h3>Required Python Libraries</h3>
<ul>
   <li>sounddevice</li>
   <li>numpy</li>
   <li>scipy</li>
   <li>vosk</li>
</ul>

<h3>Changing Sound Device</h3>
<ul>
   <li>Navigate to input_saver/find_device.py</li>
   <li>In a terminal, check the name of your sounddevice by running python3 -m sounddevice</li>
   <li>Replace the DEVICE_NAME variable with the name of the device</li>
</ul>

<h3>Program Input</h3>
<ul>
   <li>Input_Saver currently takes string input from the command line</li>
   <li>Input Mapping</li>
   <ol>
      <li>R: Record for 5 seconds</li>
      <li>T: Record for 10 seconds</li>
      <li>Y: Record for 20 seconds</li>
      <li>Z: Exit program</li>
   </ol>
</ul>

<h3>Configuring Output</h3>
<ul>
   <li>Navigate to input_saver/voskhear.py</li>
   <li>Replace the newf and filesrc variables (WARNING, could break everything!)</li>
</ul>

<h3>Cleaning Results</h3>
<ul>
   <li>Run ./clean.sh in ~/input_saver to clear out previous recordings and results</li>
</ul>

<h3> Full Release with tracking capabilities </h3>
<b>(Check complete branch)</b> Order of execution for input_saver

1) python3 inputaudio.py
2) python3 voskhear.py
