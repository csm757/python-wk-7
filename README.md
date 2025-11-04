# Week 7 Python Data Analysis Project

## 🧠 Project Overview
This project focuses on basic data analysis and visualization using the **Iris dataset**.  
The work is divided into three main tasks:
1. Loading and exploring the dataset  
2. Performing basic statistical analysis  
3. Creating different types of visualizations  

The goal was to understand data manipulation using **pandas**, perform basic insights, and visualize relationships using **matplotlib** and **seaborn**.

---

## 📂 Task Breakdown

### **Task 1: Load and Explore the Dataset**
- The Iris dataset was loaded using `sklearn.datasets.load_iris()`.
- The data was stored in a pandas DataFrame and labeled with species names.
- The first few rows were displayed using `.head()`.
- Data types and missing values were checked with `.info()` and `.isnull().sum()`.
- Since the dataset had no missing values, no cleaning was required.

### **Task 2: Basic Data Analysis**
- Basic statistics such as **mean**, **median**, and **standard deviation** were computed using `.describe()`.
- The data was grouped by the `species` column, and the average values for each group were calculated.
- Some quick insights:
  - *Setosa* species have the smallest petal sizes.
  - *Virginica* species have the largest sepal and petal measurements.
  - *Versicolor* lies between the two in most measurements.

### **Task 3: Data Visualization**
Four different charts were created to represent the data:

1. **Line Chart** – showing cumulative petal lengths.  
2. **Bar Chart** – comparing average petal length for each species.  
3. **Histogram** – displaying the distribution of sepal length.  
4. **Scatter Plot** – visualizing the relationship between sepal length and petal length.

All charts were customized with titles, axis labels, and appropriate colors.  
The visualizations help identify clear separations between the three iris species.

---

## 📊 Libraries Used
- **pandas** – for data handling and analysis  
- **matplotlib** – for plotting basic graphs  
- **seaborn** – for enhanced data visualization  
- **scikit-learn** – to load the Iris dataset  

---

## ⚙️ How to Run the Project
1. Make sure Python 3.13+ is installed.  
2. Install the required libraries:
   ```bash
   pip install pandas seaborn matplotlib scikit-learn
