import struct
import json

# Define the structure for the binary data
driver_data_format = 'BB'  # 2 bytes for each DriverData (driver_number and led_num)
frame_format = driver_data_format * 20  # 20 DriverData per frame

def main():
    # Read the binary file
    with open('data.bin', 'rb') as bin_file:
        binary_data = bin_file.read()
    
    # Initialize index and list to hold deserialized frames
    index = 0
    frames = []

    # Calculate the total number of frames
    num_frames = len(binary_data) // struct.calcsize(frame_format)
    
    # Deserialize each frame
    for _ in range(num_frames):
        frame_data = binary_data[index:index + struct.calcsize(frame_format)]
        index += struct.calcsize(frame_format)

        frame = []
        for i in range(20):
            driver_number, led_num = struct.unpack_from('BB', frame_data, i * 2)
            if driver_number == 0 and led_num == 0:
                frame.append(None)
            else:
                frame.append({"driver_number": driver_number, "led_num": led_num})

        frames.append({"frame": frame})
    
    # Output the first frame as JSON
    first_frame_json = json.dumps(frames[0], indent=4)
    print(f"First frame data: {first_frame_json}")

if __name__ == "__main__":
    main()
