# <span style="color:#ffffff; font-size: 1%;"> Introduction </span>

<div style=" border-bottom: 8px solid #9CBDFF; overflow: hidden; border-radius: 10px; height: 45px; width: 100%; display: flex;">
  <div style="height: 100%; width: 75%; background-color: #4b70c0; float: left; text-align: center; display: flex; justify-content: center; align-items: center; font-size: 25px; ">
    <b><span style="color: #ffffff; padding: 20px 20px;"> 📊 Why Did NHS Waiting Times Increase After Covid?   </span></b>
  </div>
  <div style="height: 100%; width: 25%; background-image: url('https://peopleshistorynhs.org/wp-content/uploads/2016/01/nhs-logo-880x4951.jpeg'); background-size: cover; background-position: center; float: left; border-top-right-radius: 10px; border-bottom-right-radius: 4px;">
  </div>
</div>

# 
This project investigates **why NHS waiting times have risen in England since the Covid-19 pandemic**, combining causal inference, time series methods, and survival analysis.  

![alt text](image-2.png)
---

## 🎯 Research Questions  
1. **What factors caused NHS waiting times to rise?**  
   - Causal discovery & root cause analysis.  
   - Interrupted Time Series (Covid shock).  
   - Difference-in-Differences (DiD) across NHS Trusts with different funding levels.  

2. **If workforce supply increases, will waiting times fall?**  
   - Workforce elasticity analysis.  
   - Counterfactual simulation.  

3. **What does the future look like?**  
   - Forecasting NHS waiting times.  
   - Survival analysis of “time-to-treatment.”  

---

## 🗂 Data Sources  
- **NHS England RTT Waiting Times** (monthly, provider & commissioner level). [\[link\]](https://www.england.nhs.uk/statistics/statistical-work-areas/rtt-waiting-times/?)
- **NHS Workforce Statistics** (monthly headcount, FTE, vacancies).  
- **UK Government / DHSC Funding** (yearly budgets & expenditure).  
- **ONS Population Estimates & Projections** (aging demand).  

---

## 🔎 Methods  

### 1. Causal Analysis  
- **Causal discovery**: Identify potential drivers (Covid shock, staffing shortages, funding gap, aging demand).  
- **Root cause analysis**: Map system bottlenecks (A&E delays → elective backlog).  
- **Intrinsic causal analysis**: Quantify the contribution of workforce vs demand vs funding.  

### 2. Interrupted Time Series (ITS)  
- Modelled the Covid shock (March 2020) as an interruption to England-level waiting times.  
- Estimate: backlog grew significantly faster post-2020 compared to pre-trend.  

### 3. Difference-in-Differences (DiD)  
- Treatment = Trusts receiving higher funding growth.  
- Control = Trusts with lower funding growth.  
- Finding: higher-funded trusts experienced **smaller increases in waiting times**, suggesting funding mitigated some backlog growth.  

### 4. Workforce Counterfactual  
- Regression linking workforce FTE per 1000 patients → waiting times.  
- Simulation: a **10% workforce increase** could reduce long-wait patients (>18 weeks) by **~6–8%**.  

### 5. Forecasting  
- Time series forecasting (ARIMA/Prophet).  
- Projection: without major workforce/funding interventions, waiting times remain **well above pre-Covid baseline until at least 2030**.  

### 6. Survival Analysis (Time-to-Treatment)  
- Kaplan–Meier curves: probability of still waiting after X weeks.  
- Cox proportional hazards model:  
  - Post-Covid patients have **~40% lower hazard of treatment per week** (slower throughput).  
  - Workforce shortages significantly reduce treatment hazard rates.  

---

## 📈 Key Results  

- **Covid shock** created a massive elective backlog (ITS).  
- **Staff shortages** and **limited funding** are root causes prolonging waits (causal analysis).  
- **Trusts with higher funding** fared better post-Covid (DiD).  
- **Workforce expansion** would meaningfully reduce waiting times (counterfactual).  
- **Forecasts** suggest backlog will persist for the next 5–10 years under current conditions.  
- **Survival analysis** confirms patients wait substantially longer post-Covid.  

---

## 📝 Conclusion  

NHS waiting times rose after Covid because of a **compound effect**:  
- Covid backlog (shock).  
- Growing demand from an aging population.  
- Workforce shortages (vacancies, burnout, Brexit).  
- Funding not keeping pace with demand and costs.  

👉 **Policy implication**: Scaling workforce capacity and targeted funding are the most effective levers to reduce waiting times.  

---

## 📂 Deliverables  

- **Jupyter Notebooks**: data wrangling, ITS, DiD, survival analysis.  
- **Charts & Dashboards**: backlog trends, regional variation, causal effects.  
- **Report (PDF/Markdown)**: full narrative + visuals.  
- **Portfolio site summary**: one-page insights.  

---

🔗 *This project demonstrates advanced data science methods (causal inference, ITS, DiD, survival analysis) applied to a real-world healthcare policy question.*  
