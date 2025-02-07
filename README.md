# Mapping Fluoride: A Geospatial Analysis of Groundwater Quality in Andhra Pradesh

![Project Banner](![image](https://github.com/user-attachments/assets/4a9b9f28-fda7-4541-8590-ada9870c74bc))

## 📌 Overview

**Mapping Fluoride** is a web-based application that visualizes fluoride concentration levels in Andhra Pradesh's groundwater. This tool helps in identifying high-risk, medium-risk, and low-risk zones, aiding public health officials and policymakers in making informed decisions.

## 🎯 Key Features

- **Geospatial Visualization:** Interactive maps using **Leaflet.js** to display fluoride concentration levels.
- **Data Preprocessing:** Cleaning raw groundwater quality data obtained from the **Andhra Pradesh Pollution Control Board (APPCB)**.
- **Dimensionality Reduction:** Utilized **Principal Component Analysis (PCA)** to optimize data representation.
- **Outlier Handling:** Applied **Box-Cox transformation** for statistical normalization.
- **Risk Categorization:** Classified areas into **High-Risk, Medium-Risk, and Low-Risk** zones.
- **Downloadable Insights:** Users can download cleaned datasets and analytical reports for further use.

## 🏗️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript, Leaflet.js
- **Backend:** Python (Flask)
- **Data Processing:** Pandas, NumPy, Scikit-learn
- **Visualization:** Leaflet.js, Matplotlib
- **Database:** GeoJSON

## 📂 Project Structure
```
📦 Mapping-Fluoride
├── 📂 data                # Raw & Processed data
├── 📂 notebooks           # Jupyter Notebooks for data analysis
├── 📂 src                 # Application source code
│   ├── 📂 static          # CSS, JS, Images
│   ├── 📂 templates       # HTML templates
│   ├── app.py            # Main application file (Flask/Django)
├── 📜 requirements.txt    # Dependencies
├── 📜 README.md           # Project Documentation
├── 📜 LICENSE             # License information
```

## 🚀 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Mapping-Fluoride.git
   cd Mapping-Fluoride
   ```
2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Application:**
   ```bash
   python app.py
   ```
5. **Open in Browser:**
   ```
   http://127.0.0.1:5000
   ```

## 📊 Data Sources
- **Andhra Pradesh Pollution Control Board (APPCB)**
- Publicly available groundwater quality datasets

## 🤝 Contributing
We welcome contributions! Follow these steps to contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push the branch (`git push origin feature-branch`)
5. Open a Pull Request

## 📜 License
This project is licensed under the **MIT License**.

## 🌟 Acknowledgments
Special thanks to the **Velagapudi Ramakrishna Siddhartha Engineering College** for supporting this initiative.

---

🔗 **GitHub Repository:** [[Here](https://github.com/nidhaahmed/Mapping-Fluoride.git)]

