import api
import argparse
import webbrowser

parser = argparse.ArgumentParser(description='Upload pictures to hizliresim.com')
parser.add_argument('file_paths', metavar='path', type=str, nargs='+', help='File paths of the pictures to upload')
args = parser.parse_args()
file_paths = args.file_paths[0]

link = (api.upload_pics(file_paths))
webbrowser.open(link)
