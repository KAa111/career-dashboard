import streamlit as st
import json
from pathlib import Path

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Career Dashboard · Carieyshla Soto",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Persistence helpers ───────────────────────────────────────────────────────
SAVE_FILE = Path("progress.json")

def load_progress():
    if SAVE_FILE.exists():
        try:
            return json.loads(SAVE_FILE.read_text())
        except Exception:
            pass
    return {"done": [], "notes": {}}

def save_progress(data):
    SAVE_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2))

# ── Data ──────────────────────────────────────────────────────────────────────
PHASES = {
    "1": {
        "name": "Preparación",
        "months": "Jun – Jul 2026",
        "color": "#7F77DD",
        "bg": "#EEEDFE",
        "desc": "Construye los cimientos: resume, LinkedIn, red y cursos. Sin esto, las aplicaciones no convierten.",
        "tasks": [
            ("Reescribir resume con formato de impacto cuantificado", "🔴 Urgente"),
            ("Actualizar headline y summary de LinkedIn", "🔴 Urgente"),
            ("Documentar logros con métricas (%, #, tiempo, volumen)", "🔴 Urgente"),
            ("Activar 'Open to Work' en modo privado en LinkedIn", "🟡 Esta semana"),
            ("Inscribirse en AI for Healthcare (Coursera)", "🟡 Este mes"),
            ("Conectar 5 personas nuevas/semana en LinkedIn (health IT)", "🟢 Continuo"),
            ("Listar 20 empresas target (vendors, consultoría, federal)", "🟡 Julio"),
        ],
    },
    "2": {
        "name": "Exploración activa",
        "months": "Ago – Sep 2026",
        "color": "#1D9E75",
        "bg": "#E1F5EE",
        "desc": "Visibilidad activa: aplica, conecta, aparece. El volumen y la consistencia son clave en esta fase.",
        "tasks": [
            ("Aplicar a 15–20 posiciones en el período", "🔴 Meta"),
            ("Solicitar 3–5 informational interviews por mes", "🟡 Mensual"),
            ("Asistir a evento virtual de HIMSS o PHII", "🟡 Agosto"),
            ("Publicar primer artículo en LinkedIn sobre data quality", "🟢 Agosto"),
            ("Postularse a Booz Allen, Deloitte Health, Leidos, ICF, Maximus", "🔴 Prioridad"),
            ("Completar módulos de PM frameworks (Agile/OKRs)", "🟢 Continuo"),
            ("Iniciar preparación para PMP o CAHIMS", "🟡 Septiembre"),
            ("Traducir achievements del resume a lenguaje sector privado", "🟡 Agosto"),
        ],
    },
    "3": {
        "name": "Entrevistas & Oferta",
        "months": "Oct – Nov 2026",
        "color": "#BA7517",
        "bg": "#FAEEDA",
        "desc": "Convierte oportunidades en oferta. Prepara historias, negocia con datos y cierra el año con un nuevo rol.",
        "tasks": [
            ("Preparar 5–7 historias STAR con métricas reales", "🔴 Urgente"),
            ("Investigar rangos salariales (Glassdoor, LinkedIn Salary)", "🟡 Antes de entrevistas"),
            ("Practicar pitch de 90 segundos sobre tu perfil", "🔴 Urgente"),
            ("Preparar estrategia de negociación (nunca aceptes la primera)", "🟡 Noviembre"),
            ("Enviar notas de agradecimiento post-entrevista", "🟢 Cada entrevista"),
            ("Evaluar ofertas con criterios: salario, crecimiento, cultura", "🟡 Nov–Dic"),
            ("Cerrar proceso y firmar oferta antes de Dic 2026", "🔴 Meta final"),
        ],
    },
}

GAPS = [
    {
        "title": "Impacto cuantificado",
        "icon": "📊",
        "level": 25,
        "color": "#7F77DD",
        "action": "Documenta: # registros duplicados eliminados, % mejora de calidad de datos, # EHRs onboardeados, horas ahorradas por automatizaciones.",
        "resources": "Usa el análisis de tus sistemas actuales. Pide datos históricos a tu equipo si es necesario.",
    },
    {
        "title": "AI aplicada a salud",
        "icon": "🤖",
        "level": 20,
        "color": "#1D9E75",
        "action": "Toma AI for Healthcare (Coursera/deeplearning.ai). Aprende vocabulario de NLP clínico, detección de duplicados con ML.",
        "resources": "https://www.coursera.org/learn/ai-for-medical-diagnosis",
    },
    {
        "title": "Product Management",
        "icon": "🗂️",
        "level": 30,
        "color": "#BA7517",
        "action": "Aprende: discovery, roadmapping, user stories, OKRs, Agile. Google PM Certificate en Coursera (~5h/semana).",
        "resources": "https://www.coursera.org/professional-certificates/google-project-management",
    },
    {
        "title": "Visibilidad externa",
        "icon": "🔗",
        "level": 15,
        "color": "#D85A30",
        "action": "Publica en LinkedIn 2x/mes. Asiste a HIMSS virtual. Solicita informational interviews. Expande red al sector privado.",
        "resources": "himss.org/events | phii.org",
    },
    {
        "title": "Cloud básico (AWS/GCP)",
        "icon": "☁️",
        "level": 10,
        "color": "#185FA5",
        "action": "AWS Cloud Practitioner (gratis en AWS Skill Builder). Suficiente para hablar con equipos de cloud en health tech.",
        "resources": "https://aws.amazon.com/training/learn-about/cloud-practitioner/",
    },
    {
        "title": "Networking sector privado",
        "icon": "🤝",
        "level": 20,
        "color": "#993556",
        "action": "Meta: 5 conexiones nuevas/semana en LinkedIn. Targets: HIMSS, PHII, Booz Allen, health IT startups.",
        "resources": "Busca 'Health Informatics Manager' en LinkedIn y conecta.",
    },
]

CERTS = [
    ("PMP — Project Management Professional", "3–4 meses", "Muy alto", "🟣", "Alta"),
    ("CAHIMS — HIMSS Health Informatics", "2–3 meses", "Muy alto", "🟢", "Alta"),
    ("Google PM Certificate (Coursera)", "6 meses, ~5h/semana", "Alto", "🟣", "Alta"),
    ("AI for Healthcare (deeplearning.ai)", "4–6 semanas", "Alto", "🔵", "Media"),
    ("Tableau Desktop Specialist", "1–2 meses", "Medio", "🟠", "Media"),
    ("AWS Cloud Practitioner", "4–6 semanas", "Medio", "🔵", "Media"),
    ("Stanford Digital Health Certificate", "Variable", "Alto (presencia)", "🔴", "Opcional"),
]

MILESTONES = [
    ("Julio 31", "✅ Cierre Fase 1", "Resume, LinkedIn, cursos y lista de targets listos."),
    ("Septiembre 30", "✅ Cierre Fase 2", "15–20 aplicaciones enviadas, 2–3 entrevistas iniciales agendadas."),
    ("Noviembre 30", "🎯 Oferta en mano", "Oferta firmada o negociación avanzada."),
    ("Diciembre 2026", "🚀 Nuevo rol", "Inicio del nuevo capítulo profesional."),
]

# ── Load state ────────────────────────────────────────────────────────────────
if "progress" not in st.session_state:
    st.session_state.progress = load_progress()

prog = st.session_state.progress

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }
  h1 { font-size: 1.6rem !important; font-weight: 600 !important; }
  h2 { font-size: 1.15rem !important; font-weight: 600 !important; margin-top: 1rem !important; }
  h3 { font-size: 1rem !important; font-weight: 600 !important; }
  .metric-label { font-size: 0.75rem !important; }
  .stProgress > div > div { border-radius: 10px; }
  div[data-testid="stExpander"] { border: 1px solid #e5e5e5; border-radius: 10px; }
  .phase-card {
    border-radius: 12px; padding: 14px 18px; margin-bottom: 6px;
    border-left: 4px solid;
  }
  .gap-bar-label { font-size: 0.78rem; color: #888; margin-bottom: 2px; }
  footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.markdown("# 🎯 Career Dashboard · Carieyshla Soto")
    st.caption("Plan estratégico de carrera · Jun–Dic 2026")
with col_h2:
    total_tasks = sum(len(p["tasks"]) for p in PHASES.values())
    done_count = len(prog["done"])
    pct = int(done_count / total_tasks * 100)
    st.metric("Progreso general", f"{pct}%", f"{done_count} de {total_tasks} tareas")

st.divider()

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📋 Plan de acción",
    "🧩 Áreas a mejorar",
    "🏅 Certificaciones",
    "🗓️ Milestones",
    "📝 Notas personales",
])

# ── TAB 1: Plan de acción ─────────────────────────────────────────────────────
with tab1:
    for phase_id, phase in PHASES.items():
        phase_tasks = phase["tasks"]
        phase_done = sum(1 for i, _ in enumerate(phase_tasks) if f"{phase_id}-{i}" in prog["done"])
        phase_pct = int(phase_done / len(phase_tasks) * 100)

        st.markdown(f"""
        <div class="phase-card" style="background:{phase['bg']}; border-color:{phase['color']};">
          <strong style="color:{phase['color']}; font-size:0.85rem;">FASE {phase_id}</strong>
          <span style="font-size:1rem; font-weight:600; margin-left:8px;">{phase['name']}</span>
          <span style="font-size:0.8rem; color:#666; margin-left:8px;">{phase['months']}</span>
          <span style="float:right; font-size:0.85rem; font-weight:600; color:{phase['color']};">{phase_pct}%</span>
        </div>
        """, unsafe_allow_html=True)

        st.caption(phase["desc"])

        for i, (task_text, tag) in enumerate(phase_tasks):
            task_key = f"{phase_id}-{i}"
            col_cb, col_tag = st.columns([6, 1])
            with col_cb:
                checked = st.checkbox(
                    task_text,
                    value=(task_key in prog["done"]),
                    key=f"cb_{task_key}",
                )
                if checked and task_key not in prog["done"]:
                    prog["done"].append(task_key)
                    save_progress(prog)
                elif not checked and task_key in prog["done"]:
                    prog["done"].remove(task_key)
                    save_progress(prog)
            with col_tag:
                st.caption(tag)

        st.progress(phase_pct / 100)
        st.write("")

# ── TAB 2: Áreas a mejorar ────────────────────────────────────────────────────
with tab2:
    st.markdown("### Brechas clave y cómo cerrarlas")
    st.caption("Nivel actual estimado. Actualiza manualmente al avanzar.")

    for i, gap in enumerate(GAPS):
        with st.expander(f"{gap['icon']}  {gap['title']}  —  nivel actual: {gap['level']}%"):
            new_level = st.slider(
                "Ajusta tu nivel actual",
                0, 100, gap["level"],
                key=f"gap_slider_{i}",
                help="Mueve el slider para reflejar tu progreso real"
            )
            GAPS[i]["level"] = new_level

            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**Qué hacer:**")
                st.info(gap["action"])
            with col2:
                st.markdown("**Recursos:**")
                st.success(gap["resources"])

    st.divider()
    st.markdown("#### Vista general de brechas")
    for gap in GAPS:
        st.markdown(f"<div class='gap-bar-label'>{gap['icon']} {gap['title']}</div>", unsafe_allow_html=True)
        st.progress(gap["level"] / 100)

# ── TAB 3: Certificaciones ────────────────────────────────────────────────────
with tab3:
    st.markdown("### Certificaciones por prioridad y ROI")

    col_a, col_b, col_c, col_d, col_e = st.columns(5)
    headers = ["", "Certificación", "Tiempo", "ROI esperado", "Prioridad"]
    for col, h in zip([col_a, col_b, col_c, col_d, col_e], headers):
        col.markdown(f"**{h}**")

    st.divider()
    for icon, name, time, roi, prio in CERTS:
        col_a, col_b, col_c, col_d, col_e = st.columns(5)
        cert_key = f"cert_{name}"
        col_a.markdown(icon)
        col_b.markdown(name)
        col_c.caption(time)
        col_d.caption(roi)
        col_e.caption(prio)

    st.divider()
    st.markdown("""
    **Secuencia recomendada:**
    1. **Ahora mismo** → Google PM Certificate (puedes empezar hoy en Coursera)
    2. **Mes 2** → AI for Healthcare (4–6 semanas, bajo costo)
    3. **Mes 3** → Inscripción examen CAHIMS (HIMSS, muy alineado a tu perfil)
    4. **Mes 4–6** → PMP si el rol target lo requiere
    """)

# ── TAB 4: Milestones ─────────────────────────────────────────────────────────
with tab4:
    st.markdown("### Hitos clave Jun–Dic 2026")

    for date, title, desc in MILESTONES:
        m_key = f"milestone_{title}"
        checked = m_key in prog["done"]
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"**{title}**  ·  `{date}`")
            st.caption(desc)
        with col2:
            val = st.checkbox("✓ Logrado", value=checked, key=f"ms_{m_key}")
            if val and m_key not in prog["done"]:
                prog["done"].append(m_key)
                save_progress(prog)
            elif not val and m_key in prog["done"]:
                prog["done"].remove(m_key)
                save_progress(prog)
        st.divider()

    milestones_done = sum(1 for _, title, _ in MILESTONES if f"milestone_{title}" in prog["done"])
    st.metric("Milestones completados", f"{milestones_done} / {len(MILESTONES)}")

# ── TAB 5: Notas personales ───────────────────────────────────────────────────
with tab5:
    st.markdown("### Notas y reflexiones personales")
    st.caption("Todo lo que escribas aquí se guarda automáticamente.")

    note_sections = [
        ("💼 empresas_target", "Empresas que me interesan / apliqué"),
        ("📞 entrevistas", "Notas de entrevistas y seguimiento"),
        ("💰 salarios", "Rangos salariales investigados"),
        ("🌟 logros", "Logros y métricas documentadas para el resume"),
        ("📚 aprendizaje", "Cursos en progreso / completados"),
        ("💭 reflexiones", "Reflexiones y decisiones importantes"),
    ]

    for key, label in note_sections:
        with st.expander(f"📝  {label}"):
            note = st.text_area(
                label,
                value=prog["notes"].get(key, ""),
                height=150,
                key=f"note_{key}",
                label_visibility="collapsed",
                placeholder=f"Escribe aquí tus {label.lower()}...",
            )
            if note != prog["notes"].get(key, ""):
                prog["notes"][key] = note
                save_progress(prog)
                st.success("✓ Guardado", icon="✅")

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Dashboard generado con Claude · Progreso guardado localmente en progress.json · Actualiza los sliders y checkboxes para reflejar tu avance real.")
