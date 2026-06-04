# Análisis de Ventas y Flujo de Trabajo con Git  
Trabajo Práctico N°2 – Organización Empresarial  
Tecnicatura Universitaria en Programación – UTN

## Descripción del Proyecto
Este repositorio contiene el desarrollo del Trabajo Práctico N°2 de la materia Organización Empresarial, integrando herramientas de gestión colaborativa, control de versiones y análisis de datos mediante Jira, Git, GitHub y Google Colab.

El objetivo principal es simular el funcionamiento de una célula de desarrollo ágil, aplicando roles definidos, trazabilidad mediante issues, commits estructurados y Pull Requests.  
Además, se desarrolla un análisis de datos utilizando Python para procesar un dataset de ventas y generar indicadores clave.

## Escenario Elegido
Escenario B – Análisis de Ventas de una Pequeña Empresa.

El proyecto analiza un archivo CSV con información de ventas, incluyendo:
- Producto  
- Cantidad vendida  
- Precio  
- Fecha de venta  

## Estructura del Repositorio

tp2-OE-Ventas_Alexis-Ortiz/
│
├── datos/
│   └── ventas.csv
│
├── scripts/
│   └── analisis_ventas.py
│
├── resultados/
│   ├── resumen_ventas.csv
│   ├── ventas_por_mes.csv
│   ├── ventas_por_dia.csv
│   └── grafico_ventas_diarias.png
│
├── README.md
└── .gitignore


## Funcionalidades del Script

El archivo `analisis_ventas.py` realiza:
- Lectura del dataset con `csv.DictReader`
- Conversión de tipos (int, float, datetime)
- Cálculo de:
  - Ventas totales
  - Producto más vendido (con `collections.Counter`)
  - Ventas por mes
  - Ventas por día
- Exportación de resultados a CSV
- Generación de un gráfico de evolución de ventas diarias

## Instrucciones para Ejecutar el Script en Google Colab

1. Abrir Google Colab  
2. Ejecutar:

!git clone https://github.com/TheGalaxis/tp2-OE-Ventas_Alexis-Ortiz.git
%cd tp2-OE-Ventas_Alexis-Ortiz


3. Ejecutar el script:

!python scripts/analisis_ventas.py

4. Ver los resultados generados en la carpeta `/resultados`.

## Autenticación para Push desde Google Colab

Debido a las restricciones del entorno, el push debe realizarse inyectando el token en la URL:
!git push https://{TOKEN}@github.com/TheGalaxis/tp2-OE-Ventas_Alexis-Ortiz.git feature/analisis-ventas


## Requerimientos

- Python 3.x  
- Google Colab  
- Librerías estándar: csv, datetime, collections, matplotlib  

## Autor

Alexis Leonel Ortiz  
Tecnicatura Universitaria en Programación  
Universidad Tecnológica Nacional  
2026
