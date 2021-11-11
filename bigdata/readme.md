# Laboratorios BigData

## Autores Ricardo Saldarriaga Serna

## Laboratorio 0
### Descripcion
En este Laboratirio se creara un cluster con EMR de AWS, siguiendo el paso a paso de los videos:
- https://www.youtube.com/watch?v=MyXSwxN5Zdk&ab_channel=EdwinNelsonMontoya
- https://www.youtube.com/watch?v=3sao-qJG34Y&ab_channel=EdwinNelsonMontoya

Para poder hacer el laboratorio se necesitara una cuenta en AWS Educate, un par de claves de AWS para poder configurar el cluster y un bucket que crearemos en S3.

Al crearlo debemos meternos en opciones avanzadas y poner las siguientes opciones:
- Seleccionar la version emr-6.3.1
- Seleccionaremos Hadoop 3.2.1, JupyterHub 1.2.0, Hive 3.1.2, Sqoop 1.4.7, Zeppelin 0.9.0, Tez 0.9.2, JupyerEnterpriseGateway 2.1.0, Hue 4.9.0, Spark 3.1.1, Livy 0.7.0, HCatalog 3.1.2
- Seleccionaremos las 2 opciones del AWS Glue Data Catalog Settings
- Y en el edit software settings, colocaremos lo siguiente:
```
[
    {
        "Classification": "jupyter-s3-conf",
        "Properties": {
            "s3.persistence.enabled": "true",
            "s3.persistence.bucket": "<Nombre del Bucket S3>"
        }
    }
]
```
- Le daremos a Next y en la pestaña del Hardware cambiaremos los tipos de Instancia que aparecen en la pestaña de Cluster Nodes and Instances, los cambiaremos de m5.xlarge a los m4.xlarge y cambiaremos de On-demand a Spot
- La autoterminacion la activaremos y la dejaremos en 1 hora
- El EBS Root Volumen lo cambiaremos de 10 a 20gb
- Next, le pondremos el nombre que queramos al Cluster, Next y pondremos el par de claves que creamos con anterioridad.
-  Con eso ya hemos terminado, tendremos nuestro cluster creado.

### Informacion
#### Cluster EMR Aws
Amazon EMR (anteriormente conocido como Amazon Elastic MapReduce) es una herramienta de Amazon Web Services (AWS) para el procesamiento y análisis de big data. Amazon comercializa EMR como un servicio expandible y de baja configuración que brinda una alternativa a la ejecución de la computación en clúster local.

#### Bucket S3
Amazon Simple Storage Service (Amazon S3) es un servicio de almacenamiento de objetos que ofrece escalabilidad, disponibilidad de datos, seguridad y rendimiento líderes en el sector. Gracias a Amazon S3, clientes de todos los tipos y sectores pueden almacenar y proteger cualquier volumen de datos para los más variados fines, como usarlos en lagos de datos, sitios web, aplicaciones móviles, procesos de copia de seguridad y restauración, operaciones de archivado, aplicaciones empresariales, dispositivos IoT y análisis de big data.

#### Spark Aws
Apache Spark es un motor de análisis unificado para el procesamiento de datos distribuidos a gran escala. Por lo general, las empresas con cargas de trabajo basadas en Spark en AWS usan su propia pila construida sobre Amazon Elastic Compute Cloud (Amazon EC2) o Amazon EMR para ejecutar y escalar Apache Spark, Hive, Presto y otros marcos de big data.

#### JupyterHub
Jupyter Notebook es una aplicación web de código abierto que puede utilizar para crear y compartir documentos que contienen código en vivo, ecuaciones, visualizaciones y texto narrativo. JupyterHub le permite alojar varias instancias de un servidor de cuadernos Jupyter de un solo usuario. Cuando crea un clúster con JupyterHub, Amazon EMR crea un contenedor Docker en el nodo principal del clúster. JupyterHub, todos los componentes necesarios para Jupyter y Sparkmagic se ejecutan dentro del contenedor.

#### Hive Aws
Apache Hive es un sistema de almacenamiento de datos distribuido y tolerante a fallas que permite el análisis a gran escala. Un almacén de datos proporciona un almacén central de información que se puede analizar fácilmente para tomar decisiones informadas y basadas en datos. Hive permite a los usuarios leer, escribir y administrar petabytes de datos mediante SQL.

#### Zeppelin Aws
Utilice Apache Zeppelin como un cuaderno para la exploración de datos interactiva. Para obtener más información sobre Zeppelin, consulte https://zeppelin.apache.org/. Zeppelin se incluye en las versiones 5.0.0 y posteriores de Amazon EMR. Las versiones anteriores incluyen Zeppelin como una aplicación de espacio aislado. Para obtener más información, consulte las versiones de lanzamiento de Amazon EMR 4.x.

## Laboratorio 1

Entraremos por SSH a la instancia del Cluster, tendremos como entrar con las instrucciones que nos proporciona el mismo cluster

- Instalaremos git con el comando y clonaremos el repo:
```
sudo yum install git
git clone https://github.com/st0263eafit/st0263_20212.git
```
- Crearemos la carpeta datasets (en el hdfs) y entraremos en los datasets
```
cd st0263_20212/bigdata/datasets/
hdfs dfs -mkdir /user/hadoop/datasets
```
- Ahora pasaremos lo que tenemos dentro de nuestro local (los datasets que tenemos del repo al hdfs)

```
hdfs dfs -copyFromLocal ./* /user/hadoop/datasets/
```
- Dentro del Hue, nos meteremos para crear la carpeta datasets en el S3
- Ahora por ultimo pasaremos estos datos a nuetro bucket en S3 para que se guarden

```
hadoop distcp /user/hadoop/datasets/* s3a://datasetsrsaldarris/datasets/
```
De esta forma tenemos todo guardado en el bucket
## Referencias
- https://searchaws.techtarget.com/definition/Amazon-Elastic-MapReduce-Amazon-EMR
- https://aws.amazon.com/es/s3/
- https://aws.amazon.com/es/big-data/what-is-hive/
- https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyterhub.html
- https://aws.amazon.com/es/blogs/machine-learning/running-on-demand-serverless-apache-spark-data-processing-jobs-using-amazon-sagemaker-managed-spark-containers-and-the-amazon-sagemaker-sdk/
- https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-zeppelin.html


