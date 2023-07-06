# Hizliresim Unoffical API

This program allows you to send images to hizliresim.com using selenium.

## Prerequisites

Before using this program, make sure you have the following:

- Python3
- Liblaries from `requirements.txt`

## Setup

1. Clone the repository to your local machine or download the source code.

   ```shell
   git clone https://github.com/Weyaxi/hizliresim-api/
   ```

2. Navigate to the appropriate directory by executing the following command:
   
   ```shell
   cd hizliresim-api
   ```

4. Install the required dependencies by running the following command:

   ```shell
   pip3 install -r requirements.txt
   ```


# Usage

You can use this program with command line using this code:

   ```shell
   python3 contextmenu_project.py <path_to_image>
   ```

The program will upload the image to Hizliresim and open the uploaded image url in your default web browser.


# Context Menu Integration

To add a "Upload to Hizliresim" option to the right-click context menu in Windows Explorer, follow these steps:

1. Open the `with_cmd.reg` or `without_cmd.reg` file (depending on whether you want to open a command prompt while sending the image) in a text editor.

2. Update the script's and python's file path in the registry file to match the location of the necessary files on your system.

3. Save the changes and double-click the registry file to merge the changes into the Windows Registry.

Right-click any file in Windows Explorer and select "Upload to Hizliresim". The program will upload the image to Hizliresim and open the uploaded image url.

![image](https://github.com/Weyaxi/hizliresim-api/assets/81961593/1d942ca1-0604-4841-b078-f5b4fca767bc)

## Demo





