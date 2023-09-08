import cv2
import numpy as np


def redcolor(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    
    lower = [0,150,120]
    upper = [10,255,255]
    
    lower_red = np.array(lower)  # Giá trị thấp của màu đỏ
    upper_red = np.array(upper)  # Giá trị cao của màu đỏ

    # Áp dụng Gaussian Blur
    #blurred_image = cv2.GaussianBlur(hsv_image, (5, 5), 0)
    # Tạo mask dựa trên phạm vi màu đỏ
    
    mask = cv2.inRange(hsv_image, lower_red, upper_red)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Find contours
    
    result = cv2.bitwise_and(image, hsv_image, mask=mask)
    
    
    result_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    
    
    cv2.drawContours(result_image, contours, -1, (0, 0, 255),2) #ve Contours
    
    cv2.imshow('Anh Cuoi', result_image)
    
    cv2.imshow('Mask', mask)
    cv2.imshow('Red Detection', result) 
    
    
def main():
    cam = cv2.VideoCapture(0)
    while True:
        _, img = cam.read()
        redcolor(img)
        
        cv2.imshow('Image', img)
        k = cv2.waitKey(1)
        if k%256 == 27:
            print("Close")
            break
    cam.release()
    cv2.destroyAllWindows() 
    

if __name__ == "__main__":
    main()
    