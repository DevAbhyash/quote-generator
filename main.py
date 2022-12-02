# from tkinter import *
import requests
import datetime
#
# quotes =""
#
# def get_quote():
#     global quotes
#
#     #Write your code here.
#
#     response = requests.get(url="https://api.kanye.rest")
#     data = response.json()
#     quotes= data["quote"]
#     canvas.itemconfig(quote_text,text=quotes)
#
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text=quotes, width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
#
#
# window.mainloop()
My_Lat = 33.8688,
My_Longitude =151.2093
parameter = {
    "lat":My_Lat,
    "lon":My_Longitude
}
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
response.raise_for_status()
data=response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]

sunset = data["results"]["sunset"]
current_time = datetime.datetime.now()
print(current_time)
