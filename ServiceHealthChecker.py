#Write a Python script that:
#Takes a list of services (e.g., Nginx, Docker, Jenkins)
#Checks if each service is running on the system
#Records the result in a readable report (using string formatting)
#Outputs the result to both terminal and a .txt log file
#Optionally prints summary info (how many services are running/stopped)

#🚀 Steps to Implement:
#Use a list to store service names
#Loop over the list and use subprocess.run(["systemctl", "is-active", <service>])
#Check output: if it's 'active', mark as RUNNING; 'inactive', mark as STOPPED; error = NOT INSTALLED
#Write each result line to a text file
#Use counters to track total running/stopped/not installed

import subprocess
import sys
from datetime import datetime

#getting the list of services as a command line argument and sys.argv[1:] take input after the script name which is sys.argv[0]
services= sys.argv[1:]
print(f"Checking services status...\n") 
# check if user has entered any service name
if services:

    running=0
    stopped=0
    notinstalled=0
    with open("service_report.txt", "a") as file:
        file.write(f"\n===== Service Report: {datetime.now()} =====\n")
        for i in range(len(services)):
              status = subprocess.run(["systemctl", "is-active", services[i]], capture_output=True, text=True)
              if status.stdout.strip() == "active":
                    print(f"Service: {services[i]} -> RUNNING")
                    file.write(f"{services[i]} -> RUNNING \n")
                    running = running+1
              elif status.stdout.strip() == "inactive":
                    print(f"Service: {services[i]} -> STOPPED")
                    file.write(f"{services[i]} -> STOPPED \n")
                    stopped= stopped +1
              else:
                    print(f"Service: {services[i]} -> NOT INSTALLED \n")
                    file.write(f"{services[i]} -> NOT INSTALLED \n")
                    notinstalled=notinstalled+1
    
        print(f"\nSummary: \n Running:{running} | Stopped:{stopped} | Not Installed:{notinstalled}")

else:
     print(f"Enter the services as a command line arguments. Ex: python3 scriptname.py arg1 arg2 arg3 ...")
     sys.exit(1)

    


