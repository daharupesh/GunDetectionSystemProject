# Gun Detection System

This project is a real-time gun detection system using OpenCV, a Haar Cascade classifier, and Pygame for sound alerts. The system captures video input from your camera, detects guns, and triggers an alarm if a firearm is identified in the frame.

## Features

- **Real-Time Detection**: Identifies guns in the camera feed using a pre-trained Haar Cascade classifier.
- **Alarm Notification**: Sounds an alarm when a gun is detected and stops when no gun is found.
- **Timestamp Overlay**: Displays the current date and time on the video feed for context.

## Requirements

Make sure to have the following Python libraries installed:

- `numpy`
- `opencv-python`
- `imutils`
- `pygame`

You also need:
- A gun detection cascade file (`cascade.xml`).
- An alarm sound file (`alarm.wav`).

## Installation

1. **Clone the Repository**:
   ```bash
   https://github.com/daharupesh/GunDetectionSystemProject.git
   cd gun-detection-system
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Required Files**:
   - Place `cascade.xml` in the project directory. This file contains the pre-trained model for gun detection.
   - Ensure `alarm.wav` is available in the directory. This sound will play when a gun is detected.

## Usage

To start the gun detection system:

1. **Run the Script**:
   ```bash
   python gun_detection.py
   ```

2. **Exit**: Press `q` to stop the program.

## How It Works

- **Detection**: The system continuously monitors the camera feed, resizing frames for efficiency, and converting them to grayscale for processing.
- **Alert**: When a gun is detected, the system draws a bounding box around the gun and plays an alarm sound. The alarm continues until the gun is no longer visible in the frame.
- **Timestamp**: Each frame is timestamped with the current date and time for reference.

## Contributing

Contributions are welcome! Feel free to open issues, suggest features, or submit pull requests.
