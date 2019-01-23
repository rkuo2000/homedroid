# Homebot sample codes

## rpi3 
rpi3_robocar_gpio.py - RPi3 GPIO control a robot car <br />
rpi3_robocar_webui.y - rPi3 WebUI to control a robot car <br />
rpi3_i2c_VL53L0X.y   - rPi3 I2C to read VL53L0X IR ranger <br />

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
