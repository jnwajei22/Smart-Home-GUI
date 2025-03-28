# widgets/weather.py
import dearpygui.dearpygui as dpg

def build_weather():
    """Displays current weather info."""
    dpg.add_text("Weather: Sunny, 73°F")
