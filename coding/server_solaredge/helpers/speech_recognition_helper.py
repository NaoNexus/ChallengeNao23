import speech_recognition as sr

from helpers.logging_helper import logger


class SpeechRecognition:
    r: sr.Recognizer

    path: str
    result: str

    def __init__(self, path):
        self.r = sr.Recognizer()
        self.path = path

        self.recognise()

    def recognise(self):
        file = sr.AudioFile(self.path)

        with file as source:
            audio = self.r.record(source)

            self.result = self.r.recognize_google(audio, language="it_IT")
            logger.info(self.result)
