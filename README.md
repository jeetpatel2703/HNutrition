# HNutrition - Food Nutrition App

HNutrition is a simple web application for tracking food categories, items, and their nutritional information.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- MySQL
- Flask (Python Web Framework)
- MySQL Connector Python (For connecting Flask app with MySQL database)

## Installation

1. Clone the repository:
   ```bash
    https://github.com/jeetpatel2703/HNutrition.git
   ```
   
2. Navigate to the project directory:
   ```bash
    cd HNutrition
   ```
   
3. Import the MySQL database schema:

   Execute the SQL commands in `backup.sql` to create the necessary tables and insert initial data.

4. Configure the database connection:

   Edit the `db.py` file and update the database connection details (`host`, `user`, `password`, `database`) according to your MySQL setup.

## Usage

1. Run the Flask application:

   python app.py

2. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000) to access the application.

## Features

- View food categories and their items
- View nutritional information for food items
- Search for specific food items

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, feel free to open an issue or submit a pull request.

## How to Contribute

   1. Fork the repository and clone it to your local machine.
   2. Create a new branch for your feature or bugfix.
   3. Make your changes and commit them with clear, descriptive commit messages.
   4. Push your changes to your fork.
   5. Submit a pull request to the `main` branch of the original repository.

## Coding Standards

   - Follow the existing coding style.
   - Write clear and concise commit messages.
   - Add comments to your code where necessary.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
