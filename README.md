# Serverless URL Shortener on AWS 🚀

A simple, scalable, and cost-effective URL shortener service built with Python and deployed as a serverless application on AWS. This project uses a CI/CD pipeline with GitHub Actions for automated deployments.



## Description

This web application provides a simple interface to shorten long URLs. It exposes two main API endpoints: one to create a new short URL (`/shorten`) and another to handle the redirection from a short code to the original URL. The entire backend is serverless, meaning it runs on-demand and has no idle server costs, making it extremely cost-efficient.

## Tech Stack & Architecture

The application is built using a modern, serverless-first approach on AWS.

* **Backend:** Python 3.9, Flask
* **Database:** Amazon DynamoDB (NoSQL)
* **Deployment:** AWS Lambda & Amazon API Gateway (HTTP API)
* **CI/CD:** GitHub Actions
* **AWS SDK:** Boto3

### Architecture Flow

The request flow is as follows:
`User -> API Gateway -> AWS Lambda -> Amazon DynamoDB`

## Local Development Setup

To run this project on your local machine, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/aws-url-shortener.git](https://github.com/your-username/aws-url-shortener.git)
    cd aws-url-shortener
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure AWS Credentials:**
    Make sure you have the AWS CLI installed and configured with credentials that have DynamoDB access.
    ```bash
    aws configure
    ```

5.  **Run the Flask App:**
    ```bash
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000`.

## Deployment

This project is configured for continuous deployment. Any push or merge to the `main` branch will automatically trigger the GitHub Actions workflow defined in `.github/workflows/deploy.yml`. This workflow packages the application and deploys the latest version to AWS Lambda.

## API Endpoints

* `POST /shorten`
    * Creates a new short URL.
    * **Body (JSON):** `{ "url": "https://your-long-url.com" }`
    * **Success Response:** `{ "short_url": "https://api-endpoint/short_code" }`

* `GET /{short_code}`
    * Redirects to the original long URL associated with the `short_code`.