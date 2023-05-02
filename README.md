# SecureWipe

This project contains a Python script to perform a DOD (Department of Defense) style wipe on all SSD drives in a server. The script also captures the manufacturer, model, capacity, and serial number of each drive and records the number of blocks successfully overwritten and the number that failed during the wipe process.

## Prerequisites

- Python 3.x installed on the server
- `smartctl` installed on the server. You can install it using the following command:

  ```bash
  sudo apt-get install smartmontools
