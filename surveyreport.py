import customtkinter
import csv


root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("vidura")



label = customtkinter.CTkLabel(master=root, text="SURVEY PAGE", font=("davish",50), text_color="lightblue" )
label.pack(pady=20, padx= 15 )



frame= customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx= 20, expand = True)

label = customtkinter.CTkLabel(master=frame, text="Fill according to your experience of learning in class", font=("davish",35), text_color="red" )
label.pack(pady=20, padx= 15 )

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Experience")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Learning")
entry2.pack(pady=12, padx=10)
learning= entry2._textvariable


entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Teacher's Name")
entry3.pack(pady=12, padx=10)

entry4 = customtkinter.CTkEntry(master=frame, placeholder_text="Improvement Suggestions")
entry4.pack(pady=12, padx=10)

entry5 = customtkinter.CTkEntry(master=frame, placeholder_text="Feedback")
entry5.pack(pady=12, padx=10)

def survey():
    import survey_successful
    
button= customtkinter.CTkButton(master=frame, text="Enter", command=survey)
button.pack(pady=12, padx=10)







def exitapp():
    root.destroy()
    import mainmenu

button= customtkinter.CTkButton(master=root, text="Exit", command=exitapp)
button.pack(pady=12, padx=10)


root.mainloop()