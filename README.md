# Sistema de Gestión de Expedientes Electrónicos Judiciales

## Tabla de Contenidos
1. [Descripción](#descripción)
2. [Características](#características)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Instalación](#instalación)
5. [Uso](#uso)
6. [Manual Técnico](#manual-técnico)
7. [Manual de Usuario](#manual-de-usuario)
8. [Contribución](#contribución)
9. [Registro de Cambios](#registro-de-cambios)
10. [Créditos](#créditos)
11. [Licencia](#licencia)

## Descripción

El Sistema de Gestión de Expedientes Electrónicos Judiciales es una solución avanzada que combina automatización robótica de escritorio (RDA) con tecnologías modernas para optimizar la gestión de expedientes electrónicos en el ámbito judicial. Este sistema está diseñado para cumplir con los estrictos estándares del Plan Estratégico de Transformación Digital de la Rama Judicial, así como con los requisitos técnicos y funcionales del acuerdo PCSJA20-11567 de 2020, que establece el protocolo para la gestión de documentos electrónicos, su digitalización y la conformación del expediente electrónico, en su versión 2.

## Características Principales

- **Automatización de la Creación del Índice Electrónico**: El sistema automatiza el proceso de creación del índice electrónico, reduciendo significativamente el tiempo y los recursos necesarios para esta tarea crítica.
  
- **Extracción de Metadatos de Archivos**: Utiliza técnicas avanzadas para extraer metadatos de diversos tipos de archivos, asegurando una completa y precisa documentación de cada expediente.

- **Generación de Índices en Formatos Excel**: Facilita la generación de índices en formato Excel, compatible con las necesidades específicas de la gestión documental judicial.

- **Interfaces de Usuario Intuitivas**:
  - **Versión de Escritorio con PyQt5**: Ofrece una interfaz de usuario intuitiva y amigable, desarrollada con PyQt5, que permite una experiencia de usuario fluida y eficiente.
  - **Versión Web con Streamlit**: Además, cuenta con una interfaz web desarrollada utilizando Streamlit, que brinda flexibilidad y accesibilidad para usuarios que prefieren o necesitan interactuar a través de la web.

- **Cumplimiento con los Estándares Judiciales Colombianos**: El sistema se ajusta rigurosamente a los estándares y protocolos judiciales colombianos, garantizando su aplicabilidad y aceptación en el contexto legal y judicial del país.

Este proyecto representa un avance significativo en la gestión de expedientes electrónicos, ofreciendo una solución integral que no solo mejora la eficiencia y la precisión de los procesos judiciales, sino que también fomenta la transparencia y la accesibilidad de la información en el sistema judicial.

## Estructura del Proyecto
```
GestionExpedienteElectronico/
│
├── app.py
├── main.py
├── index_generator.py
├── file_utils.py
├── metadata_extractor.py
├── excel_handler.py
│
├── assets/
│   └── 000IndiceElectronicoC0.xlsm
│
├── tests/
│   └── test_expediente_processor.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalación

1. Clonar el repositorio:
git clone https://github.com/bladealex9848/GestionExpedienteElectronico.git

2. Navegar al directorio del proyecto:
cd GestionExpedienteElectronico

3. Crear un entorno virtual:
- En Windows:
  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```
- En macOS y Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

4. Instalar las dependencias:
```
pip install --upgrade pip
pip install watchdog
pip install -r requirements.txt
```

## Uso

Para ejecutar la versión de escritorio:
```
python app.py
```
Para ejecutar la versión web:
```
streamlit run main.py
```
Siga las instrucciones en la interfaz de usuario para cargar y procesar los expedientes.

## Manual Técnico

[Incluir aquí detalles técnicos del proyecto]

## Manual de Usuario

[Incluir aquí instrucciones detalladas para el usuario final]

## Contribución

Las contribuciones son bienvenidas. Por favor, siga estos pasos:

1. Haga fork del repositorio.
2. Cree una nueva rama (`git checkout -b feature/AmazingFeature`).
3. Haga commit de sus cambios (`git commit -m 'Add some AmazingFeature'`).
4. Haga Push a la rama (`git push origin feature/AmazingFeature`).
5. Abra un Pull Request.

## Registro de Cambios

- 2024-08-09: Actualización mayor (v.1.1.0)
  - Implementación de la versión de escritorio utilizando PyQt5.
  - Adición de la funcionalidad para generar índices tanto desde cero como utilizando una plantilla.
  - Mejora en la extracción de metadatos para soportar múltiples tipos de archivos.
  - Implementación de un manejador de Excel para crear y modificar archivos de índice.
  - Actualización de la estructura del proyecto para soportar tanto la versión web como la de escritorio.
  - Adición de pruebas unitarias para las nuevas funcionalidades.
  - Actualización de la documentación para reflejar los nuevos cambios y características.

- 2024-08-08: Primera versión. (v.1.0.0)
  - Lanzamiento inicial del Sistema de Gestión de Expedientes Electrónicos Judiciales.
  - Implementación de la versión web utilizando Streamlit.

## Créditos

Este proyecto es una evolución del trabajo inicial realizado por [HammerDev99 Daniel](https://github.com/HammerDev99/GestionExpedienteElectronico_Version1), a quien se le reconoce y agradece por sentar las bases de esta herramienta.

Desarrollado y mantenido por Alexander Oviedo Fadul, Profesional Universitario Grado 11 en el Consejo Seccional de la Judicatura de Sucre.

[GitHub](https://github.com/bladealex9848) | [Website](https://alexander.oviedo.isabellaea.com/) | [Instagram](https://www.instagram.com/alexander.oviedo.fadul) | [Twitter](https://twitter.com/alexanderofadul) | [Facebook](https://www.facebook.com/alexanderof/) | [WhatsApp](https://api.whatsapp.com/send?phone=573015930519&text=Hola%20!Quiero%20conversar%20contigo!)

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - vea el archivo [MIT License](https://opensource.org/licenses/MIT) para más detalles.