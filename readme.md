# Team Skills Management

This is a Streamlit-based web application for managing team skills. It allows you to create and remove employees, add and remove skills for each employee, and view the skills data in a table format.

## Features

- Create and remove employees
- Add and remove skills for each employee
- Filter and display skills data based on selected employees
- Data is stored in a CSV file for persistence

## Installation

1. Clone the repository:

   ```bash
   https://github.com/SikamikanikoBG/employee_development_matrics.git
   ```

2. Change into the project directory:

   ```bash
   cd employee_development_matrics
```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit application with the following command:

```bash
streamlit run main.py
```

The application will launch in your browser. You can then interact with the sidebar to manage employees and their skills.

## Data Storage

The skills data is stored in a CSV file named `team_skills.csv`. Make sure this file is present in the project directory. If the file does not exist, the application will create an empty one automatically.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License