# Análisis de Criminalidad en CABA - 2019

## Objetivo
Analizar patrones de criminalidad en la Ciudad Autónoma de Buenos Aires durante 2019, identificando:
- Distribución temporal de delitos
- Zonas de mayor incidencia
- Relación con datos demográficos

## Principales Conclusiones

### 1. Distribución Temporal
- **Día pico:** 11 de marzo (466 casos)
- **Mes crítico:** Marzo (11,166 casos)

### 2. Geografía del Crimen
**Barrios más peligrosos:**
1. Palermo (9,559 casos)
2. Balvanera (9,239)
3. San Nicolás (6,246)

**Barrios con más violencia:**
1. Balvanera (4,902 casos violentos)
2. Palermo (4,711)

### 3. Patrones Detectados
- Alta correlación densidad poblacional-delitos (r=0.75)
- Zonas turísticas con mayor criminalidad no violenta

### 4. Calidad de Datos
- 99.5% registros válidos
- 597 casos sin ubicación precisa

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