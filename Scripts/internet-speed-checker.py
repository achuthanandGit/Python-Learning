from tkinter import *
from speedtest import  Speedtest

def update_speed_details():
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)
    download_speed_label.config(text="Download Speed - " + str(download_speed) + "Mbps")
    upload_speed_label.config(text="Upload Speed - " + str(upload_speed) + "Mbps")

window = Tk()
window.title("Internet Speed Tracker")
window.geometry("300x100")
button = Button(window, text="Check Speed", width=20, command=update_speed_details)
button.pack()

download_speed_label = Label(text="")
download_speed_label.pack()
upload_speed_label = Label(text="")
upload_speed_label.pack()
window.mainloop()