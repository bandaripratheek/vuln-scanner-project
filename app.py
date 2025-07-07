import streamlit as st
import nmap
import os
from utils.cve_lookup import get_cves
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# UI Setup
st.set_page_config(page_title="Vulnerability Scanner", page_icon="🛡️", layout="centered")

# Title
st.markdown("""
    <h1 style='text-align: center; color: #00FFAA;'>🛡️ Auto Vulnerability Scanner</h1>
    <p style='text-align: center; color: gray;'>Scan open ports, check for known CVEs, and generate a report instantly.</p>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📘 About This App")
    st.write("This tool uses Nmap to scan IP addresses, fetches CVE data from the NVD API, and generates a PDF report.")
    st.warning("⚠️ Use only on authorized systems!")

# Input
st.markdown("## 🔍 Enter Target IP Address")
target_ip = st.text_input("Example: 45.33.32.156", placeholder="Enter IP or domain (e.g., scanme.nmap.org)")

# Nmap + CVE Logic
def scan_target(ip):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip, arguments='-T4 -sV', timeout=120)
    services = {}
    for proto in nm[ip].all_protocols():
        for port in nm[ip][proto]:
            service_info = nm[ip][proto][port]
            name = service_info.get("name", "unknown")
            version = service_info.get("version", "")
            cves = get_cves(name, version)
            services[port] = {
                "name": name,
                "version": version,
                "cves": cves
            }
    return services

# PDF Report
def generate_pdf(ip, services, filename="sample_output/report.pdf"):
    os.makedirs("sample_output", exist_ok=True)
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    c.drawString(50, height - 50, f"Report for: {ip}")
    y = height - 100
    for port, service in services.items():
        c.drawString(50, y, f"Port {port}: {service['name']} {service['version']}")
        y -= 20
        for cve in service['cves']:
            c.drawString(70, y, f"- {cve['id']} | {cve['score']} | {cve['summary'][:50]}...")
            y -= 20
    c.save()
    return filename

# Scan Button
if st.button("🚀 Scan and Generate Report", use_container_width=True):
    if target_ip:
        with st.spinner("Running Nmap scan and fetching CVEs..."):
            try:
                results = scan_target(target_ip)
                pdf_path = generate_pdf(target_ip, results)
                st.success("✅ Scan complete! Download your report below.")
                with open(pdf_path, "rb") as f:
                    st.download_button("📄 Download PDF Report", f, file_name="vuln_report.pdf")
            except Exception as e:
                st.error(f"❌ Error during scan: {e}")
    else:
        st.warning("⚠️ Please enter a valid IP address.")

# Footer
st.markdown("""
<hr>
<p style='text-align: center; color: gray;'>
Made with ❤️ by <b>Bandari Pratheek</b> | <a href='https://github.com/pratheekbandari' target='_blank'>GitHub</a>
</p>
""", unsafe_allow_html=True)

