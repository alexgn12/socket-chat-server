# 💬 Socket Chat Server

Un chat local multicliente construido desde cero en Python utilizando sockets TCP, programación concurrente y una interfaz gráfica moderna con Tkinter.

---

## 🚀 Características implementadas

- ✅ **Servidor multicliente con `threading`**  
  Permite múltiples conexiones simultáneas mediante hilos, con gestión individualizada de cada cliente.

- ✅ **Cliente modular y reutilizable**  
  Separación del cliente en clases y módulos independientes para facilitar su mantenimiento y extensión.

- ✅ **Interfaz gráfica con `Tkinter`**  
  Interfaz limpia y funcional que permite enviar y recibir mensajes de forma cómoda. Cada cliente tiene su propia ventana gráfica.

- ✅ **Identificación por nombre de usuario**  
  Cada cliente introduce su nombre al conectarse, y los mensajes aparecen identificados.

- ✅ **Comando `/usuarios`**  
  El cliente puede escribir `/usuarios` en el chat para ver todos los usuarios actualmente conectados.

- ✅ **Registro de actividad en JSON (`logs.json`)**  
  El servidor genera automáticamente un archivo de logs con eventos clave: conexiones, desconexiones, y mensajes, todos con marca temporal.

---

## 📁 Estructura del proyecto
```
SocketChat/
├── ChatServer/
│ └── main.py # Servidor con threading, nombres y logging
├── ChatClient/
│ ├── client.py # Cliente modular con lógica de red
│ └── interfaz.py # GUI en Tkinter para enviar y recibir mensajes
├── logs.json # Archivo generado con eventos del servidor
├── README.md # Este archivo

```
---

## ⚙️ Requisitos

- Python 3.8 o superior
- Librerías estándar de Python:
  - `socket`
  - `threading`
  - `tkinter`
  - `json`

*No es necesario instalar paquetes externos.*

---

## ▶️ Cómo ejecutar

1. Ejecuta el **servidor**:

```
python ChatServer/main.py
En una o más terminales, ejecuta la interfaz gráfica del cliente:
```
Copiar
Editar
python ChatClient/interfaz.py
🔁 Puedes abrir varios clientes al mismo tiempo para simular una conversación multicliente en la red local.

📸 Capturas de pantalla (opcional)
<!-- Puedes añadir imágenes aquí más adelante si lo deseas --> <!-- ![chat gui](img/captura.png) -->
🛠️ Mejoras futuras (roadmap)
Añadir soporte para emojis o archivos adjuntos

Cifrado de mensajes punto a punto

Base de datos local (SQLite) para historiales persistentes

Panel de administración o moderación

Modo servidor remoto para conexiones externas (IPv4/IPv6)

🎓 Aprendizajes clave
Comunicación cliente-servidor mediante sockets TCP

Concurrencia en Python con threading

Estructuración de código modular y escalable

Diseño de interfaces con Tkinter

Gestión de datos en estructuras como diccionarios y listas

Logging estructurado en formato JSON
