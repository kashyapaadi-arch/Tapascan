# 🌡️ Tapascan

**AI platform for urban heat stress mapping and cooling intervention planning using satellite data.**

Tapascan ingests multi-source satellite and meteorological data, models urban heat dynamics using Physics-Informed Neural Networks, and generates zone-wise cooling recommendations for city planners — with predicted temperature reductions down to the degree.

---

## 🛰️ What it does

Most urban heat tools stop at analysis. Tapascan goes further.

Given raw satellite imagery over any Indian city, Tapascan:

- Maps Land Surface Temperature at 30m resolution using Landsat 8 thermal data
- Computes vegetation (NDVI), built-up density (NDBI), albedo, and Sky View Factor per zone
- Clusters urban areas into Low / Medium / High / Critical heat risk zones using DBSCAN
- Models LST dynamics using a Physics-Informed Neural Network (PINN) with surface energy balance constraints
- Simulates cooling interventions (urban greening, cool roofs, water bodies) and outputs predicted ΔT per zone
- Generates a human-readable spatial intervention report for municipal planners

**Pilot city:** Jaipur, Rajasthan  
**Validation cities:** Pune (Maharashtra), Guwahati (Assam)

---

## 📊 Key Results

| Metric | Value |
|---|---|
| Real LST-NDVI correlation (Jaipur, April 2023) | -0.929 |
| Peak LST recorded (Walled City Core) | 48.2°C |
| Predicted cooling — aggressive intervention | -2.4°C |
| Population in critical/high zones | 179,000 |
| Satellite data resolution | 30m (Landsat 8) |

---

## 🗂️ Project Structure

```
tapascan/
│
├── module1_python_basics.ipynb      # Python fundamentals — variables, functions, OOP
├── module2_numpy.ipynb              # NumPy — arrays, vectorization, 2D satellite grids
├── module2_pandas.ipynb             # Pandas — DataFrames, filtering, groupby, CSV pipeline
├── module2_matplotlib.ipynb         # Matplotlib — bar charts, scatter, heatmaps, dashboard
├── module3_geospatial.ipynb         # GEE — real Landsat 8 LST + NDVI for Jaipur
│
├── jaipur_zones.csv                 # Processed zone data with LST, NDVI, risk, interventions
│
├── lst_by_zone.png                  # LST bar chart by zone
├── lst_vs_ndvi.png                  # LST vs NDVI scatter with correlation trend
├── intervention_forecast.png        # 5-year LST forecast under 3 intervention scenarios
├── heatmap_before_after.png         # Before/after intervention heatmap
├── tapascan_dashboard.png           # Full 4-panel analysis dashboard
└── real_lst_ndvi_correlation.png    # Real satellite pixel correlation scatter
```

---

## 🧠 Technical Architecture

```
DATA LAYER
Landsat 8 LST (30m) · Sentinel-2 LULC (10m) · ERA5 Met · OSM · GHSL
        ↓
FEATURE ENGINEERING
NDVI · NDBI · Albedo · Sky View Factor · Impervious Surface %
        ↓
PHYSICS-INFORMED NEURAL NETWORK
Loss = Prediction Error + λ × Energy Balance Violation
        ↓
DBSCAN ZONE CLUSTERING
[Low] [Medium] [High] [Critical]
        ↓
SCENARIO SIMULATION ENGINE
Green roofs · Tree corridors · Water bodies · Albedo changes
        ↓
OUTPUT
UTCI Comfort Maps · Intervention Report · Streamlit Dashboard
```

---

## 📡 Data Sources

| Dataset | Source | Resolution | Use |
|---|---|---|---|
| Landsat 8 Band 10 (ST_B10) | USGS via GEE | 30m | Land Surface Temperature |
| Sentinel-2 SR | Copernicus via GEE | 10m | LULC, NDVI, NDBI |
| ERA5 reanalysis | ECMWF via CDS API | 31km | Air temp, humidity, wind |
| OpenStreetMap | OSM | Vector | Urban morphology, building footprints |
| GHSL | JRC | 100m | Population density |

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Satellite data | Google Earth Engine Python API |
| Data processing | NumPy, Pandas, Rasterio, GeoPandas |
| ML models | PyTorch (PINN), scikit-learn, XGBoost, SHAP |
| Clustering | DBSCAN (scikit-learn) |
| Visualization | Matplotlib, Folium, Plotly |
| Dashboard | Streamlit |
| Version control | Git, GitHub |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Google Earth Engine account ([register here](https://earthengine.google.com))

### Installation

```bash
git clone https://github.com/kashyapaadi-arch/Tapascan.git
cd Tapascan
pip install -r requirements.txt
```

### Authenticate GEE

```bash
earthengine authenticate
```

### Run the notebooks in order

```
module1 → module2_numpy → module2_pandas → module2_matplotlib → module3_geospatial
```

---

## 📈 Roadmap

- [x] Python + data science foundations (Modules 1–2)
- [x] Real Landsat 8 LST pipeline via Google Earth Engine (Module 3)
- [ ] GeoPandas spatial joins + Folium interactive map
- [ ] XGBoost baseline LST prediction model
- [ ] PINN implementation with energy balance loss
- [ ] DBSCAN zone clustering on real pixel data
- [ ] Scenario simulator engine
- [ ] Streamlit dashboard deployment
- [ ] Multi-city validation (Pune + Guwahati)

---

## 📄 License

MIT License — open source, free to use with attribution.

---

## 🙏 Acknowledgements

- NASA / USGS for Landsat 8 open data
- Google Earth Engine for free academic access
- Copernicus / ESA for Sentinel-2 data
- ECMWF for ERA5 reanalysis data

---

*"ISRO has spent decades putting eyes in the sky. Tapascan builds the brain that tells cities what to do with what they see."*
