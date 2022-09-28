# calibration_challenge
A calibration challenge
---
## PROBLEM
An attempt to predict the pitch and yaw angles of car from monocular dashboard camera. We want an output of an array containig pitch and yaw euler represenations.

---

### APPROACH
- Euler angles for pitch and yaw using rotation matrix. To obtain roll, ptch and yawa, we need to use the function decomposeProjectionMatrix after applying solvePnP
- solvePnP does not dierctly give roll, pitch and yaw but need to calculate it using a rotation matrix. 
- That's where the decomposeProjectionMatrix comes in.

---

### USEFUL SOURCES
- https://answers.opencv.org/question/16796/computing-attituderoll-pitch-yaw-from-solvepnp/
- https://www.morethantechnical.com/2010/03/19/quick-and-easy-head-pose-estimation-with-opencv-w-code/
- https://answers.opencv.org/question/12547/inconsistent-results-from-solvepnp/
- https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html
- PANGOLIN


