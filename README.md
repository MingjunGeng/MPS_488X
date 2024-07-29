# MPS_488X Automation Tool

## Overview

The MPS_488X Automation Tool is designed to automate the manual processes involved in configuring and testing the MPS_488X device on an assembly line. This tool utilizes `pyautogui` for GUI automation and `wxPython` for creating a user-friendly interface.

## Project Structure

```
├── MPS-488X.lnk                    ---> link to putty.exe
├── README.md
├── doc                             ---> Introduce how to use commands to change mac address and serial port number
├── mac_main.py                     ---> link to putty.exe
├── tools                           ---> get Image info
└── v01                             ---> tag v01
```

- **Device/dev_mpx488x.py**: Contains the main automation class for the MPS_488X device.
- **tools/getCPosition.py**: Script to get the current cursor position.
- **tools/getImage.py**: Script to capture and save screenshots of specific areas.
- **wxMac_main.py**: The main GUI application using `wxPython`.

## Installation

1. Clone the repository:
   ```sh
   git clone git@github.com:MingjunGeng/MPS_488X.git
   cd MPS_488X

2. Install the required packages:

```sh
pip install pyautogui wxPython pillow keyboard opencv-python
```

## Usage

**Running the Main GUI**

To start the GUI application, run:

```sh
python wxMac_main.py
```

**Using the Automation Tool**

1.  **Update Device Normal Mode Firmware**: Automates the firmware update process in normal mode.
1.  **Update Device Recovery Mode Firmware**: Automates the firmware update process in recovery mode.
1.  **Change Mac Address and Serial Number**: Automates the process of changing the MAC address and serial number.
1.  **Check Mac Address and Serial Number**: Automates the process of checking the MAC address and serial number.
1.  **Exit**: Closes the applicatio

**Helper Scripts**

-   Get Cursor Position:

```sh
python tools/getCPosition.py
```
This script continuously prints the current cursor position until interrupted.

-   Capture Image:

```
python tools/getImage.py
```

This script captures a screenshot of a specified area and saves it to a file.


##  Contributing

Feel free to submit issues, fork the repository, and send pull requests.

##  License

This project is licensed under the MIT License.


## Acknowledgements

Special thanks to the contributors and the open-source community for their support and contributions.


This README file provides an overview of the project, installation instructions, usage details, and information on contributing and licensing. Adjust the repository URL and other details as needed for your specific project setup.