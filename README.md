# Tarea 1 IE0521 IS 2024
## Estudiantes:
    - Jimena González
    - Juan Ignacio Hernández

## Descripción de los archivos desarrollados:
 - ie0521_bp.py: Predictor propuesto por los estudiantes, modelo de matriz en tres dimensiones utilizando perceptrones.
 - perceptron.py: Predictor basado en perceptrones propuesto por Jiménez y Lin.
 - pshared.py: Predictor de tipo p-share visto en clase implementado con tablas.

Todos los archivos corren en python, no se desarrolló nada en C.

## Ambiente de pruebas utilizado
 - Lenguaje escogido: python
 - Versión de python: 3.11.8
 - Dependencias: math
 - Sistema operativo utilizado: Manjaro Linux
 - Versión del kernel 5.15.154-1-MANJARO

## Cómo replicar las pruebas
 - Ejecutar el comando: `python3 branch_predictor.py`
 - Argumentos a usar según cómo se quiera configurar el predictor:
    - --bp: Qué predictor usar.
    - -g: Tamaño del registro de desplazamiento de la historia global (bits).
    - -n: Cantidad de bits del PC utilizados para indexar.

## Ejemplo de comandos ejecutados
 - `python3 branch_predictor.py  --bp 2 -n 12 -g 16`
 - `python3 branch_predictor.py  --bp 3 -n 4 -g 8`
 - `python3 branch_predictor.py  --bp 4`

## Cómo ejcutar la suite de pruebas utilizada
 - Correr: `bash Comandos_Resultados.txt` en la raíz del directorio del repositorio.


