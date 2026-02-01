import requests
import tkinter as tk
from PIL import Image, ImageTk

API_KEY = "7f4dfa07c7f10eca09a13b20528d8cd3"

def get_weather():
    city = city_entry.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].upper()
        result_label.config(text=f"{temp}°C\n{desc}")
    else:
        result_label.config(text="CITY NOT FOUND")

# Window
root = tk.Tk()
root.title("ATHLETIC WEATHER")
root.geometry("360x520")
root.configure(bg="#0a0a0a")

# Top Bar
top = tk.Frame(root, bg="#111111", height=60)
top.pack(fill="x")

title = tk.Label(top, text="WEATHER X", font=("Arial Black", 16),
                 bg="#111111", fg="#00ffcc")
title.pack(pady=15)

# Card
card = tk.Frame(root, bg="#1a1a1a")
card.place(relx=0.5, rely=0.55, anchor="center", width=320, height=380)

city_entry = tk.Entry(card, font=("Arial", 14, "bold"), justify="center",
                      bg="#0a0a0a", fg="#00ffcc", insertbackground="#00ffcc", bd=0)
city_entry.pack(pady=20, ipady=8, ipadx=10)

search_btn = tk.Button(card, text="CHECK WEATHER",
                       command=get_weather,
                       font=("Arial Black", 12),
                       bg="#00ffcc", fg="black", bd=0, padx=10, pady=6)
search_btn.pack(pady=10)

result_label = tk.Label(card, text="", font=("Arial Black", 28),
                        bg="#1a1a1a", fg="white")
result_label.pack(pady=40)

root.mainloop()
