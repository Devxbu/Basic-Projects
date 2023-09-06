import pyttsx3, time

engine = pyttsx3.init()

engine.say('Hello, user!')

engine.runAndWait()

engine.say('Now we breathing for the relax')

i = 0

while i != 42:
    engine.say('Breath in')
    engine.runAndWait()
    time.sleep(3)
    engine.say('Breath out')
    engine.runAndWait()
    time.sleep(3)
    i += 6