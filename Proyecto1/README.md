# Proyecto 1

Carpeta del Proyecto 1 para la materia Tópicos especiales en Telemática - ST0263
Universidad EAFIT

# Autores

+ Federico Pérez Morales
+ fperezm1@eafit.edu.co
+ 201810008010

+ Ricardo Saldarriaga Serna
+ rsaldarris@eafit.edu.co
+ codigo

# Pre-requisitos

+ Sistema operativo Windows o Linux
+ Tener instalado Python 3.7 o Python 3.8 (Fue probado y es funcional en estas dos versiones del software)

# Descripcion

El desarrollo del presente proyecto está enfocado a la aplicación de los conocimientos adquiridos, específicamente al diseño, implementación y despliegue de una sala de chat con el uso de RPC el cual es un programa que utiliza una computadora para ejecutar código en otra máquina remota sin tener que preocuparse por las comunicaciones entre ambas,  gestionando asi la comunicación entre procesos de manera fiable y requiriendo un tiempo de procesamiento relativamente corto y usando HTTP/2.
Para lograrlo debemos de seguir una serie de pasos enfocados al diseño lógico de la arquitectura y posteriormente ponerlo en práctica mediante el uso de Python y AWS.

# Instalación

## Despliegue del proyecto en AWS

Para la implementación y el despliegue del laboratorio se siguieron los siguientes pasos:

### PARTE 1 - Montar el proyecto en AWS

+ Paso 1: Nos conectamos al curso en AWS educate.
+ Paso 2: Ingresar a la consola “AWS console”.
+ Paso 3: Nos dirigimos a servicios EC2 instances.
+ Paso 4: Presionamos en donde dice “launch instance”.
+ Paso 5: Se selecciona la siguiente Amazon Machine Image: (La que viene por defecto).
+ Paso 6: Seleccionamos t2.micro y luego continuamos.
+ Paso 7: Presionamos Next o Continuar (dependiendo del idioma) hasta llegar a “configure security groups”.
+ Paso 8: En “security groups” creamos una regla para TCP con el cual abrimos el puerto que deseamos usar.
+ Paso 9: Presionamos en “review and launch”.
+ Paso 10: Presionamos en “launch”.
+ Paso 11: Creamos una nueva “key pair” y le ponemos el nombre que queramos.
+ Paso 12: Descargamos la clave .pem ya mas adelante la necesitaremos.
+ Paso 13: Presionamos en “launch instance”.
+ Paso 14: Nos dirigimos a servicios ec2 Running Instances.
+ Paso 15: Presionamos en la instancia que acabamos de crear y copiamos la DNS que también será necesaria más adelante.

### PARTE 2 - Tutorial para Windows con el fin de estabalecer Conexión SSH y conectarnos a la máquina virtual

+ Paso 1: Instalar Putty (<https://www.putty.org/>).
+ Paso 2: Puede buscar en el directorio donde instalo putty, el ejecutable puttygen, y abrirlo o buscarlo en los programas instalados.
+ Paso 3: Dónde dice Type of key to generate, escogemos RSA.
+ Paso 4: Presiona Load. Por defecto, PuTTYgen solo nos muestra los archivos con extension .ppk. Para localizar tu archivo .pem, se escoge la opción para poder ver todos los tipos de archivos. (Escoge su archivo pem   el cual descargó en el paso 12 del tutorial anterior).
+ Paso 5: Si siguió los pasos correctamente la key se generara en formato .ppk.
+ Paso 6: Después de presionar en Aceptar, presione en “save private key” y guárdela. Esta clave la usaremos después para conectarnos con putty al servidor de Amazon. Presione que si al aviso que sale, y luego se guarda la clave con el nombre queramos (se generará un archivo .ppk).
+ Paso 7: Abir putty.
    + Nos dirigmos a Connection, SSH, Auth, y cargamos la clave .ppk que transformó anteriormente.
    + Regresamos a sesión y en donde dice hostname colocamos ``` ec2-user@"public dns de su instancia" ```. (sin los ")
    EJEMPLO:
    ```
    $ ec2-user@ec2-54-196-113-35.compute-1.amazonaws.com
    ```
    + Luego en saved session, colocamos un nombre para guardar la configuración (ejemplo: ProyectoTelematica) y luego de presionamos en “Save” para qu e la configuración quede guardada, y la próxima vez, solo sea cargarla.
    + Por ultimo de click en Open, y presionamos que sí en el aviso que sale.
    + Si todo salió bien, deberá ver una terminal

### PARTE 3 - Instalar librerías en nuestra máquina virtual

+ Paso 1: Ejecutamos el siguiente comando desde SSH (putty) para actualizar el sistema.
```
sudo yum update
```
+ Paso 2: Instalar recursos
```
sudo yum install git -y
sudo yum install pip -y
sudo yum install docker -y
pip3 install cassandra-driver
pip3 install pandas
```

### PARTE 4 – Descargar los archivos

+ Paso 1: Clone el git
Abra el proyecto en GitHub, y luego copie su ruta para poder clonarlo.
+ Paso 2: Aplique el siguiente comando:
```
$ sudo git clone <URL PROYECTO>
```
Ejemplo:
```
$ sudo git clone <https://github.com/usuario/proyecto.git>
```

# Ejecución

+ Paso 1: Ya dentro de la instacias que creamos, nos dirigimos al respectivo directorio del laboratorio.
```
$ cd "carpeta"
```
+ Paso 2: Ejecutamos el archivo del servidor y se introduce la información solicitada, en el caso de IP se utiliza 0.0.0.0.
```
$ pythton3 server.py
```
+ Paso 3: En una instancia distinta a la del servidor,ejecutamos el archivo del cliente y se introduce la información solicitada.
```
$ pythton3 client.py
```
+ Paso 4: Escribir los mensajes con los clientes ya conectados al seridor y ver como el chat estará en funcionamiento.


docker login
docker pull datastax/dse-server:6.8.14
docker run -p 9042:9042 -e DSLICENSE=accept --memory 1g --name cassandra1proyecto -d datastax/dse-server:6.8.14 -g -s -k

# Referencias:
A continuación se encuentran las paginas de las cuales se investigó para desarrollar el código.

+ [OpenWebinars](https://openwebinars.net/blog/como-usar-apache-cassandra-con-python/)
