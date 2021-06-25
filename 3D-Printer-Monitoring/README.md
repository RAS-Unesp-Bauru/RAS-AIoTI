# **3D Printer Monitoring App**
If you want to read it in [portuguese (Brazil)](https://github.com/carloskadu/3D-Printer-Monitoring-App/blob/readme/README%20-%20PTBR)
Our project have as an objective create an App capable of monitoring a 3D printer movement and advise the end of the impression. It comes in two modules, the main code with a server and the App. The communication is one-way only, just making sure the code send the printer current state. The main code only use one non native library that is OpenCV and the server is easily achieved with a native module of Python.


# **License**
This project is free and non-profit. The selling of it is prohibited!


# **Installation**

## **Prerequisites**

### **Python 3.6**
### Windows
[Download](https://www.python.org/downloads/) and install.
### Linux 
### Python is a native Linux language. To check your version:
```
python3 --version
```
If you are using Ubuntu 16.10 or newer, then you can easily install Python 3.6:
```
sudo apt-get update
sudo apt-get install python3.6
```


### **OpenCV**
### Windows and Linux
After downloading Python the user also gets Pip.
```
pip3 install opencv-contrib-python
```
### **Android Ambient**
You will need an Android Ambient, it can be an Android Phone of any brand.

# **How to use it?**

 First of all you need a server, you can use the Python native module: 
```
python  -m SimpleHTTPServer 8080
```
And find the alldress of your json file and add to your url variable in main.py or demo.py.To use the main.py/demo.py code with the application it is necessary to put the same url as the code in the space indicated in the java code

 You can use another as well. Make sure both the code and the app will have access to the json file so they can write and read, respectively. If you want to be able to use the server outside of your network, it’s necessary to use the DMZ service in your router.
 Setup the App Java Code with an URL of your choice, so you can access the stream. 
 The camera has to get a clean vision of the 3D printer, putting it above the printer is the best spot and will work just fine. Look the demo video to have some ideia. 
 To get it running, start the server and get your app open. Now just run the code and it’ll start detecting movement, after five minutes without it you’ll get a notification.

# **Examples**
 First use:
```
python  -m SimpleHTTPServer 8080
```
 Install and run the app in your phone or any Android Ambient. Run the code using the demo video or use any video you have with movement. You can put any URL in the Java Code, so your app will open it.
 As the video movement ends, the app should in five minutes notificate the ending of the impression and a pop-up shows up. The console of the code will show the state of the impression as well.

# **Authors**
[Carlos Eduardo Lima Gonçalves](https://github.com/carloskadu)

[João Pedro Gôuveia](https://github.com/jaaoop)

[Maria Fernanda Kadota](https://github.com/MafeKadota)

[Nodyer Henrique Nakanishi dos Anjos](https://github.com/Nodyer)

[Pedro Caldato](https://github.com/pecaldato/)

[Thaísa Corbalan Lima](https://www.facebook.com/thaisa.lima.50596)
