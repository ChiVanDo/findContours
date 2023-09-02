import cv2
import numpy as np


def tinhChieuDaiLine(p_head,p_root):
    #do_dai = np.sqrt((diem_cuoi[0] - diem_dau[0])**2 + (diem_cuoi[1] - diem_dau[1])**2)
    pixel = np.sqrt((p_root[0] - p_head[0])**2 + (p_root[1] - p_head[1])**2)
    return pixel 
def getBorderAllContour(contours): #get all border of contours in img
    for contour in contours:
        # Tìm hình chữ nhật bao quanh đường viền
        x, y, w, h = cv2.boundingRect(contour)
    
        # Lấy 4 góc của hình chữ nhật
        top_left = (x, y)
        top_right = (x + w, y)
        bottom_left = (x, y + h)
        bottom_right = (x + w, y + h)
        print("Top left:", top_left)
        print("Top right:", top_right)
        print("Bottom left:", bottom_left)
        print("Bottom right:", bottom_right) 
     
    return top_left, top_right, bottom_left, bottom_right, x, y, w, h  
def getBorderContour(contours, index): #get border of contour from index 
    x, y, w, h = cv2.boundingRect(contours[index])
     # Lấy 4 góc của hình chữ nhật
    top_left = (x, y)
    top_right = (x + w, y)
    bottom_left = (x, y + h)
    bottom_right = (x + w, y + h)

    print("Top left:", index, ":", top_left)
    print("Top right:", index, ":", top_right)
    print("Bottom left:", index, ":", bottom_left)
    print("Bottom right:", index, ":", bottom_right) 
        
    return top_left, top_right, bottom_left, bottom_right, x, y, w, h 
def control(image):
    cv2.imshow("Contour Image", image)
    
    k = cv2.waitKey(0)
    if k%256 == 27:
        print("Close")
        cv2.destroyAllWindows()        
def drawAnythings(image, top_left, top_right, bottom_left, bottom_right, x, y, w, h):
    cv2.rectangle(image, (x, y), (x+w,y+h), (255,0,255), 2) #ve hinh chu nhat quanh contours
    cv2.line(image, top_left, bottom_right, (255,0,255), 2) #ve duong cheo
    cv2.line(image, top_right, bottom_left, (255,0,255), 2)
    cv2.circle(image, (x+int(w/2), y) , 1, (0, 0, 255), 3)
    dau = (x+int(w/2), y)
    cuoi = (x+int(w/2), y+h)
    print(h)
    print('m:', tinhChieuDaiLine(dau, cuoi))
    cv2.line(image, dau,cuoi, (0, 0, 255), 1) # ve duong thang chinh giua khung contours
    cv2.line(image, (0,y), (x,y),(255,0,0),1) # ve duong thang tu vien toi khung
    cv2.putText(image, f"S: {int((h/2) * (h/2) * 3.14)}" , (0,80 ), cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0), 2, cv2.LINE_AA)


   
def main():
    image = cv2.imread('findContours/img/img1.png', cv2.IMREAD_GRAYSCALE)  # Load image
    _, thresholded = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY) # chuyen anh sang B
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Find contours
    cv2.drawContours(image, contours, -1, (0, 0, 255),2) #ve Contours
    cv2.putText(image, f"Total: {len(contours)}" , (0,50), cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0), 2, cv2.LINE_AA)
    #===================================
    top_left, top_right, bottom_left, bottom_right, x, y, w, h = getBorderContour(contours, 1)
    
    drawAnythings(image, top_left, top_right, bottom_left, bottom_right, x, y, w, h)
    #===================================
    control(image)
    
if __name__ == "__main__":
    main()