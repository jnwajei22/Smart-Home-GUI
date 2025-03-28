# widgets/contacts.py
import dearpygui.dearpygui as dpg

def build_contacts():
    """Contacts or phone list."""
    dpg.add_text("Emergency Contacts")
    dpg.add_separator()
    dpg.add_text("Mom: 555-123-4567")
    dpg.add_text("Neighbor: 555-987-6543")
    dpg.add_text("Security: 555-000-1111")
