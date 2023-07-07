# import the libraries
import cv2
from pyzbar import pyzbar

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        
        # decode the barcode or QR code information
        barcode_info = barcode.data.decode('utf-8')
        
        # draw a rectangle around the information
        cv2.rectangle(frame, (x, y),(x+w, y+h), (255, 0, 255), 2) 
        
        # add text above the rectangle which includes decoded information-
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x - 6, y - 6), font, 0.5, (0, 0, 0), 1)
        
        #export the information to a text document
        with open("barcode_result.txt", mode ='w') as file:
            file.write("Recognized Barcode:" + barcode_info)

    return frame

def main():
    # turn on the computer camera 
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()

   # run loop to continue performing decode function 
    while ret:
        # get code info and call read_barcode function
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        # break the loop if esc key pressed
        if cv2.waitKey(1) & 0xFF == 27:
            break
    camera.release()
    # close the application window
    cv2.destroyAllWindows()

# calling main function to trigger the program
if __name__ == '__main__':
    main()
