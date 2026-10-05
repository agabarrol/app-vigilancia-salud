import streamlit as st

# 1. Base de datos con las pruebas específicas extraídas de los documentos
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
    ]
}

st.title("Gestión de Pruebas Médicas y Costes")

# 2. Desplegable para elegir el factor de riesgo
factor_seleccionado = st.selectbox(
    "Selecciona el factor de riesgo al que está expuesto el trabajador:",
    options=[""] + list(pruebas_por_riesgo.keys()),
    format_func=lambda x: "Elige una opción..." if x == "" else x
)

# 3. Mostrar pruebas y gestionar costes si hay una selección activa
if factor_seleccionado:
    st.subheader(f"Pruebas específicas para: {factor_seleccionado}")
    
    # Listar las pruebas
    for prueba in pruebas_por_riesgo[factor_seleccionado]:
        st.markdown(f"- {prueba}")
        
    st.divider()
    
    # 4. Módulo de costes
    st.subheader("Evaluación de Costes")
    coste_pruebas = st.number_input(
        f"Introduce el coste total estimado de estas pruebas para {factor_seleccionado} (€):", 
        min_value=0.0, 
        step=5.0, 
        format="%.2f"
    )
    
    num_trabajadores = st.number_input(
        "Número de trabajadores expuestos:", 
        min_value=1, 
        step=1
    )
    
    if coste_pruebas > 0:
        coste_total = coste_pruebas * num_trabajadores
        st.success(f"**Coste total estimado:** {coste_total:.2f} €")
