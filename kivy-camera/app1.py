import os
# Force Kivy to use the OpenCV backend on Windows
os.environ['KIVY_CAMERA'] = 'opencv'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

import time

class CameraRootLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        # Windows Tip: index=0 is usually your integrated laptop webcam. 
        # If you are using a USB external webcam, you may need to change index to 1 or 2.
        try:
            self.camera_widget = Camera(play=True, index=1, resolution=(640, 480))
            self.status_label = Label(text="Camera Status: Ready", size_hint_y=0.1)
            camera_failed = False
        except TypeError:
            # Catch backend failure gracefully if OpenCV fails to load
            self.camera_widget = Label(text="[Error: No Windows Camera Backend Found]", size_hint_y=0.75)
            self.status_label = Label(text="Camera Status: Error", size_hint_y=0.1)
            camera_failed = True
            
        self.capture_button = Button(text="Capture Photo", size_hint_y=0.15)
        if camera_failed:
            self.capture_button.disabled = True
        
        self.add_widget(self.camera_widget)
        self.add_widget(self.status_label)
        self.add_widget(self.capture_button)
        
        self.capture_button.bind(on_press=self.on_capture_pressed)

    def on_capture_pressed(self, instance):
        """Callback triggered when the button is pressed."""
        self.status_label.text = "Capturing image..."
        
        # Give the UI a brief 0.5-second pause to update the text before saving
        Clock.schedule_once(self.complete_capture, 0.5)

    def complete_capture(self, dt):
        """Saves the current camera frame to disk."""
        # 1. Create a unique filename based on the current date and time
        # Example: IMG_20260527_150421.png
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"IMG_{timestamp}.png"
        
        try:
            # 2. Export the camera widget's current frame to a file
            self.camera_widget.export_to_png(filename)
            self.status_label.text = f"Saved as {filename}! Ready for next shot."
        except Exception as e:
            self.status_label.text = f"Error saving photo: {e}"


class CameraApp(App):
    def build(self):
        self.title = "Windows 11 Camera Portal"
        return CameraRootLayout()


if __name__ == "__main__":
    CameraApp().run()