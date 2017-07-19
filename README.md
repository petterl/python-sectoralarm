# python-sectoralarm
A python module for reading and changing status of sectoralarm devices through their App API. 
Compatible with both Python2 (2.6+) and Python3.

### Legal Disclaimer
This is based on Per Sandströms python-verisure (https://github.com/persandstrom/python-verisure) to work with Sector Alarm systems.
This software is not affiliated with Sector Alarm AB and the developers take no legal responsibility for the functionality or security of your Sector Alarm Alarms and devices.


### Version History
```
1.0.0 First version
```

## Installation
``` pip install git+https://github.com/petterl/python-sectoralarm.git ```


## Command line usage

```
usage: sectoralarm.py [-h] 
                   ...

Read or change status of sectoralarm devices

positional arguments:
  username              MyPages username
  password              MyPages password
  panel                 Panel Id

commands
    armstate            Get arm state
    lock                Get lock status
    set                 Set status of a device
    temperature         Get climate history
    eventlog            Get event log

optional arguments:
  -h, --help            show this help message and exit
```

### Read alarm status

``` sectoralarm user@example.com mypassword 12345 status ```

output:

```
{
    "status": "success",
    "timeex": "2017-06-27T15:20:00",
    "isSystemDownForMaintenance": false,
    "user": "John Doe",
    "time": "Yesterday 15:20",
    "message": "disarmed",
    "statusAnnex": ""
}
```



