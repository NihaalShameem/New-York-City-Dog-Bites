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
├── 📂 scripts                <-- Python ETL & T-SQL Analysis Scripts
│   ├── 01_data_cleaning.py
│   ├── 02_pareto_hotspots.sql
│   ├── 03_yoy_growth.sql
│   └── ...
├── 📂 visualizations         <-- Tableau Dashboards & Static Charts
│   ├── risk_trend_2024.png
│   └── bronx_vet_desert_map.png
└── 📂 data                   <-- Raw & Cleaned Datasets
```

---

## ⚙️ Data Engineering & Pipeline Architecture
* I built a robsut end-to-end pipeline to transform raw CSV logs into a query optimized SQL database.

### 1. Python ETL (Preprocessing)
Before importing into SQL Server, I engineered a Python (Pandas) script to sanitize the raw dataset.
  * **Noise Reduction:** Removed redundant fields and standardized text using Regex.
  * **Handling Dirty Data:** Built logic to coerce mixed-type Age column and inpute sentinel values (`-1`) for integers.
  ### Code Snippet: Cleaning the 'Age' Column
  ```python
# Remove 'Y', coerce errors to NaN and impute -1 for integer integrity
data['Age'] = pd.to_numeric(
    data['Age'].astype(str).str.replace('Y', '', regex=False),
    errors= 'coerce'
).fillna(-1).astype(int)
```

### 2. SQL Schema Design & Integration 
I designed a strict T-SQL Schema to enforce data quality upon import.
  * **Storage Optimization:** Used `SMALLINT` for Age (vs `INT`) and `VARCHAR` for variable-legnth text to reduce storage footprint.
  * **Data Integrity:** Enforced `NOT NULL` constraints on critical reporting fields (Date,Borough) while allowing `NULL` for naturally missing dimensions. <br>

**Code Snippet: DDL & Optimization**
```sql
CREATE TABLE dbo.incidents (
    DateOfBite DATE NOT NULL,        -- Required for Time-Series
    Breed VARCHAR(100) NOT NULL,     -- Variable length to save space
    Age SMALLINT NOT NULL,           -- Optimized: SMALLINT (2 bytes vs INT (4 bytes)
    ZipCode VARCHAR(5) NULL          -- Allow NULLS for 'unknown' locations
); 
```

---

## 📖 Executive Summary
My analysis revealed that **2024 was the most volatile year on record**, shattering the pre-pandemic baseline. The data suggests this surge is not random, but driven by three systemic factors:

1. A **"Compliance Gap"** in Spay/Neuter rates for specific demographic segments.

2. The **"Pandemic Echo"**, with a wave of under-socialized subjects reaching maturity.

3. **Geographic Inequality**, specifically in veterinary access in The Bronx.

---

## 🔎 Key Strategic Insights & Technical Implementation

**1. The "New Normal" (Smoothing Volatility)** <br>
**The Story:** Operational Leadership felt "overwhelmed" despite flucutualting daily numbers. To seperate signal from noise, I calculated a **7-day Rolling Average**. The data confirmed that our sustained daily baseline 
has permanently shifted from 16 to **17.0 incidents/day** in 2024.

  **Technical Highlight: Window Frames** *I used a sliding window frame to calculate the rolling average specifically for the preceding week.*
  ```sql
AVG(daily_bites) OVER (
    ORDER BY DateOfBite
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
) AS rolling_average
  ```

**2. The Precision Strike Strategy (Pareto Analysis)** <br>
**The Story:** The city spreads its budget too thin. My Pareto Analysis that risk is hyper concentrated: just **53 Zip Codes**  (10% of the city) account for **50% of all incidents**.
* **Recommendation:** Reallocate 50% of the outreach budget to these 53 zones immediately to maximize ROI. <br>

**Technical Highlight: Running Totals** *I calculated the cumulative percentage of incidents per zip code to identify the 50% cutoff point dynamically.*
```sql
WITH hotspot_analysis AS (
    SELECT
      ZipCode,
      COUNT(*) AS incident_cnt,
      SUM(COUNT(*)) OVER (ORDER BY COUNT(*) DESC) AS running_total,
      SUM(COUNT(*)) OVER () AS grand_total
    FROM operations.incidents_cleaned
    WHERE ZipCode != 'Unknown'
    GROUP BY ZipCode
```

**3. The "Rebound" Warning (YoY Growth)** <br>
**The Story:** Incident volume is tied to human density. Incidents dropped **67%** during the 2020 lockdown and spiked **133%** during the 2021 reopening.
* **Recommendation:** Staffing models must treate large public gatherings (reopenings, festivals) as high-risk triggers. <br>

**Technical Highlight: Lag Functions** *Used `LAG()` to look back exactly 12 periods (months) to compare year-over-year performance.*
```sql
LAG(current_count,12) OVER (ORDER BY year,month) AS previous_count
-- Growth Calculation: (current - previous) / previous
```


**4. The Demographic Factor (Gender Aggression Ratio)** <br>
**The Story:** Across top categories, male subjects are **2.5x more likely** to be involved in an incident. Specific breeds (e.g. Shih Tzus) showed a **2.9:1** Male-to-Female ratio.
* **Recommendation:** Prevention campaigns should market "behavioral safety" specifically to owners of male subjects in these categories. <br>

**Technical Highlight: Conditional Aggregation & Pivot** *I used `SUM(CASE WHEN...)` to pivot the data from rows into columns for ratio calculation.*
```sql
SELECT
  Breed,
  CAST(ROUND(1.0* Male_cnt / NULLIF(Female_cnt,0),2) AS DECIMAL(10,2)) AS Gender_Ratio
FROM gender_analysis
WHERE Popularity_Rank <= 5 
```

---

## 🚀 Strategic Recommendations
Based on the data, I propose the following immediate actions for the Operations Team:
1. ✅**Budget Adjustment:** Increase the 2025 overtime budget by **30%** to match the new 192-day "High-Risk" baseline.
2. ✅ **Targeted Prevention:** Restrict free vouchers to **High-Risk Segments** (who have a compliance rate of 11.7%) rather than First-Come-First-Serve.
3. ✅ **The "High Density" Pivot:** Update safety PSAs in high-density housing (Manhattan/Bronx) to feature smaller breeds, educating residents that small dogs pose a legitmate risk in elevators and hallways.

---

## 📩 Contact
* **LinkedIn:** [Nihaal's LinkedIn](https://www.linkedin.com/in/nihaalshameem/)





