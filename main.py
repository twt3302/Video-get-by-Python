import cv2
import datetime
import time
flagMAX = 300   #最大拍摄张数
fp = 30.0     #拍摄帧数
t = flagMAX/fp
print("预计实际拍摄总时长为：" + str(t) + "s")
# 创建VideoCapture的对象cap。传入的参数可以是设备索引1，也可以是自己本地的视频
cap = cv2.VideoCapture(0)
# video_path = 'C:\\Users\\HP\\Desktop\\Accusefi ve.mp4'
# cap = cv2.VideoCapture(video_path)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
fps = cap.get(cv2.CAP_PROP_FPS)  # 获取视频的帧率

# 生成fourcc code
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# 需要保存，创建VideoWriter对象out
out = cv2.VideoWriter('F:\\SHIPINGPAISHE\\VIDEO\\vv.avi', fourcc, fp, (640, 480))

# 确保cap打开了
if not cap.isOpened():
    print("cap is not opened, open the cap")
    cap.open()
    exit()
else:
    print('cap is opened, read the video stream...')
flag = 1
# 使用一个While循环不间断地对usb摄像头进行读取，一直到遇到键盘终止事件时break掉
# 修改FLAG值以修改拍摄的张数,视频最终拍摄时间为：张数FLAG/帧数fp = 拍摄时间t
print("【拍摄开始】")
while cap.isOpened() and flag <= flagMAX:
    # 使用cap.read()从摄像头读取一帧
    ret, frame = cap.read()
    theTime = datetime.datetime.now()
    open('F:\\SHIPINGPAISHE\\VIDEO\\test.txt', 'a+').write(str(theTime)+'\n')
    # 用read()返回的布尔值ret判断有没有正确读取到
    if not ret:
        print(' cannot receive frames(stream end?). Exiting...')
        break
    # frame = cv.flip()

    # 写入对象out调用write()写入这一帧
    out.write(frame)

    # 同时，把我们写入视频的这一帧显示出来，这样能实时看到我们处理和保存的内容
    # cv2.imshow('frame', frame)
    # # 等待1ms按键事件,如果未在规定时间按键，返回-1.如果在规定时间按键，返回所按键的ascII码值
    # if cv2.waitKey(0) == ord('q'):
    #     break
    flag += 1

# release你的cap对象和out对象
cap.release()
out.release()
cv2.destroyAllWindows()  # 销毁所有打开的HighGUI窗口。
print("拍摄结束")
time.sleep(10000)

#pyinstaller -F main.py --paths="F:\SHIPINGPAISHE\SHIPINGPAISHETEST\lib\site-packages\cv2"

