# webdriver-framework-python

A quick written framework in Python to test apps/browser on devices using Appium.

## Prerequisites

Python 3.7+

Install Appium

Install Appium-Python-Client

## Features

Starts appium if not triggered

Follows Page Object Model - BasePage with minimum click and wait added

Example test given with Speedtest

Runner has been configured

Device ID has to be passed via command line option --device (or -d)

Entire test suites can be run using command line option --test all or (-t all):

```python3 TestCases/runner.py --device <your_device_id> --test all --os Android --noreset True --package app.package --activity app.package.activity```

To run individual tests:

```python3 TestCases/runner.py --device <your_device_id> --test test_SpeedTest --os Android --noreset True --package app.package --activity app.package.activity ```

## Options

### Add device ID
`'-d', '--device', dest="udid", help='Enter device ID to run the test', default=True`

### Add test to run
`'-t', '--test', dest="test", help='Enter test to run the test or all to run all', default="all"`

### Add android package name
`'-p', '--package', dest="package", help='App package', default=False`

### Add android activity name
`'-a', '--activity', dest="activity", help='App activity', default=False`

### Add iOS bundle ID
`'-b', '--bundleid', dest="bundleid", help='Bundle ID', default=False`

### Add OS type - "Android" or "iOS"
`'-o', '--os', dest="os", help='OS Type', default="Android"`

### Add noReset - True/False
`'-n', '--noreset', dest="noreset", help='No reset', default=False`

### Add cloud URL, default is False
`'-c', '--cloud', dest="cloud", help='Cloud URL', default=False`

## How to create tests and run:

Create "CustomPage" (any name) extend from BasePage

Create "test_YourTest.py" and extend from BaseTest

Make sure tests are saved as test_<anything>.py

Write your test case logic under "test_YourTest.py"

Similarly create other pages and test

## Improvements needed


Currently tested only on Android devices

Currently assuming that Appium is always running on localhost 4723 (hard coded in DataConfig)

Tauk project ID & token is also configured under DataConfig