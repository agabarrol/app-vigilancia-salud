import streamlit as st

# Aquí puedes ir añadiendo los 28 factores de riesgo según vayas revisando los PDFs.
# Al estar estructurado en este diccionario, el desplegable se actualizará automáticamente.
pruebas_por_riesgo = {
    "Vibraciones Mano-Brazo": [
        "Cuestionario de síntomas específico",
        "Exploración física: vascular, neurológica y musculoesquelética",
        "Test de compresión capilar y Test de Allen",
        "Pruebas de sensibilidad térmica y táctil"
    ],
    "Vibraciones Cuerpo Entero": [
        "Anamnesis dirigida (antecedentes de dolor lumbar y patologías de columna)",
        "Exploración detallada del aparato locomotor",
        "Maniobras exploratorias radiculares (Lasègue y Bragard)"
    ],
    "Ruido": [
        "Anamnesis auditiva (antecedentes de otitis, uso de fármacos ototóxicos)",
        "Otoscopia bilateral",
        "Audiometría tonal liminar (vía aérea y, si hay alteraciones, vía ósea)"
    ],
    "Polvo de Sílice (Silicosis)": [
        "Historia clínica y ocupacional exhaustiva",
        "Radiografía de tórax (lectura según clasificación OIT)",
        "Espirometría (estudio de la función pulmonar)",
        "Prueba tuberculínica (Mantoux)"
    ],
    # --- PLANTILLA PARA AÑADIR LOS SIGUIENTES ---
    # "Nombre del Riesgo 5": [
    #     "Prueba 1",
    #     "Prueba 2"
    # ],
    # "Nombre del Riesgo 6": [
    #     "Prueba 1",
    #     "Prueba 2"
    # ]
}

st.title("Gestión de Protocolos Médicos y Costes")

factor_seleccionado = st.selectbox(
    "Selecciona el factor de riesgo al que está expuesto el trabajador:",
    options=[""] + list(pruebas_por_riesgo.keys()),
    format_func=lambda x: "Elige una opción..." if x == "" else x
)

if factor_seleccionado:
    st.subheader(f"Pruebas específicas para: {factor_seleccionado}")
    
    for prueba in pruebas_por_riesgo[factor_seleccionado]:
        st.markdown(f"- {prueba}")
        
    st.divider()
    
    st.subheader("Evaluación de Costes")
    
    # Uso de columnas para que el formulario quede más compacto
    col1, col2 = st.columns(2)
    
    with col1:
        coste_pruebas = st.number_input(
            "Coste de las pruebas por trabajador (€):", 
            min_value=0.0, 
            step=5.0, 
            format="%.2f"
        )
        
    with col2:
        num_trabajadores = st.number_input(
            "Número de trabajadores expuestos:", 
            min_value=1, 
            step=1
        )
    
    if coste_pruebas > 0:
        coste_total = coste_pruebas * num_trabajadores
        st.success(f"**Coste total estimado:** {coste_total:.2f} €")
