# RAS-AIOTI
IoT project from RAS - Unesp Bauru

# AIOTI
The main objective of this project is to apply IoT (Internet of Things) concepts in order to improve the comfort, security and efficiency.

## Introduction

The AIOTI project was designed to understand and apply the concepts of IoT technologies, the objective was to communicate the projects already developed in RAS. To achieve this goal, we selected some projects that could be implemented in our IEEE student branch, they are the [ReconFace](https://github.com/lucasrs21/ReconhecimentoFacial2), [3D-Printer-Monitoring-App](https://github.com/carloskadu/3D-Printer-Monitoring-App) and [People-Flow-Monitoring](https://github.com/FabricioAmoroso/People-Flow-Monitoring). These projects were slightly modified to send data via a MQTT network. A Node-Red server is used to control data flow, and a MySQL database to store such data, from which both are stationed along with a MQTT Broker inside a Raspberry Pi (Version 3 or superior) acting as the core of the application.
