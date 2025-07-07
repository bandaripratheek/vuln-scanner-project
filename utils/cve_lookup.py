import requests

def get_cves(product, version):
    query = f"{product} {version}"
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={query}&resultsPerPage=3"
    try:
        res = requests.get(url)
        data = res.json()
        results = []
        for item in data.get("vulnerabilities", []):
            cve = item["cve"]
            results.append({
                "id": cve["id"],
                "score": cve.get("metrics", {}).get("cvssMetricV31", [{}])[0].get("cvssData", {}).get("baseScore", "N/A"),
                "summary": cve["descriptions"][0]["value"]
            })
        return results
    except Exception as e:
        print("Error:", e)
        return []
