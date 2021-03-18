import function as f
import os

unpath = "../../Resource/Images/Button/Temp/uncropped_image.jpg"
result, path = f.process_original_image(unpath)

print(result)
print(path)


