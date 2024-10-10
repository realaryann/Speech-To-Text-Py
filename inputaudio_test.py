import inputaudio
import find_device
import pytest


def test_duration():
    # 5 secs
    assert inputaudio.validate("r") == 5
    assert inputaudio.validate("R") == 5
    # 10 secs
    assert inputaudio.validate("t") == 10
    assert inputaudio.validate("T") == 10
    # 20 secs
    assert inputaudio.validate("y") == 20
    assert inputaudio.validate("Y") == 20
    # Exit/garbage value
    assert inputaudio.validate("z") == -1
    assert inputaudio.validate("Z") == -1
    assert inputaudio.validate("U") == -1

def test_default_device():
    assert find_device.find_device() == "Samson C01U"
