# EDS: HVA-04 Duct Leakage Automated Data Pipeline
*Student Name:* Lennard Geisser San Jose  
*Affiliation:* Technological University of the Philippines Manila (TUPM)  
*Course:* Engineering Data Systems (EDS)

## 📌 Project Overview
This repository contains an automated Python-based pipeline designed to ingest, process, and analyze the HVA-04 Duct Leakage dataset. The system utilizes Object-Oriented Programming (OOP) to filter specific engineering data and generate high-resolution statistical visualizations.

## 🛠️ Features
* *Automated Ingestion:* Efficient loading of large-scale CSV engineering records.
* *Data Preprocessing:* Automated cleaning and filtering for Breath IDs 1900–2100.
* *Statistical Framework:* Vectorized calculation of Mean, Variance, and Standard Deviation.
* *Advanced Visualization:* Generation of static distribution plots and dynamic animations of flow trends.

## 📂 Repository Structure
* /data: Contains the original and cleaned datasets.
* /outputs: Contains generated histograms, boxplots, scatter plots, and GIFs.
* main.py: The core execution script.
* requirements.txt: List of necessary Python libraries.

## 🚀 How to Run
1. Ensure Python is installed.
2. Install dependencies: pip install -r requirements.txt
3. Run the pipeline: python main.py