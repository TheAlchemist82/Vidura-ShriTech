import customtkinter

root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("vidura")

label = customtkinter.CTkLabel(master=root, text="ACTIVITY LIBRARY", font=("davish",50), text_color="lightblue" )
label.pack(pady=20, padx= 15 )

frame1= customtkinter.CTkFrame(master=root)
frame1.pack(pady=20,padx=20)

label= customtkinter.CTkLabel(master=frame1, text="Tab to check the cameras checked and classe fixed in the span of last one month", font=("davish",20),text_color="red")
label.pack(pady=20,padx=20)

label1= customtkinter.CTkLabel(master=frame1, text="Class", font=("davish",20), text_color="green")
label1.pack(ipady=10, ipadx=120, side="left" )

label2= customtkinter.CTkLabel(master=frame1, text="Camera", font=("davish",20), text_color="green")
label2.pack(ipady=10, ipadx=120, side="left" )

label3= customtkinter.CTkLabel(master=frame1, text="Date Checked", font=("davish",20), text_color="green")
label3.pack(ipady=10, ipadx=120, side="left" )



frame= customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=20,expand=True)

def exitapp():
    root.destroy()
    import mainmenu

button= customtkinter.CTkButton(master=frame, text="Exit", command=exitapp)
button.pack(pady=12, padx=10)

root.mainloop()