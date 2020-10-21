import cv2	
import sys
imagePath = input("Enter your image name!!!make sure it is in the same directory!!!: ")
try:
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
except:
	print("Image not found\nmake sure its in the same folder")
	exit()
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
yface = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.075,
    minNeighbors=3,
    minSize=(30, 30)
)

print("[*] Found {0} Faces.".format(len(yface)))

for (x, y, w, h) in yface:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
abcd = cv2.imwrite(str(w) + str(h) +'_faces_detect.jpg', image)
print("[INFO] Image saved to system")

ask=input("Tell me if you to cut the face and store it[y/Y/YES/yes or n/N/no/NO]: ")
if ask in ('y', 'yes', 'Y', 'YES'):
	print("Doing")
	for (x, y, w, h) in yface:
	    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
	    roi_color = image[y:y + h, x:x + w]
	    print("[INFO] Object found. Saving locally.")
	    cv2.imwrite(str(w) + str(h) + '_facesharssh.jpg',roi_color )
	

elif ask in ('N', 'NO', 'n', 'no'):
	print("ok your choise")

else:
	print("Invalid option")