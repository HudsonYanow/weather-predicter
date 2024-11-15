
# Weather Forecast App

This Python application provides weather forecasts using the [Open-Meteo API](https://open-meteo.com/). The app allows users to input their location via latitude and longitude and retrieve current and upcoming weather conditions, including temperature, sunrise, sunset, and weather codes.

## Features

- **Get the weather forecast**: Retrieve daily or weekly weather data including maximum and minimum temperatures, sunrise and sunset times.
- **Coordinate validation**: Ensures valid latitude and longitude inputs.
- **Location update**: Users can change their location coordinates to get forecasts for different areas.
- **Day of the week extraction**: Displays the day of the week for the given date.

## Installation

1. Clone this repository to your local machine.
   ```bash
   git clone <repository-url>
   ```
2. Install required dependencies:
   ```bash
   pip install requests pandas
   ```

## Usage

1. Run the program:
   ```bash
   python weather_forecast.py
   ```

2. Follow the prompts:
   - Enter the latitude and longitude of your location (e.g., **New York**: lat=40.7143, lon=-74.0060).
   - Choose from the menu to get the weather for the next day, week, change coordinates, or exit.

## Example

```bash
Welcome to the Weather Forecast App
What is the latitude of your location: 40.7143
What is the longitude of your location: -74.0060
Do you want to:
1) Get the weather forecast for the next day.
2) Get the weather forecast for the upcoming week.
3) Change coordinates.
4) Exit the program
```

## API Documentation

This app fetches weather data from the Open Meteo API. For more information, visit [Open-Meteo API Documentation](https://open-meteo.com/en/docs).

## License

This project is licensed under the MIT License.
