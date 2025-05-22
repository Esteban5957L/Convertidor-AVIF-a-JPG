#!/usr/bin/env python3
"""
Script para convertir imágenes AVIF a JPG manteniendo la máxima calidad posible.
Requiere: pip install pillow pillow-heif
"""

import os
import sys
from pathlib import Path
from PIL import Image
import pillow_heif

# Registrar el soporte HEIF/AVIF
try:
    pillow_heif.register_heif_opener()
    print("✓ Soporte HEIF/AVIF registrado correctamente")
except Exception as e:
    print(f"✗ Error al registrar soporte HEIF/AVIF: {str(e)}")
    sys.exit(1)

def convert_avif_to_jpg(input_path, output_path=None, quality=95):
    """
    Convierte una imagen AVIF a JPG.
    
    Args:
        input_path (str): Ruta de la imagen AVIF de entrada
        output_path (str): Ruta de salida (opcional, se genera automáticamente si no se especifica)
        quality (int): Calidad de la imagen JPG (1-100, recomendado 90-100 para máxima calidad)
    
    Returns:
        bool: True si la conversión fue exitosa, False en caso contrario
    """
    try:
        # Verificar que el archivo existe
        if not os.path.exists(input_path):
            print(f"Error: El archivo {input_path} no existe.")
            return False
        
        # Generar nombre de salida automáticamente si no se especifica
        if output_path is None:
            input_file = Path(input_path)
            output_path = input_file.with_suffix('.jpg')
        
        # Abrir la imagen AVIF usando pillow_heif directamente
        heif_file = pillow_heif.read_heif(input_path)
        img = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
        )
        
        # Convertir a RGB si está en modo RGBA (para eliminar canal alpha)
        if img.mode in ('RGBA', 'LA'):
            # Crear fondo blanco
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'RGBA':
                background.paste(img, mask=img.split()[-1])  # Usar canal alpha como máscara
            else:
                background.paste(img, mask=img.split()[-1])
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Guardar como JPG con máxima calidad
        img.save(
            output_path, 
            'JPEG', 
            quality=quality,
            optimize=True,
            progressive=True
        )
        
        print(f"✓ Convertido: {input_path} → {output_path}")
        return True
        
    except Exception as e:
        print(f"✗ Error al convertir {input_path}: {str(e)}")
        return False

def convert_directory(input_dir, output_dir=None, quality=95):
    """
    Convierte todas las imágenes AVIF de un directorio a JPG.
    
    Args:
        input_dir (str): Directorio con imágenes AVIF
        output_dir (str): Directorio de salida (opcional)
        quality (int): Calidad de las imágenes JPG
    """
    input_path = Path(input_dir)
    
    if not input_path.exists():
        print(f"Error: El directorio {input_dir} no existe.")
        return
    
    # Crear directorio de salida si se especifica
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    
    # Buscar archivos AVIF
    avif_files = list(input_path.glob("*.avif")) + list(input_path.glob("*.AVIF"))
    
    if not avif_files:
        print(f"No se encontraron archivos AVIF en {input_dir}")
        return
    
    print(f"Encontrados {len(avif_files)} archivos AVIF para convertir...")
    
    successful = 0
    failed = 0
    
    for avif_file in avif_files:
        if output_dir:
            output_file = output_path / (avif_file.stem + '.jpg')
        else:
            output_file = avif_file.with_suffix('.jpg')
        
        if convert_avif_to_jpg(str(avif_file), str(output_file), quality):
            successful += 1
        else:
            failed += 1
    
    print(f"\n--- Resumen ---")
    print(f"✓ Convertidas exitosamente: {successful}")
    print(f"✗ Fallidas: {failed}")

def main():
    """Función principal con interfaz de línea de comandos básica."""
    
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python convertir_avif.py <archivo.avif>                    # Convertir un archivo")
        print("  python convertir_avif.py <directorio>                     # Convertir directorio")
        print("  python convertir_avif.py <archivo.avif> <salida.jpg>      # Especificar salida")
        print("  python convertir_avif.py <directorio> <dir_salida>        # Directorio con salida")
        print()
        print("Opciones de calidad (modifica la variable 'quality' en el código):")
        print("  90-95: Alta calidad, tamaño moderado")
        print("  96-100: Máxima calidad, mayor tamaño")
        return
    
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Configuración de calidad (puedes modificar este valor)
    quality = 95  # Cambia este valor entre 1-100 según tus necesidades
    
    if os.path.isfile(input_path):
        # Convertir archivo individual
        print(f"Convirtiendo archivo: {input_path}")
        convert_avif_to_jpg(input_path, output_path, quality)
    elif os.path.isdir(input_path):
        # Convertir directorio
        print(f"Convirtiendo directorio: {input_path}")
        convert_directory(input_path, output_path, quality)
    else:
        print(f"Error: {input_path} no es un archivo ni directorio válido.")

if __name__ == "__main__":
    main()
