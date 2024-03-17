# Moodle XML Creator

Este script convierte un conjunto de preguntas de un archivo de Excel al formato XML de Moodle para su uso en cuestionarios en línea.

## Requisitos

- Python 3.6 o superior
- Pandas
- lxml

Antes de ejecutar el script, asegúrate de que todas las dependencias están instaladas en tu entorno Python. Puedes instalarlas con pip:

```bash
pip install pandas lxml
```
## Uso
```bash
python create_moodle_xml.py /path/to/your/excel/file.xlsx
```


## Entrada
El archivo Excel debe tener el siguiente formato:

Una columna titulada Pregunta para el enunciado de la pregunta.
Cuatro columnas tituladas Opcion1, Opcion2, Opcion3, Opcion4 para las opciones de respuesta.
Una columna titulada Correcta que contiene el índice de la opción correcta (1, 2, 3 o 4).
Una columna titulada Explicación que proporciona retroalimentación o una explicación para la respuesta correcta.


## Salida
El script generará un archivo XML que puedes importar directamente en Moodle bajo la sección de cuestionarios.

luisaugustos@usal.es

