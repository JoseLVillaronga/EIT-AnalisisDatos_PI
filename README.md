# Análisis de Criminalidad en CABA - 2019

## Objetivo
Analizar patrones de criminalidad en la Ciudad Autónoma de Buenos Aires durante 2019, identificando:
- Distribución temporal de delitos
- Zonas de mayor incidencia
- Relación con datos demográficos

## Principales Conclusiones

### Hallazgos Clave
1. **Distribución de homicidios por vulnerabilidad**:
   - En barrios vulnerables: 69.7% homicidios dolosos vs 30.3% siniestros viales
   - En otros barrios: 39.5% dolosos vs 60.5% viales

2. **Patrones temporales**:
   - Pico de siniestros viales: Horario laboral (mañana/tarde)
   - Mes crítico general: Marzo (11,166 casos)

3. **Factores geográficos**:
   - Barrios con mayor criminalidad violenta: Balvanera (4,902 casos)
   - Mayor criminalidad total: Palermo (9,559 casos)

### Implicaciones
- **Estrategias diferenciadas**:
  - Barrios vulnerables: Enfocar en prevención de violencia interpersonal
  - Otros barrios: Refuerzo de seguridad vial horaria

- **Políticas públicas**:
  - Programas de prevención en marzo
  - Control vial en horarios pico laborales

## Recomendaciones
1. Investigar causas del pico en marzo
2. Reforzar vigilancia en Palermo/Balvanera
3. Mejorar registro geográfico de casos

## Uso del Sistema

### Requisitos
- Python 3.8+
- Dependencias: `pip install -r requirements.txt`

### Ejecución
```bash
python analisis_delitos.py
```

```
├── analisis_delitos.py    # Script principal
├── delitos2019.csv       # Dataset original
├── datos_barrios_caba.csv # Datos demográficos
├── requirements.txt      # Dependencias
└── reporte.pdf           # Reporte generado
```