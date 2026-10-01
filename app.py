import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Page config
st.set_page_config(
    page_title="Tapascan",
    page_icon="🌡️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main { background-color: #0A0F1E; }
    .block-container { padding-top: 1rem; }
    h1 { color: #F97316; }
    h2, h3 { color: #F1F5F9; }
    .metric-card {
        background: #111827;
        border: 0.5px solid #1E293B;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('jaipur_ml_output.csv')
    return df

df = load_data()

# Header
st.title("🌡️ Tapascan")
st.markdown("**AI platform for urban heat stress mapping — Jaipur pilot**")
st.markdown("---")

# Stat bar
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Peak LST", f"{df['LST'].max():.1f}°C", "Critical")
with col2:
    st.metric("Mean LST", f"{df['LST'].mean():.1f}°C")
with col3:
    st.metric("Min LST", f"{df['LST'].min():.1f}°C", "Coolest zone")
with col4:
    st.metric("Total Pixels", f"{len(df)}", "Real satellite data")

st.markdown("---")

# Two column layout
left, right = st.columns([1.2, 1])

with left:
    st.subheader("📊 LST Distribution by Zone")

    # Color by risk
    def get_color(lst):
        if lst >= 38: return '#EF4444'
        elif lst >= 36: return '#F97316'
        elif lst >= 34: return '#EAB308'
        else: return '#22C55E'

    colors = [get_color(l) for l in df['LST']]

    fig, ax = plt.subplots(figsize=(8, 4))
    fig.patch.set_facecolor('#111827')
    ax.set_facecolor('#111827')
    ax.hist(df['LST'], bins=20, color='#F97316',
            edgecolor='#0A0F1E', alpha=0.85)
    ax.set_xlabel("Land Surface Temperature (°C)",
                  color='#94A3B8')
    ax.set_ylabel("Pixel count", color='#94A3B8')
    ax.set_title("LST Distribution — Jaipur Urban Core",
                 color='#F1F5F9', fontweight='bold')
    ax.tick_params(colors='#94A3B8')
    for spine in ax.spines.values():
        spine.set_edgecolor('#1E293B')
    st.pyplot(fig)

    st.subheader("🌿 LST vs NDVI Correlation")
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    fig2.patch.set_facecolor('#111827')
    ax2.set_facecolor('#111827')
    ax2.scatter(df['NDVI'], df['LST'],
                alpha=0.6, color='#F97316',
                edgecolors='white', linewidth=0.5, s=40)
    z = np.polyfit(df['NDVI'], df['LST'], 1)
    p = np.poly1d(z)
    x_line = np.linspace(df['NDVI'].min(),
                         df['NDVI'].max(), 100)
    corr = df['LST'].corr(df['NDVI'])
    ax2.plot(x_line, p(x_line), 'white',
             linewidth=2, label=f'r = {corr:.3f}')
    ax2.set_xlabel("NDVI", color='#94A3B8')
    ax2.set_ylabel("LST (°C)", color='#94A3B8')
    ax2.set_title("LST vs Vegetation Index",
                  color='#F1F5F9', fontweight='bold')
    ax2.tick_params(colors='#94A3B8')
    ax2.legend(facecolor='#1E293B',
               labelcolor='#F1F5F9')
    for spine in ax2.spines.values():
        spine.set_edgecolor('#1E293B')
    st.pyplot(fig2)

with right:
    st.subheader("🎯 Scenario Simulator")
    st.markdown("Adjust interventions to see predicted cooling")

    tree = st.slider("🌳 Tree canopy coverage (%)", 0, 100, 45)
    roof = st.slider("🏠 Cool roof adoption (%)", 0, 100, 25)
    water = st.slider("💧 Water body area (ha)", 0.0, 5.0, 0.3)

    cooling = (tree * 0.022) + (roof * 0.014) + (water * 0.4)

    st.markdown("---")
    st.markdown(f"""
    <div style='background:#0D1424;border:1px solid #1E293B;
    border-radius:10px;padding:20px;text-align:center'>
        <div style='font-size:48px;font-weight:500;
        color:#F97316'>-{cooling:.1f}°C</div>
        <div style='color:#94A3B8;margin-top:8px'>
        predicted cooling · urban core</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📋 Zone Risk Table")

    def classify(lst):
        if lst >= 38: return '🔴 CRITICAL'
        elif lst >= 36: return '🟠 HIGH'
        elif lst >= 34: return '🟡 MEDIUM'
        else: return '🟢 LOW'

    df['Risk'] = df['LST'].apply(classify)
    df['LST_rounded'] = df['LST'].round(2)
    df['NDVI_rounded'] = df['NDVI'].round(3)

    st.dataframe(
        df[['LST_rounded', 'NDVI_rounded',
            'Risk', 'recommendation']] \
          .rename(columns={
              'LST_rounded': 'LST (°C)',
              'NDVI_rounded': 'NDVI',
              'recommendation': 'Intervention'
          }),
        height=300,
        use_container_width=True
    )

st.markdown("---")

# Feature importance
st.subheader("🧠 SHAP Feature Importance")
feat_col1, feat_col2 = st.columns(2)

with feat_col1:
    features = ['NDVI', 'MNDWI', 'NDBI', 'Albedo']
    shap_vals = [0.351, 0.171, 0.166, 0.076]
    colors_shap = ['#22C55E', '#38BDF8',
                   '#EF4444', '#F97316']

    fig3, ax3 = plt.subplots(figsize=(6, 3))
    fig3.patch.set_facecolor('#111827')
    ax3.set_facecolor('#111827')
    bars = ax3.barh(features, shap_vals,
                    color=colors_shap)
    for bar, val in zip(bars, shap_vals):
        ax3.text(bar.get_width() + 0.005,
                 bar.get_y() + bar.get_height()/2,
                 f'{val:.3f}', va='center',
                 color='#F1F5F9', fontsize=10)
    ax3.set_xlabel("Mean |SHAP value|",
                   color='#94A3B8')
    ax3.set_title("What drives urban heat?",
                  color='#F1F5F9', fontweight='bold')
    ax3.tick_params(colors='#94A3B8')
    for spine in ax3.spines.values():
        spine.set_edgecolor('#1E293B')
    st.pyplot(fig3)

with feat_col2:
    st.markdown("""
    **How to read this:**

    🟢 **NDVI (0.351)** — Vegetation is the strongest
    driver. Low NDVI = high LST. Plant trees first.

    🔵 **MNDWI (0.171)** — Water bodies cool
    surrounding areas. Restore stepwells and lakes.

    🔴 **NDBI (0.166)** — Dense built-up areas
    trap heat. Cool roofs reduce this effect.

    🟠 **Albedo (0.076)** — Surface reflectivity
    has the smallest but still measurable impact.

    ---
    **Intervention priority:**
    1. 🌳 Tree corridors
    2. 💧 Water bodies
    3. 🏠 Cool roofs
    4. 🪞 Reflective surfaces
    """)

st.markdown("---")
st.markdown(
    "Built by **Aditya Kashyap** · "
    "[GitHub](https://github.com/kashyapaadi-arch/Tapascan) · "
    "Real Landsat 8 data · Jaipur 2023",
    unsafe_allow_html=True
)
    