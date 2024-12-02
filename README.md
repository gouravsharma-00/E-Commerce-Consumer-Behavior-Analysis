## **E-Commerce Consumer Behavior Analysis**  

### **Objective:**  
To analyze consumer purchasing behavior using an e-commerce dataset, exploring patterns in order timings, product preferences, and user engagement.

---

### **Folder Structure:**  

- **`Data Engineering/`**  
  - **`app/`**: Contains the code for the deployed **Streamlit app** that visualizes insights derived from the analysis.  
    - Note: This folder does not include functionality for retrieving data from MongoDB or storing data in SQL Server.  
  - **`codebase/`**: Includes all Jupyter notebooks (`.ipynb` files) containing the end-to-end implementation of the project:  
    - **Data Cleaning**: Handling missing values, data type conversions, and ensuring data quality.  
    - **Data Analysis**: Exploring consumer behavior trends and generating insights.  
    - **Data Storage and Retrieval**:  
      - Code for connecting to a local **MongoDB** database and loading the dataset into a DataFrame.  
      - Code for storing the processed data into an **SQL Server** database.  

---

### **Key Features of the Project:**  

1. **Data Cleaning and Preprocessing:**  
   - Handled missing values and ensured data consistency.  
   - Processed columns like `days_since_prior_order` to enable meaningful analysis.  

2. **Exploratory Data Analysis (EDA):**  
   - Purchases by day and time of day.  
   - Frequency of orders by user and time since the last order.  
   - Identification of the top 15 most popular products.  

3. **Data Storage and Retrieval:**  
   - Utilized MongoDB for initial storage and pandas for data processing.  
   - Saved the final processed data to SQL Server for structured data analysis.  

4. **Visualization App:**  
   - Built with **Streamlit** to present insights via interactive charts and graphs.  

---

### **Deployed Application:**  

**Access the deployed Streamlit app here:**  
[**E-Commerce Consumer Behavior Analysis App**](https://your-deployed-app-link.com)  

---

### **Tools and Libraries Used:**  

- **Data Cleaning & Analysis:** Pandas  
- **Visualization:** Matplotlib, Seaborn, Streamlit  
- **Database Integration:** pymongo, pyodbc  

---

Feel free to explore the deployed application for insights or run the codebase locally for a deep dive into the analysis process.