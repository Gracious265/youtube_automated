import pywhatkit

topic = input("Please enter the topic: ")

try:
    pywhatkit.playonyt(topic)
    print("Playing...")
    
except:
    print("Network Error")    