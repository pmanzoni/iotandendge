# IoT and edge computing: stories of a necessary relationship

In this technical seminar, organized in 4 sessions, two mainly theoretical and two mainly practical, we will try to trace the approach path from IoT to edge computing, presenting, as a main result, the concept of TinyML, i.e. the use of machine learning in 1 mW devices.

We will start with a description of what the IoT is and what are its various components, focusing on two relevant communication protocols: LoRaWAN, as a low power communication standard and MQTT as a widely used protocol to connect devices and services in a more flexible way than the classical REST (HTTP) based solutions.

The next step, in the first practical session, will be to provide an overview of the data path, from the sensors through the different network components, gateways, networks servers, visualization platforms up to the "TIG stack" used to facilitate the collection, storage, visualization and generation of alerts from time series data.

The next two sessions will justify the need for edge computing in IoT and describe TinyML, which is a rapidly growing area where machine learning technologies and applications, including hardware, algorithms and software, are capable of performing sensor data analysis on devices with extremely low power consumption, typically in the mW range and below, and thus enabling a variety of broader use cases targeting battery-powered devices. The theory session will describe the process of using the TensorFlow Lite libraries and devices such as the Arduino Nano 33 BLE Sense and the hands-on session will use the Edge Impulse platform, currently the leading development platform for ML on edge devices, to build a real-time model using the accelerometer, microphone or camera of a smartphone, how to collect data and train machine learning algorithms, and observe what happens live on the platform.

## Schedule at "[XII Seminario de Invierno CAPAP-H](https://capap-h.ceta-ciemat.es/2021/11/10/xii-seminario-de-invierno-capap-h-valencia-26-27-y-28-de-enero-de-2022/)", Valencia, 26, 27 y 28 de enero de 2022

### Jueves 27 de enero 2022:
* 10:00 – 11:30 Seminario técnico (Teoría)
    - [A brief introduction to IoT, LoRaWAN, and MQTT](https://github.com/pmanzoni/iotandendge/blob/main/slides/IoT_LoRaWAN_MQTT.pdf)
* 15:30 – 17:30 Seminario técnico (Laboratorio)
    - [LoRaWAN and MQTT](https://hackmd.io/@capap-h2020/lorawanmqtt)

Viernes 28 de enero 2022
* 10:00 – 11:30 Seminario técnico (Teoría)
    - TinyML with Tensorflow light and Arduino
* 12:00 – 13:30 Seminario técnico (Laboratorio)
    - TinyML with edgeimpulse
