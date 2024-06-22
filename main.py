import tkinter
import customtkinter
from pytube import YouTube
from PIL import Image

def startDownload():
    try:
        ytLink = link.get() # get link
        ytObject = YouTube(ytLink)

        if audioOnly_var.get(): # check for audio only bool
            stream = ytObject.streams.get_audio_only()
        else: # select quality
            if segemented_button_var.get() == "Lowest Available":
                stream = ytObject.streams.get_lowest_resolution()
            else:
                stream = ytObject.streams.get_highest_resolution()
        
        stream.download()
        show_message("Download successful", "green")
    except Exception as e:
        show_message(f"Failed to Download: {str(e)}", "red")

def show_message(message, color):
    error_label.configure(text=message, text_color=color)
    app.after(2000, clear_message)

def clear_message():
    error_label.configure(text="")

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Window settings
app = customtkinter.CTk()
app.minsize(720, 480)
app.resizable(False, False)
app.title("Video Downloader")

# Define UI components
error_label = customtkinter.CTkLabel(app, text="") # error or success label

my_image = customtkinter.CTkImage(dark_image=Image.open("./ytb.png"), size=(150, 150)) 
image_label = customtkinter.CTkLabel(app, image=my_image, text="") # needed for displaying the image

title = customtkinter.CTkLabel(app, text="Insert a YouTube link", text_color="White", font=("serif", 26))

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
download_btn = customtkinter.CTkButton(app, width=140, height=28, text="Download", command=startDownload)

audioOnly_var = customtkinter.BooleanVar()
checkbox_1 = customtkinter.CTkCheckBox(app, text="Audio Only?", variable=audioOnly_var)

segmented_label = customtkinter.CTkLabel(app, text="Select the video quality")
segemented_button_var = customtkinter.StringVar(value="Highest Available")
segemented_button = customtkinter.CTkSegmentedButton(app, values=["Highest Available", "Lowest Available"],
                                                     variable=segemented_button_var)

# Pack UI components
image_label.pack(padx=10, pady=10)
title.pack(padx=10, pady=10)
link.pack()
checkbox_1.pack(padx=10, pady=10)
segmented_label.pack()
segemented_button.pack()
download_btn.pack(padx=10, pady=10)
error_label.pack()

# Run the application
app.mainloop()
