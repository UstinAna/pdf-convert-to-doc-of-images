# config.py
name = input("Please enter the name of the file you wish to convert (ex. your file name is <abc.pdf>, enter <abc>)") # the name of the final pdf/doc that's gonna be outputted
zoom = 3 # Zoom factor, can be adjusted to improve quality, (higher is better quality but larger file size)
zoom = float(input("Please enter the zoom factor you wish to use (3 is suggested for balanced quality and file size)")) # Zoom factor, can be adjusted to improve quality, (higher is better quality but larger file size)
bebug = True if input("debug (y/n) ") == "y" else False # Debug mode, set to True to enable debug logging
