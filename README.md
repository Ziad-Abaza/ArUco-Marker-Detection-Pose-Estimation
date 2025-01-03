**Repo Name**: `ArUco-Marker-Detection-Pose-Estimation`

**README.md Description**:

```markdown
# ArUco Marker Detection and Pose Estimation

This project demonstrates the generation, detection, and pose estimation of ArUco markers using OpenCV and Python. It utilizes various ArUco marker types and calculates their 3D pose in space, allowing for real-time marker tracking and transformation.

## Features

- **ArUco Marker Generation**: Generate custom ArUco markers of different types (e.g., DICT_4X4_50, DICT_5X5_100) and save them as images.
- **Pose Estimation**: Detect ArUco markers in video feeds and estimate their 3D pose (translation and rotation).
- **Camera Calibration**: Supports intrinsic camera matrix and distortion coefficients for accurate pose estimation.
- **Multiple Marker Types**: Works with a variety of ArUco marker dictionaries such as DICT_4X4_50, DICT_5X5_100, DICT_APRILTAG_36h10, and more.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Matplotlib (for visualization)

To install the required dependencies, run:

```bash
pip install opencv-python numpy matplotlib
```

## Usage

### 1. Generate ArUco Marker

```python
from aruco_markers_plus import run_generate_aruco_marker
from aruco_markers_plus import ArucoType

run_generate_aruco_marker(ArucoType.DICT_4X4_50, marker_id=0, marker_width_pixels=200)
```

This will generate a marker image and save it as `aruco_marker.png`.

### 2. Pose Estimation

```python
from aruco_markers_plus import run_aruco_marker_pose_estimation
from aruco_markers_plus import ArucoType

run_aruco_marker_pose_estimation(ArucoType.DICT_6X6_250)
```

This will initiate the camera feed and estimate the pose of detected ArUco markers.

### 3. ArUco Pose Estimation with Camera Feed

The `ArUco_marker.py` script continuously detects ArUco markers from a camera feed and displays their 3D pose (translation and rotation).

```python
python ArUco_marker.py
```

Press `q` to quit the detection process.

## Contributing

Feel free to fork this repository, submit issues, and make pull requests. Contributions are welcome!
