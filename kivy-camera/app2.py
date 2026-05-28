import os
# Force Kivy to use the OpenCV backend on Windows
os.environ['KIVY_CAMERA'] = 'opencv'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

import time

class CameraScreen(Screen):
    """The primary screen hosting the camera feed and capture controls."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Main layout structure for this screen
        self.main_layout = BoxLayout(orientation='vertical')
        
        # 1. Navigation Header
        nav_layout = BoxLayout(size_hint_y=0.12, padding=5, spacing=10)
        title_label = Label(text="Windows 11 Camera Portal", font_size='18sp', halign='left')
        
        # Button to trigger screen switch to settings
        self.settings_btn = Button(text="Settings", size_hint_x=0.3)
        self.settings_btn.bind(on_press=self.go_to_config)
        
        nav_layout.add_widget(title_label)
        nav_layout.add_widget(self.settings_btn)
        self.main_layout.add_widget(nav_layout)
        
        # 2. Dynamic Camera Container 
        # Using a container allows us to safely create/destroy the camera object on the fly
        self.camera_container = BoxLayout(size_hint_y=0.63)
        self.main_layout.add_widget(self.camera_container)
        
        # 3. Status Display
        self.status_label = Label(text="Camera Status: Initializing...", size_hint_y=0.1)
        self.main_layout.add_widget(self.status_label)
        
        # 4. Action Button
        self.capture_button = Button(text="Capture Photo", size_hint_y=0.15)
        self.capture_button.bind(on_press=self.on_capture_pressed)
        self.main_layout.add_widget(self.capture_button)
        
        self.add_widget(self.main_layout)
        self.camera_widget = None

    def on_enter(self, *args):
        """Triggered automatically when switching INTO this screen."""
        # Grab global settings from the app instance
        app = App.get_running_app()
        cam_index = app.config_data['camera_index']
        
        # Clear any old widget states
        self.camera_container.clear_widgets()
        
        try:
            # Build camera dynamically based on configurations
            self.camera_widget = Camera(play=True, index=cam_index, resolution=(640, 480))
            self.camera_container.add_widget(self.camera_widget)
            self.status_label.text = f"Camera Status: Active (Index {cam_index})"
            self.capture_button.disabled = False
        except Exception as e:
            # Catch backend or validation errors gracefully
            self.camera_widget = Label(text=f"[Error: Failed to load camera index {cam_index}]")
            self.camera_container.add_widget(self.camera_widget)
            self.status_label.text = "Camera Status: Error"
            self.capture_button.disabled = True

    def on_leave(self, *args):
        """Triggered automatically when switching AWAY from this screen."""
        # Turn off the camera feed to safely release the hardware resource
        if self.camera_widget and hasattr(self.camera_widget, 'play'):
            self.camera_widget.play = False
        self.camera_container.clear_widgets()

    def go_to_config(self, instance):
        """Switch view target to configurations screen."""
        self.manager.current = 'config'

    def on_capture_pressed(self, instance):
        """Callback triggered when the button is pressed."""
        self.status_label.text = "Capturing image..."
        # Give the UI a brief 0.5-second pause to update the text before saving
        Clock.schedule_once(self.complete_capture, 0.5)

    def complete_capture(self, dt):
        """Saves the current camera frame to disk using user-defined properties."""
        app = App.get_running_app()
        prefix = app.config_data['file_prefix']
        
        # Construct unique name based on prefix configuration and system time
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"{prefix}_{timestamp}.png"
        
        try:
            if self.camera_widget and hasattr(self.camera_widget, 'export_to_png'):
                self.camera_widget.export_to_png(filename)
                self.status_label.text = f"Saved as {filename}! Ready for next shot."
            else:
                self.status_label.text = "Capture failed: Camera not operational."
        except Exception as e:
            self.status_label.text = f"Error saving photo: {e}"


class ConfigScreen(Screen):
    """The configuration screen for tweaking application environment values."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title
        layout.add_widget(Label(text="Configuration Settings", font_size='22sp', size_hint_y=0.15))
        
        # Settings Inputs Grid
        grid = GridLayout(cols=2, spacing=10, size_hint_y=0.6)
        
        # Option 1: Camera Hardware Index
        grid.add_widget(Label(text="Camera Hardware Index:", halign='right'))
        self.index_input = TextInput(multiline=False, write_tab=False)
        grid.add_widget(self.index_input)
        
        # Option 2: Filename Prefix
        grid.add_widget(Label(text="Filename Prefix Name:", halign='right'))
        self.prefix_input = TextInput(multiline=False, write_tab=False)
        grid.add_widget(self.prefix_input)
        
        layout.add_widget(grid)
        
        # Action Button: Save and Return
        self.save_btn = Button(text="Save & Return to Camera", size_hint_y=0.2)
        self.save_btn.bind(on_press=self.save_and_return)
        layout.add_widget(self.save_btn)
        
        self.add_widget(layout)

    def on_pre_enter(self, *args):
        """Populates the input forms with current values before the UI presents itself."""
        app = App.get_running_app()
        self.index_input.text = str(app.config_data['camera_index'])
        self.prefix_input.text = app.config_data['file_prefix']

    def save_and_return(self, instance):
        """Validates inputs, commits alterations globally, and restores camera view."""
        app = App.get_running_app()
        
        # Basic validation: ensure the index input is a valid integer string
        try:
            app.config_data['camera_index'] = int(self.index_input.text.strip())
        except ValueError:
            # Safe fallback if input is invalid text
            app.config_data['camera_index'] = 0 
            
        # Parse and store text prefix configuration safely
        clean_prefix = self.prefix_input.text.strip()
        app.config_data['file_prefix'] = clean_prefix if clean_prefix else "IMG"
        
        # Direct the ScreenManager back to the camera view pipeline
        self.manager.current = 'camera'


class CameraApp(App):
    def build(self):
        self.title = "Windows 11 Camera Portal"
        
        # Global runtime variable scope mapping accessible across all instances
        self.config_data = {
            'camera_index': 1,
            'file_prefix': 'IMG'
        }
        
        # Initialize ScreenManager to organize system screens layout flows
        sm = ScreenManager()
        sm.add_widget(CameraScreen(name='camera'))
        sm.add_widget(ConfigScreen(name='config'))
        
        return sm


if __name__ == "__main__":
    CameraApp().run()