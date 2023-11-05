import customtkinter

root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("vidura")

label = customtkinter.CTkLabel(master=root, text="ANALYTICAL REPORT", font=("davish",50), text_color="lightblue" )
label.pack(pady=20, padx= 15 )



frame1= customtkinter.CTkFrame(master=root)
frame1.pack(pady=20,padx=20,expand=True)

label = customtkinter.CTkLabel(master=frame1, text="All teachers must be made aware of the feedback received by the app and take measures accordingly.", font=("davish",20), text_color="red" )
label.pack(pady=2, padx= 15 )

label1= customtkinter.CTkLabel(master=frame1, text="Average class response good as detected by the app -", font=("davish",20), text_color="green" )
label1.pack(pady=2, padx= 15 )

label2 = customtkinter.CTkLabel(master=frame1, text="1.Teacher can sometimes initiate activities relating to the topic to increase the level of participation.", font=("davish",20), text_color="grey" )
label2.pack(pady=2, padx= 15 )

label3 = customtkinter.CTkLabel(master=frame1, text="Average class response not bad as detected by the app-", font=("davish",20), text_color="green" )
label3.pack(pady=2, padx= 15 )

label4= customtkinter.CTkLabel(master=frame1, text="1.Pose questions in between teaching to the class, allowing them to think and try to incorporate different students to answer each question.", font=("davish",20), text_color="grey" )
label4.pack(pady=2, padx= 15 )

label5= customtkinter.CTkLabel(master=frame1, text=" 2.Create a good learning environment starts with creating a positive classroom climate where students' needs are met. Whether it's about \n allowing enough time to finish tasks, organizing fun activities, or providing social and emotional support, teachers are responsible for \n creating a safe space where students can make mistakes and evolve.", font=("davish",20), text_color="grey" )
label5.pack(pady=2, padx= 15 )

label6= customtkinter.CTkLabel(master=frame1, text="Average class response bad as detected by the app-", font=("davish",20), text_color="green" )
label6.pack(pady=2, padx= 15 )

label7= customtkinter.CTkLabel(master=frame1, text="1.Have a system of rotation of seats in a row on a daily or weekly basis so that no student is permanently sitting on the first or last bench.", font=("davish",20), text_color="grey" )
label7.pack(pady=2, padx= 15 )

label8= customtkinter.CTkLabel(master=frame1, text="2.Teacher some initiate some practical demonstrations along side with theoretical knowledge which will encourage students to take part in \n class and excite them.", font=("davish",20), text_color="grey" )
label8.pack(pady=2, padx= 15 )



frame= customtkinter.CTkFrame(master=root)
frame.pack(pady=10,padx=20,expand=True)

def exitapp():
    root.destroy()
    import mainmenu

button= customtkinter.CTkButton(master=frame, text="Exit", command=exitapp)
button.pack(pady=12, padx=10)

root.mainloop()