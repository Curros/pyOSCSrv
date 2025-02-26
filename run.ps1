# Verificar si el entorno virtual está activado
if (-not $env:VIRTUAL_ENV) {
    Write-Host "Loading virtual environment..."
    .\venv\Scripts\Activate.ps1
} else {
    Write-Host "Virtual environment ready."
}

$env:LOG_LEVEL = "INFO"
$env:SERVER_IP = "0.0.0.0"
$env:SERVER_PORT = "8002"

# Ejecutar el script de Python
Write-Host "Executing main.py..."
python main.py