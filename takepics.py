import cv2
import os


if not os.path.exists('images'):
    os.mkdir('images')

class ClickPic:
    def __init__(self, ):
        pass

    def takePic(self):
        name = input('enter your name : ')
        cam = cv2.VideoCapture(0)

        cv2.namedWindow("test")

        img_counter = 0

        while True:
            ret, frame = cam.read()   # opening web cam
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)   # showing cam

            k = cv2.waitKey(1)   # waiting for actual pic when press any key
            print(k)
            if k !=-1:
                img_name = name + "opencv_frame_{}.png".format(img_counter)
                if not os.path.exists('images/'+name):
                    os.mkdir('images/'+name)
                cv2.imwrite("images/"+name+'/'+img_name, frame)    # saving img
                print("{} written!".format(img_name))   
                img_counter += 1

            if img_counter > 4:
                img_counter = 0
                break


        cam.release()   # closing cam

        cv2.destroyAllWindows() 
        print('complted')

obj = ClickPic()
obj.takePic()