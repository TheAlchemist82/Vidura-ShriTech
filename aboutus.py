import customtkinter

root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("vidura")

label = customtkinter.CTkLabel(master=root, text="ABOUT US", font=("davish",50), text_color="lightblue" )
label.pack(pady=20, padx= 15 )


frame1= customtkinter.CTkFrame(master=root)
frame1.pack(pady=20,padx=20,expand=True)

label = customtkinter.CTkLabel(master=frame1, text="Founded in 2023, Vidura is a startup solution provider mainly for the educational market. The company is based in India with 5 founders.", font=("davish",20), text_color="lightgrey" )
label.pack(pady=0, padx= 15 )

label = customtkinter.CTkLabel(master=frame1, text="We strive for perfection; perform to excellence, assess and evolve. We are continuously innovating and reinventing ourselves, \n while we foster teamwork and collaboration.", font=("davish",20), text_color="lightgrey" )
label.pack(pady=0, padx= 15 )




frame= customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=20,expand=True)

def exitapp():
    root.destroy()
    import mainmenu

button= customtkinter.CTkButton(master=frame, text="Exit", command=exitapp)
button.pack(pady=12, padx=10)

root.mainloop()