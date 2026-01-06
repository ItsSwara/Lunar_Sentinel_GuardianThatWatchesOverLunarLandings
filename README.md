#  🌕Lunar Sentinel - Guardian that watches over lunar landings

Lunar Sentinel is an AI-driven system designed to identify safe lunar landing zones by detecting terrain hazards such as craters, steep slopes, shadowed regions, and surface roughness using satellite imagery and elevation data.
The project leverages Machine Learning, Computer Vision, and Remote Sensing techniques on real lunar datasets from Chandrayaan-2 and LROC missions to compute a Landing Safety Index (LSI) for autonomous landing decision support.
---

## 📌 Motivation

Safe lunar landings require accurate terrain evaluation under extreme conditions.  
Single-source analysis (only imagery or only elevation data) often fails to capture all hazards.

This project addresses that by:
- Fusing **multi-source lunar datasets**
- Automating **crater and hazard detection**
- Producing an interpretable **safety score map** for landing decisions

---

## 🧠 Key Features

- **Multi-source data fusion**
  - Chandrayaan-2 TMC-2 imagery  
  - Digital Elevation Models (DEM)  
  - LROC NAC high-resolution images  

- **Terrain analysis**
  - Slope derivation from DEM  
  - Surface roughness and elevation metrics  
  - Hillshade-based illumination & shadow detection  

- **AI-powered crater detection**
  - YOLOv8 object detection model  
  - Trained on manually annotated lunar crater data  
  - Automated crater localization and density mapping  

- **Landing Safety Index (LSI)**
  - Weighted fusion of:
    - Terrain slope  
    - Illumination (shadow regions)  
    - Crater density  
  - Classifies terrain into **Safe**, **Moderate-Risk**, and **High-Risk** zones  

- **Geospatial visualization**
  - Hazard and LSI maps generated using QGIS  
  - Clear visual interpretation for mission planning  

---

## 🔁 System Workflow

1. Data acquisition from Chandrayaan-2 TMC-2, DEM, and LROC NAC  
2. Geospatial preprocessing and alignment (QGIS, GDAL)  
3. Terrain parameter extraction (slope, roughness, hillshade)  
4. YOLOv8-based crater detection on LROC imagery  
5. Hazard surface construction and normalization  
6. Landing Safety Index (LSI) computation  
7. Terrain classification into landing risk zones  

---

## 🛠️ Tech Stack

- **Programming:** Python  
- **Machine Learning:** YOLOv8  
- **Computer Vision:** Object Detection, Image Processing  
- **Geospatial Tools:** QGIS, GDAL  
- **Data:** Satellite imagery, DEM, Remote sensing datasets  
