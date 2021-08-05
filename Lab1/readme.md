<h2><b>Titulo</b></h2>
Lab1 Topicos telematicas
<h3><b>Nombre</b></h3>
Ricardo Saldarriaga Serna
<h3><b>Descripcion</b></h3>
Uno de los mecanismos de comunicación más básico es a través de Sockets, lo cual plantea una tubería o enlace de comunicación de intercambio de mensajes entre los procesos. Usando Python se crea de forma sencilla un chat grupal con la ayuda de lo anteriormente descrito
<h3><b>Descripcion y Despliegue</b></h3>
Se debe crear una instancia en EC2 de AWS
<br>Al crear en detalles de la Instancia se deben crear 3 instacias
<br>En la pagina de configuracion de Seguridad se agrega un nueva regla colocando en ella el <b>puerto</b> (dentro del codigo es el 3333, pero puede colocar el de su preferencia) a usar que se colocara en los archivos de python y colocando como origen cualquier ip
<br>Por comodidad nombrar a una de las instancias como servidor para tener en cuenta
<br> Abrir las diferentes instancias y a cada una le vamos a hacer los siguiente:
<code>
<br>sudo yum install git
<br>sudo yum install python3
<br>git clone https://github.com/rsaldarris/st0263eafit20212.git
</code>
<br>Despues de hacer esto procedemos a llegar a la carpeta del proyecto \st0263eafit20212\Lab1 y en todas las instancias vamos a cambiar en los 2 archivos cliente.py y servidor.py la ip (IP privada de la instancia al que le pusimos el nombre de servidor) y port que hayamos escogido en la configuracion de seguridad.
<code>
<br> cd st0263eafit20212/Lab1/
<br> nano cliente.py 
<br> nano servidor.py
</code>
<br>Una vez cambies los datos ya podemos ejecutar las instancias
<code>
<br> python3 servidor.py (para la instancia del servidor)
<br> python3 cliente.py (para la instancia del cliente)
<br> python3 cliente.py (para la instancia del cliente)
</code>