# Topicos Especiales en Telemática Laboratorio 2

## Autor: Ricardo Saldarriaga Serna

## Descripción
En el segundo laboratorio de la materia se podrá evidenciar el uso del protocolo HTTP, con el objetivo de crear una aplicación de chat grupal, siendo la arquitectura de este Cliente/Servidor, haciendo posible que dos o más clientes se puedan comunicar entre ellos por medio del chat, con la condición de que el servidor este corriendo. Para hacer esto posible se usarán instancias EC2 de AWS, siendo una la que actue como servidor y el resto como clientes.

Al estar usando HTTP como protocolo, tendremos metodos GET,POST,PUT y DELETE, estos son usados para poder recibir informacion (GET), enviar informacion (POST), actualizar informacion (PUT) y eliminar informacion (DELETE), ademas que para cada respuesta que da el servidor al cliente son referenciados por numeros de 3 cifras:

**Respuestas informativas** son los 1XX, como lo es 100 para continuar

**Peticiones Correctas** son los 2XX, siendo 200 la respuesta estandar para una peticion correcta

**Redirecciones** son las 3XX

**Errores del cliente** son las 4XX, siendo 404 la respuesta para un recurso no encontrado

**Errores del servidor** son las 5XX, siendo 504 la respuesta a que no ha recibido a tiempo la respuesta de otro servidor

Por lo que siempre desde nuetro cliente que enviemos una peticion al servidor usando cualquiera de los metodos anteriormente descritos recibiremos una de estas respuestas tambien llamadas status

## Instalación y Despliegue
Para ver la aplicación en funcionamiento se deben de instanciar como minimo 3 instancias EC2 en AWS, siendo una de estas la que actuará como servidor, que además se le debe de asociar una IP elástica, y las otras como clientes que enviaran mensajes en el chat. Se usarán dos grupos de seguridad (SG), uno para el servidor y otro para los clientes, el SG del servidor debe tener una regla de entrada con el tipo en ***Custom TCP***, para este caso se seleccionó el puerto 1543, abierto para cualquier IP, pero se puede escoger uno diferente siendo mayor al puerto 1100. Asimismo el SG de los clientes es casi igual al del servidor con la diferencia de que no debe estar abierto para cualquier IP, unicamente debe estar abierto para la IP pública del Servidor.

Para un funcionamiento correcto las instancias deben de contar con git, python3 y un editor de texto de preferencia, por defecto la mayoría de máquinas traen VIM.

***¡Tener en cuenta que para poder ejecutar los comandos a continuación se debe de acceder a las diferentes instancias via SSH!, en la parte de ejecución hay un ejemplo del comando para realizar esta conexión.***

Se puede usar los siguientes comandos:

#### Instalar Git
```sh
$ sudo yum install git
```

#### Instalar Python3
```sh
$ sudo yum install python3
```

#### Instalar Emacs
```sh
$ sudo yum install emacs
```

## Ejecución
Para la ejecución de la aplicación (chat) se debe de acceder a las diferentes instacias via SSH, clonar el repositorio y acceder a la carpeta del proyecto:

```sh
$ ssh -i "Par de claves utilizado para crear las instancias(*.pem)" ec2-user@"DNS de IPv4 pública de la instancia"
$ git clone https://github.com/rsaldarris/st0263eafit20212.git
$ cd st0263eafit20212/Lab2/
```


Despues de esto se debe de poner a correr el servidor con el comando que se muestra a continuación, teniendo en cuenta que el segundo argumento del comando debe de ser el puerto que escogió al configurar los SG:

```sh
$ python3 Server2.py 0.0.0.0 "El_puerto_designado(1543)"
```

Despues de que el servidor este corriendo se puede poner a correr los diferentes clientes con el siguiente comando, teniendo en cuenta que el primer argumento debe de ser la IP pública del Servidor y el segundo argumento debe de ser el mismo puerto del comando anterior:
```sh
$ python3 Cliente2.py "IP_publica del Servidor" "El_puerto_designado(1543)"
```

Despues de que los clientes estén conectados (el servidor te lo hará saber con un mensaje), se podrán mensajear entre ellos.

Los clientes actualizaran los mensajes recibidos por otros clientes una vez envien un mensaje, por lo que no es a tiempo real los mensajes, si entras al chat deberas escribir un mensaje o simplemente enviar un vacio (undir el enter) para actualizar los mensajes que han sido enviados por otros Usuarios (clientes)

## Referencias

Para la creacion de este laboratorio se tuvo en cuenta los siguientes links

https://docs.python.org/3/library/http.client.html

https://docs.python.org/3/library/http.server.html

https://gist.github.com/junian/99e402db918cbe150002dc8c6736feb6

https://github.com/Shiroke-013/TET_LAB1/edit/main/README.md (Usado para ver como se debe hacer un buen README.md para la materia Topicos Especiales en Telemática)