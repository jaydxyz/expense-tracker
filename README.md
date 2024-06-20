# Expense Tracker

Expense Tracker is a web application built with Python and Django that allows users to track their expenses. It provides an easy-to-use interface for adding and managing expenses, helping users stay on top of their finances.

## Features

- Add new expenses with details such as description, amount, date, and category
- View a list of recent expenses on the home page
- Categorize expenses for better organization and analysis
- User-friendly interface with responsive design using Bootstrap

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/expense-tracker.git
```

2. Navigate to the project directory:

```
cd expense-tracker
```

3. Create a virtual environment:

```
python -m venv venv
```

4. Activate the virtual environment:

- For Windows:
  ```
  venv\Scripts\activate
  ```
- For Unix or Linux:
  ```
  source venv/bin/activate
  ```

5. Install the required dependencies:

```
pip install -r requirements.txt
```

6. Apply the database migrations:

```
python manage.py migrate
```

7. Start the development server:

```
python manage.py runserver
```

8. Open your web browser and visit `http://localhost:8000` to access the Expense Tracker application.

## Usage

- On the home page, click on the "Add Expense" button to add a new expense.
- Fill in the expense details such as description, amount, date, and category.
- Click the "Add Expense" button to save the expense.
- The list of recent expenses will be displayed on the home page.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Django](https://www.djangoproject.com/) - The web framework used
- [Bootstrap](https://getbootstrap.com/) - The CSS framework used for styling
