from tkinter import *
from datetime import datetime
from tkcalendar import Calendar
import requests

# Ideas on improving this:
# Creating a Login Interface
# Create New user and creating new Graphs
# Displaying graphs

#### Declaring Global Variables ####

USERNAME = 'YOUR_USER'
TOKEN = 'YOUR_TOKEN'
GRAPH_ID = 'YOUR_GRAPH_ID'
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'

#### Creating functions ####

# Create a new user:
# On next update

# Create new graph:
# On next update

# Create Pixel:


def addPixel():
    cal.config(date_pattern="yyyyMMdd")
    date = cal.get_date()
    time = hours.get()
    pixel_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}'
    headers = {
        'X-USER-TOKEN': TOKEN,
    }
    pixel_param = {
        'date': str(date),
        'quantity': str(time)
    }
    response = requests.post(
        url=pixel_endpoint, json=pixel_param, headers=headers)
    print(response.text)


# Update Pixel:
# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
def updatePixel():
    cal.config(date_pattern="yyyyMMdd")
    date = cal.get_date()
    time = hours.get()
    pixel_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}'
    headers = {
        'X-USER-TOKEN': TOKEN,
    }
    pixel_param = {
        'date': str(date),
        'quantity': str(time)
    }
    response = requests.put(
        url=pixel_endpoint, json=pixel_param, headers=headers)
    print(response.text)

# Delete Pixel:
# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>


def deletePixel():
    cal.config(date_pattern="yyyyMMdd")
    date = cal.get_date()
    pixel_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}'
    headers = {
        'X-USER-TOKEN': TOKEN,
    }
    pixel_param = {
        'date': str(date)
    }
    response = requests.delete(
        url=pixel_endpoint, json=pixel_param, headers=headers)
    print(response.text)

# Calendar for Adding Pixel


def addCal():
    cal.grid(row=3, column=1, padx=20)
    pick_date.grid(column=1, row=2, pady=20)
    hours.grid(column=1, row=4)
    add_label.grid(column=0, row=4, pady=20)
    confirm_Button = Button(text='Confirm', command=addPixel)
    confirm_Button.grid(column=1, row=5)

# Calendar for updating Pixel


def updateCal():
    cal.grid(row=3, column=1, padx=20)
    pick_date.grid(column=1, row=2, pady=20)
    hours.grid(column=1, row=4)
    add_label.grid(column=0, row=4, pady=20)
    confirm_Button = Button(text='Confirm', command=updatePixel)
    confirm_Button.grid(column=1, row=5)

# Calendar and Button for Deleting Pixel


def deleteCal():
    cal.grid(row=3, column=1, padx=20)
    pick_date.grid(column=1, row=2, pady=20)
    confirm_Button = Button(text='Confirm', command=deletePixel)
    confirm_Button.grid(column=1, row=5, pady=20)


#### Creating GUI ####
root = Tk()
root.title("My Coding Journey")
root.config(padx=50, pady=50, bg="white")

# adding logo
canvas = Canvas(width=250, height=125, highlightthickness=0)
logo = PhotoImage(file='Img/logo.png')
canvas.create_image(125, 63, image=logo)
canvas.grid(row=0, column=1)

# creating Buttons
add_Button = Button(text='Add Pixel', command=addCal)
add_Button.grid(row=1, column=0)
update_Button = Button(text='Update Pixel', command=updateCal)
update_Button.grid(row=1, column=1)
delete_Button = Button(text='Delete Pixel', command=deleteCal)
delete_Button.grid(row=1, column=2)


cal = Calendar(root, selectmode='day',
               year=2021, month=5,
               day=22)


pick_date = Label(text="Select a date", bg="white")
add_label = Label(text="How many hours?", bg='white')
hours = Entry(width=40)

root.mainloop()
