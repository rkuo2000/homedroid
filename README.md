# Homebot sample codes

## linkit7688 duo
linkit7688_robot_cat.py - randomly play meow sounds(mp3) on linkit7688 with Breakout (audio DAC) <br />
linkit7688duo_readtty.py - reading /dev/ttyS0, serial output from ATmega32u4 (arduino) <br />
linkit7688duo_gpio_motor.py - test gpio control DC motors (L298N/LS9110S)<br />
linkit7688duo_stop_motor.py - gpio stop DC motors<br />
linkit7688duo_imu.py - reading IMU azimuth (yaw)<br />
linkit7688duo_imu_motor.py - gpio spin DC motor and read IMU yaw angle<br />

## fbchat (for FB Messenger)
fbchat_basic.py - login FB to find owner uid <br />
fbchat_echobot.py - messenger auto echo to message <br />
fbchat_fetchid.py - list all FB friend's id <br />
fbchat_send.py - send text, emoji, local image, remote image

## Text-To-Speech 
`gtts-cli 'hello' --output hello.mp3`
`python3 gTTS.py`
`python3 gttsx3.py`

## parse KML (Google Earth pro as Mission Planner)
`python3 parse_kml.py test.kml`
