import cv2
import sys


if len(sys.argv)>1:
    image_name = str(sys.argv[1])
else:
    image_name = "red_car.jpg"

image = cv2.imread(f"{image_name}")
if image.all() == None:
    raise Exception("File not found, please check spelling and file extension.")

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

result = []
for i,row in enumerate(grey_image):
    row_list = []
    for j,brightness in enumerate(row):
        if brightness < 50:
            row_list.append("*")
        if brightness < 100 and brightness > 49:
            row_list.append("£")
        if brightness < 150 and brightness > 99:
            row_list.append("$")
        if brightness < 200 and brightness > 149:
            row_list.append("%")
        if brightness < 256 and brightness > 199:
            row_list.append("#")
    result.append(''.join(row_list))

image_name_without_extension = image_name.rsplit(".", 1)[0]
with open(f"{image_name_without_extension}.txt", "w") as f:
    for row in result:
        f.write(row)
        f.write('\n')






