import customtkinter
 

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("600x350")
root.title("vidura login")


def login():
    root.destroy()
    import mainmenu

def changetheme():
    customtkinter.set_appearance_mode("dark")   
    customtkinter.set_default_color_theme("dark-blue")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label= customtkinter.CTkLabel(master=frame, text="Login", font=("Roboto",24))
label.pack(pady=12,padx=10,)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="UserName")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button= customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox= customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(pady=12, padx= 10)

checkbox1= customtkinter.CTkCheckBox(master = root, text="Dark mode on", command=changetheme)
checkbox1.pack(pady=0.1,padx=10, expand=True)


def exitapp():
    root.destroy()

button= customtkinter.CTkButton(master=root, text="Exit", command=exitapp,font=("davish",30))
button.pack(pady=4, padx=10)


root.mainloop()