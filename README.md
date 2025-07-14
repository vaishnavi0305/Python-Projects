# 🛠️ Service Health Checker – Python DevOps Utility

This is a command-line Python tool that checks the **status of system services** (like `nginx`, `docker`, `jenkins`, etc.) on a Linux system using `systemctl`, and logs their status to a report file.

> ✅ Ideal for DevOps engineers to monitor service health, automate audits, or integrate with cron jobs & CI/CD workflows.

---

## 🚀 Features

- Accepts any number of service names via command-line
- Checks whether each service is:
  - ✅ RUNNING
  - ❌ STOPPED
  - 🔍 NOT INSTALLED / UNKNOWN
- Logs results to `service_report.txt`
- Outputs summary: number of running/stopped/missing services
- Appends a timestamped header to each new scan

---

## 🧪 Example Output

**Command:**
```bash
python3 service_health_checker.py docker nginx jenkins ssh
```

**Terminal Output:**
```
Checking services status...

Service: docker   → RUNNING
Service: nginx    → STOPPED
Service: jenkins  → NOT INSTALLED
Service: ssh      → RUNNING

Summary:
Running: 2 | Stopped: 1 | Not Installed: 1
```

**Report File (`service_report.txt`):**
```
===== Service Report: 2025-07-01 20:44:52 =====
docker -> RUNNING
nginx -> STOPPED
jenkins -> NOT INSTALLED
ssh -> RUNNING
```

---

## 📦 How to Use

### ✅ Prerequisites

- Linux system (Ubuntu, CentOS, etc.)
- Python 3.x installed
- Services managed by `systemd` (use `systemctl`)

### 🧾 Usage

```bash
python3 service_health_checker.py service1 service2 service3 ...
```

Example:
```bash
python3 service_health_checker.py docker ssh nginx
```

---

## 📁 File Structure

```text
├── service_health_checker.py    # Main script
├── service_report.txt           # Auto-generated log file
└── README.md                    # You're here!
```

---

## ⚙️ How It Works (Logic Flow)

1. Takes service names from command-line
2. Uses `subprocess.run()` to check each via `systemctl is-active`
3. Classifies them as RUNNING / STOPPED / NOT INSTALLED
4. Logs results to file with current timestamp
5. Displays a clean summary in terminal

---

## ✅ Skills Demonstrated

- Python built-ins: `sys`, `subprocess`, `datetime`, `file I/O`
- CLI tooling
- Log/report generation
- DevOps scripting logic (automation-focused)

---

## 📌 Use Cases

- Pre-deployment checks
- Cronjob service monitoring
- Audit reports for services
- Self-healing scripts (can be extended!)

---

## 📜 License

This project is open-source and free to use under the MIT License.

---

## 🙋‍♀️ Author

**Vaishnavi Buradkar**  
DevOps Enthusiast | Cloud Engineer | Python Automator  
🔗 [GitHub Profile](https://github.com/vaishnavi0305)
