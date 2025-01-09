# **ClimatoSync: Real-Time Weather Data ETL Pipeline & Dashboard** 🌦️ 

## 📋 **Project Overview**:
ClimatoSync is a real-time weather data pipeline and dashboard built using **Confluent Kafka**, **Python**, **PostgreSQL**, and **Power BI**. It fetches weather data from an external API, processes it, and stores it in a PostgreSQL database for analysis and visualization. The processed data is then displayed on a dynamic, interactive dashboard built with **Power BI**. This solution allows users to monitor weather metrics in real time with insights like temperature and humidity trends.

---

## 🛰️ **Data Flow & Architecture**:

### 1. **Weather Data API** 🌦️:
   - We use a **OpenWeatherMap API** to fetch real-time weather data, including **temperature** and **humidity**, for various cities.
   - Example API: [OpenWeatherMap API](https://openweathermap.org/api)
   - The API sends data in JSON format, which includes location, temperature, humidity, and timestamp.

### 2. **Producer-Consumer Architecture** 🔄:

   - **Producer (Weather Data Producer)**:
     - The **producer script** fetches real-time weather data from the API.
     - It pushes the weather data into **Kafka topics** using **Confluent Kafka**.
     - This script continuously polls the API at regular intervals to fetch the latest weather data.

   - **Consumer (Weather Data Consumer)**:
     - The **consumer script** subscribes to the Kafka topics, receives the weather data, and processes it.
     - The data is transformed and cleaned before being inserted into a **PostgreSQL** database.
     - The consumer processes the data and prepares it for analysis and visualization.

### 3. **PostgreSQL Database** 💾:
   - The processed data is stored in a **PostgreSQL** database. 
   - Data includes columns such as **city**, **temperature**, **humidity**, and **timestamp**.
   - This structured data allows for easy querying and integration with visualization tools.

### 4. **Power BI Dashboard** 📊:
   - **Power BI** connects to the PostgreSQL database to dynamically fetch the weather data.
   - The dashboard updates every 10 minutes to provide real-time visualizations of key metrics, such as:
     - **Temperature trends** 🌡️
     - **Humidity trends** 💧
   - Users can filter the data by **city** or view historical trends for deeper insights.
   - The dashboard also includes **average**, **min**, **max**, and **current temperature**.

#### **Dashboard Details**:
## 📊 Dashboard Screenshot:
![Real-Time Weather Dashboard](https://github.com/NakshatraDeshmukh/ClimatoSync/blob/main/screenshots/dashboard1%20(1).png)
The dashboard provides a comprehensive overview of real-time weather data for **Pune**. Here's what it displays:

**Current Weather Data**:
- **Temperature**: Current temperature in **Kelvin** (e.g., 295.16 K).
- **Humidity**: Current humidity (e.g., 26%).
- **Weather Condition**: Current weather (e.g., "few clouds").

**Charts and Visualizations**:
- **Weather Condition Distribution**: Pie chart showing weather condition proportions.
- **Temperature Trends**: Line chart with temperature variation and weather conditions.
- **Humidity Trends**: Line chart for humidity changes.
- **Daily Averages**: Bar chart of daily average temperature and humidity.

**Gauges**:
- **Max Temperature Today**: Highest recorded temperature today (e.g., 300.47 K).
- **Min Humidity Today**: Lowest recorded humidity today (e.g., 23%).

**Interactive Features**:
- **Date Selector**: Select specific dates for analysis.
- **Last Updated Timestamp**: Displays the latest data update (e.g., "09-01-2025 14:15:53").
---
### 5. **Features** 🚀 :
- **Real-time Weather Monitoring**: Get live updates of weather conditions.
- **Dynamic Dashboard**: Interactive dashboard with key weather metrics and trends.
- **Power BI Integration**: Seamless integration with Power BI for real-time data visualization.
- **Kafka-based Messaging**: Efficient producer-consumer architecture using Confluent Kafka for real-time data streaming.
- **Scalable Data Storage**: Use of PostgreSQL for reliable, structured data storage.

### 6. **Technologies Used** 🔧:
- **Confluent Kafka**: Real-time data streaming and messaging.
- **Python**: Data processing, Kafka integration, and API handling.
- **PostgreSQL**: Structured data storage.
- **Power BI**: Data visualization and dashboard creation.
- **Weather API**: Fetching real-time weather data.

### 8. **Jupyter Notebook Graphs**:

Below are the visualizations generated in the Jupyter notebook:

**- Temperature Trends**

<img src="https://github.com/NakshatraDeshmukh/ClimatoSync/blob/main/screenshots/temperature%20trend.png" alt="Temperature Trends" width="600"/>

**- Humidity Trends**

<img src="https://github.com/NakshatraDeshmukh/ClimatoSync/blob/main/screenshots/humidity%20trend.png" alt="Humidity Trends" width="600"/>

**- Average Temperature & Humidity By Condition**

<img src="https://github.com/NakshatraDeshmukh/ClimatoSync/blob/main/screenshots/avg%20by%20condition.png" alt="Average Temperature & Humidity By Condition" width="600"/>

**- Correlation Heatmap**

<img src="https://github.com/NakshatraDeshmukh/ClimatoSync/blob/main/screenshots/correlation%20heatmap.png" alt="Correlation Heatmap" width="600"/>

### 9.  **Conclusion** :

This project provides a comprehensive and scalable solution for real-time weather data monitoring, analysis, and visualization. By leveraging modern technologies like Confluent Kafka, PostgreSQL, Power BI, and a weather API, we are able to stream and store live data while providing insightful visualizations. The integration with Power BI further enhances the user experience by providing an interactive dashboard for real-time decision making.

Feel free to explore, contribute, and improve upon this project to help enhance its capabilities!

🔗 **Connect with me**:  
[LinkedIn](https://www.linkedin.com/in/nakshatra-deshmukh/) | [GitHub](https://github.com/NakshatraDeshmukh)

