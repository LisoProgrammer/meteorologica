# Meteorológica

## 🌤️ Descripción

**Meteorológica** es una aplicación diseñada para monitorear y analizar datos meteorológicos en tiempo real. Utilizando una arquitectura basada en microservicios, el sistema se compone de tres componentes principales:

- **Producer**: Encargado de obtener datos meteorológicos de diversas fuentes.
- **Consumer**: Responsable de procesar y almacenar los datos obtenidos.
- **DB**: Base de datos que almacena la información procesada para su posterior análisis.

Este enfoque modular permite una fácil escalabilidad y mantenimiento del sistema.

## 🛠️ Tecnologías utilizadas

- **Python**: Lenguaje principal para el desarrollo de los microservicios.
- **Docker**: Contenerización de los servicios para facilitar su despliegue y ejecución.
- **Docker Compose**: Orquestación de los contenedores para una gestión eficiente de los servicios.

## 🚀 Instrucciones de uso

### Requisitos previos

Antes de ejecutar la aplicación, asegúrate de tener instalados los siguientes programas:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Pasos para ejecutar la aplicación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/LisoProgrammer/meteorologica.git
   cd meteorologica
2. Construye y levanta los contenedores:
    ```bash
   docker-compose up
3. Accede a la aplicación a través de los puertos configurados en el archivo docker-compose.yml
## 📂 Estructura del proyecto
    ```bash
    meteorologica/
    ├── consumer/
    ├── db/
    ├── producer/
    ├── .env
    ├── docker-compose.yml
    └── README.md

1. consumer/: Código fuente del microservicio Consumer.

2. db/: Scripts y configuraciones para la base de datos.

3. producer/: Código fuente del microservicio Producer.

4. .env: Variables de entorno para la configuración del sistema.

5. docker-compose.yml: Archivo de configuración para Docker Compose.

6. README.md: Este archivo.
