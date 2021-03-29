import function as f
import os

unpath = "../../Database/Temp/temp_painting.png"
result, tau, path = f.process_original_image(unpath)

print(result)
print(path)


