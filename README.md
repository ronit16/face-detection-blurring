# Face Detection and Blurring with OpenCV and MediaPipe

This project uses OpenCV and MediaPipe to detect faces in images, videos, or webcam feeds and applies a blur effect to the detected faces. The processed media is then saved to an output directory or displayed in real-time for webcam input.

Install the required packages using:

```bash
pip install -r requirements.txt
```

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ronit16/face-detection-blurring.git
    cd face-detection-blurring
    ```

2. **Run the main script:**

    - To process an image:

        ```bash
        python main.py --image path_to_your_image.jpg
        ```

    - To process a video:

        ```bash
        python main.py --video path_to_your_video.mp4
        ```

    - To use the webcam:

        ```bash
        python main.py --webcam
        ```

    Press `q` to exit the webcam feed.

## How It Works

- The script captures input from an image file, video file, or webcam.
- Converts the frame from BGR to RGB color space for MediaPipe processing.
- Detects faces and applies a blur effect to the detected faces.
- Saves the processed image or video to the `output` directory or displays the real-time feed for the webcam.

## Customization

- You can change the blur intensity by modifying the kernel size in the `cv2.blur` function within the `process_image` function.

## Output

### Example Output
<p align="center">
    <img src="assets/test_image.jpg" alt="Output Image 1" width="45%"/>
    <img src="output/output.jpg" alt="Output Image 2" width="45%"/>
</p>

(![output/output.jpg](https://github.com/ronit16/face-detection-blurring/blob/main/output/output.jpg))

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any improvements or bug fixes.


### Notes

- Replace `path_to_your_output_image.png` with the actual path to your output image file in the repository.
- Ensure the input paths provided to the script are correct.
- The `cv2.blur` function uses a kernel size of (200, 200) which can be adjusted for different blur intensities.
