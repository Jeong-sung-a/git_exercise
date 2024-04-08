import cv2
import os, glob

detector = cv2.FaceDetectorYN.create("../FaceDetection/Resource/face_detection_yunet_2023mar.onnx", "", (0, 0))

eye_cascPath = "../FaceDetection/Resource/haarcascade_eye_tree_eyeglasses.xml"  #eye detect model
eyeCascade = cv2.CascadeClassifier(eye_cascPath)

base_dir = './faces'
dirs = [d for d in glob.glob(base_dir) if os.path.isdir(d)]
for dir in dirs:
    files = glob.glob(dir+'/*.jpg')
    print('\t path:%s, %dfiles'%(dir, len(files)))
    for file in files:
        image_cv2_yunet = cv2.imread(file)
        gray = cv2.cvtColor(image_cv2_yunet, cv2.COLOR_BGR2GRAY)
        height, width, _ = image_cv2_yunet.shape
        detector.setInputSize((width, height))
        _, faces = detector.detect(image_cv2_yunet)
        for(x1, y1, w, h, x_re, y_re, x_le, y_le, x_nt, y_nt, x_rcm, y_rcm, x_lcm, y_lcm, extra) in faces:
            roi_gray = gray[int(y1):int(y1 + h), int(x1):int(x1 + w)]
            roi_color = image_cv2_yunet[int(y1):int(y1 + h), int(x1):int(x1 + w)]

            eyes = eyeCascade.detectMultiScale(roi_gray)

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)

        cv2.imshow('Eyes Detection', image_cv2_yunet)
        if cv2.waitKey(0) == ord('q') or cv2.waitKey(0) == ord('Q'):
            cv2.destroyAllWindows()