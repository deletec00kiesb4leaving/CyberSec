# Portfolio Activity: IP Address Management

## Overview

This activity involved creating a Python script to manage IP addresses by:

1. **Generating Random IPs** (Bonus):
   - Coded a script to generate `X` randomized IPv4 addresses.
   - Created an `remove_list.txt` with 3 IP addresses to be removed from the generated list.

   ![Screenshot of Generated IP Addresses](Generated.PNG)

## Main Task

- **IP Filtering Script**: 
  - Given two files:
    - `allow_list.txt`: Contains a list of allowed IP addresses.
    - `remove_list.txt`: Contains IP addresses to be removed.

  The script reads both files, filters out any IPs from `allow_list.txt` that appear in `remove_list.txt`, and outputs the filtered list.
  
   ![Screenshot of Updated IP List](Updated.PNG)

## Usage

Have an `allow_list.txt` and a `remove_list.txt` on the same folder.

Run the script:

```bash
python3 UpdateFileAlgo.py
```
