
# Topicos Especiales en Telemática Laboratorio 4

## Autor: Ricardo Saldarriaga Serna 201810038010

## Descripción
Este laboratorio se da para mostrar el conocimiento de los middleware, en este caso siendo el caso del RabbitMQ, teniendo en cuenta que un middleware es un elemento fundamental para el desarrollo y despliegue de los sistemas distribuidos ademas de ser un intermediario en aplicaciones/objetos/componentes/servicios distribuidos y los cuales requieren comunicarse entre si, por lo que nos es de gran ayuda para este fin. RabbitMQ funciona como un intermediario entre aplicaciones que pueden ser independientes entre si

## Instalación y Despliegue
Se debe hacer el paso a paso del documento [lab4-MOM-RabbitMQ.pdf](https://github.com/rsaldarris/st0263eafit20212/files/7141083/lab4-MOM-RabbitMQ.pdf) para poder llevar a cabo la instalacion del RabbitMQ

Se deben usar los siguientes comandos:

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

#### Instalar Pika
```sh
$ pip3 install pika
```

## Ejecución
Para la ejecución de la aplicación (chat) se debe de acceder a las diferentes instacias via SSH, clonar el repositorio y acceder a la carpeta del proyecto:

```sh
$ git clone https://github.com/rsaldarris/st0263eafit20212.git
$ cd st0263eafit20212/Lab4/
```


Despues de esto se debe de poner a correr el servidor con el comando que se muestra a continuación, teniendo en cuenta que el segundo argumento del comando debe de ser a IP pública del Servidor:

```sh
$ python3 Server4.py "IP_publica del Servidor"
```

Despues de que el servidor este corriendo se puede poner a correr los diferentes clientes con el siguiente comando, teniendo en cuenta que el primer argumento debe de ser la IP pública del Servidor:
```sh
$ python3 Cliente4.py "IP_publica del Servidor"
```

Despues de que los clientes estén conectados se les pedira su usuario y correo, y ya podran enviar los tasks que quieran realizar y el servidor los procesara


## Referencias

Para la creacion de este laboratorio se tuvo en cuenta los siguientes links

https://www.rabbitmq.com/getstarted.html
