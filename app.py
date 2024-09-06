import datetime
import time

end_time=datetime.datetime(2024,9,7)
site=["www.remove.bg","www.facebook.com"]
host_path="C:/Windows/System32/drivers/etc/hosts"
redirect="127.0.0.1"

while True:
    if datetime.datetime.now()<end_time:
        print("Start Blocking...")
        with open(host_path,"r+") as file:
            content=file.read()
            for website in site:
                if website not in content:
                    file.write(redirect+" "+website+"\n")
                else:
                    pass
    else:
        print("Blocking Stopped")
        with open(host_path,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in site):
                    file.write(line)
            file.truncate()

    time.sleep(5)