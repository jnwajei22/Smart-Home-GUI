# widgets/datetime.py
import dearpygui.dearpygui as dpg
import datetime

def build_datetime():
    """Displays time (HH:MM AM/PM) and date (Day, Month DD), centered in a small container."""
    now = datetime.datetime.now()
    time_str = now.strftime("%I:%M %p")   # e.g. 01:29 PM
    date_str = now.strftime("%A, %B %d")  # e.g. Sunday, March 26

    with dpg.child_window(width=250, height=90, no_scrollbar=True):
        # We use 'indent' to approximate center alignment
        dpg.add_text(time_str, indent=70)  # tweak indent as needed
        dpg.add_text(date_str, indent=70)
