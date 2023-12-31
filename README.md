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

You can use this api like this:

   ```python
   import api

# Single File Upload

single_image_path = r'C:/absolute/path1'

api.upload_pics(single_image_path)  # Output: https://i.hizliresim.com/image.png

# Multi File Upload

image_paths = [r'C:/absolute/path1', r'C:/absolute/path2', r'C:/absolute/path3']

api.upload_pics(image_paths)  # Output: ['https://i.hizliresim.com/image.png', 'https://i.hizliresim.com/image2.png', 'https://i.hizliresim.com/image3.png']



   ```

The api will upload the image(s) to Hizliresim and returns the link(s) of the uploaded images.

# Context Menu Integration

To add a "Upload to Hizliresim" option to the right-click context menu in Windows Explorer, follow these steps:

1. Open the `add_to_context.reg` file in a text editor.

2. Update the script's and python's file path in the registry file to match the location of the necessary files on your system.

3. Save the changes and double-click the registry file to merge the changes into the Windows Registry.

Right-click any file in Windows Explorer and select "Upload to Hizliresim". The program will upload the image to Hizliresim and open the uploaded image url.

![context](https://github.com/Weyaxi/hizliresim-api/assets/81961593/4c0bf154-64e8-40c5-a512-73441e75e2d7)

## Note

Unfortunately I couldn't fixed the multifile context menu integratation. So if user selects more than one image and click to "Upload to Hızliresim" it will upload images seperatly (opening more than one browser in background). But my `api.py` code supports multi file uploading in one browser. You only have to send the paths to the function in an array.

## Demo

## Single File Upload

![1](https://github.com/Weyaxi/hizliresim-api/assets/81961593/62a64588-c8e2-4fd7-aa71-409668c113a2)

## Multi File Upload

![2](https://github.com/Weyaxi/hizliresim-api/assets/81961593/8c07beab-5a26-46e6-9cac-9bd7f93f18c7)

