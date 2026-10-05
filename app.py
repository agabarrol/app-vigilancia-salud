import streamlit as st

# 1. Base de datos estructurada con los factores de riesgo extraídos
protocolos = [
    {
        "factor_riesgo": "Vibraciones Mano-Brazo",
        "descripcion": "Exposición a vibraciones mecánicas transmitidas al sistema mano-brazo (herramientas manuales, maquinaria percutora). Riesgo de alteraciones vasculares, neurológicas o musculoesqueléticas.",
        "criterios_evaluacion": "Valor límite de exposición diaria normalizado a 8 horas: 5 m/s². Valor de acción: 2,5 m/s².",
        "pruebas_clinicas": "Cuestionario de síntomas, exploración física (vascular, neurológica y musculoesquelética), test de compresión capilar, test de Allen, pruebas de sensibilidad.",
        "periodicidad": "Examen inicial (previo a la exposición), periódico (cada 1-3 años dependiendo del nivel de riesgo, edad y síntomas) y tras ausencias prolongadas."
    },
    {
        "factor_riesgo": "Vibraciones Cuerpo Entero",
        "descripcion": "Exposición a vibraciones transmitidas a todo el cuerpo (conducción de vehículos industriales, tractores, carretillas). Riesgo principal: lumbalgias y lesiones de la columna vertebral.",
        "criterios_evaluacion": "Valor límite de exposición diaria normalizado a 8 horas: 1,15 m/s². Valor de acción: 0,5 m/s².",
        "pruebas_clinicas": "Anamnesis dirigida (antecedentes de dolor lumbar), exploración del aparato locomotor, maniobras de Lasègue y Bragard.",
        "periodicidad": "Inicial, periódica (según evaluación de riesgos y aparición de sintomatología) y por cambio de puesto."
    },
    {
        "factor_riesgo": "Ruido",
        "descripcion": "Exposición a niveles de ruido elevados que pueden provocar hipoacusia o sordera profesional, además de efectos extrauditivos (estrés, fatiga).",
        "criterios_evaluacion": "Valores inferiores que dan lugar a una acción: LAeq,d = 80 dB(A). Valores superiores: 85 dB(A). Valor límite: 87 dB(A).",
        "pruebas_clinicas": "Anamnesis auditiva, otoscopia, audiometría tonal liminar (vía aérea y, si hay alteraciones, vía ósea).",
        "periodicidad": "Inicial, periódica (cada 3-5 años para exposición >80 dB, y cada 1-2 años para >85 dB o uso de EPIs)."
    },
    {
        "factor_riesgo": "Polvo de Sílice (Silicosis)",
        "descripcion": "Enfermedad fibrósica pulmonar irreversible ocasionada por la inhalación continuada de polvo de sílice libre cristalina.",
        "criterios_evaluacion": "Medición de concentración de fracción respirable de sílice libre. Requiere control ambiental estricto.",
        "pruebas_clinicas": "Historia clínica ocupacional exhaustiva, radiografía de tórax (clasificación OIT), espirometría, prueba tuberculínica.",
        "periodicidad": "Inicial, periódica (frecuencia anual o cada 1-3 años según el nivel de exposición y antigüedad), y vigilancia post-ocupacional."
    }
]

# 2. Configuración de la interfaz en Streamlit
st.title("Buscador de Protocolos de Vigilancia de la Salud")
st.markdown("Busca por factor de riesgo, tipo de prueba médica o palabra clave.")

# 3. Barra de búsqueda
termino_busqueda = st.text_input("🔍 Buscar:", "").lower()

# 4. Motor de filtrado dinámico
resultados = []
if termino_busqueda:
    for protocolo in protocolos:
        # Verifica si el término está en cualquier campo del diccionario del protocolo
        if any(termino_busqueda in str(valor).lower() for valor in protocolo.values()):
            resultados.append(protocolo)
else:
    # Si no hay texto, muestra todos por defecto
    resultados = protocolos 

st.write(f"**Resultados encontrados:** {len(resultados)}")
st.divider()

# 5. Renderizado de los resultados
for res in resultados:
    with st.expander(f"⚠️ {res['factor_riesgo']}", expanded=True):
        st.markdown(f"**Descripción:** {res['descripcion']}")
        st.markdown(f"**Criterios de Evaluación:** {res['criterios_evaluacion']}")
        st.markdown(f"**Pruebas Clínicas Requeridas:** {res['pruebas_clinicas']}")
        st.markdown(f"**Periodicidad:** {res['periodicidad']}")
