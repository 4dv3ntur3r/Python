from tkinter import *
import requests

# HTTP response codes
# 1XX : hold on
# 2XX : here you go
# 3XX : go away
# 4XX : You screwed up
# 5XX : I (Server) Screwed up
# https://www.webfx.com/web-development/glossary/http-status-codes/
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)

#######################################################################################################################
#                               Kanye Quote APP                                                                       #
#######################################################################################################################


def get_quote():
    responose = requests.get(url="https://api.kanye.rest/")
    responose.raise_for_status()
    got_response = responose.json()
    quote = got_response['quote']
    canvas.itemconfig(quote_txt, text=quote)


window = Tk()
window.title("Kanye Syas...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_txt = canvas.create_text(150, 207, text="Click the emoji!!", width=250, font=('Arial', 18, "bold"), fill='#fff')
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file='kanye.png')
kanye_btn = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_btn.grid(row=1, column=0)

window.mainloop()