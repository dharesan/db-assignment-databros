# Database Assignment 2 - Spark and HDFS

This repository contains the implementation of Database Assignment 2 focusing on Apache Spark and Hadoop HDFS data processing.

## Assignment Overview

Part 1: Restaurant Review Data Processing
- **Question 1**: Data cleaning - removing rows with no reviews or rating < 1.0
- **Question 2**: [To be implemented]
- **Question 3**: [To be implemented] 
- **Question 4**: [To be implemented]

Part 2: Movie Credits Data Processing
- **Question 5**: [To be implemented]

## Project Structure

```
├── q1.py              # Question 1 implementation
├── q2.py              # Question 2 implementation
├── q3.py              # Question 3 implementation
├── q4.py              # Question 4 implementation
├── q5.py              # Question 5 implementation
├── hw2.sh             # Execution script
├── data/              # Input data files
│   ├── TA_restaurants_curated_cleaned.csv
│   └── tmdb_5000_credits.parquet
└── README.md          # This file
```

## Setup Requirements

### Prerequisites
- Java 11+
- Apache Hadoop 3.x
- Apache Spark 3.x
- Python 3.x with PySpark

### Environment Setup
1. Install Hadoop and Spark
2. Configure HDFS (see hw2.sh for directory setup)
3. Install Python dependencies:
   ```bash
   pip install pyspark==3.5.0
   ```

### HDFS Setup
```bash
# Create directories
hdfs dfs -mkdir -p /assignment2/part1/input/
hdfs dfs -mkdir -p /assignment2/part2/input/

# Upload data
hdfs dfs -put data/TA_restaurants_curated_cleaned.csv /assignment2/part1/input/
hdfs dfs -put data/tmdb_5000_credits.parquet /assignment2/part2/input/
```

## Running the Assignment

### Option 1: Run individual questions
```bash
export JAVA_HOME=/path/to/java11
python q1.py localhost
python q2.py localhost
# etc.
```

### Option 2: Run all questions
```bash
chmod +x hw2.sh
./hw2.sh
```

## Data Schema

### Restaurant Data (TA_restaurants_curated_cleaned.csv)
- Name: Restaurant name
- City: Location city
- Cuisine Style: Type of cuisine
- Ranking: Restaurant ranking
- Rating: Customer rating (1-5)
- Price Range: Price category
- Number of Reviews: Review count
- Reviews: Customer reviews
- URL_TA: TripAdvisor URL
- ID_TA: TripAdvisor ID

### Movie Credits Data (tmdb_5000_credits.parquet)
- [Schema to be documented]

## Assignment Status

- [x] **Question 1**: ✅ Completed - Data cleaning implementation
- [ ] **Question 2**: 🔄 In progress
- [ ] **Question 3**: 📋 Pending
- [ ] **Question 4**: 📋 Pending
- [ ] **Question 5**: 📋 Pending

## Notes

- HDFS runs on localhost:9000
- Output files are stored in `/assignment2/output/questionX/`
- All implementations use Spark DataFrames with HDFS as storage backend

---
*Assignment completed as part of Database course DB.50.043*
