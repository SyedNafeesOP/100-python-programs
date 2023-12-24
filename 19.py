import tkinter as tk
import pyttsx3
import wikipedia
root=tk.Tk()
label=tk.Label(text="search")
label.pack()
entry=tk.Entry(root)
entry.pack()
voice = pyttsx3.init()
In = input("searching from wikipedia/google:")
result = wikipedia.summary(In, sentences = 5)
print(result)
voice.say(result)
voice.runAndWait()
button=tk.Button(text="click",command= "button_click" )
button.pack()
root.mainloop()
