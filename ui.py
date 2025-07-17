import customtkinter as ctk
from PIL import Image

def load_icons():
    return {
        "curr_temp": ctk.CTkImage(Image.open("assets/curr_temp.png"), size=(30, 30)),
        "min_temp": ctk.CTkImage(Image.open("assets/min_temp.png"), size=(30, 30)),
        "max_temp": ctk.CTkImage(Image.open("assets/max_temp.png"), size=(30, 30)),
        "humidity": ctk.CTkImage(Image.open("assets/humidity.png"), size=(30, 30)),
        "wind": ctk.CTkImage(Image.open("assets/wind.png"), size=(30, 30)),
        "desc": ctk.CTkImage(Image.open("assets/desc.png"), size=(30, 30)),
        "weather": {
            "rain": ctk.CTkImage(Image.open("assets/rain.png"), size=(30, 30)),
            "snow": ctk.CTkImage(Image.open("assets/snow.png"), size=(30, 30)),
            "storm": ctk.CTkImage(Image.open("assets/storm.png"), size=(30, 30)),
            "cloud": ctk.CTkImage(Image.open("assets/cloud.png"), size=(30, 30)),
            "clear": ctk.CTkImage(Image.open("assets/clear.png"), size=(30, 30)),
        }
    }

def create_widgets(app, icons):
    widgets = {}

    widgets["city_entry"] = ctk.CTkEntry(app, placeholder_text="Enter the city", width=220)
    widgets["search_button"] = ctk.CTkButton(app, text="Show the weather")

    widgets["city_label"] = ctk.CTkLabel(app, text="", font=("Arial", 30, "bold"))

    widgets["curr_temp_icon_label"] = ctk.CTkLabel(app, image=icons["curr_temp"], text="")
    widgets["curr_temp_label"] = ctk.CTkLabel(app, text="", font=("Arial", 16))

    widgets["min_temp_icon_label"] = ctk.CTkLabel(app, image=icons["min_temp"], text="")
    widgets["min_temp_label"] = ctk.CTkLabel(app, text="", font=("Arial", 16))

    widgets["max_temp_icon_label"] = ctk.CTkLabel(app, image=icons["max_temp"], text="")
    widgets["max_temp_label"] = ctk.CTkLabel(app, text="", font=("Arial", 16))

    widgets["desc_icon_label"] = ctk.CTkLabel(app, image=icons["desc"], text="")
    widgets["desc_label"] = ctk.CTkLabel(app, text="", font=("Arial", 16))

    widgets["humidity_icon_label"] = ctk.CTkLabel(app, image=icons["humidity"], text="")
    widgets["humidity_label"] = ctk.CTkLabel(app, text="", font=("Arial", 16))

    widgets["wind_icon_label"] = ctk.CTkLabel(app, image=icons["wind"], text="")
    widgets["wind_label"] = ctk.CTkLabel(app, text="", font=("Arial", 16))

    return widgets

def place_static_widgets(widgets):
    widgets["city_entry"].place(relx=0.5, rely=0.07, anchor="n")
    widgets["search_button"].place(relx=0.5, rely=0.14, anchor="n")

def place_weather_widgets(widgets):
    widgets["city_label"].place(relx=0.5, rely=0.22, anchor="n")
    widgets["curr_temp_icon_label"].place(relx=0.2, rely=0.3, anchor="n")
    widgets["curr_temp_label"].place(relx=0.5, rely=0.3, anchor="n")
    widgets["min_temp_icon_label"].place(relx=0.2, rely=0.4, anchor="n")
    widgets["min_temp_label"].place(relx=0.5, rely=0.4, anchor="n")
    widgets["max_temp_icon_label"].place(relx=0.2, rely=0.5, anchor="n")
    widgets["max_temp_label"].place(relx=0.5, rely=0.5, anchor="n")
    widgets["desc_icon_label"].place(relx=0.2, rely=0.6, anchor="n")
    widgets["desc_label"].place(relx=0.5, rely=0.6, anchor="n")
    widgets["humidity_icon_label"].place(relx=0.2, rely=0.7, anchor="n")
    widgets["humidity_label"].place(relx=0.5, rely=0.7, anchor="n")
    widgets["wind_icon_label"].place(relx=0.2, rely=0.8, anchor="n")
    widgets["wind_label"].place(relx=0.5, rely=0.8, anchor="n")

def hide_weather_widgets(widgets):
    for key in widgets:
        if "label" in key and "icon" in key or key.endswith("_label"):
            widgets[key].place_forget()
