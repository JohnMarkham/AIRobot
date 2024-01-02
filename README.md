# AIRobot
ChatGPT controller simple prototype robot.

You pass an objective written in clear English, as a parameter to the robot. It passes the command to ChatGPT, then ChatGPT will issue directions to the robot to achieve the objective. Directions are {forward, backward, left, right, and found}. That's it, very simple!
## Video Examples
https://vimeo.com/manage/videos/898588452

https://www.youtube.com/watch?v=XoMICkLN2Cc

## Running Locally
### Installing Dependencies
**NOTE**: This assumes you have Python3 installed. If you do not install it from here: https://www.python.org/downloads/
#### Virtual Environment
Setup a virtual environment (optional, but recommended):
```
conda create -n chatgptrobot -y
```
You can change the name, or the perimeter after -n, to anything you want.
```
conda activate chatgptrobot
```
#### Python Packages
Install all the Python dependencies needed to run these scripts. I would recommend downloading them separately as I show below so you can fix any error messages:
```
python3 -m pip install paho-mqtt
```
```
python3 -m pip install python-etcd
```
```
python3 -m pip install RPi.GPIO
```
```
python3 -m pip install openai
```
```
python3 -m pip install picamera
```
### Running
#### GIT Scripts
You can use the tool GIT to easily download all the scripts to your computer:
```
git clone https://github.com/grandell1234/AIRobot.git
```
Then enter the file with this command:
```
cd AIRobot
```
#### Running the Robot
You are ready to begin:
```
python3 comms.py
```
