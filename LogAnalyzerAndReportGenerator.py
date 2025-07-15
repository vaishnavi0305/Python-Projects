#Parse a log file(job_logs.txt) containing job statuses and durations
#Filter successful jobs
#Calculate total and average duration
#Save a clean summary report with line numbers
#Bonus: Highlight failed jobs separately

import subprocess
import sys
import os


with open("job_logs.txt", "r") as file:
    content = file.readlines()
successJob=0
successDuration= []
failed_builds=[]

for line in content:
    line = line.strip()
    if "SUCCESS" in line:
        parts = line.split(" - ")
        duration_str = parts[2].replace("s", "")
        duration = int(duration_str)
        successDuration.append(duration)
    elif "FAILED" in line:
        build_id = line.split(" - ")[0]
        failed_builds.append(build_id)
total = sum(successDuration)
count = len(successDuration)
avg = total/count if count != 0 else 0

print(" Job Summary report \n")
print("---------------------")
print(f"Succesful Build :{count}")
print(f"Total Build time: {total}s")
print(f"Average build time: {avg:.2f}s \n ")

if failed_builds:
    print("❌ Failed Builds:")
    for fb in failed_builds:
        print(f"- {fb}")

# Output to report.txt
with open("report.txt", "w") as report:
    report.write("📄 Job Summary Report\n")
    report.write("-----------------------\n")
    report.write(f"Successful Builds  : {count}\n")
    report.write(f"Total Build Time   : {total}s\n")
    report.write(f"Average Build Time : {avg:.2f}s\n\n")

    if failed_builds:
        report.write("❌ Failed Builds:\n")
        for fb in failed_builds:
            report.write(f"- {fb}\n")
