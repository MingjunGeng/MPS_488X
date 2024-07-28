# mps-update

# index

```
├── MPS-488X.lnk                    ---> link to putty.exe 
├── MPS488X_CMD.txt                 ---> Introduce how to use commands
├── README.md
├── mac_Normal_Mode_Update.py       ---> update Device Normal Mode Fireware
├── mac_Normal_Mode_Update.bat      ---> run mac_Normal_Mode_Update.py
├── mac_Recovery_Mode_Update.bat    ---> run mac_Recovery_Mode_Update.py
├── mac_Recovery_Mode_Update.py     ---> update Device Recovery Mode_ Fireware
├── mac_check.bat                   ---> run mac_check.bat
├── mac_check.py                    ---> check change mac address and serial port number
├── mac_putty.bat                   ---> run mac_putty.bat
├── mac_putty.py                    ---> change mac address and serial port number
└── tools
    ├── README.md
    ├── getCPosition.py             ---> run mac_Recovery_Mode_Update.py
    └── getImage.py                 ---> run mac_Recovery_Mode_Update.py
```

## MPS488X_CMD.txt  
Introduce how to use commands to change mac address and serial port number
### --- 0x01 connect MPS488X 
### --- 0x02 change MAC address and  Serial Number
### --- 0x03 Update Normal Mode FW
### --- 0x04 Update Recovery Mode FW

## run cmd
```
1>
mac_putty.bat
2>
mac_check.bat
3>
mac_Normal_Mode_Update.bat 
4>
mac_Recovery_Mode_Update.bat 

```