from gtts import gTTS  #import the google text to speech package
import os # import the operating system module


textFile = open("text.txt","r") #File Handler Variable
textInput1 = "This text will be converted to speech using the google text to speech package"
textInput2 = textFile.read().replace("\n"," ") #Read the File Handler Variable
language = 'en'


#next we pass the language and the text to the gTTS Engine
output = gTTS(text=textInput2, lang=language, slow=False)

#Save the output as an mp3 file
output.save("output.mp3")

#Run the output file
os.system("start output.mp3")


