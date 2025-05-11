from ultralytics import YOLO
import cv2
import math
import smtplib
from email.message import EmailMessage
import pygame

def email_alert(subject, body, to):
    if not hasattr(email_alert, "has_run"):
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to

        user = "senderemail@gmail.com"
        msg['from'] = user
        password = "password(16)"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)

        server.quit()
        email_alert.has_run = True

def email_alert1(subject, body, to):
    if not hasattr(email_alert1, "has_run"):
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to

        user = "senderemail@gmail.com"
        msg['from'] = user
        password = "password(16)"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)

        server.quit()
        email_alert1.has_run = True

def email_alert2(subject, body, to):
    if not hasattr(email_alert2, "has_run"):
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to

        user = "senderemail@gmail.com"
        msg['from'] = user
        password = "password(16)"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)

        server.quit()
        email_alert2.has_run = True

def email_alert3(subject, body, to):
    if not hasattr(email_alert3, "has_run"):
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to

        user = "senderemail@gmail.com"
        msg['from'] = user
        password = "password(16)"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)

        server.quit()
        email_alert3.has_run = True

def email_alert4(subject, body, to):
    if not hasattr(email_alert4, "has_run"):
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to

        user = "senderemail@gmail.com"
        msg['from'] = user
        password = "password(16)"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)

        server.quit()
        email_alert4.has_run = True


def ring_alarm():
    if not hasattr(ring_alarm, "has_run"):
        pygame.mixer.init()
        pygame.mixer.music.load('sher_aaya.mp3')  # Replace with your alarm sound file
        pygame.mixer.music.play()
        ring_alarm.has_run = True

def ring_alarm1():
    if not hasattr(ring_alarm1, "has_run"):
        pygame.mixer.init()
        pygame.mixer.music.load('Alarm_Sound.mp3')  # Replace with your alarm sound file
        pygame.mixer.music.play()
        ring_alarm1.has_run = True


def video_detection(path_x):
    video_capture = path_x
    #Create a Webcam Object
    cap=cv2.VideoCapture(video_capture)
    frame_width=int(cap.get(3))
    frame_height=int(cap.get(4))
    #out=cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P','G'), 10, (frame_width, frame_height))

    model=YOLO("YOLO-Weights/best.pt")
    classNames = ['Antelope', 'Cheetah', 'Elephant', 'Giraffe', 'Leopard', 'Lion', 'Monkey', 'Zebra']
    while True:
        success, img = cap.read()
        results=model(img,stream=True)
        for r in results:
            boxes=r.boxes
            for box in boxes:
                x1,y1,x2,y2=box.xyxy[0]
                x1,y1,x2,y2=int(x1), int(y1), int(x2), int(y2)
                print(x1,y1,x2,y2)
                conf=math.ceil((box.conf[0]*100))/100
                cls=int(box.cls[0])
                class_name=classNames[cls]
                label=f'{class_name}{conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                print(t_size)
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                if class_name == "Lion":
                    color=(0, 204, 255)
                    email_alert("Danger!", "Lion detected", "receiveremail@gmail.com")
                    ring_alarm()

                elif class_name == "Cheetah":
                    color = (222, 82, 175)
                    email_alert1("Danger!", "Tiger detected", "receiveremail@gmail.com")
                    ring_alarm1()

                elif class_name == "Elephant":
                    color = (222, 82, 175)
                    email_alert2("Danger!", "Elephant detected", "receiveremail@gmail.com")
                    ring_alarm1()

                elif class_name == "Leopard":
                    color = (0, 149, 255)
                    email_alert3("Danger!", "Leopard detected", "receiveremail@gmail.com")
                    ring_alarm1()

                else:
                    color = (85,45,255)
                    email_alert4("Hey!", "Wild Animal detected", "receiveremail@gmail.com")
                if conf>0.5:
                    cv2.rectangle(img, (x1,y1), (x2,y2), color,3)
                    cv2.rectangle(img, (x1,y1), c2, color, -1, cv2.LINE_AA)  # filled
                    cv2.putText(img, label, (x1,y1-2),0, 1,[255,255,255], thickness=1,lineType=cv2.LINE_AA)



        yield img
        #out.write(img)
        #cv2.imshow("image", img)
        #if cv2.waitKey(1) & 0xFF==ord('1'):
            #break
    #out.release()
cv2.destroyAllWindows()
