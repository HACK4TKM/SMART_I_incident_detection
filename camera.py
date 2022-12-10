import cv2
from detection import AccidentDetectionModel
import numpy as np
import os
import datetime
import uuid
from upload import doThingsWithNewFiles,uploadNewFile

model = AccidentDetectionModel("model.json", 'model_weights.h5')
font = cv2.FONT_HERSHEY_SIMPLEX



def create_new_file(frames,width,height):
    filename='results/{}.mp4'.format(str(uuid.uuid1()))
    ouput_video = cv2.VideoWriter(filename,cv2.VideoWriter_fourcc(*'H264'), 10,(width,height))
    # print(frames)
    # print(len(frames))
    for i in frames:
        ouput_video.write(i)
    ouput_video.release()
    uploadNewFile(filename)

     

def startapplication():
    accident_frames=[]
    accident_times=[]
    # video = cv2.VideoCapture('accident1.mp4')
    video = cv2.VideoCapture("rtsp://192.168.1.6:4747/h264_pcm.sdp",cv2.CAP_FFMPEG)
    
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    width = int(video.get(cv2. CAP_PROP_FRAME_WIDTH ))
    height = int(video.get(cv2. CAP_PROP_FRAME_HEIGHT ))
    fps = video.get(cv2. CAP_PROP_FPS)
    frame_no=0
    is_accident=False
   
    

    while True:
        frame_no=frame_no+1
        ret, frame = video.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


        roi = cv2.resize(gray_frame, (250, 250))
        seconds = round(frame_no / fps)
        video_time = datetime.timedelta(seconds=seconds)
        # print(video_time)
        pred, prob = model.predict_accident(roi[np.newaxis, :, :])
        # print(accident_times)
        if(len(accident_frames)>200):
            create_new_file(accident_frames,width,height)
            accident_frames=[]

        if(pred == "Accident"):
            prob = (round(prob[0][0]*100, 2))
            accident_times.append(str(video_time))
            accident_frames.append(frame)
            # ouput_video.write(frame)
            # print(frame)
            # print("Accident")
            


            cv2.rectangle(frame, (0, 0), (280, 40), (0, 0, 0), -1)
            cv2.putText(frame, pred+" "+str(prob), (20, 30), font, 1, (255, 255, 0), 2)

        if cv2.waitKey(33) & 0xFF == ord('q'):
            create_new_file(accident_frames,width,height)
            return
        cv2.imshow('Video', frame)
    
    

if __name__ == '__main__':
    startapplication()
