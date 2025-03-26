import dearpygui.dearpygui as dpg
import datetime

# ---------- Page Management ----------
pages = ["widgets_page", "devices_page", "media_page", "climate_page", "security_page", "system_page"]
current_page_index = 0

# ---------- Theme ----------
def apply_theme():
    with dpg.theme() as theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (248, 248, 248))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 15)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 12, 12)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 10, 10)
    return theme

# ---------- Page Switching ----------
def show_page(index):
    for i, page in enumerate(pages):
        dpg.configure_item(page, show=(i == index))

def navigate_to_page(sender, app_data, user_data):
    global current_page_index
    current_page_index = user_data
    show_page(current_page_index)

# ---------- Widgets Page (Home) ----------
def create_widgets_page():
    dpg.add_text("Widgets Dashboard", color=(20, 20, 20))
    dpg.add_separator()

    now = datetime.datetime.now()
    date_string = now.strftime("%A, %B %d")
    time_string = now.strftime("%I:%M %p")

    with dpg.group(horizontal=True):
        with dpg.child_window(width=450, height=150):
            dpg.add_text(date_string, bullet=True)
            dpg.add_text(time_string, bullet=True)
            dpg.add_spacer(height=10)
            dpg.add_text("Weather: Sunny, 73°F")

        with dpg.child_window(width=450, height=150):
            dpg.add_text("Calendar / To-Do")
            dpg.add_separator()
            dpg.add_text("- 10 AM: HVAC Maintenance")
            dpg.add_text("- 1 PM: Package Delivery")
            dpg.add_text("- 4 PM: Water Plants")

    dpg.add_spacer(height=15)

    with dpg.child_window(width=-1, height=150):
        dpg.add_text("Status Summary")
        dpg.add_separator()
        dpg.add_text("Lights On: 2 / 6")
        dpg.add_text("Doors Locked: Yes")
        dpg.add_text("Thermostat: 72°F")
        dpg.add_text("Media: Idle")

# ---------- Placeholder Pages ----------
def placeholder_page(name):
    dpg.add_text(f"{name} Page")

# ---------- Build Layout ----------
def build_layout():
    with dpg.window(tag="main_window"):
        with dpg.group(horizontal=True):
            with dpg.child_window(width=150, autosize_y=True):
                dpg.add_text("Menu")
                dpg.add_separator()
                for i, label in enumerate(["Widgets", "Devices", "Media", "Climate", "Security", "System"]):
                    dpg.add_button(label=label, width=-1, callback=navigate_to_page, user_data=i)

            with dpg.group():
                with dpg.child_window(tag="widgets_page", width=800, height=550, show=True):
                    create_widgets_page()
                with dpg.child_window(tag="devices_page", width=800, height=550, show=False):
                    placeholder_page("Devices")
                with dpg.child_window(tag="media_page", width=800, height=550, show=False):
                    placeholder_page("Media")
                with dpg.child_window(tag="climate_page", width=800, height=550, show=False):
                    placeholder_page("Climate")
                with dpg.child_window(tag="security_page", width=800, height=550, show=False):
                    placeholder_page("Security")
                with dpg.child_window(tag="system_page", width=800, height=550, show=False):
                    placeholder_page("System")

# ---------- Main ----------
dpg.create_context()
theme = apply_theme()
dpg.create_viewport(title="Smart Home Dashboard", width=1000, height=600)
dpg.setup_dearpygui()
build_layout()
dpg.bind_theme(theme)
dpg.set_primary_window("main_window", True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
