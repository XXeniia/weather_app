import customtkinter as ctk
from tkinter import messagebox
from utils.weather_api import get_weather_data
from ui import create_widgets, place_static_widgets, place_weather_widgets, hide_weather_widgets, load_icons


ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("🌦️ Weather Dashboard")
app.geometry("500x500")
app.resizable(False, False)
app.configure(bg="#aee1f9")

icons = load_icons()
widgets = create_widgets(app, icons)
place_static_widgets(widgets)
hide_weather_widgets(widgets)

def show_weather():
    city = widgets["city_entry"].get()
    if not city:
        messagebox.showwarning("Missing Info", "Enter the city name!")
        return
    try:
        data = get_weather_data(city)
        widgets["city_label"].configure(text=f"{data['name']}, {data['sys']['country']}")
        widgets["curr_temp_label"].configure(text=f"{data['main']['temp']}°C (feels like {data['main']['feels_like']}°C)")
        widgets["min_temp_label"].configure(text=f"Min: {data['main']['temp_min']}°C")
        widgets["max_temp_label"].configure(text=f"Max: {data['main']['temp_max']}°C")

        desc = data["weather"][0]["description"].capitalize()
        desc_lower = desc.lower()

        if "rain" in desc_lower:
            icon = icons["weather"]["rain"]
        elif "snow" in desc_lower:
            icon = icons["weather"]["snow"]
        elif "storm" in desc_lower or "thunder" in desc_lower:
            icon = icons["weather"]["storm"]
        elif "cloud" in desc_lower:
            icon = icons["weather"]["cloud"]
        elif "clear" in desc_lower:
            icon = icons["weather"]["clear"]
        else:
            icon = icons["desc"]

        widgets["desc_icon_label"].configure(image=icon)
        widgets["desc_label"].configure(text=desc)
        widgets["humidity_label"].configure(text=f"{data['main']['humidity']}% humidity")
        widgets["wind_label"].configure(text=f"{data['wind']['speed']} m/s wind")

        place_weather_widgets(widgets)

    except Exception as e:
        messagebox.showerror("Error", f"Could not get the data: {e}")

widgets["search_button"].configure(command=show_weather)

app.mainloop()
