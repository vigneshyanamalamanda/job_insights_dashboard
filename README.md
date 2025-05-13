# Job Insights Dashboard

A Streamlit-based data product that scrapes and visualizes job postings across the U.S. for data-related roles. This interactive dashboard enables users to explore job titles, companies, locations, and in-demand skills from real-time data sources.

---

## Features

- Scrapes real-time job listings using **SerpAPI** (Google Jobs engine)
- Filter jobs by **location** and **skills** (e.g., Python, SQL, Tableau)
- Interactive visualizations for:
  - Top job titles
  - Hiring companies
  - Skill mentions in job summaries
- Built with **Streamlit**, **Pandas**, and **Matplotlib**
- Designed for job seekers, educators, and career advisors

---

## Project Structure

job_insights_dashboard/
├── app/
│ └── dashboard.py # Streamlit dashboard UI
├── data/
│ └── job_data.csv # Scraped data output (auto-generated)
├── notebooks/
│ └── analysis.ipynb # Exploratory data analysis
├── scraper/
│ └── indeed_serpapi.py # Job data scraper via SerpAPI
├── .gitignore
├── README.md
└── requirements.txt


---

## Tech Stack

- **Python 3.10+**
- [**Streamlit**](https://streamlit.io) – frontend
- [**SerpAPI**](https://serpapi.com) – job search API
- **Pandas, Matplotlib** – data wrangling and visualization

---

## How to Use Locally

### 1. Clone the repo
```bash
git clone https://github.com/vigneshyanamalamanda/job_insights_dashboard.git
cd job_insights_dashboard

## INSTALL DEPENDENCIES
pip install -r requirements.txt

## Scrape job data from INDEED
python scraper/indeed_serpapi.py

##  Launch the dashboard
streamlit run app/dashboard.py
