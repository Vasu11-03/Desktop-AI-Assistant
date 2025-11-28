from tkinter import*
from PIL import Image, ImageTk
import speech_to_text
import action
import threading
import speech_recognition as sr

root=Tk()
root.title("AI Assistant")
root.geometry("600x800")
root.resizable(False , False)
root.config(bg="#6F8FAF")

def ask():
    def process_ask():
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)  
            print("Listening...")
            try:
                audio_data = recognizer.listen(source)
                user_data = recognizer.recognize_google(audio_data)
                if user_data is None or user_data.strip() == "":
                    text.insert(END, "Error: Could not understand speech.\n")
                    return
                bot_val = action.Action(user_data)
                text.insert(END, "User--->" + user_data + "\n")
                if bot_val is not None:
                    text.insert(END, "BOT-->" + str(bot_val) + "\n")
                if bot_val == "ok sir":
                    root.destroy()
            except sr.UnknownValueError:
                text.insert(END, "Error: Could not understand speech.\n")
            except sr.RequestError as e:
                text.insert(END, "Error: Could not request results from Google Speech Recognition service.\n")

    # Run in a separate thread
    thread = threading.Thread(target=process_ask)
    thread.start()

def send():
    def process_send():
        send = entry.get()
        bot = action.Action(send)
        text.insert(END, "User--->" + send + "\n")
        if bot is not None:
            text.insert(END, "BOT-->" + str(bot) + "\n")
        if bot == "ok sir":
            root.destroy()

    # Run in a separate thread
    thread = threading.Thread(target=process_send)
    thread.start()


def delete():
   text.delete("1.0","end")

#frame
frame=LabelFrame(root, padx=130,pady=7,borderwidth=3,relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0,column=1,padx=55,pady=10)

#text label
text_label=Label(frame,text="AIVA",font=("comic Sans ms",14,"bold"),bg="#356696")
text_label.grid(row=0,column=0,padx=20,pady=10)

#image label
image = ImageTk.PhotoImage(Image.open(r"C:\Users\sanju\OneDrive\Desktop\MAJOR\assistant.png"))
image_label= Label(frame,image=image)
image_label.grid(row=1,column=0,pady=20)

#adding text widget
text=Text(root,font=('courior 10 bold'),bg="#356696")
text.grid(row=2,column=0)
text.place(x=100,y=375,width=375,height=100)

#entry widget
entry=Entry(root,justify=CENTER)
entry.place(x=100,y=500,width=350,height=30)

#button 1
Button1=Button(root,text="ASK",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
Button1.place(x=70,y=575)
#button 2
Button2=Button(root,text="send",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=send)
Button2.place(x=400,y=575)
#button 
Button3=Button(root,text="delete",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=delete)
Button3.place(x=225,y=575)

entry.bind("<Return>", lambda event: send())

root.mainloop()
