import cv2 as cv
from cv2 import aruco
import numpy as np

# Define the real width of the ArUco marker (in cm)
MARKER_REAL_WIDTH = 5.0  # Adjust this based on your actual marker size

# Load the ArUco marker dictionary
marker_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

# Define ArUco detection parameters
param_markers = aruco.DetectorParameters()

# Focal length (in pixels). Adjust this value based on your camera's calibration.
FOCAL_LENGTH = 700  # You may need to calibrate your camera for the exact value.

# Intrinsic camera parameters (camera matrix and distortion coefficients)
# These should be obtained from a camera calibration process.
camera_matrix = np.array([[FOCAL_LENGTH, 0, 320],
                          [0, FOCAL_LENGTH, 240],
                          [0, 0, 1]], dtype=np.float64)  # Ensure it's float
dist_coeffs = np.zeros((5, 1), dtype=np.float64)  # Ensure it's float

# Open the camera feed from Iriun (or another IP webcam)
cup = cv.VideoCapture("http://192.168.1.20:8080/video")

# Verify camera opened correctly
if not cup.isOpened():
    print("Error: Cannot open camera")
    exit()

while True:
    ret, frame = cup.read()

    if not ret:
        print("Error: Failed to grab frame")
        break

    # Convert the frame to grayscale for ArUco detection
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect the ArUco markers in the grayscale frame
    marker_corners, marker_IDs, rejected = aruco.detectMarkers(
        gray_frame, 
        marker_dict, 
        parameters=param_markers
    )

    if marker_corners:
        # Estimate the pose of the detected markers
        rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(
            marker_corners, MARKER_REAL_WIDTH, camera_matrix, dist_coeffs
        )

        for i, ids in enumerate(marker_IDs):
            corners = marker_corners[i].astype(np.int32)

            # Draw polygon around the markers
            cv.polylines(frame, [corners], True, (0, 255, 255), 4, cv.LINE_AA)

            # Draw the axes of the detected markers (representing 3D pose)
            cv.drawFrameAxes(frame, camera_matrix, dist_coeffs, rvecs[i], tvecs[i], 5)

            # Reshape and convert corner points to integers
            corners = corners.reshape(4, 2)
            corners = corners.astype(int)

            # Top-right corner for displaying the marker ID
            top_right = corners[0].ravel()
            cv.putText(
                frame, 
                f"ID: {int(ids[0])}",  # Convert ID to integer for better display
                top_right, 
                cv.FONT_HERSHEY_PLAIN, 
                1.3, 
                (255, 255, 255), 2, cv.LINE_AA
            )

            # Display translation (x, y, z in cm) and rotation (rvec) values
            translation = tvecs[i].ravel() * 100  # Convert to cm
            rotation = np.degrees(rvecs[i].ravel())  # Convert to degrees

            # Display translation vector
            cv.putText(
                frame,
                f"Translation (cm): x={translation[0]:.2f}, y={translation[1]:.2f}, z={translation[2]:.2f}",
                (top_right[0], top_right[1] + 20),
                cv.FONT_HERSHEY_PLAIN,
                1.3,
                (0, 255, 0), 2, cv.LINE_AA
            )

            # Display rotation vector (Euler angles approximated from the rotation vector)
            cv.putText(
                frame,
                f"Rotation (deg): x={rotation[0]:.2f}, y={rotation[1]:.2f}, z={rotation[2]:.2f}",
                (top_right[0], top_right[1] + 40),
                cv.FONT_HERSHEY_PLAIN,
                1.3,
                (0, 255, 255), 2, cv.LINE_AA
            )

    # Display the frame with the detected markers and pose information
    cv.imshow("ArUco Marker Detection with 6D Pose", frame)

    # Break the loop on 'q' key press
    key = cv.waitKey(1)
    if key == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cup.release()
cv.destroyAllWindows()