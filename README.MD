
# Proyecto de Predicción con Flask y Docker

Este proyecto implementa un endpoint de predicción utilizando Flask y un modelo de regresión lineal entrenado con datos de vivienda de California. También incluye configuraciones para CI/CD utilizando GitHub Actions y DockerHub.

## Uso del Proyecto

### Ejecutar el Proyecto Localmente

1. Asegúrese de tener Python y Docker instalados en su máquina.

2. Instale las dependencias del proyecto utilizando pip:

```bash
pip install -r requirements.txt
```

3. Ejecute la aplicación Flask:

```bash
python app.py
```

La aplicación estará disponible en http://localhost:5000.

### CI/CD con GitHub Actions

Este proyecto está configurado para ejecutar pruebas automatizadas, construir la imagen de Docker y publicarla en DockerHub utilizando GitHub Actions.

## Contribuciones

¡Las contribuciones son bienvenidas! Si desea contribuir a este proyecto, siga estos pasos:

1. Fork este repositorio.
2. Cree una rama con el nombre de su característica: `git checkout -b nombre_de_la_caracteristica`.
3. Realice sus cambios y commits: `git commit -m "Agregado nuevo endpoint"`.
4. Empuje su rama a su repositorio fork: `git push origin nombre_de_la_caracteristica`.
5. Cree un pull request en el repositorio original.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo [LICENSE](LICENSE) para obtener más detalles.

### Para realizar la prediccion se debe ingresar el siguiente POST:

$headers = @{ "Content-Type" = "application/json" }
$body = @{
    "features" = [0.00632, 18.0, 2.31, 0, 0.538, 6.575, 65.2, 4.0900]
} | ConvertTo-Json

$response = Invoke-WebRequest -Uri "http://IP/predict" -Method POST -Headers $headers -Body $body
$response.Content

Esto por medio de PowerShell, recordar editar el IP.

## Saludos!