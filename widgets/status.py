# widgets/status.py
import dearpygui.dearpygui as dpg

def build_status():
    """Shows system or home status summary."""
    dpg.add_text("Status Summary")
    dpg.add_separator()
    dpg.add_text("Lights On: 2 / 6")
    dpg.add_text("Doors Locked: Yes")
    dpg.add_text("Thermostat: 72°F")
    dpg.add_text("Media: Idle")
