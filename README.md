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

## Speech 
`$python3 gTTS.py hello en` - Text to Speech (output gTTS.mp3)<br />
`$python3 gSR.py en` - Speech to Text<br />
`$python3 gSTT.py en` - Speech to Text then Text to Speech<br />
`$python3 gTranslator.py en fr` - Speech Translation<br />
### Speech with Dialogflow
`$python3 dialogflow_test.py hello en` - test Dialogflow agent<br />
`$python3 dialogflow_gSR.py en` - Dialogflow with SR<br />
`$python3 dialogflow_gSTT.py en` - Dialogflow with SR & TTS<br />

## parse KML (Google Earth pro as Mission Planner)
`$python3 parse_kml.py test.kml`
