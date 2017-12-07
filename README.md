# Dissertation_Project

# Required Packages

## Ubuntu or Debian

  ```apt-get install build-essential python-dev libnetfilter-queue-dev```
  
## Arch

  ```TODO ```
  
# Install for Python

Note: Python 3.6 is required

  ```
  sudo pip install NetfilerQueue
  sudo pip install scapy
  sudo pip install python-nmap
  ```

# Configuring PI as a router

[Guide followed here](https://jacobsalmela.com/2014/05/19/raspberry-pi-and-routing-turning-a-pi-into-a-router/)

# Hostapd Settings
```
  interface=wlan0
  driver=rtl871xdrv
  ssid=NAME
  hw_mode=g
  channel=3
  wpa=2
  wpa_passphrase=PASSWORD
  wpa_key_mgmt=WPA-PSK
  wpa_pairwise=TKIP
  rsn_pairwise=CCMP
  auth_algs=1
  macaddr_acl=0
````
