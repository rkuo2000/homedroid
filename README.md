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
`python3 gTTS.py hello en` - Text-To-Speech (output gTTS.mp3)<br />
`python3 gSR.py en` - Speech Recognition<br />
`python3 gSTT.py en zh-TW` - Speech Translation (run once)<br />
`python3 gTranslate.py en zh-TW` - Speech Translation (loop with greeting)<br />
### Dialogflow
`python3 gSR_dialogflow.py en` - SR->Dialogflow<br />
`python3 gSTT_dialogflow.py en` - SR->Dialogflow->TTS (run once)<br />

## parse KML (Google Earth pro as Mission Planner)
`python3 parse_kml.py test.kml`
