import psutil
import time
import csv
import datetime
 
while True:
        dt_now = datetime.datetime.now()
        cpuused = str(psutil.cpu_percent())
        cpu_freq2 = psutil.cpu_freq()
        freqprint = cpu_freq2.current

        with open('ここにファイルのパスを入力します｡', 'a', newline="") as f:
         f = csv.writer(f)
         f.writerow([freqprint, cpuused, dt_now.strftime('%H:%M:%S')])
         
         print(f"Current Frequency: {freqprint:.2f}Mhz")
         print(f"CPU Used: " + cpuused + "%")
         print(dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
        
         time.sleep(1)