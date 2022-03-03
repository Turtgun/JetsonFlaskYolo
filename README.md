# Yolo object detection on NVIDIA jetson nano that is then transmitted to a flask server

This repository extends on two different projects, mainly [**JetsonYolo**](https://github.com/amirhosseinh77/JetsonYolo) and [**Face Detection Web Apps In Flask**](https://www.youtube.com/watch?v=i_-m1kBTdBI) that I then repurposed into a web application for 5057 Robobusters. This tool can be repurposed by anyone but must remain with the GPLv3 license.

### Current use case
Use a yolocv5 model on a JetsonNano that is connected to two USB Cameras, this model will be used to detect balls and send the position back to the roborio so that the robot can move to that spot, the purpose for flask is so that a driver and/or programmers can connect to the roborio and get a stream of what the camera sees.

### Models
This project has some models currently preinstalled inside of weights/ folder delete them if you wish.

## Requirements
These steps are essential for software and hardware configuration.

##### PyTorch & torchvision
Yolov5 network model is implemented in the Pytorch framework.
PyTorch is an open source machine learning library based on the Torch library, used for applications such as computer vision and natural language processing.
Heres a complete guide to [**install PyTorch & torchvision**](https://forums.developer.nvidia.com/t/pytorch-for-jetson-version-1-9-0-now-available/72048) for Python on Jetson Development Kits 

##### NetworkTables & flask
A simpler install, just do:

```
pip3 install networktables flask
```

## Running
Run ```app.py``` to start the webserver and then detect the objects with the 2 USB(!!!) cameras.
```
python3 app.py
```

## Support
If you need explanations on how this project works, check the links above or file an issue on this github page.
