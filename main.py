import os
import argparse
import cv2
import mediapipe as mp

def process_image(image, face_detection):
    try:
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(img_rgb)

        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = image.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                
                # Blur faces
                image[y:y+h, x:x+w] = cv2.blur(image[y:y+h, x:x+w], (150, 150))
        return image
    except Exception as e:
        print(f"Error processing image: {e}")
        return image

def main():
    parser = argparse.ArgumentParser(description='Face Detection and Blurring')
    
    parser.add_argument('--image', type=str, help='Path to the image file')
    parser.add_argument('--video', type=str, help='Path to the video file')
    parser.add_argument('--webcam', action='store_true', help='Use webcam')

    args = parser.parse_args()
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Initialize MediaPipe Face Detection
    mp_face_detection = mp.solutions.face_detection

    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        
        # If image in argument
        if args.image:
            try:
                image = cv2.imread(args.image)
                if image is None:
                    raise ValueError("Image not found or unable to load.")
                image = process_image(image, face_detection)
                # Save image
                cv2.imwrite(f'{output_dir}/output.jpg', image)
            except Exception as e:
                print(f"Error processing image file: {e}")

        # If video in argument
        elif args.video:
            try:
                cap = cv2.VideoCapture(args.video)
                if not cap.isOpened():
                    raise ValueError("Video not found or unable to open.")
                frames = []
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    frames.append(process_image(frame, face_detection))
                cap.release()
                # Save video
                out = cv2.VideoWriter(f'{output_dir}/output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frames[0].shape[1], frames[0].shape[0]))
                for frame in frames:
                    out.write(frame)
                out.release()
            except Exception as e:
                print(f"Error processing video file: {e}")

        # If webcam in argument
        elif args.webcam:
            try:
                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    raise ValueError("Unable to access webcam.")
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    frame = process_image(frame, face_detection)
                    cv2.imshow('frame', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()
            except Exception as e:
                print(f"Error accessing webcam: {e}")

if __name__ == "__main__":
    main()
