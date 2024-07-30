import json
import struct

# Define the structure for the binary data
driver_data_format = 'BB'  # 2 bytes for each DriverData (driver_number and led_num)
frame_format = driver_data_format * 20  # 20 DriverData per frame
visualization_format = frame_format * 8879  # 8879 frames

def main():
    # Read the JSON file
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
    
    # Prepare binary data
    binary_data = b''

    for frame_dict in data:
        frame = frame_dict['frame']
        for driver_data in frame:
            if driver_data is not None:
                driver_number = driver_data['driver_number']
                led_num = driver_data['led_num']
            else:
                driver_number = 0
                led_num = 0
            # Pack the driver data into binary format
            binary_data += struct.pack('BB', driver_number, led_num)

    # Write the binary data to a file
    with open('data.bin', 'wb') as bin_file:
        bin_file.write(binary_data)

if __name__ == "__main__":
    main()
