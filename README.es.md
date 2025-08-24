# Phone Tracker

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Poetry](https://img.shields.io/badge/Poetry-1.0%2B-orange.svg)](https://python-poetry.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)](https://github.com/jmeiracorbal/phone-tracker)

Una herramienta útil para obtener información detallada sobre números de teléfono. Te permite descubrir la ubicación, operador, zona horaria y otros detalles de cualquier número que te interese.

## Qué hace

- **Análisis de números** - Obtén información completa sobre cualquier teléfono
- **Detección de país y región** - País, región, ciudad y coordenadas
- **Detalles del operador** - Información del proveedor de servicios móviles
- **Identificación de zona horaria** - Encuentra automáticamente la zona correcta
- **Validación de números** - Verifica si el número es válido y posible
- **Interfaz agradable** - Salida limpia y con colores, fácil de leer

## Inicio Rápido

### Descargar y Ejecutar

1. **Ve a [Releases](https://github.com/jmeiracorbal/phone-tracker/releases)**
2. **Descarga el ejecutable para tu plataforma:**
   - **Linux**: `phone-tracker` (binario)
   - **macOS**: `phone-tracker` (binario)
   - **Windows**: `phone-tracker.exe` (ejecutable)
3. **Ejecuta directamente** - ¡No requiere instalación!

### Uso

**Linux/macOS:**

```bash
chmod +x phone-tracker
```

```bash
./phone-tracker
```

**Windows:**

```cmd
phone-tracker.exe
```

## Ejemplo de salida

_Ejemplo de salida_:

```
Enter phone number information:
Country Code Ex [34, 1, 81] : 34
Phone Number Ex [666666666] : xxxxxxxxx

========== SHOW INFORMATION PHONE NUMBERS ==========

Full Number         : +34xxxxxxxxx
Location             : Spanyol
Region Code          : ES
Timezone             : Atlantic/Canary, Europe/Madrid
Operator             : Orange
Valid number         : True
Possible number      : True
International format : +34 xxx xx xx xx
Mobile format        : +34 xxx xx xx xx
Type                 : This is a mobile number
```

## Cómo funciona

La herramienta usa la librería `phonenumbers` para:

1. Analizar y validar números de teléfono
2. Extraer información del país y región
3. Determinar detalles del operador
4. Identificar información de zona horaria
5. Formatear números en varios estándares internacionales

## Formatos soportados

- **Códigos de país**: +1 (EEUU/Canadá), +34 (España), +81 (Japón), +86 (China), etc.
- **Tipos de número**: Móvil, Línea fija, Gratuito, Tarifa premium
- **Estándares internacionales**: E.164, Internacional, Nacional

## Para Desarrolladores

### Ejecutar desde el código fuente
Si quieres ejecutar el código fuente:

```bash
git clone https://github.com/jmeiracorbal/phone-tracker.git
cd phone-tracker
pip install phonenumbers requests
python phone_tracker.py
```

### Construir ejecutables
Los ejecutables se construyen y publican automáticamente vía GitHub Actions cuando se suben tags.

## Contribuir

1. Haz fork del repositorio
2. Crea una rama para tu función (`git checkout -b feature/funcion-increible`)
3. Haz commit de tus cambios (`git commit -m 'Agrega función increíble'`)
4. Haz push a la rama (`git push origin feature/funcion-increible`)
5. Abre un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para más detalles.

## Agradecimientos

- **Autor original**: [HUNXBYTS](https://github.com/HUNXBYTS)
- **Forkeado por**: [jmeiracorbal](https://github.com/jmeiracorbal)
- **Basado en**: Herramienta Ghost Tracker

## Soporte

Si encuentras algún problema o tienes preguntas:
- Crea un issue en GitHub
- Revisa la página de [Releases](https://github.com/jmeiracorbal/phone-tracker/releases) para la última versión

---

**Nota**: Esta herramienta es solo para propósitos educativos y legítimos. Siempre respeta la privacidad y úsala de manera responsable.
