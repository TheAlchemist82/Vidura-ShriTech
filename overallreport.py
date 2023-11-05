import customtkinter

root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("vidura")

label = customtkinter.CTkLabel(master=root, text="OVERALL REPORT", font=("davish",50), text_color="lightblue" )
label.pack(pady=20, padx= 15 )


frame1= customtkinter.CTkFrame(master=root)
frame1.pack(pady=20,padx=20,expand=True)

label = customtkinter.CTkLabel(master=frame1, text="Displays the over all progress made since purchase of the app.\n Uses AI tools to monitor, analyse and grade the progress.", font=("davish",30), text_color="red" )
label.pack(pady=20, padx= 15 )

frame2= customtkinter.CTkFrame(master=frame1)
frame2.pack(pady=20,padx=20,expand=True)

def sa():
    import analysis_error

button= customtkinter.CTkButton(master=frame2, text="Start Analysis", command=sa)
button.pack(pady=10,padx=10)

label = customtkinter.CTkLabel(master=frame2, text="Your score is:", font=("davish",30), text_color="green" )
label.pack(pady=20, padx= 15 )


frame= customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=20,expand=True)

def exitapp():
    root.destroy()
    import mainmenu

button= customtkinter.CTkButton(master=frame, text="Exit", command=exitapp)
button.pack(pady=12, padx=10)

root.mainloop()