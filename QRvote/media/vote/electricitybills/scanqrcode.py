import cv2
from pyzbar.pyzbar import decode

capture=cv2.VideoCapture(0)
received_data=None
while True:
    _,frame=capture.read()
    decoded_data=decode(frame)
    try:
        data=decoded_data[0][0]
        if data != received_data:
            print(data)
            received_data=data
    except:
        pass
    cv2.imshow("qr code scanner",frame)
    key=cv2.waitKey(1)
    if key== ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
        