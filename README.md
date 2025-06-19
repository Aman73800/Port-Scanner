# 🔍 Python Port Scanner

A multithreaded **Port Scanner** built using Python that scans a custom range of ports on a target IP or domain to identify open ports.

➡️ **GitHub Repo**: [Aman73800/Port-Scanner](https://github.com/Aman73800/Port-Scanner.git)

---

## 📌 Features

* Accepts target IP/domain and port range via input
* Uses `socket` to test connectivity to each port
* Implements `threading` for fast parallel scanning
* Outputs only **open** ports in real time
* CLI-based, lightweight tool for basic cybersecurity or networking tasks

---

## 🛠️ Tech Stack

* **Python 3**
* `socket` – for checking port connections
* `threading` – to enable concurrent scanning

---

## 🖥️ How It Works

1. User inputs a **target IP or domain** and a **port range** (start to end).
2. For each port in the range:

   * A new thread is spawned that attempts a TCP connection
   * If successful (port is open), the result is printed
3. Threads run concurrently for faster performance

### 📸 Example Output:

```
🔍 Scanning 127.0.0.1 from port 70 to 90...

[+] Port 80 is OPEN
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed

### Run the Script

```bash
git clone https://github.com/Aman73800/Port-Scanner.git
cd Port-Scanner
python port_scanner.py
```

---

## 📁 File Structure

```
port_scanner.py   # Main script for port scanning
```

---

## ⚠️ Disclaimer

This tool is meant for **educational purposes only**. Do not use it to scan servers or IPs that you do not own or have permission to test.

---

## 🙌 Acknowledgments

* Built as part of **Internship Task 3** under the guidance of **@YourCompanyName**

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).

---

📬 Contributions and suggestions welcome! Fork or star the repo here: [GitHub Link](https://github.com/Aman73800/Port-Scanner.git)
