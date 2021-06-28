# RAS-AIOTI
IoT project from RAS - Unesp Bauru

# AIOTI
The main objective of this project is to apply IoT (Internet of Things) concepts in order to improve the comfort, security and efficiency.

## Introduction

The AIOTI project was designed to understand and apply the concepts of IoT technologies, the objective was to communicate the projects already developed in RAS. To achieve this goal, we selected some projects that could be implemented in our IEEE student branch, they are the [ReconFace](https://github.com/lucasrs21/ReconhecimentoFacial2), [3D-Printer-Monitoring-App](https://github.com/carloskadu/3D-Printer-Monitoring-App) and [People-Flow-Monitoring](https://github.com/FabricioAmoroso/People-Flow-Monitoring). These projects were slightly modified to send data via a MQTT network. A Node-Red server is used to control data flow, and a MySQL database to store such data, from which both are stationed along with a MQTT Broker inside a Raspberry Pi (Version 3 or superior) acting as the core of the application.

## Installation
To be able to run each program, you will need to install some libraries. First of all, update your pip version using the following command:
```
pip install --upgrade pip
```

### Face recognition

This program require computer vision and neural networks functionalities, so make sure to install the following libraries:

Numpy
```
pip install numpy
```

OpenCV
```
pip install opencv-python
```

OpenCV Contrib
```
pip install opencv-contrib-python
```

Imultils
```
pip install imutils
```

Pillow
```
pip install pillow
```

Pytest-shutil
```
pip install pytest-shutil
```

Scikit Learn
```
pip install scikit-learn
```

Paho-MQTT
```
pip install paho-mqtt
```


### People-Flow

This program, like the one above, requires computer vision and neural networks. So, certify yourself of install correctly the packages described in the requirements file:

```
pip install -r people_flow_requirements.txt
```

### 3D-Printer

This program needs just computer vision, so you will need to install the packages bellow:
 
Numpy
```
pip install numpy
```

OpenCV
```
pip3 install opencv-contrib-python
```

Paho-MQTT
```
pip install paho-mqtt
```

## AIoTI Team

> AIoTI

| <a href="https://github.com/claudiogabriel-1" target="_blank">**Claudio Gabriel Rosa Dujanski**</a> | <a href="https://github.com/zechelf" target="_blank">**Felipe Maziero Zechel (Scrum Master)**</a> | <a href="https://github.com/JpZwAr" target="_blank">**João Pedro Olimpio**</a> |
| :---: |:---:| :---:|
| [![FVCproductions](https://avatars.githubusercontent.com/u/72581866?v=4)](http://fvcproductions.com)    | [![FVCproductions](https://avatars.githubusercontent.com/u/51209420?v=4)](http://fvcproductions.com) | [![FVCproductions](https://avatars.githubusercontent.com/u/54182167?v=4)](http://fvcproductions.com)  |
| <a href="https://github.com/claudiogabriel-1" target="_blank">`github.com/claudiogabriel-1`</a> | <a href="https://github.com/zechelf" target="_blank">`github.com/zechelf`</a> | <a href="https://github.com/JpZwAr" target="_blank">`github.com/JpZwAr`</a> |  
<br />
<br />

| <a href="https://github.com/lucas-serrano" target="_blank">**Lucas Serrano Costa**</a> | <a href="https://github.com/MatheusMABR" target="_blank">**Matheus Augusto Barbosa Rodrigues**</a> | <a href="https://github.com/paulo-gigliotti" target="_blank">**Paulo Gigliotti (Product Owner)**</a> |
| :---: |:---:| :---:|
| [![FVCproductions](https://avatars.githubusercontent.com/u/72429343?v=4)](http://fvcproductions.com)    | [![FVCproductions](https://avatars.githubusercontent.com/u/55408283?v=4)](http://fvcproductions.com) | [![FVCproductions](https://avatars.githubusercontent.com/u/54952751?v=4)](http://fvcproductions.com)  |
| <a href="https://github.com/lucas-serrano" target="_blank">`github.com/lucas-serrano`</a> | <a href="https://github.com/MatheusMABR" target="_blank">`github.com/MatheusMABR`</a> | <a href="https://github.com/paulo-gigliotti" target="_blank">`github.compaulo-gigliotti`</a> |
