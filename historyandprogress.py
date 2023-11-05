import customtkinter

root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("vidura")

label = customtkinter.CTkLabel(master=root, text="HISTORY AND PROGRESS", font=("davish",50), text_color="lightblue" )
label.pack(pady=20, padx= 15 )


frame1= customtkinter.CTkFrame(master=root)
frame1.pack(pady=20,padx=20,expand=True)

label = customtkinter.CTkLabel(master=frame1, text="Camera Name", font=("davish",30), text_color="red" )
label.pack(pady=20, ipadx= 120, side="left" )

label1 = customtkinter.CTkLabel(master=frame1, text="Progress Made", font=("davish",30), text_color="red" )
label1.pack(pady=20, ipadx= 120, side="left" )

label2 = customtkinter.CTkLabel(master=frame1, text="Date Checked", font=("davish",30), text_color="red" )
label2.pack(pady=20, ipadx= 120, side="left" )


frame= customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=20,expand=True)

def exitapp():
    root.destroy()
    import mainmenu

button= customtkinter.CTkButton(master=frame, text="Exit", command=exitapp)
button.pack(pady=12, padx=10)

root.mainloop()