# WEATHER FORECAST

# ------------ window basic -------------

import tkinter
import requests
from tkinter import BOTH, IntVar
from PIL import ImageTk, Image
from io import BytesIO

# ----------- define window -------------------
root = tkinter.Tk()
root.title("Weather Forecast")
root.iconbitmap("weather.ico")
root.geometry("400x400")
root.resizable(0, 0)

# ------------ create colors -------------
sky_color = "#219ebc"
grass_color = "#76c893"
output_color = "#e9edc9"
input_color = "#ecf2ae"
large_font = ("SimSun", 14)
small_font = ("SimSun", 10)

# ---------------- define functions ----------------


def search():
    '''Use open weather api to look up current weather conditions given a city/ city, country'''
    global response
    # Get API response
    # URL and my api key .... Use Your own api key
    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = 'df7e379aed83b599a3b446c995f8705c'

    # search by the appropriate query, either city name or zipcode
    if search_method.get() == 1:
        querystring = {'q': city_entry.get(), 'appid': api_key,
                       'units': 'imperial'}
    elif search_method.get() == 2:
        querystring = {'zip': city_entry.get(), 'appid': api_key,
                       'units': 'imperial'}

    # call api
    response = requests.request("GET", url, params=querystring)
    response = response.json()
    # print(response)
    # example response return
    '''
    {'coord': {'lon': -71.0598, 'lat': 42.3584}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}],
    'base': 'stations', 'main': {'temp': 295.54, 'feels_like': 294.93, 'temp_min': 293.12, 'temp_max': 297.87, 'pressure': 1020, 'humidity': 42},
    'visibility': 10000, 'wind': {'speed': 3.58, 'deg': 338, 'gust': 7.6}, 'clouds': {'all': 75},
    'dt': 1624472296, 'sys': {'type': 2, 'id': 2013408, 'country': 'US',
    'sunrise': 1624439282, 'sunset': 1624494293}, 'timezone': -14400, 'id': 4930956, 'name': 'Boston', 'cod': 200}
    '''
    get_weather()
    get_icon()


def get_weather():
    '''Grab information from API response and update our weather labels'''
    # gather the data to be used from the API response
    city_name = response['name']
    city_lat = str(response['coord']['lat'])
    city_lon = str(response['coord']['lon'])

    main_weather = response['weather'][0]['main']
    description = response['weather'][0]['description']

    temp = str(response['main']['temp'])
    feels_like = str(response['main']['feels_like'])
    temp_min = str(response['main']['temp_min'])
    temp_max = str(response['main']['temp_max'])
    humidity = str(response['main']['humidity'])


    # update output labels
    city_info_label.config(text=city_name + "(" + city_lat +
                           "," + city_lon + ")", font=large_font, bg=output_color)
    weather_label.config(text="Weather :  " + main_weather +
                         "," + description, font=small_font, bg=output_color)
    temp_label.config(text="Temperature : " + temp + "F",
                      font=small_font, bg=output_color)
    feels_label.config(text="Feels Like :  " + feels_like +
                       "F", font=small_font, bg=output_color)
    temp_min_label.config(text="Min Temperature : " +
                          temp_min + "F", font=small_font, bg=output_color)
    temp_max_label.config(text="Max Temperature : " +
                          temp_max + "F", font=small_font, bg=output_color)
    humidity_label.config(text="Humidity : " + humidity + "F",
                          font=small_font, bg=output_color)


def get_icon():
    # get the appropriate weather icon from API response
    global img

    # get the icon id from API response
    icon_id = response['weather'][0]['icon']

    # get the icon from the correct website
    url = 'https://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)

    # make a request at the url to download the icon; stream = True automatically dl
    icon_response = requests.get(url, stream=True)

    # turn into a form tkinter/ python can use
    img_data = icon_response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

    # update label
    photo_label.config(image=img)


# --------------- define layout ----------------------
# create frames
sky_frame = tkinter.Frame(root, bg=sky_color, height=250)
grass_frame = tkinter.Frame(root, bg=grass_color)
sky_frame.pack(fill=BOTH, expand=True)
grass_frame.pack(fill=BOTH, expand=True)

output_frame = tkinter.LabelFrame(
    sky_frame, bg=output_color, width=325, height=225)
input_frame = tkinter.LabelFrame(grass_frame, bg=input_color, width=325)
output_frame.pack(pady=30)
output_frame.pack_propagate(0)
input_frame.pack(pady=15)

# ------------------- output frame layout -----------------
city_info_label = tkinter.Label(output_frame, bg=output_color)
weather_label = tkinter.Label(output_frame, bg=output_color)
temp_label = tkinter.Label(output_frame, bg=output_color)
feels_label = tkinter.Label(output_frame, bg=output_color)
temp_min_label = tkinter.Label(output_frame, bg=output_color)
temp_max_label = tkinter.Label(output_frame, bg=output_color)
humidity_label = tkinter.Label(output_frame, bg=output_color)
photo_label = tkinter.Label(output_frame, bg=output_color)

city_info_label.pack(pady=8)
weather_label.pack()
temp_label.pack()
feels_label.pack()
temp_min_label.pack()
temp_max_label.pack()
humidity_label.pack()
photo_label.pack(pady=8)

# ---------------- Input frame layout -------------------------
# create input frame button and entry
city_entry = tkinter.Entry(input_frame, width=20, font=large_font)
submit_button = tkinter.Button(
    input_frame, text="Submit", font=large_font, bg=input_color, command=search)

search_method = IntVar()
search_method.set(1)
search_city = tkinter.Radiobutton(input_frame, text="Search by city name",
                                  variable=search_method, value=1, font=small_font, bg=input_color)
search_zip = tkinter.Radiobutton(input_frame, text="Search by zipcode",
                                 variable=search_method, value=2, font=small_font, bg=input_color)

city_entry.grid(row=0, column=0, padx=10, pady=(10, 0))
submit_button.grid(row=0, column=1, padx=10, pady=(10, 0))
search_city.grid(row=1, column=0, pady=2)
search_zip.grid(row=1, column=1, padx=5, pady=2)


# ---------------- run root window -------------------------
root.mainloop()
