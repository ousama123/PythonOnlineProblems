# Check if .venv already exists
if (!(Test-Path -Path ".venv")) {
    Write-Host "Creating a new virtual environment..."
    python -m venv .venv
}
else {
    Write-Host "Virtual environment already exists. Skipping creation."
}

# Activate the virtual environment
& .\.venv\Scripts\activate

# Install dependencies
Write-Host "Installing dependencies from requirements.txt..."
pip install -r requirements.txt
