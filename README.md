# 📉 NYC Operational Risk & Trend Analysis
### *Optimizing Public Safety Resource Allocation using 9 Years of Incident Data*

### 📊 Project Overview
**Role:** Lead Data Analyst  
**Tools:** SQL Server (T-SQL), Python (Pandas), Tableau, Excel  
**Dataset:** NYC Department of Health (2015-2024 Data)  
**Status:** [Completed]

**The Challenge:** The NYC Department of Health was operating on pre-pandemic safety models. Stakeholders needed to know if the post-2020 landscape had changed and how to optimize limited enforcement resources.

**The Solution:** I conducted a strategic audit of 9 years of incident data using advanced SQL (Window Functions, CTEs, Rolling Averages) to identify hidden risk factors, forecast staffing needs, and propose an evidence-based resource allocation strategy.

---

## 📂 Repository Structure
*This project is structured to mimic a production analytics environment.*

```text
📂 NYC-Operational-Risk-and-Trend-Analysis
│
├── 📜 README.md              <-- Executive Summary & Strategic Report
├── 📂 sql_queries            <-- Full T-SQL scripts for all 12 business questions
│   ├── 01_pareto_hotspots.sql
│   ├── 02_yoy_growth.sql
│   ├── 03_risk_categorization.sql
│   └── ...
├── 📂 visualizations         <-- Tableau Dashboards & Static Charts
│   ├── risk_trend_2024.png
│   └── bronx_vet_desert_map.png
└── 📂 dataset                   <-- Raw & Cleaned Datasets
