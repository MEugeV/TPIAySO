# Universidad Tecnológica Nacional

# TECNICATURA EN PROGRAMACIÓN A DISTANCIA

# Materia: Arquitectura y Sistemas Operativos

## Trabajo Integrador

## Virtualización con Docker

## Profesor

- Profesor: Patricio Costello

## Integrantes

- Jeremias Wilvers Ocampo
- María Eugenia Vogt

# Contenerización de una Aplicación con Redis y Python

Este proyecto conteneriza una aplicación Python que gestiona "favoritos" de usuarios utilizando Redis como base de datos en memoria. Se utiliza Docker y Docker Compose para facilitar la configuración y ejecución del entorno.

## Requisitos

- [Docker](https://www.docker.com/products/docker-desktop/)

## Instalación y Ejecución

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/MEugeV/TPIAySO.git
   cd TPIAySO

2. Levantar Redis con Docker Compose:

    ```bash
    docker compose up -d redis

3. Levantar y acceder al contenedor del servidor para ejecutarlo:
    ```bash
    docker compose run --rm servidor

## Funcionamiento
- Permite agregar, consultar y eliminar "favoritos" de distintas colecciones por usuario.
- Utiliza Redis para almacenar la información en memoria.
- El servidor está hecho en Python y se conecta al contenedor de Redis usando la red interna de Docker.
