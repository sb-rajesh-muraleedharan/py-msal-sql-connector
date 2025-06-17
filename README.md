# Azure SQL Authentication via Entra ID (Python)

This project demonstrates how to connect to an Azure SQL Database using an **Azure Entra App Registration** (Client ID and Secret) with **MSAL** and **pyodbc** in Python.

## 🔧 Features

- Authenticates using Azure Entra ID (App Registration)
- Uses MSAL to acquire access tokens
- Connects to Azure SQL using `pyodbc`
- Loads configuration securely from `.env` file
- Modular code (`connect_to_sql.py` and `main.py`)

---

## 📁 Project Structure
.
├── .env
├── connect_to_sql.py # Handles MSAL auth and SQL connection
└── main.py # Runs a sample query using the connection

## 🔐 Prerequisites

- Python 3.7+
- An Azure SQL Database configured for Entra ID authentication
- Azure App Registration with:
  - **API permissions**: `Azure SQL Database` → `Application`
  - A **Client Secret**
  - The app added as a user in SQL with appropriate roles

## 📦 Installation

```bash
git clone https://github.com/sb-rajesh-muraleedharan/py-msal-sql-connector
cd azure-sql-auth-py

# Create virtual environment (optional)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Environment Configuration
1. Create your local .env file
This project includes a dev.env file with placeholder keys. To run the app, you need to:

cp dev.env .env

Then open .env and fill in your actual values:
CLIENT_ID=your-actual-app-id
CLIENT_SECRET=your-actual-app-secret
TENANT_ID=your-tenant-id
SQL_SERVER=your-sql-server-name.database.windows.net
SQL_DATABASE=your-database-name

⚠️ Do not commit .env to Git. This file is ignored via .gitignore for security reasons.
