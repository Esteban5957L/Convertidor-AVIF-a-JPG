# 🖼️ Convertidor AVIF a JPG

Un script de Python simple y eficiente para convertir imágenes del formato AVIF a JPG manteniendo la máxima calidad posible.

## ✨ Características

- ✅ **Alta calidad**: Convierte manteniendo calidad de imagen óptima (configurable)
- ✅ **Procesamiento por lotes**: Convierte carpetas completas automáticamente
- ✅ **Manejo de transparencia**: Convierte automáticamente canales alpha a fondo blanco
- ✅ **Detección automática**: Encuentra archivos `.avif` y `.AVIF`
- ✅ **Reporte detallado**: Muestra progreso y resumen de conversiones
- ✅ **Multiplataforma**: Compatible con Windows, Mac y Linux

## 📋 Requisitos

- Python 3.7 o superior
- Librerías: `pillow` y `pillow-heif`

## 🚀 Instalación

### 1. Instalar Python

#### Windows:
- **Opción A**: Desde [Microsoft Store](https://apps.microsoft.com/store/detail/python-312/9NCVDN91XZQP) (recomendado)
- **Opción B**: Desde [python.org](https://www.python.org/downloads/) 
  - ⚠️ **Importante**: Marcar "Add Python to PATH" durante la instalación

#### Mac:
```bash
# Con Homebrew
brew install python

# O descargar desde python.org
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 2. Verificar instalación
```bash
python --version
pip --version
```

### 3. Instalar dependencias
```bash
pip install pillow pillow-heif
```

### 4. Descargar el script
Descarga `convertir_avif.py` y guárdalo en una carpeta de fácil acceso.

## 📖 Uso

### Sintaxis básica:
```bash
python convertir_avif.py <origen> [destino]
```

### Ejemplos de uso:

#### 🔹 Convertir un archivo individual:
```bash
# Genera imagen.jpg en la misma carpeta
python convertir_avif.py imagen.avif

# Especificar nombre de salida
python convertir_avif.py imagen.avif mi_foto.jpg
```

#### 🔹 Convertir toda una carpeta:
```bash
# Convierte todas las AVIF de la carpeta (JPG en misma ubicación)
python convertir_avif.py "/ruta/a/imagenes"

# Convertir a carpeta separada
python convertir_avif.py "/ruta/origen" "/ruta/destino"
```

#### 🔹 Ejemplos específicos por sistema:

**Windows:**
```bash
# Archivo individual
python convertir_avif.py "C:\Imagenes\foto.avif"

# Carpeta completa
python convertir_avif.py "C:\Imagenes\AVIF" "C:\Imagenes\JPG"

# Si la ruta tiene espacios, usar comillas
python convertir_avif.py "C:\Mi Carpeta\Fotos"
```

**Mac/Linux:**
```bash
# Archivo individual
python convertir_avif.py ~/Pictures/foto.avif

# Carpeta completa
python convertir_avif.py ~/Pictures/AVIF ~/Pictures/JPG
```

## ⚙️ Configuración

### Ajustar calidad de imagen:
Edita la línea 107 en el script:
```python
quality = 95  # Cambia este valor (1-100)
```

**Valores recomendados:**
- `90-95`: Alta calidad, tamaño moderado
- `96-100`: Máxima calidad, mayor tamaño de archivo
- `85-89`: Buena calidad, archivos más pequeños

## 📁 Estructura de salida

```
📂 Carpeta Original/
├── foto1.avif
├── foto2.avif
├── foto1.jpg          ← Convertida
└── foto2.jpg          ← Convertida
```

Con carpeta de destino:
```
📂 Origen/              📂 Destino/
├── foto1.avif         ├── foto1.jpg
└── foto2.avif         └── foto2.jpg
```

## 🖥️ Ejemplo de ejecución

```bash
$ python convertir_avif.py "C:\Fotos\Vacaciones"

✓ Soporte HEIF/AVIF registrado correctamente
Convirtiendo directorio: C:\Fotos\Vacaciones
Encontrados 3 archivos AVIF para convertir...
✓ Convertido: C:\Fotos\Vacaciones\playa.avif → C:\Fotos\Vacaciones\playa.jpg
✓ Convertido: C:\Fotos\Vacaciones\montaña.avif → C:\Fotos\Vacaciones\montaña.jpg
✓ Convertido: C:\Fotos\Vacaciones\ciudad.avif → C:\Fotos\Vacaciones\ciudad.jpg

--- Resumen ---
✓ Convertidas exitosamente: 3
✗ Fallidas: 0
```

## 🔧 Troubleshooting

### ❌ Error: `'python' no se reconoce`
**Windows:**
- Reinstala Python marcando "Add Python to PATH"
- O usa `py` en lugar de `python`: `py convertir_avif.py imagen.avif`

### ❌ Error de instalación `pillow-heif`
```bash
# Actualizar pip primero
pip install --upgrade pip

# Reinstalar dependencias
pip install --upgrade pillow pillow-heif
```

### ❌ Error: `No module named 'pillow_heif'`
```bash
pip uninstall pillow-heif
pip install pillow-heif
```

### ❌ Archivo no encontrado
- Verifica que la ruta sea correcta
- Usa comillas si la ruta contiene espacios
- En Windows, puedes arrastrar archivos al CMD para obtener la ruta automáticamente

## 🚀 Uso avanzado

### Crear script .bat para Windows (arrastrar y soltar):
Crea un archivo `convertir.bat`:
```batch
@echo off
python "C:\ruta\al\convertir_avif.py" %1
pause
```

Arrastra archivos AVIF sobre este `.bat` para conversión automática.

### Integración con sistemas de build:
```bash
# Ejemplo para procesar assets de un proyecto
python convertir_avif.py "./src/assets/images" "./public/images"
```

## 🔍 Detalles técnicos

- **Formato de entrada**: AVIF (Advanced Video Coding)
- **Formato de salida**: JPEG (Joint Photographic Experts Group)
- **Calidad**: Compresión con pérdida mínima configurable
- **Transparencia**: Convierte canal alpha a fondo blanco
- **Optimización**: Usa compresión progresiva y optimizada

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Notas

- La conversión de AVIF (sin pérdida) a JPG (con pérdida) implica ligera degradación
- Para conservar calidad al 100%, considera PNG como alternativa
- Los archivos AVIF originales nunca se modifican o eliminan
- El script es seguro para usar en carpetas con archivos mixtos

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

---

### 🛠️ Desarrollado con:
- **Python** - Lenguaje de programación
- **Pillow** - Procesamiento de imágenes
- **pillow-heif** - Soporte para formatos HEIF/AVIF

### 📞 Soporte
Si encuentras algún problema o tienes sugerencias, por favor abre un issue en el repositorio.

---
⭐ Si este proyecto te fue útil, considera darle una estrella!
