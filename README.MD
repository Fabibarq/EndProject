Para realizar la prediccion se debe ingresar el siguiente POST:

$headers = @{ "Content-Type" = "application/json" }
$body = @{
    "features" = [0.00632, 18.0, 2.31, 0, 0.538, 6.575, 65.2, 4.0900]
} | ConvertTo-Json

$response = Invoke-WebRequest -Uri "http://IP/predict" -Method POST -Headers $headers -Body $body
$response.Content

Esto por medio de PowerShell, recordar editar el IP.