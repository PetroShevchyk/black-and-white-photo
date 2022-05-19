from PIL import Image

sunset = Image.open("sunset.jpg")
sunset_c = sunset.convert("L")

sunset_c.show()
