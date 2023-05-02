#!/usr/bin/env python3

"""Module providingFunction local process."""
import subprocess
"""Module providingFunction unknown."""
import re

def get_drive_info(device):
    info = subprocess.check_output(['smartctl', '-i', device]).decode('utf-8')

    model = re.search(r'Device Model:\s*(.*)', info).group(1).strip()
    serial = re.search(r'Serial Number:\s*(.*)', info).group(1).strip()
    capacity = re.search(r'User Capacity:\s*(.*)', info).group(1).strip()
    manufacturer = re.search(r'Vendor:\s*(.*)', info)
    if manufacturer:
        manufacturer = manufacturer.group(1).strip()
    else:
        manufacturer = "Unknown"

    print(f'Device: {device}')
    print(f'Manufacturer: {manufacturer}')
    print(f'Model: {model}')
    print(f'Serial Number: {serial}')
    print(f'Capacity: {capacity}')
    print()

def single_pass(device):
    pass_result = subprocess.run(
        ['dd', 'if=/dev/urandom', f'of={device}', 'bs=1M', 'status=progress'],
        capture_output=True, text=True
    ).stderr

    success_blocks = re.search(r'blocks=(\d+)', pass_result).group(1)
    failed_blocks = re.findall(r'blocks=(\d+)', pass_result)[-1]

    print(f'Successfully overwritten blocks: {success_blocks}')
    print(f'Failed blocks: {failed_blocks}')

def dod_wipe(device):
    print(f'Performing DOD wipe on device: {device}')

    for pass_num in range(1, 4):
        print(f'Wiping pass {pass_num}')
        single_pass(device)

    print(f'DOD wipe completed on device: {device}')
    print()

def main():
    devices_output = subprocess.check_output(
        "lsblk -o NAME,TYPE -p -n -l | grep 'disk' | awk '{print $1}'",
        shell=True
    ).decode('utf-8')
    devices = devices_output.strip().split('\n')

    for device in devices:
        get_drive_info(device)
        dod_wipe(device)

if __name__ == '__main__':
    main()
