import serial
import requests
import time

# Open the serial port
ser = serial.Serial('COM4', 115200)  # Replace 'COM1' with your serial port name

while True:
    # Read data from the serial port
    data = ser.readline().decode().strip()  # Decode the bytes to string and remove whitespace

    # Create a dictionary of the data for ThingSpeak
    ts_data = {
        'api_key': 'KXXCRVWL7FEAORDI',  # Replace with your ThingSpeak API key
        'field1': data,
        # Add more fields as needed
    }

    # Send the data to ThingSpeak using HTTP POST request
    response = requests.post('https://api.thingspeak.com/update', data=ts_data)

    # Check if the request was successful
    if response.status_code == 200:
        print('Data sent successfully to ThingSpeak')
    else:
        print('Failed to send data to ThingSpeak')
    # Wait for 5 minutes
    time.sleep(300)  # 5 minutes = 5 * 60 seconds