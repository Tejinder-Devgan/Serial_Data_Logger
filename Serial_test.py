# use "python -m pip install pyserial" to install pyserial 

import serial
import csv

#

#---------------------Ask user to select the Serial Port he want to record and display-----------------------------

print("Please select the Serial Port you want to record and display:")

#---------------------- List available serial ports-----------------------------------------------------------------
ports = serial.tools.list_ports.comports()
for port in ports:
    print(port)

#-----------------------Read the Input port from the user------------------------------------------------------------
port_name = input("Enter the port name (e.g., COM18): ")

#-----------------------Open the serial port and set the baud rate---------------------------------------------------

ser = serial.Serial(port_name, 19200, timeout=1)  # open serial port
print(ser.name)         # check which port was really used
print("COM Port opened:", ser.name)
# ------------------------define the output file name----------------------------------------------------------------
output_file = 'serial_data.csv'
print("File name 'serial_data.csv' created")
#-----------------------Open the CSV file in write mode---------------------------------------------------------------

with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Data"])  # Add headers to the CSV file

    try:
        while True:
            if ser.in_waiting > 0:
                # Read data from Arduino
                line = ser.readline().decode('utf-8').strip()
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"{timestamp}: {line}")

                # Write data to CSV
                writer.writerow([timestamp, line])
    except KeyboardInterrupt:
        print("\nData recording stopped.")
    finally:
        ser.close()
        print("Serial connection closed.")


