# widgets/calendar.py
import dearpygui.dearpygui as dpg

def build_calendar():
    """Creates a small calendar widget group."""
    dpg.add_text("Calendar / To-Do")
    dpg.add_separator()
    dpg.add_text("- 10 AM: HVAC Maintenance")
    dpg.add_text("- 1 PM: Package Delivery")
    dpg.add_text("- 4 PM: Water Plants")
