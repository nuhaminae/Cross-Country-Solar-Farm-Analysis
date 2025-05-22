## Cross Country Solar Farm Analysis
This repository contains Jupyter Notebooks and resources for analysing for Cross-Country Solar Farm Analysis project. The goal of this project is to analyse solar radiation and weather data from three countries in West Africa countries. It aims to understand patterns, identify outliers, and explore relationships between different environmental factors and solar irradiance.

## Project Overview
The analysis focuses on:
- Comparing solar farm performance metrics across multiple countries.
- Identifying key factors affecting solar farm productivity, such as geographic location, climate, and technological differences.
- Visualizing trends and presenting actionable insights for stakeholders interested in renewable energy.

## Business Objective
The goal of this analysis is to support **MoonLight Energy Solutions** in optimizing solar investments through **data-driven insights**. The Goal is to:
- Analyze environmental measurement data.
- Identify key trends and actionable insights.
- Provide recommendations aligned with long-term sustainability goals.

## Dataset Overview
The dataset consists of **solar radiation measurements, weather conditions, wind speeds, cleaning events, and more**. Key columns include:
- **Solar Irradiance:** `GHI`, `DNI`, `DHI`
- **Module Measurements:** `ModA`, `ModB`
- **Weather Data:** `Tamb`, `RH`, `WS`, `WD`, `BP`
- **Cleaning Events & Precipitation:** `Cleaning`, `Precipitation`
- **Time Series:** `Timestamp`

## Repository Structure
├── .github/ 
│ └── workflows/
│       ├── ci.yml
├── .venv                                   #virutal environment (no included)
├── app
│ └── dashboard screenshot/
│       ├── Benin Dashboard.png
│       ├── Sierra Leone Dashboard.png
│       ├── Togo Dashboard.png
│ └── main.py
│ └── README.md
├── data                                    #raw and processed datasets (not included)
├── EDA-notebooks
│ └── EDA-Benin.ipynb
│ └── EDA-SierraLeone.ipynb
│ └── EDA-Togo.ipynb
├── .gitignore
├── compare_countries.ipynb
├── README.md
├── requirements.txt

## Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Notebook
- Common data science libraries: pandas, numpy, matplotlib, seaborn, scikit-learn
- Install dependencies using pip:


### Usage

1. Clone this repository:
    git clone https://github.com/nuhaminae/Cross-Country-Solar-Farm-Analysis.git
2. Launch Jupyter Notebook:
    jupyter notebook
3. Open the notebooks in the `EDA-notebooks/` directory and `compare_countries.ipynb` notebook directory and and follow the steps within the notebooks 


## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, additional analyses, or bug fixes.