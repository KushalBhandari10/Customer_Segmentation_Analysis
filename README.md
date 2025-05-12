# Customer Segmentation Project

This project focuses on preprocessing and feature engineering of raw customer data for segmentation and analysis.

## 📊 Dataset
The dataset contains the following fields:
- `Customer_ID`: Unique ID for each customer.
- `Join_Date`: The date the customer joined.
- `Total_Purchases`: Total number of purchases made.
- `Avg_Spend`: Average spend per purchase.
- `Region`: Geographical region of the customer.

## 🔧 Feature Engineering
- **Customer_Tenure**: Days since the customer joined.
- **Customer_Value**: Calculated as `Total_Purchases * Avg_Spend`.
- **Customer_Value_Tier**: Binned into:
  - Low (< 600)
  - Medium (600–1500)
  - High (> 1500)

## 📉 Memory Optimization
Data types of numerical columns were optimized using:
- `int16` for count-based features
- `float32` for monetary values

## 📈 Analysis
Two key analytical summaries were generated:
1. **Pivot Table**: Shows average spend (`Avg_Spend`) grouped by `Region`.
2. **Region-wise Average Customer Value**: Grouped by `Region`.

## 🗂️ Sample Output

### ➕ Engineered Features
| Customer_ID | Customer_Tenure | Customer_Value | Customer_Value_Tier |
|-------------|------------------|----------------|----------------------|
| 1           | 483              | 250.0          | Low                  |
| 2           | 1089             | 1800.0         | High                 |
| 3           | 429              | 640.0          | Medium               |
| 4           | 316              | 4000.0         | High                 |

### 📍 Avg. Customer Value by Region
| Region | Avg_Value |
|--------|-----------|
| North  | 445.0     |
| South  | 1800.0    |
| East   | 4000.0    |

## 🛠 Tools Used
- Python 3
- Pandas
- Datetime

---

Feel free to use or adapt this code for your own customer segmentation projects.
