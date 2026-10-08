# NLP-based Analysis of Consumer Complaints

## Project
Portfolio project for:
DLBDSEDA02_D – Projekt: Data Analysis

## Objective
Identification of frequently discussed topics in consumer complaints
using Natural Language Processing.

## Dataset
Consumer Financial Protection Bureau (CFPB)
Consumer Complaint Database Narratives Archive
January–February 2026.

## Workflow
- Data preparation
- Exploratory data analysis
- Text preprocessing with spaCy
- Bag-of-Words
- TF-IDF
- Latent Semantic Analysis
- Latent Dirichlet Allocation
- Topic evaluation using coherence and perplexity
- Topic interpretation and validation

## Reproducibility
A fixed random state of 42 is used where applicable.

## Setup

pip install -r requirements.txt

## Data preparation

Download the CFPB Consumer Complaint Database export
(January 2026 through February 2026) and save it as:

data/raw/complaints.csv

Then run:

python src/prepare_data.py

The complete analysis is available in:

notebooks/01_analysis.ipynb