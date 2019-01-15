### $pip3 install SpeechRecognition
### $pip3 install PyAudio
### $pip3 install Dialogflow
import speech_recognition as sr
import dialogflow_v2 as dialogflow
import sys
import random

# defines for SpeechRecognition
sample_rate = 48000
chunk_size = 512

sl = sys.argv[1]
r= sr.Recognizer()

# defines for Dialogflow
PROJECT_ID = "homedroid-228703"
random.seed(0x228703)

# Dialogflow detect intent
def detect_intent_text(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(response.query_result.intent.display_name, response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(response.query_result.fulfillment_text))

with sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    while True:
        print("Speak:")
        audio = r.listen(source)
        print("Recognizing...")
        try:
            text = r.recognize_google(audio, language=sl)
            print("You said:", text)
            session_id = str(random.random())[2:]
            detect_intent_text(PROJECT_ID, session_id, text, sl)
        except sr.UnknownValueError:
            print("Could not understand audio!")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
