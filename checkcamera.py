import customtkinter

root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("vidura")

label = customtkinter.CTkLabel(master=root, text="CHECK CAMERAS", font=("davish",50), text_color="lightblue" )
label.pack(pady=20, padx= 15 )

frame1= customtkinter.CTkFrame(master=root)
frame1.pack(pady=20,padx=20,expand=True)

label = customtkinter.CTkLabel(master=frame1, text="Enter camera name to check", font=("davish",25), text_color="red" )
label.pack(pady=20, padx= 15 )

entry= customtkinter.CTkEntry(master=frame1, placeholder_text="Camera Name")
entry.pack(pady=10,padx=10)


def exitapp1():
    import realtimedetection_main
    

button1= customtkinter.CTkButton(master=frame1, text="Check live feed", command=exitapp1)
button1.pack(pady=12, padx=10)

label1 = customtkinter.CTkLabel(master=frame1, text="Sr no.", font=("davish",25), text_color="green" )
label1.pack(pady=20, padx= 15, side="left" )

label2 = customtkinter.CTkLabel(master=frame1, text="Camera Name", font=("davish",25), text_color="green")
label2.pack(pady=20, padx= 15, side= "left" )

label3 = customtkinter.CTkLabel(master=frame1, text="Camera Location", font=("davish",25), text_color="green" )
label3.pack(pady=20, padx= 15, side= "left" )



frame= customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=20,expand=True)

def exitapp():
    root.destroy()
    import mainmenu

button= customtkinter.CTkButton(master=frame, text="Exit", command=exitapp)
button.pack(pady=12, padx=10)

root.mainloop()