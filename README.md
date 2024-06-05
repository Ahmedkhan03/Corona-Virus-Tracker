# Corona Virus Tracker

This is the "Corona Virus Tracker" project built with Python. It collects, processes, and visualizes COVID-19 data from reliable sources, providing an interactive user interface and ensuring regular data updates.

## Features

- **Data Collection**: Gathers up-to-date COVID-19 statistics from trusted APIs.
- **Data Processing**: Cleans and organizes data for accurate analysis.
- **Data Visualization**: Creates informative charts and graphs to depict the spread and impact of the virus.
- **User Interface**: Interactive web interface built with Flask for easy data access.
- **Automated Updates**: Keeps data current with regular updates.

## Project Structure

- `app.py`: Main application file
- `data_fetcher.py`: Script for fetching data from APIs
- `data_processor.py`: Script for cleaning and organizing data
- `visualizer.py`: Script for creating data visualizations
- `templates/`: HTML templates for the web interface
- `static/`: Static files like CSS and JavaScript

## Getting Started

### Prerequisites

Make sure you have Python 3.6+ installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/corona-virus-tracker.git
   cd corona-virus-tracker
   ```

2. **Create a virtual environment** (optional but recommended):
   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application

1. **Run the application**:
   ```sh
   python app.py
   ```

2. **Access the web interface**:
   Open your browser and navigate to `http://127.0.0.1:5000`

## Usage

Once the application is running, you can access various features through the web interface:
- View current COVID-19 statistics globally and by country.
- Visualize data through charts and graphs.
- Get regular updates as the data is refreshed.

## Dependencies

- `requests`: For fetching data from APIs
- `pandas`: For data processing
- `matplotlib` & `seaborn`: For data visualization
- `flask`: For the web interface

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
