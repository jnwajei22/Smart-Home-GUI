# widgets/to_do.py
import dearpygui.dearpygui as dpg

def build_todo():
    """Creates a to-do list widget group."""
    dpg.add_text("To-Do List")
    dpg.add_separator()
    dpg.add_text("[ ] Buy groceries")
    dpg.add_text("[ ] Change air filter")
    dpg.add_text("[ ] Feed the cat")
