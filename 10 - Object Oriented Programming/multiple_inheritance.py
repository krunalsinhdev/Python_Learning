# Multiple Inheritance
# A child class can inherit from more than one parent class.

class Camera:
    def take_photo(self):
        print("Photo captured.")

class Phone:
    def make_call(self):
        print("Calling...")

class SmartPhone(Camera, Phone):
    def browse_internet(self):
        print("Browsing the internet.")

mobile = SmartPhone()
mobile.take_photo()
mobile.make_call()
mobile.browse_internet()
