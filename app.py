import dearpygui.dearpygui as dpg

# Widget imports
from widgets.datetime import build_datetime
from widgets.status import build_status
from widgets.to_do import build_todo
from widgets.contacts import build_contacts

# ---------- Globals ----------
pages = ["home_page", "devices_page", "media_page", "climate_page", "security_page", "system_page"]
current_page_index = 0
dark_mode_enabled = False
current_theme = None

# ---------- THEME ----------
def apply_theme():
    global current_theme
    if current_theme:
        dpg.delete_item(current_theme)

    with dpg.theme() as theme:
        with dpg.theme_component(dpg.mvAll):
            bg_color = (34, 34, 34) if dark_mode_enabled else (248, 248, 248)
            text_color = (255, 255, 255) if dark_mode_enabled else (0, 0, 0)
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, bg_color)
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, bg_color)
            dpg.add_theme_color(dpg.mvThemeCol_Text, text_color)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 15)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 12, 12)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 10, 10)

        with dpg.theme_component(dpg.mvButton):
            if dark_mode_enabled:
                dpg.add_theme_color(dpg.mvThemeCol_Button, (238, 238, 238))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (220, 220, 220))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (200, 200, 200))
                dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0))
            else:
                dpg.add_theme_color(dpg.mvThemeCol_Button, (51, 51, 51))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (70, 70, 70))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (90, 90, 90))
                dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255))

    dpg.bind_theme(theme)
    current_theme = theme

# ---------- PAGE SWITCHING ----------
def show_page(index):
    for i, page in enumerate(pages):
        dpg.configure_item(page, show=(i == index))

def navigate_to_page(sender, app_data, user_data):
    global current_page_index
    current_page_index = user_data
    show_page(current_page_index)

def toggle_theme(sender, app_data):
    global dark_mode_enabled
    dark_mode_enabled = app_data
    apply_theme()

# ---------- HOME PAGE ----------
def create_home_page():
    with dpg.table(header_row=False, resizable=True, policy=dpg.mvTable_SizingStretchProp,
                   borders_innerH=True, borders_innerV=True, borders_outerH=True, borders_outerV=True):
        dpg.add_table_column()
        dpg.add_table_column()

        with dpg.table_row():
            with dpg.child_window(height=150):
                build_datetime()
            with dpg.child_window(height=150):
                build_status()

        with dpg.table_row():
            with dpg.child_window(height=250):
                build_todo()
            with dpg.child_window(height=250):
                build_contacts()

# ---------- PLACEHOLDER PAGES ----------
def placeholder_page(name):
    dpg.add_text(f"{name} Page")

# ---------- BUILD LAYOUT ----------
def build_layout():
    with dpg.window(tag="main_window"):
        with dpg.group(horizontal=True):
            with dpg.child_window(width=160, autosize_y=True):
                dpg.add_text("Menu")
                dpg.add_separator()

                for i, label in enumerate(["Home", "Devices", "Media", "Climate", "Security", "System"]):
                    dpg.add_button(label=label, width=-1, callback=navigate_to_page, user_data=i)

                dpg.add_spacer(height=20)
                dpg.add_checkbox(label="Dark Mode", default_value=False, callback=toggle_theme)

            with dpg.child_window(autosize_x=True, autosize_y=True):
                with dpg.group(tag="home_page", show=True):
                    create_home_page()
                with dpg.group(tag="devices_page", show=False):
                    placeholder_page("Devices")
                with dpg.group(tag="media_page", show=False):
                    placeholder_page("Media")
                with dpg.group(tag="climate_page", show=False):
                    placeholder_page("Climate")
                with dpg.group(tag="security_page", show=False):
                    placeholder_page("Security")
                with dpg.group(tag="system_page", show=False):
                    placeholder_page("System")

# ---------- MAIN ----------
if __name__ == "__main__":
    dpg.create_context()
    dpg.create_viewport(title="Smart Home Dashboard", width=1280, height=720)
    dpg.setup_dearpygui()
    build_layout()
    apply_theme()
    dpg.set_primary_window("main_window", True)
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
