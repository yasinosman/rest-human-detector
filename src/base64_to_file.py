import base64
from werkzeug.utils import secure_filename
from os.path import join, dirname
from datetime import datetime



def base64_to_file(base64_string):
    mime_type = base64_string.split(",")[0].split(";")[0].split("/")[1]

    now = datetime.now() # current date and time
    date_time = now.strftime("%m-%d-%Y_%H-%M-%S")

    filename = secure_filename(date_time + "." + mime_type)
    filepath = join(join(dirname(__file__), 'uploads/'), filename)

    print(mime_type)
    print(date_time)
    print(filename)
    print(filepath)

    try:
        image_data = base64_string.split(",")[1]

        with open(filepath,"wb") as f:
                f.write(base64.decodebytes(image_data.encode()))
                return filepath
    except Exception as e:
        print("Exception in base64_to_file")
        print(str(e))

