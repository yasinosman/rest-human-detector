import os
from detect_human import detect_human

file_name = os.path.join(os.path.dirname(__file__), 'assets/gym3.jpg')
assert os.path.exists(file_name)

should_display = True

detect_human(file_name, should_display)