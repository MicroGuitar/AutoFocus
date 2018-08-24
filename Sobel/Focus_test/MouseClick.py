import cv2
def draw_rectangle(event,x,y,flags,param):
    global ix, iy
    if event==cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        print("point1:=", x, y)
    elif event==cv2.EVENT_LBUTTONUP:
        print("point2:=", x, y)
        print("width=",x-ix)
        print("height=", y - iy)
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)

img = cv2.imread("Src_0.png")  
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)
while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()