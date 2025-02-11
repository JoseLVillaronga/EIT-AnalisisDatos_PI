import sys
import pandas as pd
import numpy as np
from fpdf import FPDF
import matplotlib.pyplot as plt

def generar_graficos(df):
    """Genera gráficos comparativos de delitos totales vs violentos"""
    # Gráfico 1: Top 5 barrios (total delitos)
    plt.figure(figsize=(12,6))
    df['barrio'].value_counts().head(5).plot(kind='bar', color='#2ecc71')
    plt.title('Top 5 Barrios más Peligrosos (Total Delitos)')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('top_peligrosos_total.png')
    
    # Gráfico 2: Top 5 barrios (delitos violentos)
    plt.figure(figsize=(12,6))
    df[df['es_violento']]['barrio'].value_counts().head(5).plot(kind='bar', color='#e74c3c')
    plt.title('Top 5 Barrios más Peligrosos (Delitos Violentos)')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('top_peligrosos_violentos.png')
    """Genera gráficos comparativos"""
    # Obtener barrios violentos para exclusión
    barrios_violentos = df[df['es_violento']]['barrio'].value_counts().head(5).index
    
    # Gráfico 3: Barrios más seguros (excluyendo violentos)
    plt.figure(figsize=(12,6))
    (df[~df['barrio'].isin(barrios_violentos)]['barrio']
     .value_counts()
     .tail(5)  # Los menos frecuentes
     .sort_values(ascending=True)
     .plot(kind='barh', color='#27ae60'))
    plt.title('Top 5 Barrios más Seguros (Excl. Violentos)')
    plt.xlabel('Cantidad')
    plt.tight_layout()
    plt.savefig('top_seguros.png')
    
    # Gráfico 4: Distribución mensual por tipo de delito
    plt.figure(figsize=(14,7))
    df_mes = df.groupby([df['fecha'].dt.month, 'es_violento']).size().unstack()
    df_mes.columns = ['Sin violencia', 'Con violencia']
    df_mes.index = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
    
    df_mes.plot(kind='bar', stacked=True, color=['#3498db', '#e74c3c'])
    plt.title('Distribución Mensual de Delitos por Tipo')
    plt.ylabel('Cantidad')
    plt.xlabel('Mes')
    plt.xticks(rotation=0)
    plt.legend(title='Tipo de Delito')
    plt.tight_layout()
    plt.savefig('distribucion_mensual.png')
    # Gráfico 5: Distribución por tipo de delito
    plt.figure(figsize=(10,10))
    top_delitos = df['tipo_delito'].value_counts().nlargest(6)
    otros = df['tipo_delito'].value_counts().nsmallest(len(df['tipo_delito'].unique()) - 6).sum()
    top_delitos['Otros'] = otros
    
    colores = ['#e74c3c', '#3498db', '#2ecc71', '#f1c40f', '#9b59b6', '#1abc9c', '#95a5a6']
    top_delitos.plot.pie(autopct='%1.1f%%', colors=colores, startangle=90)
    plt.title('Distribución por Tipo de Delito')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig('distribucion_tipos.png')

def mostrar_progreso(paso, total, mensaje):
    print(f"\n[Paso {paso}/{total}] {mensaje}", flush=True)

# Nueva función al final:
def generar_reporte(dia_max, mes_max, archivo='reporte.pdf'):
    pdf = FPDF()
    pdf.add_page()
    
    # Título
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Reporte de Criminalidad 2019 - Análisis Estratégico', 0, 1, 'C')
    
    # Resultados clave
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f'Día pico: {dia_max}', 0, 1)
    pdf.cell(0, 10, f'Mes crítico: {mes_max}', 0, 1)
    
    # Agregar gráficos
    pdf.image('top_peligrosos_total.png', x=10, y=50, w=90)
    pdf.image('top_peligrosos_violentos.png', x=10, y=140, w=180)
    # Agregar tercer gráfico
    pdf.image('top_seguros.png', x=110, y=50, w=90)
    # Agregar gráfico mensual
    pdf.add_page()
    pdf.image('distribucion_mensual.png', x=10, y=25, w=190)
    pdf.image('distribucion_tipos.png', x=30, y=160, w=150)

    pdf.output(archivo)
    print(f"✓ Reporte PDF con gráficos generado: {archivo}")


def main():

    try:
        print("\n=== INICIO DEL ANÁLISIS ===", flush=True)
        
        # PASO 1: Carga inicial
        mostrar_progreso(1, 5, "Cargando archivo CSV")
        df = pd.read_csv('delitos2019.csv', encoding='latin-1')
        print(f"✓ Registros cargados: {len(df):,}")
        print("\nMuestra de fechas crudas:", df['fecha'].head(3).tolist())
        
        # PASO 2: Limpieza y validación
        mostrar_progreso(2, 5, "Procesando datos")
        df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d', errors='coerce')
        
        print("\nValidación previa a limpieza:")
        print("Fechas inválidas:", df['fecha'].isna().sum())
        print("Barrios vacíos:", df['barrio'].isna().sum())
        
        df = df.dropna(subset=['fecha', 'barrio'])
        registros_validos = len(df)
        print(f"\n✓ Registros válidos: {registros_validos:,} ({registros_validos/117661*100:.1f}%)")
        
        # PASO 3: Análisis diario
        mostrar_progreso(3, 5, "Calculando día con más delitos")
        delitos_diarios = df.groupby(df['fecha'].dt.date).size()
        dia_max = delitos_diarios.idxmax()
        print(f"► Día máximo: {dia_max} ({delitos_diarios.max():,} casos)")
        
        print("\nValidación cruzada de fechas:")
        print("Primera fecha válida:", df['fecha'].min().date())
        print("Última fecha válida:", df['fecha'].max().date())
        
        # PASO 4: Análisis mensual
        mostrar_progreso(4, 5, "Calculando mes más inseguro")
        meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',
                'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
        mes_max = df['fecha'].dt.month.value_counts().idxmax()
        conteo_mes = df['fecha'].dt.month.value_counts().max()
        print(f"► Mes máximo: {meses[mes_max-1]} ({conteo_mes:,} casos)")
        print("\nTop 5 Barrios por Delitos Violentos:")
        # Modificar la línea que causa el warning:
        df['es_violento'] = df['tipo_delito'].str.contains('(con violencia)', case=False, na=False, regex=False)
        delitos_violentos = df[df['es_violento']]['barrio'].value_counts().head(5)
        print(delitos_violentos)
        
        # Agregar al final del Paso 4:
        print("\nTop 5 Barrios más Peligrosos:")
        print(df['barrio'].value_counts().head(5))
        
        # PASO 5: Finalización
        mostrar_progreso(5, 5, "Proceso completado")
        print("\n=== RESULTADOS FINALES ===")
        print(f"Día con mayor criminalidad: {dia_max}")
        print(f"Mes más inseguro: {meses[mes_max-1]}")
        print("==========================")
        generar_graficos(df)
        generar_reporte(dia_max, meses[mes_max-1])
        
    except Exception as e:
        print(f"\nERROR: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()