# Experimento 2

## Integrantes

- Brayan Henao
- Rodrigo Escobar
- Felipe Cerquera
- Erik Loaiza

## Objetivo

El objetivo de este experimento es demostrar las estrategias de seguridad para la aplicación utilizando un API Gateway.

## Requisitos

- Tener instalado [Docker](https://docs.docker.com/install/)
- Tener instalado [Docker Compose](https://docs.docker.com/compose/install/)

## Despliegue

Para desplegar la aplicación, ejecutar el siguiente comando:

```bash
KONG_DATABASE=postgres docker compose --profile database up
```

Este comando desplegará:

- Una base de datos PostgreSQL
- Un API Gateway Kong
- Una aplicación de ejemplo en Flask
- Konga (Dashboard)

## Explicación servicios desplegados

### Base de datos (solo se creara, mas no se utilizara)

La base de datos se desplegará en el puerto `5432`. El usuario y contraseña de la base de datos es `kong`. La base de datos se llama `kong`. 

### API Gateway

El API Gateway se desplegará en el puerto 8000. El administrador del API Gateway se desplegará en el puerto 8001.

### Aplicación

La aplicación se desplegará en el puerto `5000`. La aplicación tiene el siguiente endpoint:

- `/api/v1/clients` - Endpoint protegido por OAuth2 (JWT)

 Este endpoint, será el encargado de devolver la información de los clientes, con los planes de venta y las ventas realizadas, además de validar que el usuario que ingresa tenga el rol `seller` y sea un usuario válido para consultar los datos.

 Esta app corre en el puerto `5000`, sin embargo este no es expuesto, ya que correrá en la red privada de docker y solo podrá ser accedida por otros servicios (el API Gateway lo expone). Para exponer la app descomentar la configuración de port en de la app en [docker-compose.yml](docker-compose.yml#L28)

### Dashboard

El dashboard se desplegará en el puerto `8080`. Este dashboard utiliza el API Gateway para obtener la información de
los servicios desplegados. Se utiliza Konga para el dashboard.

## Configuración

### Konga

#### Crear usuario de Konga

Para crear un usuario de Konga, ir a la url del dashboard de Konga [http://localhost:8080](http://localhost:8080) y crear un usuario.

![Create  User](./images/konga-create-user.png)

#### Generar un token de acceso para Konga (Dashboard)

Como estandar de seguridad, se debe proteger el admin API de Kong mediante un token de acceso, así Konga puede acceder
al API Gateway.

Para generar un token de acceso para Konga, ejecutar el siguiente comando:

```bash
./scripts/create-admin-key-auth.sh
```

Este comando generará un token de acceso para Konga. El token de acceso se mostrará en la consola al igual que los demás
campos qu debe llenar en Konga.

![Konga token](./images/register-konga-kong-admin-api.png)

##  OAuth2 Server

Proporcionamos un servidor ficticio para solicitudes de Oauth2 que se ejecuta de forma pública en [http://localhost:8080/](http://localhost:8080/) basado en la especificación de OpenID Connect (sobre Oauth2), al cual se puede acceder desde [http://localhost:8080/default/.well-known/openid-configuration](http://localhost:8080/default/.well-known/openid-configuration)

## Presentación

[Enlace a la presentación](https://docs.google.com/presentation/d/1uYt95urNN9boWJWflE8Pyh2lTtzfPkI7/edit?usp=sharing&ouid=114669455645104582686&rtpof=true&sd=true)
## Demo (video)


