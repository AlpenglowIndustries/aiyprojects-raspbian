#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Activates the Google Assistant with hotword detection, using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio.

.. note:

    This example depends on hotword detection (such as "Okay Google") to activate the Google
    Assistant, which is supported only with Raspberry Pi 2/3. If you're using a Pi Zero, this
    code won't work. Instead, you must use the button or another type of trigger, as shown
    in assistant_library_with_button_demo.py.
"""

import logging
import platform
import subprocess
import sys
import aiy.voice.audio
import RPi.GPIO as GPIO

from google.assistant.library.event import EventType

from aiy.assistant import auth_helpers
from aiy.assistant.library import Assistant
from aiy.board import Board, Led
from aiy.voice import tts
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN)

def power_off_pi():
    tts.say('Good bye!')
    GPIO.cleanup()
    subprocess.call('sudo shutdown -h now', shell=True)

def reboot_pi():
    tts.say('See you in a bit!')
    GPIO.cleanup()
    subprocess.call('sudo reboot', shell=True)
    
def say_ip():
    ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)
    # ip_address = subprocess.check_output("ifconfig wlan0 | grep inet | awk '{ print $2 }'", shell=True)
    tts.say('My IP address is %s' % ip_address.decode('UTF-8'))

def funicorn():
    GPIO.setup(26,GPIO.OUT)
    GPIO.output(26,GPIO.LOW)
    sleep(0.100)
    GPIO.output(26,GPIO.IN)
    tts.say('No, fuck you')

def process_event(assistant, led, event):
    logging.info(event)

    if event.type == EventType.ON_START_FINISHED:
        led.state = Led.BEACON_DARK  # Ready.
        logging.info('Say "OK, Google" then speak, or press Ctrl+C to quit...')

    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        led.state = Led.ON  # Listening.

    elif event.type == EventType.ON_END_OF_UTTERANCE:
        led.state = Led.PULSE_QUICK  # Thinking.
        
    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        logging.info('You said:', event.args['text'])
        text = event.args['text'].lower()
        if text == 'power off':
            assistant.stop_conversation()
            power_off_pi()
        elif text == 'reboot':
            assistant.stop_conversation()
            reboot_pi()
        elif text == 'IP address':
            assistant.stop_conversation()
            say_ip()
        elif text == 'fuck you':
            assistant.stop_conversation()
            funicorn()
 
    elif (event.type == EventType.ON_CONVERSATION_TURN_FINISHED
          or event.type == EventType.ON_CONVERSATION_TURN_TIMEOUT
          or event.type == EventType.ON_NO_RESPONSE):
        led.state = Led.BEACON_DARK

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)


def main():
    logging.basicConfig(level=logging.INFO)

    credentials = auth_helpers.get_assistant_credentials()
    with Board() as board, Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(assistant, board.led, event)


if __name__ == '__main__':
    main()
