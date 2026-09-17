import asyncio
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters
import os
import tkinter as tk
from tkinter import filedialog
import platform
import subprocess
import shutil

MODELO= "qwen2.5:1.5b"
llm= ChatOllama(model= MODELO, temperature=0.1)

prompt_extractor= PromptTemplate.from_template(""" 
        Actúa como un analista de datos, extrae y cataloga cada una de las clases del archivo desestructurado.
        Identifica y clasifica las columnas más lógicas, por ejemplo: fechas, nombres de clientes, conceptos, monto, 
        productos, servicios,etc.
        Se conciso y devuelve únicamente la información estructurada en una lista, sin texto introductorio.\n\n
        Texto:\n{texto}              
""")

prompt_formato= PromptTemplate.from_template("""
        Actúa como un estricto formateador de archivos. Toma los adatos devueltos por el prompt_extractor y conviértela.
        Al convertirlo, usa SOLO un formato CSV delimitado por comas. La primera fila DEBE contener los encabezados normalizados. 
        No incluyas comillas invertidas de código, ni saludos, ni explicaciones o textos introductorios. Únicamente el texto del CSV en crudo.\n\n
        Información:\n{datos}
 """)

pipeline_extraccion= prompt_extractor | llm
pipeline_formato= prompt_formato | llm

async def inicio():
    root=tk.Tk()
    root.withdraw()
    
    print("Seleccione la carpeta en la que se encuentra el archivo a formatear...")
    entrada=filedialog.askopenfilename(title="Seleccionando archivo...",filetypes=[("Archivos de texto","*.txt"),("Todos los archivos","*.*")])
    
    if not entrada:
        print("Deteniendo proceso...")
        return
    
    directorio_actual=os.path.dirname(entrada)    
    #entrada=os.path.join(directorio_actual, "entrada.txt")
    salida=os.path.join(directorio_actual, "salida.csv")
    
    print(f"Carpeta en uso: {directorio_actual}")
    
    comando_npx = "npx.cmd" if platform.system() == "Windows" else "npx"
    ruta= shutil.which(comando_npx)
    if ruta is None:
        print(f"Error, no se encontró la ruta {ruta}")
        return
    print(f"Se encontró la ruta {ruta}")
    
    servidor= StdioServerParameters(command= ruta, args=["-y", "@modelcontextprotocol/server-filesystem", directorio_actual])
    #subprocess.run(servidor, check=True)
    
    print("Inicializando...")
    async with stdio_client(servidor) as (read, write):
        async with ClientSession(read,write) as consulta:
            await consulta.initialize()
            
            #Lectura MCP
            print(f"Leyendo archivo: {entrada}")
            resultado= await consulta.call_tool(
                "read_file", arguments={"path":entrada})
            texto_crudo= resultado.content[0].text
            
            #flujo LLM
            print("LLM 1: Extrayendo datos...")
            resultado_ext=pipeline_extraccion.invoke({"texto":texto_crudo})
            
            print("LLM 2: Actualizando formato...")
            formato= pipeline_formato.invoke({"datos":resultado_ext})
            
            # Limpiar posibles bloques de código de markdown residuales
            csv_final= formato.content.replace("```csv","").replace("```","").strip()
            
            #Escirtura MCP
            print(f"Guardando formato actualizado:{salida}")
            await consulta.call_tool(
                "write_file", arguments={"path":salida, "content":csv_final})
            
            print("¡Proceso completado con éxito!")

if __name__== "__main__":
    asyncio.run(inicio())
            
            
            
    




