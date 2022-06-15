# webdriver-framework-python

A quick written framework in Python to test apps/browser on devices using Appium.

## Prerequisites 
Python 3.7+
Install Appium-Python-Client
Install Appium

## Features

Starts appium if not triggered
Follows Page Object Model - BasePage with minimum click and wait added
Example test given with Speedtest
Runner has been configured
Device ID has to be passed via command line option --device (or -d)
Entire test suites can be run using command line option --test all or (-t all):
python3 TestCases/runner.py --device <your_device_id> --test all

To run individual tests:
python3 TestCases/runner.py --device <your_device_id> --test test_SpeedTest


## How to run:

Create "CustomPage" (any name) extend from BasePage
Create "test_YourTest.py" and extend from BaseTest
Make sure tests are saved as test_<anything>.py
Write your test case logic under "test_YourTest.py"

Similarly create other pages and test
  
To run the entire suites, 

python3 TestCases/runner.py --device <your_device_id> --test test_SpeedTest

## Improvements needed  
  
Desired capabilities have been hard coded for the app which is fixed as Ookla Speedtest
Currently tested on Android devices
