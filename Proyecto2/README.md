# Proyecto 2

Carpeta del Proyecto 2 para la materia Tópicos especiales en Telemática - ST0263
Universidad EAFIT

# Autores

+ Ricardo Saldarriaga Serna
+ rsaldarris@eafit.edu.co
+ 201810038010

+ Federico Pérez Morales
+ fperezm1@eafit.edu.co
+ 201810008010

# Pre-requisitos

+ Cuenta en Google Cloud Platform (GCP)

# Descripcion

El desarrollo del presente proyecto está enfocado a la aplicación de los conocimientos adquiridos, específicamente al diseño, implementación y despliegue de una aplicación open source LAMP de comunidad que represente un sistema de información del tipo Sistema de Gestión de Contenidos (CMS), en esté caso Wordpress.

Para lograrlo debemos de seguir una serie de pasos enfocados al diseño lógico de la arquitectura y posteriormente ponerlo en práctica mediante el uso de Google Cloud Platafform (GCP) y Docker.

# Instalación

## Despliegue del proyecto en GCP

Para la implementación y el despliegue del laboratorio se siguieron los siguientes pasos:

## Desde Marketplace

### PARTE 1 - Crear WordPress
En el GCP entraremos al menu deplegable y buscaremos el marketplace, alli buscaremos la opcion de wordpress de bitnami, este nos pedira que habilitemos algunos apis, aceptaremos esto, y en pocos segundos tendremos wordpress desplegado, de aca tendremos en cuenta la IP que nos da la instancia.

### PARTE 2 - Crear dominio
Dentro del GCP en el menu desplegable buscaremos Red de VCP -> Direcciones IP Externa, buscaremos la IP de la instancia y la volveremos estatica, este nos pedira un nombre y se lo daremos.

Despues de tener la IP estatica, entraremos a freenom, buscamos este en google, creamos una cuenta y buscamos y creamos nuestro propio domino (por lo general seria sudomionio.tk) buscaremos Servicios de Red -> Servicios DNS, y con el dominio creado, le damos a la opcion de crear zona, el nombre sera a nuestro gusto pero el nombre DNS pondremos el dominio.

Una vez creado agregaremos 2 conjuntos de datos, el primero de ellos sera solo poner la direccion IP, en donde nos lo pide, en el segundo conjunto pondremos la misma IP pero en el nombre DNS pondremos el WWW

Una vez creado estos 2, buscaremos en el registro NS, mostramos las politicas de enrutamiento (expandiremos la info de este conjunto), y copiaremos esta informacion para pegarla dentro de freenom, en freenom, dentro de manage your domain, buscaremos la opcion de servername, la habilitaremos y colocaremos todas las que nos muestra el registro NS, despues guardaremos y ya estaria el dominio correcto.

### PARTE 3 - Certificado SSL

Nos meteremos dentro del SSH del GCP, lo cual es bastante sencillo, entraremos a la instancia y undiremos en el boton de SSH, ahora pondremos el siguiete comando:

```
sudo /opt/bitnami/bncert-tool
```
Seguiremos el paso a paso que nos pide, y ya tendremos el SSL

### PARTE 4 - Diferentes dominios

Volveremos a entrar a Servicios de Red -> Servicios DNS en la zona creada, y crearemos los registros necesarios con su respectiva IP


# Referencias
* https://docs.bitnami.com/general/how-to/generate-install-lets-encrypt-ssl/
* https://kinsta.com/blog/wordpress-on-google-cloud/
* https://www.youtube.com/watch?v=cG9kv5-5bPI


