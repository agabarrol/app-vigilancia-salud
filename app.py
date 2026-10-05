import streamlit as st

# Base de datos de los protocolos extraídos de la documentación oficial
PROTOCOLOS_VIGILANCIA = {
    "Polvo de Sílice (Silicosis)": {
        "descripcion": "Vigilancia específica para neumoconiosis por inhalación de sílice cristalina[cite: 151].",
        "pruebas_especificas": [
            "Historia laboral exhaustiva y cuestionario respiratorio estandarizado[cite: 161, 162].",
            "Exploración física con auscultación cardiopulmonar[cite: 162].",
            "Radiografía de tórax (proyecciones P-A y lateral) con lectura estandarizada según normativa ILO 2011[cite: 162, 185].",
            "Espirometría realizada e interpretada según las recomendaciones de la SEPAR[cite: 162].",
            "Electrocardiograma (obligatorio para trabajadores bajo la ORDEN ITC/2585/2007)[cite: 163]."
        ]
    },
    "Ruido y Químicos Ototóxicos": {
        "descripcion": "Detección de hipoacusia inducida por ruido. Requiere vigilancia estrecha si existe exposición conjunta a químicos como tolueno, estireno o monóxido de carbono[cite: 246, 249].",
        "pruebas_especificas": [
            "Audiometría tonal (prueba diagnóstica de referencia o gold standard)[cite: 243].",
            "Productos de distorsión/otoemisiones acústicas (DPOAE) como prueba de detección precoz y seguimiento complementario[cite: 243]."
        ]
    },
    "Vibraciones (Mano-Brazo y Cuerpo Entero)": {
        "descripcion": "Prevención del síndrome por vibraciones mano-brazo, túnel carpiano y problemas osteomusculares (como dolor lumbar)[cite: 86, 88].",
        "pruebas_especificas": [
            "Cuestionarios de síntomas: HAVS, Cuestionario Nórdico Estandarizado y Escala de Boston para túnel carpiano[cite: 96, 120, 122].",
            "Diagrama de Katz para localizar cambios vasculares y de sensibilidad[cite: 96].",
            "Test de provocación por frío para evaluar la afectación vascular (ISO 14835-1 e ISO 14835-2)[cite: 97].",
            "Evaluación de percepción sensorial mediante monofilamentos de Semmes-Weinstein[cite: 98].",
            "Evaluación de la destreza de manipulación con la prueba del tablero perforado de Purdue (Purdue Pegboard Test)[cite: 98].",
            "Pruebas de provocación física: test de Phalen, signo de Tinel, test de compresión del carpo[cite: 98]."
        ]
    }
}

def main():
    st.set_page_config(page_title="Vigilancia de la Salud - Cuadro Profesional", layout="wide")
    st.title("Gestión de Pruebas Médicas: Enfermedades Profesionales")
    
    st.write("Seleccione el riesgo laboral para consultar las pruebas clínicas específicas exigidas por los protocolos vigentes:")

    # Selector de riesgo
    riesgo_seleccionado = st.selectbox("Factor de Riesgo / Protocolo", list(PROTOCOLOS_VIGILANCIA.keys()))

    if riesgo_seleccionado:
        datos = PROTOCOLOS_VIGILANCIA[riesgo_seleccionado]
        
        st.subheader("Descripción del Riesgo")
        st.info(datos["descripcion"])
        
        st.subheader("Pruebas Específicas Requeridas")
        for prueba in datos["pruebas_especificas"]:
            st.markdown(f"- {prueba}")
            
    st.markdown("---")
    st.caption("Los datos han sido extraídos de las guías de vigilancia sanitaria específica publicadas por el Ministerio de Sanidad.")

if __name__ == "__main__":
    main()
