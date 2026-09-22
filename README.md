
# Organizador-CSV

Selecciona un archivo .txt con los datos semanales que quieras recabar y recibe un archivo .csv con la información tabulada.

#### Conversor Inteligente de Datos Desestructurados a CSV/Excel

- Script al que le adjuntamos un archivo de texto plano con información desordenada (como un correo con una lista de compras, un reporte de gastos copiado y pegado, o un registro de clientes) y lo convierte en un archivo tabular estructurado.

- La herramienta funciona a través de un modelo de inteligencia artificial ligero en local. Internamente la gobiernan dos modelos de lenguaje (LLM), quienes se especializan en instrucciones específicas como extraer y posteriormente dar formato a la información de un archivo dado por el usuario.
![Logo](https://images.seeklogo.com/logo-png/48/1/python-logo-png_seeklogo-480570.png)


## Insignias

[![Python](https://img.shields.io/badge/Python-3.14%2B-blue?logo=python&logoColor=white)](https://www.python.org/)

[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-lightgrey?logo=ollama&logoColor=black)](https://ollama.com/)

[![Qwen 2.5](https://img.shields.io/badge/LLM-Qwen%202.5%201.5B-orange?logo=alibabacloud&logoColor=white)](https://huggingface.co/Qwen)

[![LangChain](https://img.shields.io/badge/LangChain-Integration-yellow?logo=chainlink&logoColor=white)](https://www.langchain.com/)
[![MCP](https://img.shields.io/badge/MCP-Multi%20Context%20Protocol-purple?logo=protocols&logoColor=white)](https://modelcontextprotocol.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Requisitos previos

1. Instala Ollama para ejecutar modelos localmente.

```bash
https://ollama.com/download/windows
```
2. Después de correr Ollama por primera vez, haz clic en "Permitir acceso para redes privadas" y mantén abierta la aplicación de escritorio.

3. En el CMD, ejecuta:

```bash
ollama pull qwen2.5:1.5b
```
4. Descarga Node Js en su última versión LTS (Soporte a largo plazo):

```bash
https://nodejs.org/
```
5. Abre el archivo que se descargó. Sigue las instrucciones del instalador haciendo clic en "Next".

#### Importante: 
Deja todas las opciones por defecto. El instalador automáticamente agregará Node.js al "PATH" de tu sistema

6. Reinicia tu computadora.

7. Finalmente, abre nuevamente tu terminal (Busca cmd o Símbolo del sistema en Windows).

Escribe npx -v y presiona Enter.

Si te da la versión del programa (por ejemplo, 10.8.2), significa que todo está listo para que ejecutes el main.exe.

## Correr en local

Para utilizar esta aplicación debes:

1. Descarga el ejecutable desde Releases en el repositorio:

```bash
https://github.com/HamletNerey/Organizador-CSV/releases/tag/v1.0.0
```
2. Ejecuta el programa dando doble click y comprueba su funcionamiento seleccionando un archivo .txt desde tu explorador de archivos.

## License

[MIT](https://choosealicense.com/licenses/mit/)

