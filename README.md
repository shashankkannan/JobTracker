
# JobTracker

## Overview

JobTracker is a web application designed to help users manage their job applications. It allows users to add, edit, and view job details, including job position, company name, application date, location, and salary. The application provides features for location search using OpenStreetMap, company name suggestions from a local JSON file, and a map display for job locations.

## Features

- **Add Job**: Add new job entries with detailed information.
- **Edit Job**: Update existing job details including position, company, date of application, and more.
- **Location Search**: Search and select job locations using OpenStreetMap.
- **Company Suggestions**: Get company name suggestions from a JSON file or enter a new company name.
- **Map Integration**: View job locations on a map with Leaflet.js.

## Technology Stack

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: JSON file (`data.json`)
- **Map Service**: OpenStreetMap with Leaflet.js

## Setup and Installation

### Prerequisites

- Python 3.x
- Flask
- Flask-Cors (if needed for cross-origin requests)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/shashankkannan/JobTracker.git
   cd JobTracker
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**

   ```bash
   python app.py
   ```

   The application will be available at `http://127.0.0.1:5000`.

## Usage

1. **Navigate to the Application**

   Open your web browser and go to `http://127.0.0.1:5000`.

2. **Add or Edit Jobs**

   - Use the form to add new jobs or edit existing ones.
   - For location search, enter the location in the search box and select from the suggestions.
   - Use the calendar to pick the date of application.
   - Get company name suggestions from the JSON data or manually enter a new name.

3. **View Job Details**

   - Click on a job entry to view and edit details.

## File Structure

- `app.py`: Main application file with Flask routes and logic.
- `data.json`: Contains job data.
- `templates/`: HTML templates for rendering pages.
- `static/css/`: CSS files for styling.
- `static/js/`: JavaScript files for frontend functionality.

## Roadmap

- **Enhanced UI**: Improve user interface with advanced styling and user experience enhancements.
- **User Authentication**: Implement user authentication and authorization.
- **Database Integration**: Replace JSON file with a database for scalable data management.

## Acknowledgments

- **OpenStreetMap**: For providing free and open mapping services.
- **Leaflet.js**: For the interactive map library.

## Contact

For any questions or issues, please contact [Shashank Kannan](mailto:shashank.kannan.cs@gmail.com).
