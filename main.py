import cv2
import numpy as np



def drawAnythings(image):
    cv2.rectangle(image, (229, 173), (350,290), (255,0,255), 2)
    # Vẽ đoạn thẳng trên hình ảnh
    cv2.line(image, top_left, bottom_right, (255,0,255), 2)
    cv2.circle(image, (x+int(w/2), y) , 1, (0, 0, 255), 3)
    cv2.line(image, dau,cuoi, (0, 0, 255), 3)
    cv2.line(image, (0,173), (229,173),(255,0,0),1)
    cv2.drawContours(image, contours, -1, (0, 0, 255),2)
    cv2.line(image, (590,0), (590,441), (0,0,255) , 2)
    cv2.putText(image, f"SL: {sl}" , (0,50), cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0), 2, cv2.LINE_AA)
    cv2.putText(image, f"S: {s}" , (0,80 ), cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0), 2, cv2.LINE_AA)
    
def getsBorderContour(contours):
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
        
        
def contours( top_left,top_right,bottom_left,bottom_right,x,y,w,h):
    # Load image
    image = cv2.imread('findContours/img/img11.png', cv2.IMREAD_GRAYSCALE)
    # scaling_factor = 1
    # # Sử dụng phương thức resize để thay đổi tỷ lệ ảnh
    # resized_image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor)
    # cv2.imshow('anhgoc',image)
    # Threshold the image
    _, thresholded = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    # # Find contours
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    getsBorderContour(contours)
    drawAnythings(image)
   
    # Tính độ dài của đoạn thẳng
    do_dai = np.sqrt((bottom_right[0] - top_left[0])**2 + (bottom_right[1] - top_left[1])**2)
    dau = (x+int(w/2), y)
    cuoi = (y+h, x+int(w/2))
    #do_dai = np.sqrt((diem_cuoi[0] - diem_dau[0])**2 + (diem_cuoi[1] - diem_dau[1])**2)
    duongKinh = np.sqrt((cuoi[0] - dau[0])**2 + (cuoi[1] - dau[1])**2)



   

    print("Độ dài của đoạn thẳng:", do_dai)


    # # Create a blank image to draw contours
    # #contour_image = np.zeros_like(image)

    # # Draw contours on the blank image
    


    # # Display the original image and the contour image
    #dien tich hinh tron
    khoang_cach_cm = int((int(h/2) * int(h/2)) * 2.54) / 96
    print('kc:', khoang_cach_cm)

    s = (khoang_cach_cm * 3.14) 

    sl = len(contours)
    print("count:", sl)
        
    
    cv2.imshow("Contour Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    top_left,top_right,bottom_left,bottom_right,x,y,w,h = 0,0,0,0,0,0,0,0
    contours( top_left,top_right,bottom_left,bottom_right,x,y,w,h)
    
 