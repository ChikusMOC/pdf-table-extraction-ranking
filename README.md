# PDF Ranking Analyzer

## Overview

This project extracts and transforms structured data from a large official PDF document (600+ relevant pages) to generate an automated ranking based on candidate scores.

The original document only provided raw individual scores without any classification or ranking.  
This solution processes the entire dataset, handles inconsistencies, and produces a clean, sortable ranking table using Python.

---

## Problem

The official document presented several technical challenges:

- 1200+ total pages (with hundreds of blank pages)
- Tables with headers only on the first page
- Mixed category sections (female and male lists)
- Encoding inconsistencies (Latin-1 issues)
- Inconsistent table detection across pages
- No official ranking available

The objective was to extract all relevant data and reconstruct a reliable ranking system programmatically.

---

## Technical Challenges

- Parsing large multi-page PDFs efficiently
- Reconstructing missing headers across pages
- Detecting and removing empty or malformed tables
- Handling encoding errors during extraction
- Cleaning NaN-heavy DataFrames
- Standardizing column structures
- Concatenating hundreds of tables safely
- Ensuring correct category segmentation before ranking

---

## Solution Approach

1. Extracted tables using `tabula-py`
2. Applied preprocessing to remove blank pages
3. Captured and reapplied headers programmatically
4. Normalized column structures
5. Cleaned empty rows and columns
6. Converted score fields to numeric types
7. Generated ranking using sorted score values

---

## Technologies Used

- Python
- pandas
- tabula-py
- Jupyter Notebook

---

## Results

- Successfully processed 600+ pages of structured tabular data
- Generated a complete ranking dataset
- Reduced manual analysis time to zero
- Created a reusable data-processing workflow

---

## What This Project Demonstrates

- Real-world PDF data extraction
- Data cleaning and transformation
- Handling large datasets
- Debugging encoding and structural inconsistencies
- Analytical thinking and automation
- Practical problem-solving using Python
