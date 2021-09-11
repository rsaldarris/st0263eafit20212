
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

https://www.pragma.com.co/academia/lecciones/conozcamos-sobre-rabbitmq-sus-componentes-y-beneficios
https://www.rabbitmq.com/getstarted.html

## Mas acerca de RabbitMQ (Punto 10)
RabbitMQ implementa el protocolo mensajería de capa de aplicación AMQP (Advanced Message Queueing Protocol), el cual está enfocado en la comunicación de mensajes asíncronos con garantía de entrega, a través de confirmaciones de recepción de mensajes desde el broker al productor y desde los consumidores al broker.
En una forma simplificada, en RabbitMQ se definen colas que van a almacenar los mensajes que envían los productores hasta que las aplicaciones consumidoras obtienen el mensaje y lo procesan. Esto nos permite diseñar e implementar sistemas distribuidos, en los cuales un sistema se divide en módulos independientes que se comunican entre sí a través de mensajes.

Tipos de Mensaje:
![Directo](https://user-images.githubusercontent.com/37939454/132930207-abc94b1d-7b16-4479-b79c-53eef301ecca.jpg)
Un mensaje directo seria enviado a una unica direccion es decir a Apto 010
Un mensaje topic envia a un grupo que cumpla cierto requisito es decir, si digo envie a Apto 00*, se enviaria a la Apto 001 y 002
Un mensaje fanout seria enviado a todos
