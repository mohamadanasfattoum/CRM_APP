# CRM_APP

The **CRM_APP** is a web application built using Python, Django, MySQL, API, Bootstrap, and other technologies. It is designed to help businesses manage their customer relationships.

To run the application, you will need to follow these steps:

1. Prerequisites:
   - Python: Ensure that Python is installed on your system. You can download it from the official Python website (https://www.python.org/downloads/).
   - Django: Install Django by executing the command `pip install django` in your command prompt or terminal.
   - MySQL: Make sure you have MySQL installed on your system. You can download it from the official MySQL website (https://www.mysql.com/downloads/).

2. Clone the Repository:
   - Visit the GitHub repository URL: https://github.com/mohamadanasfattoum/CRM_APP.
   - Click on the "Code" button and copy the repository's URL.

3. Set up the Database:
   - Create a MySQL database for the CRM application.
   - Update the database configuration in the `settings.py` file located in the `CRM_APP` directory. Set the `DATABASES` dictionary with your MySQL database credentials.

4. Install Dependencies:
   - Open your command prompt or terminal and navigate to the directory where you want to clone the repository.
   - Run the command `git clone <repository_url>` to clone the repository to your local machine.
   - Navigate to the cloned repository's directory using the command prompt or terminal.
   - Run the command `pip install -r requirements.txt` to install the required Python packages.

5. Run Migrations:
   - Execute the following command to apply the database migrations:
     ```
     python manage.py migrate
     ```

6. Start the Server:
   - Run the following command to start the development server:
     ```
     python manage.py runserver
     ```

7. Access the Application:
   - Open your web browser and visit `http://localhost:8000` to access the CRM application.

Please note that these instructions assume a basic setup, and additional configuration steps may be required based on your specific environment. It's recommended to refer to the repository's documentation or readme file for more detailed instructions or troubleshooting steps.
