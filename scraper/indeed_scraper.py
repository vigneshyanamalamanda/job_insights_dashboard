from serpapi import GoogleSearch
import pandas as pd
import os

def fetch_jobs_via_serpapi(query="data analyst", location="United States", num_results=30):
    API_KEY = "d063beda6a50e333576df2666e2a13c804e1610b1bb262ae59a67491512a8024"  # 🔁 Replace this with your real key

    params = {
        "engine": "google_jobs",
        "q": query,
        "location": location,
        "api_key": API_KEY,
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    job_list = []
    for job in results.get("jobs_results", [])[:num_results]:
        job_list.append({
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("location"),
            "summary": job.get("description", "")[:300],
            "salary": job.get("extensions", [""])[0] if "salary" in str(job.get("extensions", "")) else "",
        })

    if not os.path.exists("data"):
        os.makedirs("data")

    df = pd.DataFrame(job_list)
    df.to_csv("data/job_data.csv", index=False)
    print(f"✅ Saved {len(df)} job postings to data/job_data.csv")

if __name__ == "__main__":
    fetch_jobs_via_serpapi()
