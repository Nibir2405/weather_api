# Weather Data API

Welcome to the Weather Data API! This API provides access to historical weather data collected from various weather stations. It allows users to retrieve temperature data for specific dates, stations, and years. The API is designed to be simple and easy to use, making it ideal for developers, researchers, and hobbyists interested in weather data analysis.

## Features

- **Home Page**: Displays a list of weather stations with their IDs and names.
- **About Page**: Provides information about the API and its creator.
- **Temperature Data by Date**: Retrieve the temperature for a specific station on a specific date.
- **All Data for a Station**: Retrieve all available temperature data for a specific station.
- **Yearly Data for a Station**: Retrieve temperature data for a specific station for an entire year.

## Endpoints

- **Home**: `/`
  - Displays a list of weather stations.
- **About**: `/about/`
  - Provides information about the API and its creator.
- **Get Data by Date**: `/api/v1/<stationid>/<date>`
  - Retrieves the temperature for a specific station on a specific date.
  - **Parameters**:
    - `stationid`: The ID of the weather station.
    - `date`: The date for which the temperature data is requested (format: YYYY-MM-DD).
- **Get All Data for a Station**: `/api/v1/<stationid>`
  - Retrieves all available temperature data for a specific station.
  - **Parameters**:
    - `stationid`: The ID of the weather station.
- **Get Yearly Data for a Station**: `/api/v1/yearly/<stationid>/<year>`
  - Retrieves temperature data for a specific station for an entire year.
  - **Parameters**:
    - `stationid`: The ID of the weather station.
    - `year`: The year for which the temperature data is requested.

## Example Usage

- **Get Temperature by Date**:
  - `GET /api/v1/12/20000307`
  - Response: `{"Date": "20000307", "Station": "12", "Temperature": 15.2}`

- **Get All Data for a Station**:
  - `GET /api/v1/12`
  - Response: `[{"Date": "20020307", "Temperature": 15.2}, ...]`

- **Get Yearly Data for a Station**:
  - `GET /api/v1/yearly/12/2002`
  - Response: `[{"Date": "2002307", "Temperature": 15.2}, ...]`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Nibir2405/weather_api.git
    ```
2. Navigate to the project directory:
    ```sh
    cd weather_data_api
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the Flask application:
    ```sh
    python main.py
    ```

## About the Creator

Hi, I am Navid Ul Islam, a dedicated student currently pursuing my studies in Management. I am passionate about technology and currently building a strong foundation in Python. I aspire to specialize in data science and machine learning, using data-driven insights to solve real-world problems.

---

