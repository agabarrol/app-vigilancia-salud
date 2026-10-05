import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Vigilancia de la Salud PRL", layout="wide")
st.title("🩺 Asignación de Pruebas Médicas por Puesto de Trabajo")
st.markdown("Selecciona una de las actividades tipificadas en el RD 1299/2006 para conocer sus pruebas.")

# 1. Base de datos interna con la nomenclatura exacta del BOE
# Las actividades están copiadas literalmente del documento legal para evitar errores.
datos_boe = [
    {
        "Actividad BOE": "Trabajos de calderería", 
        "Agente BOE": "Ruido", 
        "Enfermedad": "Hipoacusia o sordera profesional",
        "Pruebas Sanidad (Ejemplo Protocolo)": "Audiometría tonal liminar, Otoscopia."
    },
    {
        "Actividad BOE": "Talado y corte de árboles con sierras portátiles", 
        "Agente BOE": "Ruido y Vibraciones", 
        "Enfermedad": "Hipoacusia y Afectación vascular/osteoarticular",
        "Pruebas Sanidad (Ejemplo Protocolo)": "Audiometría, Exploración vascular y articular de miembros superiores."
    },
    {
        "Actividad BOE": "Trabajos de fontanería", 
        "Agente BOE": "Plomo y sus compuestos", 
        "Enfermedad": "Saturnismo",
        "Pruebas Sanidad (Ejemplo Protocolo)": "Plumbemia (plomo en sangre), Analítica renal, Hemograma."
    },
    {
        "Actividad BOE": "Trabajos de soldadura y corte", 
        "Agente BOE": "Óxidos de carbono / Cadmio", 
        "Enfermedad": "Intoxicación por CO / Bronquitis / Afecciones renales",
        "Pruebas Sanidad (Ejemplo Protocolo)": "Espirometría, Radiografía de tórax, Analítica específica de metales."
    },
    {
        "Actividad BOE": "Personal sanitario", 
        "Agente BOE": "Agentes biológicos", 
        "Enfermedad": "Enfermedades infecciosas",
        "Pruebas Sanidad (Ejemplo Protocolo)": "Serología (VHB, VHC, VIH), Control de vacunación."
    },
    {
        "Actividad BOE": "Odontólogos", 
        "Agente BOE": "Agentes biológicos / Posturas forzadas", 
        "Enfermedad": "Enfermedades infecciosas / Tendinitis",
        "Pruebas Sanidad (Ejemplo Protocolo)": "Serología, Exploración osteomuscular de miembros superiores y cervical."
    },
    {
        "Actividad BOE": "Trabajos en minas, túneles, canteras, galerías, obras públicas", 
        "Agente BOE": "Polvo de sílice libre", 
        "Enfermedad": "Silicosis / Neoplasia maligna de bronquio y pulmón",
        "Pruebas Sanidad (Ejemplo Protocolo)": "Radiografía de tórax (Criterios OIT), Espirometría, Cuestionario respiratorio."
    }
]

# Convertir los datos a un DataFrame de Pandas
df = pd.DataFrame(datos_boe)

# 2. Interfaz de usuario: El sistema propone los puestos (Menú desplegable)
# Esto evita que el usuario escriba y cometa errores de nomenclatura
st.subheader("Búsqueda por menú desplegable")
lista_puestos_propuestos = df["Actividad BOE"].unique().tolist()

# El widget 'selectbox' es el que obliga a elegir de la lista
puesto_seleccionado = st.selectbox(
    "Haz clic y selecciona la actividad del trabajador:", 
    ["--- Selecciona una opción ---"] + lista_puestos_propuestos
)

# 3. Mostrar los resultados de forma dinámica
if puesto_seleccionado != "--- Selecciona una opción ---":
    st.divider()
    # Filtramos la base de datos para obtener solo la fila del puesto elegido
    datos_filtrados = df[df["Actividad BOE"] == puesto_seleccionado].iloc[0]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("📋 **Datos tipificados en el BOE**")
        st.write(f"**Actividad seleccionada:** {datos_filtrados['Actividad BOE']}")
        st.write(f"**Agente de Riesgo:** {datos_filtrados['Agente BOE']}")
        st.write(f"**Enfermedad Profesional Posible:** {datos_filtrados['Enfermedad']}")
        
    with col2:
        st.error("⚕️ **Pruebas Médicas Asignadas**")
        st.write(f"**Reconocimiento Específico:** {datos_filtrados['Pruebas Sanidad (Ejemplo Protocolo)']}")