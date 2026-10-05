import streamlit as st

# Diccionario actualizado con los factores de riesgo y protocolos de los documentos adjuntos
pruebas_por_riesgo = {
    "Radón": [
        "Historia laboral con historial dosimétrico",
        "Historia clínica con antecedentes personales, familiares y cuantificación del hábito tabáquico",
        "Anamnesis dirigida a síntomas de cáncer de pulmón (tos persistente, dolor torácico, hemoptisis, disnea, afonía)",
        "Exploración física general a criterio médico (no se recomienda radiografía de tórax ni tomografía computarizada de baja dosis)"
    ],
    "Radiaciones Ionizantes": [
        "Historial laboral y dosimétrico detallado",
        "Anamnesis que incluya antecedentes de estudios o tratamientos con radiaciones",
        "Exploración oftalmológica anual con examen del cristalino, agudeza visual y fondo de ojo",
        "Exploración dermatológica (piel, pelo, uñas, mucosas) y neurológica",
        "Análisis de sangre completo (hematológico y bioquímico) y análisis de orina",
        "Electrocardiograma, espirometría y audiometría"
    ],
    "Posturas Forzadas": [
        "Anamnesis dirigida por aparatos buscando predisposiciones del sistema osteomuscular[cite: 668]",
        "Exploración clínica específica de columna vertebral, cintura escapular y extremidades (inspección, palpación y movilidad)[cite: 668, 672, 673, 674]",
        "Maniobras de exploración neurológica (Lasègue, Schober, Bragard, Valsalva, etc.)[cite: 689]",
        "Analítica sistemática de sangre y orina, y electrocardiograma para mayores de 40 años[cite: 668]"
    ],
    "Plomo": [
        "Exploración clínica de piel, cavidad bucal (ribete de Burton), abdomen, y sistemas neurológico y cardiocirculatorio[cite: 733, 734, 735]",
        "Hematimetría completa, Urea, Creatinina y pruebas hepáticas (bilirrubina, albúmina, fosfatasas alcalinas, GOT, GPT, Gamma GT)[cite: 734, 735]",
        "Control biológico de plomo inorgánico: Plumbemia (Pb-B) y Zinc-protoporfirina eritrocitaria (ZPP)[cite: 734, 735]",
        "Control biológico de plomo orgánico: Plumburia (Pb-U)[cite: 748, 749]"
    ],
    "Plaguicidas": [
        "Anamnesis dirigida a síntomas de intoxicación aguda o crónica (dermatológicos, neurológicos, oculares, cardiorrespiratorios y digestivos)[cite: 767, 776]",
        "Exploración física general y exploración mental e intelectual básica (orientación temporoespacial)[cite: 768, 777]",
        "Control biológico: Determinación de Colinesterasa plasmática y Colinesterasa eritrocitaria[cite: 769, 778]",
        "Determinación de enzimas hepáticas (GPT y GGT) para descartar patologías concurrentes[cite: 769, 778]"
    ],
    "Pantallas de Visualización de Datos (PVD)": [
        "Reconocimiento oftalmológico: agudeza visual (lejos y cerca), refracción, equilibrio muscular, reflejos pupilares, motilidad y sentido cromático[cite: 829, 830, 834, 835]",
        "Tonometría y vigilancia de la presbicia por el oftalmólogo para mayores de 40 años[cite: 830, 834]",
        "Examen osteomuscular: inspección de desviaciones de columna (simetría de hombros y crestas ilíacas) y movilidad articular[cite: 830, 835, 836]",
        "Valoración de la carga mental mediante cuestionario específico[cite: 837]"
    ],
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
        "Audiometría tonal liminar (vía aérea y, si hay alteraciones, vía ósea)",
        "Pruebas complementarias opcionales/detección precoz: Productos de distorsión / otoemisiones acústicas (DPOAE)[cite: 1199, 1226]"
    ],
    "Ruido + Disolventes (Tolueno / Estireno)": [
        "Vigilancia específica del conocimiento de exposición a tolueno o estireno[cite: 1199]",
        "Seguimiento más estrecho de los efectos auditivos frente a la exposición aislada[cite: 1199]",
        "Implementación de medidas preventivas para evitar la exposición conjunta[cite: 1199]"
    ],
    "Ruido + Asfixiantes (Monóxido de Carbono)": [
        "Control del conocimiento de exposición a monóxido de carbono[cite: 1199]",
        "Seguimiento audiométrico y clínico más estrecho por potenciación de hipoacusia[cite: 1200]",
        "Medidas preventivas estrictas orientadas a evitar la coinhalación"
    ],
    "Ruido + Fármacos Ototóxicos (Gentamicina / Cisplatino)": [
        "Anamnesis y registro de tratamientos con gentamicina, kanamicina, neomicina o cisplatino[cite: 1200]",
        "Fortalecimiento de medidas de protección y prevención ante tratamientos farmacológicos simultáneos[cite: 1200]",
        "Control y seguimiento auditivo estrecho[cite: 1200]"
    ],
    "Polvo de Sílice (Silicosis)": [
        "Historia clínica y ocupacional exhaustiva[cite: 1145]",
        "Cuestionario respiratorio estandarizado[cite: 1145, 1164]",
        "Radiografía de tórax en proyecciones PA y lateral (lectura estandarizada OIT 2011)[cite: 1145, 1168]",
        "Espirometría (estudio de la función pulmonar según recomendaciones SEPAR)[cite: 1145, 1173]",
        "Prueba tuberculínica (Mantoux)[cite: 1145]",
        "Electrocardiograma (obligatorio para sectores sujetos a la ITC 2.0.02 de Minería)[cite: 1146]",
        "Consejo para la deshabituación tabáquica (efecto sinérgico con la sílice)[cite: 1141, 1153]"
    ],
    "Óxido de Etileno": [
        "Historia laboral detallada con exposiciones anteriores y actual al riesgo[cite: 1563]",
        "Historia clínica con anamnesis familiar, personal y tratamientos previos (citotóxicos, radioterapia)[cite: 1563, 1564]",
        "Exploración clínica específica centrada en alteraciones oculares, dérmicas, respiratorias, neurológicas y digestivas[cite: 1564]",
        "Control biológico y estudios complementarios: hemograma completo, bioquímica sanguínea, orina y estudios complementarios a criterio médico (radiografía de tórax, función respiratoria, aductos de hemoglobina)[cite: 1564, 1565]"
    ],
    "Neuropatías por Presión": [
        "Historia laboral con antecedentes y registro de factores de riesgo biomecánicos y ergonómicos[cite: 1602]",
        "Anamnesis clínica neurológica dirigida a síntomas sensitivos y motores (parestesias, dolor, debilidad)[cite: 1602, 1614]",
        "Exploración clínica de desfiladeros nerviosos, hallazgos a la inspección/palpación y signo de Tinel[cite: 1616, 1617]",
        "Maniobras exploratorias específicas para compresión nerviosa (Adson, Phalen, Allen, etc.)[cite: 1617]"
    ],
    "Movimientos Repetidos de Miembro Superior": [
        "Historia clínico-laboral con análisis de exposiciones anteriores y actuales al riesgo[cite: 1663, 1664]",
        "Anamnesis y antecedentes personales del sistema osteomuscular y factores predisponentes[cite: 1665, 1683]",
        "Exploración clínica específica del sistema osteomuscular en hombros, codos, muñecas, manos y dedos[cite: 1665, 1684]",
        "Pruebas y test clínicos específicos (Phalen, Tinel, Finkelstein, etc.)[cite: 1686]"
    ],
    "Manipulación Manual de Cargas": [
        "Historia laboral con análisis de la exposición actual, características de la carga y factores de riesgo[cite: 1705, 1712, 1713]",
        "Historia clínica, anamnesis y cuestionario de síntomas osteomusculares en los últimos 12 meses[cite: 1706, 1714, 1715]",
        "Exploración clínica inespecífica (antropometría, presión arterial, frecuencia cardíaca, auscultación y palpación abdominal)[cite: 1706, 1714]",
        "Exploración clínica específica de columna vertebral y articulaciones, incluyendo pruebas funcionales (Lasègue, Schöber, Phalen, Tinel)[cite: 1706, 1716, 1717]"
    ]
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
