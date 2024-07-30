import json
import struct

# Define the structure for the binary data
driver_data_format = 'BB'  # 2 bytes for each DriverData (driver_number and led_num)
frame_format = driver_data_format * 20  # 20 DriverData per frame
visualization_format = frame_format * 8879  # 8879 frames

# Define the file paths
binary_file_path = 'data.bin'
json_file_path = 'data.json'

# Load the JSON data
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

# Deserialize the binary data
binary_data = []
with open(binary_file_path, 'rb') as bin_file:
    for _ in range(8879):  # Total number of frames
        frame = []
        for _ in range(20):  # Each frame contains 20 DriverData entries
            driver_data = struct.unpack('BB', bin_file.read(2))
            frame.append({'driver_number': driver_data[0], 'led_num': driver_data[1]})
        binary_data.append({'frame': frame})

# Compare the two data structures
if binary_data == json_data:
    print("The data in both files are equal.")
else:
    print("The data in the files are not equal.")
