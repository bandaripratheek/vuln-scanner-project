 🔍 Automated Vulnerability Scanner with CVE Report

A Python-based cybersecurity project that scans any target using **Nmap**, looks up known vulnerabilities from the **CVE database**, and generates a clean, professional **PDF report** — all via a simple **Streamlit GUI**.

 📌 Features

- 🔍 Scan IPs or domains using Nmap
- 🔓 Detect open ports & running services
- 🧠 Fetch known vulnerabilities (CVEs) from public databases
- 📄 Auto-generate PDF vulnerability reports
- 🖥️ Run via a simple Streamlit-based GUI
- ✅ Great for learning real-world recon & automation

 🧰 Tech Stack

| Technology     | Role                                |
|----------------|-------------------------------------|
| `Python`       | Core programming language           |
| `Streamlit`    | GUI for user input & output         |
| `nmap`         | Port scanner (called via subprocess)|
| `requests`     | For CVE API calls                   |
| `reportlab`    | PDF generation                      |
| `GitHub`       | Version control and project hosting |

 📁 Project Structure
vuln-scanner-project/
├── app.py # Main Streamlit GUI App
├── utils/
│ └── cve_lookup.py # CVE lookup logic
├── sample_output/
│ └── report.pdf # Generated report
└── README.md # This file!

1. Clone this repository
bash: git clone https://github.com/bandaripratheek/vuln-scanner-project.git
cd vuln-scanner-project

2. Install required libraries
bash: pip install streamlit nmap requests reportlab  or pip install -r requirements.txt

3.Run the app
bash: streamlit run app.py

4.View the generated reports in **sample_output/**

🧠 What I Learned
> Automated recon using Python + Nmap

> Real-world CVE lookup using external APIs

> PDF report generation

> GUI development with Streamlit

> End-to-end project structuring and GitHub deployment

📷 Screenshots
![Vulnerability Scanner](https://github.com/user-attachments/assets/d226c58f-d2a8-4442-9915-e01462e6d3e2)
![Vulnerability Scanner 2](https://github.com/user-attachments/assets/13471328-1666-486c-aa01-1cc466b65928)



🏷️ License
This project is licensed under the MIT License — feel free to use or build on it!





