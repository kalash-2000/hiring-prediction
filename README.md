# Salary Prediction for Data Professionals

This project aims to predict the salaries of data professionals using various machine learning techniques. The primary objective is to gain hands-on experience with technologies such as Jupyter Notebook, Heroku, and GitHub Actions.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Continuous Integration and Continuous Deployment](#continuous-integration-and-continuous-deployment)
- [License](#license)

## Project Overview

The purpose of this project is to help hiring managers whether to hire or not based on experience, education, location, and scores of the applicant. 

The main focus of this project is not on the accuracy of classification but on gaining practical experience with the following technologies:

- **Exploratory Data Analysis (EDA) and Model Creation**: Using Jupyter Notebook
- **Web Application and Frontend**: Using Flask
- **Deployment**: Using Heroku
- **Continuous Integration and Continuous Deployment (CI/CD)**: Using GitHub Actions

## Technologies Used

- **Python**: Programming language for data analysis and model creation.
- **Jupyter Notebook**: For EDA and model development.
- **Flask**: For creating the web application and frontend.
- **Heroku**: Platform for deployment.
- **GitHub Actions**: For CI/CD pipeline.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/kalash-2000/hiring_prediction.git
    cd hiring-prediction
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Exploratory Data Analysis and Model Creation:**
    - Open `hiring_decision.ipynb` in Jupyter Notebook.
    - Follow the steps in the notebook to perform EDA and train the model.

2. **Running the Application Locally:**
    - Ensure all dependencies are installed.
    - Run the application:

      ```bash
      python app.py
      ```

3. **Access the application:**
    - Open your web browser and go to `http://localhost:5000`.

## Deployment

The application is deployed on Heroku. Follow these steps to deploy your version:

1. **Login to Heroku:**

    ```bash
    heroku login
    ```

2. **Create a new Heroku application:**

    ```bash
    heroku create your-app-name
    ```

3. **Deploy the application:**

    ```bash
    git push heroku main
    ```

4. **Procfile:**
    - Ensure that a `Procfile` is included in the root directory of your project with the following content:

    ```bash
    web: gunicorn app:app 
    ```

## Continuous Integration and Continuous Deployment

This project uses GitHub Actions for CI/CD. The GitHub Actions workflow is defined in `.github/workflows/main.yml`. This workflow ensures that the application is automatically tested and deployed to Heroku whenever changes are pushed to the main branch.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
