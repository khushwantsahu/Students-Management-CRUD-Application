# Students Management CRUD Application with AI Extension

A Student Management REST API developed using **Python, FastAPI, and SQLite**, with an AI assistant powered by **Llama 3.2 through Ollama**, as part of the EWB Edu Tech Pvt. Ltd. Python Backend Development Internship Project.

The application is organized into modular route files and is designed to manage student records through CRUD operations. It also includes an AI query route for a natural-language question feature.

## Features

- **Create** student records.
- **Read** student records, including listing and retrieving students where implemented.
- **Update** existing student records.
- **Delete** student records.
- SQLite database for persistent storage.
- Modular FastAPI route organization.
- Request/response schemas and application configuration.
- AI assistant powered by Llama 3.2 through Ollama for natural-language questions about student data (when configured).
- Nginx configuration file included in the project.

> **Note:** The exact fields, endpoint paths, filtering options, and AI provider depend on the implementation in the source files. Verify them in the code and in the generated API documentation before presenting them as completed features.

## Technology Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy (if used by the current implementation)
- Pydantic
- Uvicorn
- Nginx configuration (optional, for reverse-proxy deployment)

## Project Structure

```text
Student-Management/
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── ai_query.py
│   │   ├── base.py
│   │   ├── create_students.py
│   │   ├── delete_students.py
│   │   ├── get_students.py
│   │   └── update_students.py
│   ├── config.py
│   ├── database.py
│   ├── model.py
│   └── schema.py
├── main.py
├── nginx.conf
├── pyproject.toml
├── requirements.txt
├── .env                  # Local configuration; do not commit
├── .gitignore
├── .python-version
├── students.db           # Local SQLite database; do not commit real data
└── README.md
```

Virtual-environment folders, Python cache folders, and `uv.lock` may also be present locally.

## Prerequisites

- Python version compatible with `.python-version` and `pyproject.toml`
- `pip` or `uv`
- Git (for version control)

## Installation and Setup

### 1. Clone the repository

Replace `<your-github-username>` with your GitHub username.

```bash
git clone https://github.com/<your-github-username>/Students-Management-CRUD-Application.git
cd Students-Management-CRUD-Application
```

### 2. Create a virtual environment

**Windows (Command Prompt):**

```bat
python -m venv .venv
.venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

Using pip:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If the project is managed with `uv` and `pyproject.toml`, you can alternatively use:

```bash
uv sync
```

Use the dependency-management method that matches the committed project files.

### 4. Configure environment variables

If the application reads settings from `.env`, create a local `.env` file using the variable names expected by `app/config.py`.

Example template only:

```env
# Add the variables required by app/config.py.
# Do not place real credentials or secrets in version control.
```

Do not invent or copy environment-variable names without checking the application configuration. Keep credentials and private student information out of Git.

### 5. Run the application

From the project root, run:

```bash
python -m uvicorn main:app --reload
```

The development server is typically available at:

- API base: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

These URLs assume the application uses Uvicorn on its default host and port.

## API Documentation and Testing

Open Swagger UI at `http://127.0.0.1:8000/docs` after starting the server. It displays the routes registered by the running application and lets you send test requests.

The EWB assignment suggests the following endpoint design. Treat these as expected examples, not a guarantee that the current code uses these exact paths.

| Method | Example endpoint | Purpose |
|---|---|---|
| `POST` | `/students` | Create a student |
| `GET` | `/students` | List or filter students |
| `GET` | `/students/{student_id}` | Retrieve one student |
| `PUT` or `PATCH` | `/students/{student_id}` | Update a student |
| `DELETE` | `/students/{student_id}` | Delete a student |

Check the actual route decorators and router prefixes in `app/routes/` and `main.py` to confirm the final paths and request schemas.

### Example request body

Use only fields accepted by your current Pydantic schema in `app/schema.py`. For example, if the schema supports these fields:

```json
{
  "name": "Sample Student",
  "student_dob": "2004-05-20",
  "email": "student@example.com",
  "phone": "9876543210"
}
```

This is an illustrative payload. Adjust field names and required fields to match the actual schema. Use dummy data for testing.

### Testing checklist

- [ ] Create a student and confirm the response.
- [ ] List students and confirm the new record appears.
- [ ] Retrieve a student by ID, if that endpoint is implemented.
- [ ] Update an existing record.
- [ ] Delete a record.
- [ ] Test invalid input and a nonexistent student ID.
- [ ] Restart the application and confirm that SQLite data persists.
- [ ] Test the AI query endpoint, if configured.

## Database

The project contains `app/database.py` for database setup and `app/model.py` for database models. The local `students.db` file is an SQLite database.

The database initialization and table-creation behavior depend on the code in `main.py` and `app/database.py`. If tables are not created automatically, follow the initialization approach implemented by the project before testing endpoints.

**Do not commit a database containing real student information.** Use dummy records for demos and testing.

## Optional AI Query Feature

The project includes `app/routes/ai_query.py` for the AI assistant. The intended model is **Llama 3.2**, run locally through **Ollama**.

Example questions the assistant may support, depending on the implementation:

- “How many students are there?”
- “List students born after 2005.”

### Set up Llama 3.2 with Ollama

1. Install Ollama from [ollama.com](https://ollama.com/).
2. Download the model:

   ```bash
   ollama pull llama3.2
   ```

3. Start the model locally:

   ```bash
   ollama run llama3.2
   ```

4. Keep Ollama running while testing the API. Confirm the model name, Ollama URL, and any environment variables expected by `app/routes/ai_query.py` and `app/config.py`.
5. Start FastAPI in another terminal and test the AI endpoint through Swagger UI at `http://127.0.0.1:8000/docs`.

The exact request path and JSON body for the AI endpoint depend on the route implementation. Check `app/routes/ai_query.py` and the live Swagger documentation for the correct endpoint and payload.

For safety and accuracy, retrieve relevant records through controlled backend code and provide only the necessary data to the model. Do not allow the model to execute unrestricted SQL. Use dummy student data and avoid exposing real student personal information.

## Nginx Configuration

The repository includes `nginx.conf`. Nginx can be used as a reverse proxy in a deployment setup, depending on the configuration.

For local development, run FastAPI directly using Uvicorn. Before using Nginx, review `nginx.conf`, verify the upstream address and port, and test the configuration using the Nginx executable appropriate to your operating system.

## Security and Git Hygiene

Before pushing the project to GitHub:

- Add `.env` and local secrets to `.gitignore`.
- Exclude virtual environments and Python cache files.
- Exclude `students.db` if it contains local or personal data.
- Never commit API keys, passwords, tokens, or real student records.
- Use dummy data in examples and screenshots.

Example `.gitignore` entries (merge with your existing file rather than overwriting project-specific rules):

```gitignore
.venv/
venv/
__pycache__/
*.py[cod]
.env
students.db
```

If a secret has already been committed, removing it in a later commit may not remove it from Git history. Rotate the exposed credential and clean the repository history if necessary.

## Troubleshooting

### Application does not start

- Activate the correct virtual environment.
- Install dependencies from `requirements.txt` or synchronize the `uv` environment.
- Check the terminal traceback and configuration values.
- Confirm that the command is run from the directory containing `main.py`.

### Address already in use

Another process may already be using port `8000`. Stop the other server or choose another port:

```bash
python -m uvicorn main:app --reload --port 8001
```

### Database table does not exist

Check that the SQLite path and table initialization logic in `app/database.py`, `app/model.py`, and `main.py` match. Confirm the application is opening the intended database file.

### Request returns `422 Unprocessable Entity`

Compare the request body with the Pydantic schema in `app/schema.py`. Check required fields, field names, data types, and date formats in Swagger UI.

## Assignment Context

This project is based on the **EWB Edu Tech Pvt. Ltd. — Python Backend Development Internship Project**. The assignment prioritizes a functional FastAPI + SQLite application with all four CRUD operations, persistent storage, input validation, missing-record handling, and reproducible documentation. The AI extension is optional.

## Future Improvements

- Add automated tests with `pytest` and FastAPI's test client.
- Add pagination and search/filtering where needed.
- Improve consistent HTTP status codes and error responses.
- Add database migrations if the project grows.
- Deploy behind a properly configured reverse proxy.
- Add authentication and authorization if required for the intended use.

## Author

**Khushwant Sahu**

GitHub: `https://github.com/khushwantsahu`

---

Built as an internship project for Python backend development.
