# GitHub Embedder

A tool to embed contents of `src` and `href` attributes into `index.html` from a GitHub repository.

## Setup

1. Clone the repository.
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and go to `http://localhost:5000`.

## Usage

1. Enter the GitHub repository (e.g., `owner/repo`) in the input field.
2. Click the "Submit" button.
3. The tool will fetch the contents of `src` and `href` attributes from the specified repository's `index.html` and embed them directly into `index.html`.
4. The updated `index.html` will be created in the project root directory.
