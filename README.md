# SecureWipe

This project contains a Python script to perform a DOD (Department of Defense) style wipe on all SSD drives in a server. The script also captures the manufacturer, model, capacity, and serial number of each drive and records the number of blocks successfully overwritten and the number that failed during the wipe process.

## Prerequisites

- Python 3.x installed on the server
- `smartctl` installed on the server. You can install it using the following command:

  ```bash
  sudo apt-get install smartmontools
  ```
  
 ## Usage
 1. Clone the repository
 ```bash
git clone https://github.com/jkmills/SecureWipe
cd SecureWipe
```

2. Ensure the script is executable:
```bash
chmod +x dod_wipe_extended.py
```

3. Execute the script with root privileges:
4. ```bash
5. sudo ./dod_wipe_extended.py
```
The script will perform a DOD-style wipe (3 passes) on all the SSD drives in the server. It will first list all available disk devices and then perform the wipe on each device, capturing the required information.
