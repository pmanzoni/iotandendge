# IoT y Edge Computing: Historias de una relación necesaria

> "[XII Seminario de Invierno (tardío) CAPAP-H, Valencia, 6, 7 y 8 de abril de 2022](https://capap-h.ceta-ciemat.es/2022/02/22/xii-seminario-de-invierno-2022/)", Valencia, SPAIN

En este seminario tecnico, organizado en 4 sesiones, dos principalmente teóricas y dos principalmente practicas se intentará trazar el camino de acercamiento del IoT al edge computing, presentando, como resultado principal, el concepto de TinyML, es decir el uso del machine learning en dispositivos de 1 mW.

Se comenzará con una descripción de que es el IoT y cuales son sus varias componentes centrándonos en dos protocols de comunicación relevantes: LoRaWAN, como estándar de comunicación de baja potencia y MQTT como protocolo ampliamente utilizado para conectar dispositivos y servicios de una manera más flexible que las clásicas soluciones basadas en REST (HTTP).

El siguiente paso, en la primera sesión practica, será ofrecer una visión del camino de los datos, desde los sensores a través de las diferentes componentes de la red, gateways, networks servers, plataformas de visualización hasta llegar al “TIG stack” utilizado para facilitar la recopilación, el almacenamiento, la visualización y la generación de alertas a partir de series de datos temporales.

En las siguientes dos sesiones, se justificará la necesitad del edge computing en IoT y se describirá TinyML, que es un area en rápido crecimiento donde tecnologías y aplicaciones de aprendizaje automático, que incluye hardware, algoritmos y software, son capaces de realizar análisis de datos de sensores en dispositivos con un consumo de energía extremadamente bajo, normalmente en el rango de los mW y menos, y por lo tanto permitiendo una variedad de casos de uso más amplios dirigidos a dispositivos que funcionan con baterías. Se describirá, en la sesión de teoría, cual es el proceso de uso utilizando las librerías TensorFlow Lite y dispositivos como el Arduino Nano 33 BLE Sense y, en la sesión practica se utilizará la plataforma Edge Impulse, actualmente la plataforma de desarrollo líder para el ML en dispositivos edge, para construir un modelo en tiempo real utilizando el acelerómetro, el micrófono o la cámara de un smartphone, como recopilar datos y entrenar algoritmos de aprendizaje automático, y observar lo que ocurre en directo en la plataforma.

## Programa

### Jueves 7 de abril 2022
* 10:00 – 11:30 Seminario técnico (Teoría)
  * [A brief introduction to IoT, LoRaWAN, and MQTT](https://github.com/pmanzoni/iotandendge/blob/main/slides/IoT_LoRaWAN_MQTT.pdf)
* 15:30 – 17:30 Seminario técnico (Laboratorio)
  * [LoRaWAN and MQTT](https://hackmd.io/@capap-h2020/lorawanmqtt)

### Viernes 8 de abril 2022
* 10:00 – 11:30 Seminario técnico (Teoría)
  * [A brief introduction to TinyML](https://github.com/pmanzoni/iotandendge/blob/main/slides/TinyML_CAPAH.pdf)
  * [TinyML hands-on examples: TensorFlow Lite Micro](https://hackmd.io/@capap-h2020/tinymltlight)
* 12:00 – 13:30 Seminario técnico (Laboratorio)
  * [TinyML hands-on examples: Edge Impulse](https://hackmd.io/@capap-h2020/edgeimpulse)
