import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()
root.geometry("1920x1080")
root.title("vidura")



def lc():
    import linkcamera

def cc():
    import checkcamera

def sr():
    import surveyreport

def ar():
    import analyticalreport

def Or():
    import overallreport

def hap():
    import historyandprogress

def al():
    import activitylibrary

def au():
    import aboutus


label= customtkinter.CTkLabel(master=root, text="MAIN MENU", font=("davish",50), text_color="lightblue" )
label.pack(pady=20, padx= 15 )




frame= customtkinter.CTkFrame(master=root)
frame.pack(pady=5,padx=20,expand=True)

button1= customtkinter.CTkButton(master=frame, text="Link Cameras", command=lc, font=("davish",40), text_color="lightblue")
button1.pack(pady=30,padx=50, side="left")

button2= customtkinter.CTkButton(master=frame, text="Check Cameras", command=cc, font=("davish",40), text_color="lightblue")
button2.pack(pady=30,padx=50,side="right")




frame1= customtkinter.CTkFrame(master=root)
frame1.pack(pady=5,padx=20, expand=True)

button3= customtkinter.CTkButton(master=frame1, text="Survey Page", command=sr, font=("davish",40), text_color="lightblue")
button3.pack(pady=30,padx=50, side="left")

button4= customtkinter.CTkButton(master=frame1, text="Analytical Report", command=ar, font=("davish",40), text_color="lightblue")
button4.pack(pady=30,padx=50,side="right")




frame2= customtkinter.CTkFrame(master=root)
frame2.pack(pady=5,padx=20, expand=True)

button5= customtkinter.CTkButton(master=frame2, text="Overall Report", command=Or, font=("davish",40), text_color="lightblue")
button5.pack(pady=30,padx=50, side="left")

button6= customtkinter.CTkButton(master=frame2, text="History and progress", command=hap, font=("davish",40), text_color="lightblue")
button6.pack(pady=30,padx=50,side="right")




frame3= customtkinter.CTkFrame(master=root)
frame3.pack(pady=5,padx=20, expand=True)

button7= customtkinter.CTkButton(master=frame, text="Activity Library", command=al, font=("davish",40), text_color="lightblue")
button7.pack(pady=30,padx=50, side="bottom")

button8= customtkinter.CTkButton(master=frame1, text="About Us", command=au, font=("davish",40), text_color="lightblue")
button8.pack(pady=30,padx=50,side="bottom")




def exitapp():
    root.destroy()

button= customtkinter.CTkButton(master=root, text="Exit", command=exitapp,font=("davish",30))
button.pack(pady=12, padx=10)



root.mainloop()