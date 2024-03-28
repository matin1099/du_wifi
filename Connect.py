import subprocess, time

def wifi():
    devices=""
    ok='Connection request was completed successfully.\n'

    while devices != ok :  
        try:
            devices = subprocess.check_output(['netsh','wlan','connect','name=','du']) 
    
            devices = devices.decode('ascii') 
            devices= devices.replace("\r","")      
            print("wifi Connected.")

        except:
            print("No Du Wi-Fi??!!  retry in 15s.")
            time.sleep(15)
            pass
        
