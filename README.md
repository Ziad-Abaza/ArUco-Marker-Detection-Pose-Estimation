# ArUco Marker Detection and Pose Estimation

This project demonstrates the detection of ArUco markers and the estimation of their 6D pose (position and orientation) using OpenCV and Python. The project contains scripts for generating ArUco markers and detecting them using a camera, with visualization of their position and orientation.

## Files

### 1. **aruco-markers-plus.py**
   - Generates and displays ArUco markers of various types and sizes.
   - Detects ArUco markers in real-time from a camera feed.
   - Estimates the 3D pose (rotation and translation vectors) of detected markers.
   - Displays the detected marker with axes showing its pose.

### 2. **ArUco_marker.py**
   - Detects ArUco markers from an IP webcam stream.
   - Estimates the pose of the detected markers, displaying translation (in cm) and rotation (in degrees).
   - Draws markers and axes on the video feed to visualize the detected markers' positions and orientations.

## Setup Instructions

### Requirements:
1. **Python 3.x**
2. **OpenCV** (with ArUco module)
   - Install OpenCV using:
   ```bash
   pip install opencv-python opencv-contrib-python
   ```
3. **NumPy** (for numerical operations)
   - Install NumPy using:
   ```bash
   pip install numpy
   ```
4. **Matplotlib** (optional, for displaying images)
   - Install Matplotlib using:
   ```bash
   pip install matplotlib
   ```

### Calibration:
For pose estimation to work correctly, you need to calibrate your camera to obtain the camera matrix and distortion coefficients. You can adjust the `camera_matrix` and `dist_coeffs` parameters in the code to match your own camera's calibration values.

### Running the Scripts:
1. **Generating an ArUco Marker**:
   - Run `aruco-markers-plus.py` with the following function call to generate a marker:
     ```python
     run_generate_aruco_marker(ArucoType.DICT_6X6_250, marker_id=0, marker_width_pixels=200)
     ```
   - This will generate an image of an ArUco marker with the specified parameters and display it.

2. **Detecting ArUco Markers and Estimating Pose**:
   - Run `aruco-markers-plus.py` with the following function call to detect markers and estimate pose:
     ```python
     run_aruco_marker_pose_estimation(ArucoType.DICT_6X6_250)
     ```
   - This will open a camera feed and start detecting ArUco markers. If detected, it will display the position and orientation of the marker in the video feed.

3. **Detecting ArUco Markers from IP Webcam Stream**:
   - Run `ArUco_marker.py` to capture frames from an IP webcam and estimate the pose of detected markers.

### Key Parameters:
- `MARKER_REAL_WIDTH`: The real-world size of the marker in centimeters. This should be set according to the actual physical size of the marker being used.
- `FOCAL_LENGTH`: The camera's focal length (in pixels). You may need to adjust this based on your camera's calibration.

## Example Output

- **Marker Detection**: The script will detect the markers, display their IDs, and draw axes representing the marker's orientation.
- **Pose Information**: The translation vector (in cm) and rotation vector (in degrees) will be displayed next to the detected marker.

## Notes

- Make sure your camera is calibrated and that the intrinsic parameters (`camera_matrix` and `dist_coeffs`) are properly set for accurate pose estimation.
- You may need to adjust the `aruco_type` depending on the marker dictionary you're using.
