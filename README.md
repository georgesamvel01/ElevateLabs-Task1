# 📊 Netflix Movies and TV Shows Dataset Cleaning

This project involves cleaning and preparing the **Netflix Movies and TV Shows Dataset** for analysis. It includes handling missing values, duplicates, formatting issues, and data type corrections using **Python (Pandas)** and **Excel**.

---

## 🧰 Tools Used

- Python (Pandas)
- Excel
- Jupyter Notebook / VS Code

---

## 🧼 Cleaning Steps Performed

1. **Removed duplicate rows** to ensure data integrity.
2. **Dropped rows with critical missing values** in:
   - `country`
   - `rating`
   - `date_added`
3. **Standardized formatting**:
   - `type`: converted to lowercase
   - `country`: converted to title case (e.g., *united states* → *United States*)
   - `rating`: converted to uppercase (e.g., *pg-13* → *PG-13*)
4. **Converted** `date_added` to `datetime` format.
5. **Renamed column headers** to snake_case for consistency (e.g., `Show ID` → `show_id`).
6. **Corrected data types**:
   - `release_year` as integer
   - `date_added` as datetime

---

## 🗃️ Files Included

| File Name                        | Description                              |
|----------------------------------|------------------------------------------|
| `Netflix_movies_and_tv_shows.csv` | Raw dataset (original)                   |
| `cleaned_netflix_data.csv`       | Cleaned version of the dataset           |
| `Netflix_Cleaning_Summary.pdf`   | Summary of all cleaning steps performed  |
| `cleaning_script.py` *(optional)*| Python script used for cleaning          |

---

## 📈 Dataset Source

Dataset originally from **Kaggle**: [Netflix Movies and TV Shows Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)

---

## ✅ Author

**Max (H. George Samvel)**  
🛠 Built with Python, Pandas, and Excel  
📧 Reach me for collaboration or feedback!

---

## 📌 License

This project is open-source and available under the [MIT License](LICENSE).
