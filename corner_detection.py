# importing the module
import cv2
from PIL import Image
# function to display the coordinates of
# of the points clicked on the image

coordinates = []
folder = '/home/chanduri/Desktop/cropped_images/'

def distance(point1, point2):
	return ((point2[0] -point1[0])**2 + (point2[1] -point1[1])**2)**0.5

def section(point1, point2, m, n ):
	
	x= (m*point2[0] + n*(point1[0]))/(m+n)
	y = (m * point2[1] + n * (point1[1])) / (m + n)
	
	return [x, y]

def custom_section(point1, point2, m, n, row):
	m = 42 * m + (m * (m - 1) * 8.428) / 2
	n = distance(top[row - 1], bottom[row - 1]) - m
	return section(point1,point2,m,n)
	
def make_image(point, i, j):
	img = Image.open('/home/chanduri/Pictures/chess_board1.png')
	destination = folder + 'board' + str(i) + str(j) + '.png'
	width = point[2][0] - point[3][0]
	height = point[3][1] - point[0][1]
	print(point[0][0] + width, point[0][1] + height)
	
	cropped = img.crop((point[0][0]-width/2 ,point[0][1] -height ,point[0][0] + 1.5*width , point[0][1] + 1.5*height))
	# cropped = img.crop((point[0][0], point[0][1], point[0][0] + point[2][0] - point[3][0], point[0][1]+ point[3][1] - point[0][1]))
	cropped.save(destination)
	



def click_event(event, x, y, flags, params):

	# checking for left mouse clicks
	if event == cv2.EVENT_LBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		print(x, ' ', y)
		coordinates.append([x,y])

		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, str(x) + ',' +
                    str(y), (x, y), font,
                    1, (255, 0, 0), 2)
		cv2.imshow('image', img)

	# checking for right mouse clicks
	if event == cv2.EVENT_RBUTTONDOWN:

		# displaying the coordinates
		# on the Shell
		print(x, ' ', y)

		# displaying the coordinates
		# on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x, y), font, 1,
                    (255, 255, 0), 2)
		cv2.imshow('image', img)


# driver function
if __name__ == "__main__":
	# print(distance([3, 0], [0, 4]))
	# exit(0)

	# reading the image
	img = cv2.imread('/home/chanduri/Pictures/chess_board1.png', 1)

	# displaying the image
	cv2.imshow('image', img)


	# setting mouse hadler for the image
	# and calling the click_event() function
	cv2.setMouseCallback('image', click_event)

	# wait for a key to be pressed to exit
	cv2.waitKey(0)

	# close the window
	cv2.destroyAllWindows()

	x1=coordinates[0][0]
	x2=coordinates[1][0]
	x3 = coordinates[2][0]
	x4 = coordinates[3][0]

	y1 = coordinates[0][1]
	y2 = coordinates[1][1]
	y3 = coordinates[2][1]
	y4 = coordinates[3][1]

	top = []
	# right = []
	bottom = []
	# left = []


	for i in range(9):
		top.append(section(coordinates[0], coordinates[1], i, 8 - i))
	
	# for i in range(9):
	# 	right.append(section(coordinates[1], coordinates[2], i, 8 - i))
	
	# for i in range(9):
	# 	left.append(section(coordinates[0], coordinates[3], i, 8 - i))
	
	for i in range(9):
		bottom.append(section(coordinates[3], coordinates[2], i, 8 - i))

	# print(coordinates)
	# print(top)
	# print(right)
	# print(left)
	# print(bottom)
	cropped_coordinates = []
	for i in range(1, 9, 1):
		for j in range(1, 9, 1):
			#cell coordinates(4,3)
			topleft = custom_section(top[i-1], bottom[i-1], j-1, 8-j+1,i)
			topright = custom_section(top[i], bottom[i], j-1, 8-j+1 ,i)
			bottomleft = custom_section(top[i-1], bottom[i-1], j, 8-j,i)
			bottomright = custom_section(top[i], bottom[i], j, 8-j,i)
			cropped_coordinates.append([topleft, topright, bottomright, bottomleft])
			#coordinates in clockwise direction

	make_image(cropped_coordinates[21], 6, 6)
	print('photo cropped and saved')
	# start = coordinates[5][1] - coordinates[4][1] 
	# end = coordinates[7][1] - coordinates[6][1]
	# print(start) 
	# print(end) 
	# print(top[5], bottom[5])
	# print(section(left[5],right[5],6,2))
	# print(cropped_coordinates[53])
	exit(0)





	xl = min([x1, x2, x3, x4])
	yl = min([y1, y2, y3, y4])
	xr = max([x1, x2, x3, x4])
	yr = max([y1, y2, y3, y4])

	crop_img = img[yl:yr, xl:xr]
	print(type(cropped_coordinates) )
	exit(0)

	cv2.imshow("cropped", crop_img)
	cv2.waitKey(0)

	# print(coordinates)


