#!/bin/bash

echo "INFO: Running audio listener"
python3 keyboard_input.py | python3 inputaudio.py
echo "INFO: Audio listener finished"
echo "INFO: Running audio transcriber"
python3 voskhear.py
echo "INFO: Audio transcriber finished"
echo " "
cat ./results/test.txt