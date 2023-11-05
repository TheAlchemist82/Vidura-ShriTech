import customtkinter

root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("vidura")



label = customtkinter.CTkLabel(master=root, text="LINK CAMERAS", font=("davish",50), text_color="lightblue" )
label.pack(pady=20, padx= 15 )


frame1= customtkinter.CTkFrame(master=root)
frame1.pack(pady=20,padx=20,expand=True)

label = customtkinter.CTkLabel(master=frame1, text="For linking camera link camera to the device", font=("davish",35), text_color="red" )
label.pack(pady=20, padx= 15 )

entry= customtkinter.CTkEntry(master=frame1, placeholder_text="Enter cam location" )
entry.pack(pady=10,padx=10)

entry1= customtkinter.CTkEntry(master=frame1, placeholder_text="Enter cam name" )
entry1.pack(pady=10,padx=10)

entry2= customtkinter.CTkEntry(master=frame1, placeholder_text="Location on device" )
entry2.pack(pady=10,padx=10)

entry3= customtkinter.CTkEntry(master=frame1, placeholder_text="Teacher associated" )
entry3.pack(pady=10,padx=10)

def lc():
    import link_successful

button= customtkinter.CTkButton(master=frame1, text="click to link",command=lc)
button.pack(pady=10,padx=10)

def cc():
    import realtimedetection_main

button1= customtkinter.CTkButton(master=frame1, text="run linked camera",command=cc)
button1.pack(pady=10,padx=10)



frame= customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=20,expand=True)

def exitapp():
    root.destroy()
    import mainmenu

button= customtkinter.CTkButton(master=frame, text="Exit", command=exitapp)
button.pack(pady=12, padx=10)

root.mainloop()