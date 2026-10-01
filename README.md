🌡️ Tapascan

AI platform for urban heat stress mapping and cooling intervention planning using satellite data.

Live Demo GitHub Python

🚀 Live Demo

tapascan-urban-heat.streamlit.app

Tapascan is a fully deployed web application that maps urban heat stress using real Landsat 8 satellite data and generates zone-wise cooling recommendations for city planners.

🛰️ What it does

Most urban heat tools stop at analysis. Tapascan goes further.

Given raw satellite imagery over any Indian city, Tapascan:

Maps Land Surface Temperature at 30m resolution using Landsat 8 thermal data
Computes vegetation (NDVI), built-up density (NDBI), albedo, and water index (MNDWI) per pixel
Clusters urban areas into Low / Medium / High / Critical heat risk zones
Models LST dynamics using a Physics-Informed Neural Network (PINN) with surface energy balance constraints
Simulates cooling interventions (urban greening, cool roofs, water bodies) and outputs predicted ΔT
Generates intervention recommendations per zone based on SHAP feature importance

Pilot city: Jaipur, Rajasthan
Validation cities: Pune (Maharashtra), Guwahati (Assam)

📊 Key Results
Metric	Value
Real LST-NDVI correlation (Jaipur urban core)	r = -0.872
Peak LST recorded	39.0°C (June 2023)
Mean LST — Jaipur urban core	35.8°C
Random Forest R² on real satellite data	0.397
Random Forest RMSE	1.071°C
PINN R²	0.324
Zone classification accuracy	76.6%
Real satellite pixels in training data	107
NDVI contribution to LST (SHAP)	35.1%
🗂️ Project Structure
tapascan/
│
├── app.py                           # Streamlit dashboard — live deployment
│
├── module1_python_basics.ipynb      # Python fundamentals
├── module2_numpy.ipynb              # NumPy — arrays, vectorization
├── module2_pandas.ipynb             # Pandas — DataFrames, CSV pipeline
├── module2_matplotlib.ipynb         # Matplotlib — charts and dashboard
├── module3_geospatial.ipynb         # GEE — real Landsat 8 LST + NDVI
├── module3_geospatial_colab.ipynb   # GEE on Colab — LST-NDVI correlation
├── module4_ml_models               # ML models + SHAP (Colab)
├── module5_pytorch_pinn            # PyTorch + PINN (Colab)
│
├── jaipur_features.csv              # Real satellite feature matrix (107 pixels)
├── jaipur_ml_output.csv             # ML predictions + zone classifications
├── jaipur_pinn_output.csv           # PINN predictions + residuals
├── jaipur_zones.csv                 # Processed zone data
│
├── lst_by_zone.png                  # LST bar chart
├── lst_vs_ndvi.png                  # LST vs NDVI scatter
├── intervention_forecast.png        # 5-year forecast under 3 scenarios
├── heatmap_before_after.png         # Before/after intervention heatmap
├── tapascan_dashboard.png           # Full 4-panel dashboard
└── real_lst_ndvi_correlation.png    # Real pixel correlation scatter
🧠 Technical Architecture
DATA LAYER
Landsat 8 LST (30m) · Sentinel-2 LULC (10m) · ERA5 Met · OSM · GHSL
        ↓
FEATURE ENGINEERING
NDVI · NDBI · MNDWI · Albedo · Sky View Factor
        ↓
ML MODELS
Linear Regression (baseline) · Random Forest · XGBoost · SHAP
        ↓
PHYSICS-INFORMED NEURAL NETWORK
Loss = MSE + λ × Energy Balance Violation
        ↓
ZONE CLUSTERING
[Low] [Medium] [High] [Critical]
        ↓
SCENARIO SIMULATION ENGINE
Tree corridors · Cool roofs · Water bodies · Albedo changes
        ↓
STREAMLIT DASHBOARD
Live at tapascan-urban-heat.streamlit.app
📡 Data Sources
Dataset	Source	Resolution	Use
Landsat 8 Band 10 (ST_B10)	USGS via GEE	30m	Land Surface Temperature
Sentinel-2 SR	Copernicus via GEE	10m	LULC, NDVI, NDBI
ERA5 reanalysis	ECMWF via CDS API	31km	Air temp, humidity, wind
OpenStreetMap	OSM	Vector	Urban morphology
GHSL	JRC	100m	Population density
🤖 Model Results
Model	R²	RMSE	Notes
Linear Regression	0.327	1.132°C	Baseline
XGBoost	0.360	1.104°C	Needs more data
Random Forest	0.397	1.071°C	Best performer
PINN (PyTorch)	0.324	1.134°C	Physics-constrained

SHAP Feature Importance:

Feature	Mean |SHAP|	Interpretation
NDVI	0.351	Vegetation — plant trees first
MNDWI	0.171	Water bodies — second priority
NDBI	0.166	Built-up density — cool roofs
Albedo	0.076	Surface reflectivity
🛠️ Tech Stack
Category	Tools
Satellite data	Google Earth Engine Python API
Data processing	NumPy, Pandas, Rasterio, GeoPandas
ML models	scikit-learn, XGBoost, SHAP
Deep learning	PyTorch (PINN with energy balance loss)
Visualization	Matplotlib, Folium, Plotly
Dashboard	Streamlit
Version control	Git, GitHub
🚀 Getting Started
Prerequisites
Python 3.11+
Google Earth Engine account (register here)
Installation
bash
git clone https://github.com/kashyapaadi-arch/Tapascan.git
cd Tapascan
pip install -r requirements.txt
Run locally
bash
streamlit run app.py

Opens at localhost:8501

Authenticate GEE (for satellite data notebooks)
bash
earthengine authenticate
📈 Roadmap
 Python + data science foundations (Modules 1–2)
 Real Landsat 8 LST pipeline via Google Earth Engine (Module 3)
 ML models — Random Forest, XGBoost, SHAP (Module 4)
 Physics-Informed Neural Network — PyTorch (Module 5)
 Streamlit dashboard — deployed live (Module 6)
 GeoPandas spatial joins + Folium interactive map
 DBSCAN zone clustering on real pixel data
 Multi-city validation (Pune + Guwahati)
 UTCI thermal comfort index integration
 Real-time heatwave alert system
📄 License

MIT License — open source, free to use with attribution.

🙏 Acknowledgements
NASA / USGS for Landsat 8 open data
Google Earth Engine for free academic access
Copernicus / ESA for Sentinel-2 data
ECMWF for ERA5 reanalysis data
ISRO Bharatiya Antariksh Hackathon 2026 — original inspiration
*"ISRO has spent decades putting eyes in the sky. Tapascan builds the brain that tells cities what to do with what they see."*
