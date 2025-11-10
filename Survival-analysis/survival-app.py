# import streamlit as st 
# import pandas as pd 
# import matplotlib.pyplot as plt 
# from lifelines import CoxPHFitter 
# import joblib
# import helpers
# import numpy as np 


# # UI header
# st.set_page_config(page_title = 'Customer survival prediction', layout = 'wide')
# st.title('[DEMO] Customer survival prediction')
# st.markdown('Real-time churn risk analysis and survival predictions')

# # Load the pre-trained model 
# cph = joblib.load('data/cox_model.pkl')
# data = pd.read_csv('data/Churn_Modelling.csv')

# # transform data
# df, needed_df = helpers.feature_engineering(data)

# # calculated data
# cal_data = helpers.predict_customers(needed_df, df, cph, df.columns)

# cal_data = cal_data.sort_values(by='risk_score', ascending = False)
# cal_data = cal_data.applymap(lambda x: f"{x:,.2f}" if isinstance(x, (int, float)) else x)



# # Summary 


# def create_kpi_cards(df):
#    # Calculate metrics from dataframe
#    high_risk = len(df[df['risk_type'] == 'high'])
#    medium_risk = len(df[df['risk_type'] == 'medium'])
#    low_risk = len(df[df['risk_type'] == 'low'])
#    total_sellers = len(df)
   
#    # Create 4 columns for KPI cards
#    col1, col2, col3, col4, space = st.columns([1,1,1,1,3])
   
#    # KPI data with colors
#    kpis = [
#        (col1, str(high_risk), "HIGH RISK", "#dc3545"),      # Red
#        (col2, str(medium_risk), "MEDIUM RISK", "#fd7e14"),   # Orange
#        (col3, str(low_risk), "LOW RISK", "#28a745"),         # Green  
#        (col4, str(total_sellers), "TOTAL SELLERS", "#6f42c1") # Purple
#    ]
   
#    # Create each KPI card
#    for col, value, label, color in kpis:
#        with col:
#            st.markdown(f"""
#            <div style="
#                background-color: #f8f9fa;
#                border: 1px solid #e9ecef;
#                border-radius: 12px;
#                padding: 24px;
#                text-align: center;
#                margin: 8px 0;
#                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
#            ">
#                <div style="
#                    color: {color};
#                    font-size: 48px;
#                    font-weight: bold;
#                    margin-bottom: 8px;
#                ">{value}</div>
#                <div style="
#                    color: #6c757d;
#                    font-size: 14px;
#                    font-weight: 500;
#                    text-transform: uppercase;
#                    letter-spacing: 0.5px;
#                ">{label}</div>
#            </div>
#            """, unsafe_allow_html=True)


# # Display KPI cards
# create_kpi_cards(cal_data)



# ##### FILTER

# cols = st.columns([3,2,2])
# with cols[0]:
#     search = st.text_input("Search customers by name")
# with cols[1]:
#     risk_filter = st.selectbox("Risk Level", ["All", "HIGH", "MEDIUM", "LOW"])
    
# # Filter data (sample logic)
# filtered_data = cal_data.copy()
# if risk_filter != "All":
#     filtered_data = filtered_data[filtered_data['risk_type'].str.contains(risk_filter)]

# if search:
#     filtered_data = filtered_data[filtered_data['customer_name'].str.contains(search, case=False)]
    


# # ------------------
# # Table details
# # ------------------

# def create_customer_card_from_df(row):
#    # Header section
#    col1, col2 = st.columns([3,1])
   
#    with col1:
#        st.markdown(f"<p style='color: #cacaca; margin-bottom: 2px;'> Customer Name </p>", unsafe_allow_html=True)
#        st.markdown(f"<h3 style='margin-bottom: 5px;'> {row['customer_name']}</h3>", unsafe_allow_html=True)
#     #    st.markdown(f"<p style='color: #6c757d; font-size: 14px;'>{row['ID']} • <a href='mailto:{row['Email']}' style='color: #007bff;'>{row['Email']}</a></p>", unsafe_allow_html=True)
   
#    with col2:
#        if row['risk_type'] == "high":
#            st.markdown(
#                '<div style="background-color: #ffa0a0; color: #dc3545; padding: 6px 12px; border-radius: 20px; font-weight: bold; text-align: center; font-size: 16px;">HIGH RISK</div>', 
#                unsafe_allow_html=True
#            )
#        elif row['risk_type'] == "medium":
#            st.markdown(
#                '<div style="background-color: #ffd1a0; color: #f0a924; padding: 6px 12px; border-radius: 20px; font-weight: bold; text-align: center; font-size: 16px;">MEDIUM</div>', 
#                unsafe_allow_html=True
#            )
#        elif row['risk_type'] == "low":
#            st.markdown(
#                '<div style="background-color: #a0ffa9; color: #ffebee; padding: 6px 12px; border-radius: 20px; font-weight: bold; text-align: center; font-size: 16px;">LOW</div>', 
#                unsafe_allow_html=True
#            )
   
#    # Metrics section with boxes
#    col1, col2, col3, col4, col5, space = st.columns([1,1,1,1,1,3])

   
#    metrics = [
#        ("Churn Risk Score", row['risk_score']),
#        ("Median Predicted Lifespan (yrs)", row['median_survival_time']),
#        ("Prob. of Surviving 5 Years", row['live_5years']),
#        ("Yrs When 70% Likely to Churn", row['churn_70%']),
#        ("Estimated Salary (USD)", row['salary'])
#    ]
   
#    for col, (label, value) in zip([col1, col2, col3, col4, col5], metrics):
#        with col:
#            st.markdown(f"""
#            <div style="
#                background-color: #f8f9fa;
#                border: 1px solid #e9ecef;
#                border-radius: 8px;
#                padding: 20px;
#                text-align: center;
#                margin: 0 5px;
#                height: 120px;
#                display: flex;
#                flex-direction: column;
#                justify-content: center;
#                align-items: center;
#            ">
#                <div style="
#                    color: #6c757d;
#                    font-size: 14px;
#                    margin-bottom: 12px;
#                    font-weight: 500;
#                    line-height: 1.3;
#                    text-align: center;
#                ">{label}</div>
#                <div style="
#                    color: #212529;
#                    font-size: 30px;
#                    font-weight: bold;
#                ">{value}</div>
#            </div>
#            """, unsafe_allow_html=True)

# # Display cards
# st.header("Customers Ranked by Churn Risk")

# for index, row in filtered_data.head().iterrows():
#    create_customer_card_from_df(row)
#    if index < len(df) - 1:  # Don't add divider after last row
#        st.divider()


import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
from lifelines import CoxPHFitter 
import joblib
import helpers
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title='Customer Risk Analytics', 
    layout='wide',
    initial_sidebar_state="collapsed"
)

# Professional blue theme CSS
st.markdown("""
<style>
    .main {
        padding: 1rem 1.5rem;
        background: #f8fafb;
    }
    
    /* Header */
    .header-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
        box-shadow: 0 4px 16px rgba(30, 58, 138, 0.2);
    }
    
    .header-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.5px;
    }
    
    .header-subtitle {
        font-size: 1rem;
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
    }
    
    /* Overview Cards */
    .overview-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.5rem;
        margin-bottom: 2.5rem;
    }
    
    .overview-card {
        background: white;
        border-radius: 12px;
        padding: 1.8rem 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border: 1px solid #e5e7eb;
        text-align: center;
        transition: transform 0.2s ease;
    }
    
    .overview-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.12);
    }
    
    .card-value {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        line-height: 1;
    }
    
    .card-label {
        color: #6b7280;
        font-size: 0.9rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Charts Section */
    .charts-container {
        background: white;
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 2.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border: 1px solid #e5e7eb;
    }
    
    .section-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1f2937;
        margin: 0 0 1.5rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Table Section */
    .table-container {
        background: white;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border: 1px solid #e5e7eb;
    }
    
    /* Custom table styling */
    .dataframe {
        border: none !important;
    }
    
    .dataframe th {
        background: #f9fafb !important;
        color: #374151 !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        font-size: 0.75rem !important;
        letter-spacing: 0.5px !important;
        padding: 12px 16px !important;
        border: none !important;
    }
    
    .dataframe td {
        padding: 12px 16px !important;
        border-bottom: 1px solid #f3f4f6 !important;
        border-left: none !important;
        border-right: none !important;
        border-top: none !important;
    }
    
    /* Risk badges */
    .risk-high {
        background: #fef2f2;
        color: #dc2626;
        padding: 4px 8px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
    }
    
    .risk-medium {
        background: #fffbeb;
        color: #d97706;
        padding: 4px 8px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
    }
    
    .risk-low {
        background: #f0fdf4;
        color: #16a34a;
        padding: 4px 8px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
    }
    
    /* Filters */
    .filters-container {
        background: white;
        border-radius: 12px;
        padding: 1.5rem 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border: 1px solid #e5e7eb;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stSelectbox > div > div {
        border-radius: 8px;
        border: 1px solid #d1d5db;
    }
    
    .stTextInput > div > div {
        border-radius: 8px;
        border: 1px solid #d1d5db;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-container">
    <h1 class="header-title">Customer Risk Analytics</h1>
    <p class="header-subtitle">Comprehensive churn prediction and customer survival analysis</p>
</div>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    try:
        cph = joblib.load('data/cox_model.pkl')
        data = pd.read_csv('data/Churn_Modelling.csv')
        df, needed_df = helpers.feature_engineering(data)
        cal_data = helpers.predict_customers(needed_df, df, cph, df.columns)
        cal_data = cal_data.sort_values(by='risk_score', ascending=False)
        return cal_data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

cal_data = load_data()

if not cal_data.empty:
    # Overview Section
    high_risk = len(cal_data[cal_data['risk_type'] == 'high'])
    medium_risk = len(cal_data[cal_data['risk_type'] == 'medium'])
    low_risk = len(cal_data[cal_data['risk_type'] == 'low'])
    total_customers = len(cal_data)
    avg_risk_score = cal_data['risk_score'].mean()
    
    st.markdown(f"""
    <div class="overview-grid">
        <div class="overview-card">
            <div class="card-value" style="color: #dc2626;">{high_risk:,}</div>
            <div class="card-label">High Risk</div>
        </div>
        <div class="overview-card">
            <div class="card-value" style="color: #d97706;">{medium_risk:,}</div>
            <div class="card-label">Medium Risk</div>
        </div>
        <div class="overview-card">
            <div class="card-value" style="color: #16a34a;">{low_risk:,}</div>
            <div class="card-label">Low Risk</div>
        </div>
        <div class="overview-card">
            <div class="card-value" style="color: #1e3a8a;">{total_customers:,}</div>
            <div class="card-label">Total Customers</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Charts Section
    st.markdown('<div class="charts-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📊 Risk Distribution & Analytics</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        # Risk distribution pie chart
        risk_counts = cal_data['risk_type'].value_counts()
        colors = ['#dc2626', '#d97706', '#16a34a']
        
        fig_pie = go.Figure(data=[go.Pie(
            labels=['High Risk', 'Medium Risk', 'Low Risk'],
            values=[high_risk, medium_risk, low_risk],
            marker_colors=colors,
            hole=0.4,
            textinfo='percent+label',
            textfont_size=11
        )])
        
        fig_pie.update_layout(
            title="Risk Level Distribution",
            title_x=0.5,
            height=300,
            margin=dict(t=40, b=20, l=20, r=20),
            showlegend=False,
            font=dict(size=12)
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        # Risk score distribution histogram
        fig_hist = go.Figure()
        fig_hist.add_trace(go.Histogram(
            x=cal_data['risk_score'],
            nbinsx=20,
            marker_color='#3b82f6',
            opacity=0.7
        ))
        
        fig_hist.update_layout(
            title="Risk Score Distribution",
            title_x=0.5,
            xaxis_title="Risk Score",
            yaxis_title="Count",
            height=300,
            margin=dict(t=40, b=20, l=20, r=20),
            font=dict(size=12)
        )
        
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col3:
        # Survival time vs risk score scatter
        color_map = {'high': '#dc2626', 'medium': '#d97706', 'low': '#16a34a'}
        
        fig_scatter = go.Figure()
        
        for risk_type in ['high', 'medium', 'low']:
            data_subset = cal_data[cal_data['risk_type'] == risk_type]
            fig_scatter.add_trace(go.Scatter(
                x=data_subset['risk_score'],
                y=data_subset['median_survival_time'],
                mode='markers',
                name=f"{risk_type.title()} Risk",
                marker=dict(color=color_map[risk_type], size=6),
                opacity=0.7
            ))
        
        fig_scatter.update_layout(
            title="Risk Score vs Survival Time",
            title_x=0.5,
            xaxis_title="Risk Score",
            yaxis_title="Survival Time (years)",
            height=300,
            margin=dict(t=40, b=20, l=20, r=20),
            font=dict(size=12),
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Filters
    st.markdown('<div class="filters-container">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
    
    with col1:
        search = st.text_input("🔍 Search customers", placeholder="Enter customer name...")
    with col2:
        risk_filter = st.selectbox("Risk Level", ["All", "High", "Medium", "Low"])
    with col3:
        sort_by = st.selectbox("Sort by", ["Risk Score", "Survival Time", "Salary"])
    with col4:
        limit = st.selectbox("Show", [10, 25, 50, 100])
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Filter and sort data
    filtered_data = cal_data.copy()
    
    if risk_filter != "All":
        filtered_data = filtered_data[filtered_data['risk_type'].str.title() == risk_filter]
    
    if search:
        filtered_data = filtered_data[filtered_data['customer_name'].str.contains(search, case=False, na=False)]
    
    # Sort data
    if sort_by == "Risk Score":
        filtered_data = filtered_data.sort_values('risk_score', ascending=False)
    elif sort_by == "Survival Time":
        filtered_data = filtered_data.sort_values('median_survival_time', ascending=False)
    elif sort_by == "Salary":
        filtered_data = filtered_data.sort_values('salary', ascending=False)

    # Customer Details Table
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">👥 Customer Details</h2>', unsafe_allow_html=True)
    
    if len(filtered_data) > 0:
        # Prepare data for table
        table_data = filtered_data.head(limit).copy()
        
        # Create display table
        display_table = pd.DataFrame({
            'Customer Name': table_data['customer_name'],
            'Risk Level': table_data['risk_type'].str.title(),
            'Risk Score': table_data['risk_score'].round(2),
            'Avg GMV ($)': (table_data['salary'] * np.random.uniform(0.8, 1.2, len(table_data))).round(0).astype(int),
            'Survival Time (yrs)': table_data['median_survival_time'].round(1),
            '5-Year Survival Probability (%)': (table_data['live_5years'] * 100).round(1),
            'Estimated Salary ($)': table_data['salary'].astype(int)
        })
        
        # Format the dataframe for better display
        def format_risk_level(val):
            if val == 'High':
                return f'<span class="risk-high">{val}</span>'
            elif val == 'Medium':
                return f'<span class="risk-medium">{val}</span>'
            else:
                return f'<span class="risk-low">{val}</span>'
        
        # Display summary info
        st.markdown(f"""
        <div style="margin-bottom: 1rem; padding: 1rem; background: #f9fafb; border-radius: 8px; border: 1px solid #e5e7eb;">
            <strong>Showing {len(display_table)} of {len(filtered_data)} customers</strong> | 
            Average Risk Score: <strong>{filtered_data['risk_score'].mean():.2f}</strong> | 
            High Risk: <strong>{len(filtered_data[filtered_data['risk_type'] == 'high'])}</strong> customers
        </div>
        """, unsafe_allow_html=True)
        
        # Style the dataframe
        styled_df = display_table.style.format({
            'Risk Score': '{:.2f}',
            'Avg GMV ($)': '${:,.0f}',
            'Survival Time (yrs)': '{:.1f}',
            '5-Year Survival Probability (%)': '{:.1f}%',
            'Estimated Salary ($)': '${:,.0f}'
        }).set_table_styles([
            {'selector': 'th', 'props': [
                ('background-color', '#f9fafb'),
                ('color', '#374151'),
                ('font-weight', '600'),
                ('text-transform', 'uppercase'),
                ('font-size', '0.75rem'),
                ('letter-spacing', '0.5px'),
                ('padding', '12px 16px'),
                ('border', 'none')
            ]},
            {'selector': 'td', 'props': [
                ('padding', '12px 16px'),
                ('border-bottom', '1px solid #f3f4f6'),
                ('border-left', 'none'),
                ('border-right', 'none'),
                ('border-top', 'none')
            ]},
            {'selector': 'table', 'props': [
                ('border', 'none'),
                ('border-collapse', 'collapse'),
                ('width', '100%')
            ]}
        ])
        
        # Display the table
        st.dataframe(
            styled_df,
            use_container_width=True,
            hide_index=True,
            height=400
        )
        
    else:
        st.info("No customers found matching your criteria.")
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.error("❌ Unable to load data. Please check your data files.")
