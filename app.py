import streamlit as st
import json
from pathlib import Path
import uuid
from datetime import date

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
            data = json.loads(SAVE_FILE.read_text())
            if "jobs" not in data:
                data["jobs"] = []
            if "skill_levels" not in data:
                data["skill_levels"] = {}
            return data
        except Exception:
            pass
    return {"done": [], "notes": {}, "jobs": [], "skill_levels": {}}

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

# ── Target companies ──────────────────────────────────────────────────────────
TARGET_COMPANIES = [
    "Epic Systems",
    "Datavant",
    "Rhapsody",
    "Redox",
    "Harris Computer",
    "Booz Allen Hamilton",
    "Deloitte Health",
    "Leidos",
    "ICF",
    "Maximus",
    "Oracle Health",
    "Otra",
]

# ── HealthTech Skills ─────────────────────────────────────────────────────────
HEALTHTECH_SKILLS = [
    {
        "id": "sql", "name": "SQL / Bases de datos", "cat": "💻 Técnico",
        "in_resume": True, "weight": 8, "default": 80, "color": "#7F77DD",
        "tips": "Practica JOINs complejos, CTEs, window functions. Plataforma: Mode Analytics o LeetCode SQL.",
    },
    {
        "id": "python", "name": "Python (análisis / automatización)", "cat": "💻 Técnico",
        "in_resume": True, "weight": 8, "default": 55, "color": "#7F77DD",
        "tips": "Refuerza pandas, matplotlib. Añade un proyecto en GitHub con datos de salud pública.",
    },
    {
        "id": "tableau_bi", "name": "Tableau / Power BI", "cat": "💻 Técnico",
        "in_resume": True, "weight": 7, "default": 70, "color": "#7F77DD",
        "tips": "Crea un portfolio público en Tableau Public con dashboards de salud.",
    },
    {
        "id": "ehr_fhir", "name": "EHR / FHIR / HL7", "cat": "🏥 Health IT",
        "in_resume": True, "weight": 9, "default": 75, "color": "#1D9E75",
        "tips": "Explora FHIR R4 spec en hl7.org. Recursos Patient, Observation, Encounter. Conecta a tu experiencia IIS.",
    },
    {
        "id": "iis_registry", "name": "IIS / Registros de Inmunización", "cat": "🏥 Health IT",
        "in_resume": True, "weight": 6, "default": 95, "color": "#1D9E75",
        "tips": "Expertise sólido. Documenta métricas de impacto y casos de uso concretos para entrevistas.",
    },
    {
        "id": "data_quality", "name": "Data Quality & Governance", "cat": "💻 Técnico",
        "in_resume": True, "weight": 8, "default": 85, "color": "#7F77DD",
        "tips": "Añade frameworks formales: DAMA-DMBOK. Cuantifica resultados (ej: % reducción de duplicados).",
    },
    {
        "id": "hipaa", "name": "HIPAA / Regulatory Compliance", "cat": "⚖️ Regulatorio",
        "in_resume": True, "weight": 8, "default": 80, "color": "#BA7517",
        "tips": "Actualiza a HIPAA 2023 amendments. Considera CIPP/US cert para diferenciarte.",
    },
    {
        "id": "ai_ml", "name": "AI / ML aplicado a salud", "cat": "💻 Técnico",
        "in_resume": False, "weight": 7, "default": 15, "color": "#D85A30",
        "tips": "Toma AI for Healthcare (deeplearning.ai/Coursera). Vocabulario: NLP clínico, modelos predictivos.",
    },
    {
        "id": "cloud", "name": "Cloud: AWS / GCP / Azure", "cat": "💻 Técnico",
        "in_resume": False, "weight": 6, "default": 10, "color": "#D85A30",
        "tips": "AWS Cloud Practitioner gratis en AWS Skill Builder (~10h). Suficiente para roles health IT.",
    },
    {
        "id": "api_integration", "name": "API Integration / REST / ETL", "cat": "💻 Técnico",
        "in_resume": False, "weight": 7, "default": 30, "color": "#D85A30",
        "tips": "Practica con Postman + APIs públicas de salud (CDC, CMS). Mini-proyecto de integración.",
    },
    {
        "id": "project_mgmt", "name": "Project Management (Agile / PMP)", "cat": "🗂️ Gestión",
        "in_resume": True, "weight": 9, "default": 65, "color": "#185FA5",
        "tips": "Formaliza con Google PM Cert o PMP. Aprende Agile/Scrum vocabulary para el sector privado.",
    },
    {
        "id": "product_mgmt", "name": "Product Management", "cat": "🗂️ Gestión",
        "in_resume": False, "weight": 7, "default": 20, "color": "#D85A30",
        "tips": "Aprende: discovery, roadmaps, user stories, OKRs. Google PM Certificate en Coursera.",
    },
    {
        "id": "vendor_mgmt", "name": "Vendor & Contract Management", "cat": "🗂️ Gestión",
        "in_resume": True, "weight": 7, "default": 75, "color": "#185FA5",
        "tips": "Ya sólido. Traduce a lenguaje privado: SLA management, RFP evaluation, procurement.",
    },
    {
        "id": "stakeholder", "name": "Stakeholder & Executive Comm.", "cat": "🗂️ Gestión",
        "in_resume": True, "weight": 8, "default": 80, "color": "#185FA5",
        "tips": "Documenta presentaciones ejecutivas con impacto. Cuantifica decisiones que tomaste.",
    },
    {
        "id": "strategic_plan", "name": "Strategic Planning", "cat": "🗂️ Gestión",
        "in_resume": True, "weight": 7, "default": 70, "color": "#185FA5",
        "tips": "Formaliza con OKR, Balanced Scorecard. Añade métricas a logros del resume.",
    },
    {
        "id": "public_health", "name": "Public Health / Epidemiology", "cat": "🌐 Dominio",
        "in_resume": True, "weight": 9, "default": 90, "color": "#993556",
        "tips": "Expertise central. Conecta a lenguaje healthtech: population health, value-based care.",
    },
    {
        "id": "clinical_wf", "name": "Clinical Workflows & Informatics", "cat": "🌐 Dominio",
        "in_resume": True, "weight": 7, "default": 65, "color": "#993556",
        "tips": "Profundiza en clinical decision support, care coordination, patient journey mapping.",
    },
    {
        "id": "interop", "name": "Health Data Interoperability", "cat": "🌐 Dominio",
        "in_resume": True, "weight": 8, "default": 75, "color": "#993556",
        "tips": "CMS Interoperability Rule, USCDI, CommonWell, Carequality. Muy valorado en healthtech.",
    },
    {
        "id": "linkedin_vis", "name": "LinkedIn / Thought Leadership", "cat": "🔗 Visibilidad",
        "in_resume": False, "weight": 5, "default": 15, "color": "#888",
        "tips": "Publica 2x/mes sobre data quality, IIS, salud pública. Activa modo Open to Work privado.",
    },
    {
        "id": "networking", "name": "Networking sector privado", "cat": "🔗 Visibilidad",
        "in_resume": False, "weight": 5, "default": 15, "color": "#888",
        "tips": "Meta: 5 conexiones/semana. Targets: Epic, Datavant, Rhapsody, Redox, Harris Computer.",
    },
]

# ── Skill keyword mapping (for job description matching) ──────────────────────
SKILL_KEYWORDS = {
    "sql": [
        "sql", "database", " db ", "query", "queries", "relational database",
        "mysql", "postgresql", "oracle sql", "t-sql", "data warehouse",
        "snowflake", "redshift", "bigquery", "sql server",
    ],
    "python": [
        "python", "pandas", "numpy", "jupyter", "pyspark", "scripting",
        "python script", "python developer", "python programming",
    ],
    "tableau_bi": [
        "tableau", "power bi", "powerbi", "looker", "data visualization",
        "bi tool", "qlik", "business intelligence", "reporting tool", "sisense",
    ],
    "ehr_fhir": [
        "fhir", "hl7", "ehr", "emr", "epic", "cerner", "meditech",
        "electronic health record", "electronic medical record",
        "smart on fhir", "health data exchange", "clinical data",
    ],
    "iis_registry": [
        "immunization information system", "iis", "immunization registry",
        "vaccine registry", "preis", "iz gateway", "immunization data",
        "registry system",
    ],
    "data_quality": [
        "data quality", "data governance", "data integrity",
        "data management", "data stewardship", "master data",
        "data cleansing", "data validation", "data hygiene",
    ],
    "hipaa": [
        "hipaa", " phi ", " pii ", "compliance", "regulatory",
        "privacy rule", "security rule", "data privacy",
        "protected health", "health privacy",
    ],
    "ai_ml": [
        "machine learning", "artificial intelligence", " ml ", " ai ",
        "nlp", "natural language processing", "predictive model",
        "deep learning", "neural network", "llm", "generative ai",
        "predictive analytics", "algorithm",
    ],
    "cloud": [
        "aws ", "azure", " gcp", "google cloud", "cloud computing",
        "cloud platform", "cloud-based", "s3 ", "lambda", "terraform",
        "kubernetes",
    ],
    "api_integration": [
        "api ", "rest ", "restful", "integration", "web services",
        "microservices", "json", "xml", "etl", "data pipeline", "middleware",
    ],
    "project_mgmt": [
        "project management", "pmp", "agile", "scrum", "kanban",
        "waterfall", "jira", "program management", "pmo", "okr", "sprint",
        "project planning",
    ],
    "product_mgmt": [
        "product management", "product manager", "product owner",
        "roadmap", "user stor", "sprint planning", "backlog",
        "product strateg", "go-to-market", "product development",
    ],
    "vendor_mgmt": [
        "vendor management", "vendor ", "contract management",
        "procurement", "rfp", "rfq", "scope of work", "third-party",
        "supplier management", "sow",
    ],
    "stakeholder": [
        "stakeholder", "cross-functional", "collaboration",
        "executive communication", "engagement", "relationship management",
        "liaison",
    ],
    "strategic_plan": [
        "strategic plan", "strategy", "strategic initiative",
        "long-term plan", "business strategy", "organizational strategy",
    ],
    "public_health": [
        "public health", "epidemiology", "surveillance",
        "population health", "community health", "mph", "cdc",
        "health department", "disease prevention",
    ],
    "clinical_wf": [
        "clinical workflow", "care coordination", "clinical informatics",
        "care management", "clinical operations", "clinical data",
        "clinical program",
    ],
    "interop": [
        "interoperability", "data exchange", "health information exchange",
        "hie ", "uscdi", "commonwell", "carequality", "data integration",
        "system integration",
    ],
    "linkedin_vis": [
        "thought leadership", "publications", "speaking engagement",
        "conference presentation",
    ],
    "networking": [
        "relationship building", "professional network",
        "community engagement", "industry network",
    ],
}

JOB_STATUS_OPTIONS = [
    "🔵 Interesada",
    "🟡 Aplicada",
    "🟢 Entrevista",
    "⭐ Oferta recibida",
    "❌ Descartada",
]


# ── Match function ─────────────────────────────────────────────────────────────
def analyze_job_match(job_description: str, skill_levels: dict) -> dict:
    jd_lower = " " + job_description.lower() + " "
    skill_map = {s["id"]: s for s in HEALTHTECH_SKILLS}

    required_skill_ids = []
    for skill_id, keywords in SKILL_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in jd_lower:
                if skill_id not in required_skill_ids:
                    required_skill_ids.append(skill_id)
                break

    matched, gap = [], []
    for skill_id in required_skill_ids:
        skill = skill_map.get(skill_id)
        if not skill:
            continue
        level = skill_levels.get(skill_id, skill["default"])
        entry = {"id": skill_id, "name": skill["name"], "level": level, "cat": skill["cat"]}
        if skill["in_resume"] or level >= 60:
            matched.append(entry)
        else:
            gap.append(entry)

    total = len(required_skill_ids)
    match_pct = int(len(matched) / total * 100) if total > 0 else 0

    return {
        "match_pct": match_pct,
        "total_required": total,
        "matched": matched,
        "gap": gap,
    }


# ── Load state ────────────────────────────────────────────────────────────────
if "progress" not in st.session_state:
    st.session_state.progress = load_progress()
    for skill in HEALTHTECH_SKILLS:
        if skill["id"] not in st.session_state.progress["skill_levels"]:
            st.session_state.progress["skill_levels"][skill["id"]] = skill["default"]

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
  .skill-tag {
    display: inline-block; padding: 3px 10px; border-radius: 14px;
    font-size: 0.75rem; margin: 2px 2px 4px 0; border: 1px solid;
  }
  .prob-box {
    text-align: center; padding: 22px 16px; border-radius: 14px;
    border: 2px solid; margin-bottom: 8px;
  }
  .impact-card {
    padding: 14px; border-radius: 10px; border: 2px solid;
    background: #fafafa; text-align: center; height: 100%;
  }
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
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📋 Plan de acción",
    "🧩 Áreas a mejorar",
    "🏅 Certificaciones",
    "🗓️ Milestones",
    "📝 Notas personales",
    "💼 Job Tracker",
    "📈 Skills HealthTech",
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
                help="Mueve el slider para reflejar tu progreso real",
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
    for date_str, title, desc in MILESTONES:
        m_key = f"milestone_{title}"
        checked = m_key in prog["done"]
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"**{title}**  ·  `{date_str}`")
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

# ── TAB 6: Job Tracker ────────────────────────────────────────────────────────
with tab6:
    st.markdown("### 💼 Job Tracker — Match de Resume")
    st.caption(
        "Pega la descripción completa de un trabajo para ver qué % match tienes con tu resume "
        "y qué skills te faltan. Criterio: remoto · $100k+ (ideal $120k) · con beneficios."
    )

    # ── Summary bar (if jobs exist)
    if prog["jobs"]:
        statuses = [j["status"] for j in prog["jobs"]]
        sm1, sm2, sm3, sm4, sm5 = st.columns(5)
        sm1.metric("Total trabajos", len(prog["jobs"]))
        sm2.metric("Aplicadas", sum(1 for s in statuses if "Aplicada" in s))
        sm3.metric("Entrevistas", sum(1 for s in statuses if "Entrevista" in s))
        sm4.metric("Ofertas", sum(1 for s in statuses if "Oferta" in s))
        avg_m = int(sum(j["match_pct"] for j in prog["jobs"]) / len(prog["jobs"]))
        sm5.metric("Match promedio", f"{avg_m}%")
        st.write("")

    # ── Add new job form
    with st.expander("➕  Analizar nuevo trabajo", expanded=len(prog["jobs"]) == 0):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            company_options = TARGET_COMPANIES
            j_company_sel = st.selectbox("Empresa", company_options, key="j_company_sel")
            j_company_custom = ""
            if j_company_sel == "Otra":
                j_company_custom = st.text_input("Nombre de la empresa", key="j_company_custom", placeholder="ej: Health Catalyst")
            j_title = st.text_input("Título del puesto *", key="j_title", placeholder="ej: Health Informatics Manager")
            j_url = st.text_input("URL del trabajo (opcional)", key="j_url", placeholder="https://...")

        with col_f2:
            j_salary = st.text_input("Rango salarial anunciado", key="j_salary", placeholder="ej: $110k – $130k")
            j_remote = st.selectbox("Modalidad", ["Remoto", "Híbrido", "Presencial", "No especificado"], key="j_remote")
            j_benefits = st.multiselect(
                "Beneficios mencionados",
                ["Medical/Dental/Vision", "401k", "PTO generoso", "Equity/RSUs", "Paid parental leave", "Tuition reimbursement", "Flexible hours"],
                key="j_benefits",
            )
            j_notes = st.text_area("Notas (opcional)", key="j_notes", height=68, placeholder="Por qué me interesa, contacto, etc.")

        j_desc = st.text_area(
            "Pega aquí la descripción completa del trabajo *",
            key="j_desc",
            height=200,
            placeholder="Copia y pega el texto completo del job posting aquí...",
        )

        analyze_btn = st.button("🔍 Analizar Match", type="primary", use_container_width=True)

    # ── Run analysis
    if analyze_btn:
        company_name = j_company_custom if j_company_sel == "Otra" else j_company_sel
        if not company_name or not j_title or not j_desc:
            st.warning("Por favor completa empresa, título y descripción del trabajo.")
        else:
            result = analyze_job_match(j_desc, prog["skill_levels"])
            st.session_state["last_analysis"] = {
                "company": company_name,
                "title": j_title,
                "url": j_url,
                "salary": j_salary,
                "remote": j_remote,
                "benefits": j_benefits,
                "notes": j_notes,
                "description": j_desc,
                "result": result,
            }

    # ── Show analysis result
    if "last_analysis" in st.session_state:
        la = st.session_state["last_analysis"]
        r = la["result"]
        pct_val = r["match_pct"]

        if pct_val >= 75:
            mcolor = "#1D9E75"
            mlabel = "Excelente match — aplica con confianza 🎯"
        elif pct_val >= 55:
            mcolor = "#BA7517"
            mlabel = "Match moderado — cierra 1–2 brechas antes de aplicar 📊"
        else:
            mcolor = "#D85A30"
            mlabel = "Match bajo — necesitas cerrar brechas clave ⚠️"

        # Salary & remote fit check
        meets_remote = la["remote"] == "Remoto"
        fit_notes = []
        if not meets_remote:
            fit_notes.append(f"⚠️ Modalidad: {la['remote']} — verifica si aplica para PR")
        if la["salary"]:
            fit_notes.append(f"💰 Salario anunciado: {la['salary']}")
        if la["benefits"]:
            fit_notes.append(f"✅ Beneficios: {', '.join(la['benefits'])}")

        st.markdown(f"""
        <div style="background:#f8f8f8; border-radius:12px; padding:18px 22px;
                    border-left:5px solid {mcolor}; margin:12px 0;">
          <div style="font-size:0.85rem; color:#666; margin-bottom:2px;">
            {la['company']} · {la['title']}
          </div>
          <div style="font-size:2.2rem; font-weight:700; color:{mcolor};">{pct_val}% match</div>
          <div style="font-size:0.88rem; color:{mcolor}; margin-bottom:6px;">{mlabel}</div>
          <div style="font-size:0.8rem; color:#888;">
            {len(r['matched'])} skills cubiertas &nbsp;·&nbsp;
            {len(r['gap'])} brechas &nbsp;·&nbsp;
            {r['total_required']} skills detectadas en el job posting
          </div>
        </div>
        """, unsafe_allow_html=True)

        if fit_notes:
            st.caption("  ·  ".join(fit_notes))

        col_m, col_g = st.columns(2)
        with col_m:
            st.markdown("**✅ Skills que ya tienes:**")
            if r["matched"]:
                tags = "".join(
                    f"<span class='skill-tag' style='background:#e8f8f2; border-color:#1D9E75; color:#167a5a;'>✅ {s['name']}</span>"
                    for s in r["matched"]
                )
                st.markdown(tags, unsafe_allow_html=True)
            else:
                st.caption("—")
        with col_g:
            st.markdown("**❌ Skills a desarrollar:**")
            if r["gap"]:
                tags = "".join(
                    f"<span class='skill-tag' style='background:#fdecea; border-color:#D85A30; color:#b54020;'>❌ {s['name']}</span>"
                    for s in r["gap"]
                )
                st.markdown(tags, unsafe_allow_html=True)
            else:
                st.caption("¡Ninguna brecha detectada! 🎉")

        col_save, col_clear = st.columns([3, 1])
        with col_save:
            if st.button("💾 Guardar en tracker", type="primary", use_container_width=True):
                new_job = {
                    "id": str(uuid.uuid4())[:8],
                    "company": la["company"],
                    "title": la["title"],
                    "url": la["url"],
                    "salary": la["salary"],
                    "remote": la["remote"],
                    "benefits": la["benefits"],
                    "notes": la["notes"],
                    "description": la["description"],
                    "match_pct": r["match_pct"],
                    "matched_skills": [s["name"] for s in r["matched"]],
                    "gap_skills": [s["name"] for s in r["gap"]],
                    "status": "🔵 Interesada",
                    "added_date": str(date.today()),
                }
                prog["jobs"].append(new_job)
                save_progress(prog)
                del st.session_state["last_analysis"]
                st.success("✓ Trabajo guardado!")
                st.rerun()
        with col_clear:
            if st.button("Limpiar", use_container_width=True):
                del st.session_state["last_analysis"]
                st.rerun()

    # ── Saved jobs list
    if prog["jobs"]:
        st.divider()
        st.markdown(f"#### Trabajos guardados ({len(prog['jobs'])})")

        col_sort, col_filter = st.columns([2, 2])
        with col_sort:
            sort_by = st.selectbox(
                "Ordenar por",
                ["Match % (mayor)", "Fecha (reciente)", "Empresa A–Z"],
                key="job_sort",
            )
        with col_filter:
            filter_status = st.selectbox(
                "Filtrar por estado",
                ["Todos"] + JOB_STATUS_OPTIONS,
                key="job_filter",
            )

        jobs_sorted = list(prog["jobs"])
        if sort_by == "Match % (mayor)":
            jobs_sorted.sort(key=lambda x: x["match_pct"], reverse=True)
        elif sort_by == "Empresa A–Z":
            jobs_sorted.sort(key=lambda x: x["company"])
        else:
            jobs_sorted.sort(key=lambda x: x.get("added_date", ""), reverse=True)

        if filter_status != "Todos":
            jobs_sorted = [j for j in jobs_sorted if j["status"] == filter_status]

        for job in jobs_sorted:
            pct_j = job["match_pct"]
            jcolor = "#1D9E75" if pct_j >= 75 else "#BA7517" if pct_j >= 55 else "#D85A30"

            header = f"{job['company']}  ·  {job['title']}  ·  **{pct_j}% match**  ·  {job['status']}"
            with st.expander(header):
                row1, row2 = st.columns([3, 1])
                with row1:
                    st.markdown(
                        f"<span style='font-size:1.6rem; font-weight:700; color:{jcolor};'>{pct_j}%</span>"
                        f"<span style='color:#888; font-size:0.8rem;'> match · agregado {job.get('added_date','')}</span>",
                        unsafe_allow_html=True,
                    )
                    info_parts = []
                    if job.get("remote"):
                        info_parts.append(f"📍 {job['remote']}")
                    if job.get("salary"):
                        info_parts.append(f"💰 {job['salary']}")
                    if job.get("benefits"):
                        info_parts.append(f"✅ {', '.join(job['benefits'])}")
                    if info_parts:
                        st.caption("  ·  ".join(info_parts))
                    if job.get("url"):
                        st.markdown(f"[🔗 Ver oferta]({job['url']})")
                    if job.get("notes"):
                        st.caption(f"📝 {job['notes']}")

                with row2:
                    new_status = st.selectbox(
                        "Estado",
                        JOB_STATUS_OPTIONS,
                        index=JOB_STATUS_OPTIONS.index(job["status"])
                        if job["status"] in JOB_STATUS_OPTIONS else 0,
                        key=f"status_{job['id']}",
                    )
                    if new_status != job["status"]:
                        job["status"] = new_status
                        save_progress(prog)

                col_ms, col_gs = st.columns(2)
                with col_ms:
                    st.markdown("**✅ Skills cubiertas:**")
                    tags = "".join(
                        f"<span class='skill-tag' style='background:#e8f8f2; border-color:#1D9E75; color:#167a5a;'>✅ {sk}</span>"
                        for sk in job.get("matched_skills", [])
                    )
                    st.markdown(tags or "<span style='color:#888'>—</span>", unsafe_allow_html=True)
                with col_gs:
                    st.markdown("**❌ Brechas:**")
                    tags = "".join(
                        f"<span class='skill-tag' style='background:#fdecea; border-color:#D85A30; color:#b54020;'>❌ {sk}</span>"
                        for sk in job.get("gap_skills", [])
                    )
                    st.markdown(tags or "<span style='color:#888'>Ninguna 🎉</span>", unsafe_allow_html=True)

                if st.button("🗑️ Eliminar trabajo", key=f"del_{job['id']}"):
                    prog["jobs"] = [j for j in prog["jobs"] if j["id"] != job["id"]]
                    save_progress(prog)
                    st.rerun()
    else:
        st.info(
            "Aún no hay trabajos guardados. Analiza tu primer trabajo arriba ↑\n\n"
            "**Empresas sugeridas para empezar:** Epic Systems · Datavant · Rhapsody · Redox · Harris Computer"
        )

# ── TAB 7: Skills HealthTech ──────────────────────────────────────────────────
with tab7:
    st.markdown("### 📈 Skills HealthTech — Probabilidad de Landing")
    st.caption(
        "✅ = ya en tu resume actual  ·  🔲 = skill a desarrollar  ·  "
        "Pesos basados en demanda del mercado healthtech 2025–2026"
    )

    # ── Calculate landing probability
    total_weight = sum(s["weight"] for s in HEALTHTECH_SKILLS)
    weighted_score = sum(
        (prog["skill_levels"].get(s["id"], s["default"]) / 100) * s["weight"]
        for s in HEALTHTECH_SKILLS
    )
    landing_prob = int(weighted_score / total_weight * 100)

    if landing_prob >= 70:
        prob_color = "#1D9E75"
        prob_label = "Perfil fuerte para healthtech 🚀"
    elif landing_prob >= 50:
        prob_color = "#BA7517"
        prob_label = "Perfil en construcción — sigue cerrando brechas 📈"
    else:
        prob_color = "#D85A30"
        prob_label = "Enfócate en las skills de mayor peso primero ⚠️"

    # ── Probability header
    _, center_col, _ = st.columns([1, 2, 1])
    with center_col:
        st.markdown(f"""
        <div class="prob-box" style="border-color:{prob_color}; background:#fafafa;">
          <div style="font-size:0.85rem; color:#666; margin-bottom:4px;">
            Probabilidad de landing en HealthTech
          </div>
          <div style="font-size:3rem; font-weight:700; color:{prob_color}; line-height:1.1;">
            {landing_prob}%
          </div>
          <div style="font-size:0.88rem; color:{prob_color}; margin-top:6px;">{prob_label}</div>
          <div style="margin-top:10px;">
        """, unsafe_allow_html=True)
        st.progress(landing_prob / 100)
        st.markdown("</div></div>", unsafe_allow_html=True)

    st.write("")

    # ── Top 3 high-impact skills to improve
    skill_map_ht = {s["id"]: s for s in HEALTHTECH_SKILLS}
    potential_gains = []
    for s in HEALTHTECH_SKILLS:
        current = prog["skill_levels"].get(s["id"], s["default"])
        if current < 95:
            # Simulate +30 points gain
            improvement = min(current + 30, 100) - current
            new_ws = weighted_score + (improvement / 100) * s["weight"]
            new_prob = int(new_ws / total_weight * 100)
            delta = new_prob - landing_prob
            potential_gains.append((s, delta, current))

    potential_gains.sort(key=lambda x: x[1], reverse=True)

    st.markdown("#### 🎯 Top 3 skills con mayor impacto si las mejoras (+30 pts)")
    t3c1, t3c2, t3c3 = st.columns(3)
    for idx, (sk, delta, curr) in enumerate(potential_gains[:3]):
        col = [t3c1, t3c2, t3c3][idx]
        with col:
            st.markdown(f"""
            <div class="impact-card" style="border-color:{sk['color']};">
              <div style="font-size:1.4rem;">{sk['cat'].split()[0]}</div>
              <div style="font-size:0.85rem; font-weight:600; margin:4px 0; color:#333;">{sk['name']}</div>
              <div style="font-size:0.78rem; color:#888;">Nivel actual: {curr}%</div>
              <div style="font-size:1rem; color:{sk['color']}; font-weight:700; margin-top:8px;">
                +{delta}pp de probabilidad
              </div>
            </div>
            """, unsafe_allow_html=True)
            st.caption(sk["tips"])

    st.divider()

    # ── Skill sliders by category
    st.markdown("#### Ajusta tu nivel en cada skill")
    st.caption("Mueve los sliders para reflejar tu progreso real. Se guarda automáticamente.")

    categories: dict = {}
    for skill in HEALTHTECH_SKILLS:
        cat = skill["cat"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(skill)

    for cat_name, skills in categories.items():
        avg_cat = int(
            sum(prog["skill_levels"].get(s["id"], s["default"]) for s in skills) / len(skills)
        )
        with st.expander(f"{cat_name}  ·  promedio {avg_cat}%  ({len(skills)} skills)", expanded=True):
            for skill in skills:
                current_val = prog["skill_levels"].get(skill["id"], skill["default"])
                in_res = "✅" if skill["in_resume"] else "🔲"

                col_sl, col_badge = st.columns([5, 1])
                with col_sl:
                    new_val = st.slider(
                        f"{in_res} {skill['name']}",
                        0, 100, current_val,
                        key=f"ht_{skill['id']}",
                        help=skill["tips"],
                    )
                    if new_val != prog["skill_levels"].get(skill["id"]):
                        prog["skill_levels"][skill["id"]] = new_val
                        save_progress(prog)
                with col_badge:
                    bcolor = "#1D9E75" if new_val >= 75 else "#BA7517" if new_val >= 50 else "#D85A30"
                    st.markdown(
                        f"<div style='text-align:center; margin-top:24px;'>"
                        f"<span style='font-size:1.2rem; font-weight:700; color:{bcolor};'>{new_val}%</span>"
                        f"</div>",
                        unsafe_allow_html=True,
                    )

    # ── Skills vs. saved jobs cross-reference
    if prog["jobs"]:
        st.divider()
        st.markdown("#### 🔁 Brechas más frecuentes en tus trabajos guardados")
        st.caption("Skills que aparecen como gap en los jobs que rastreaste.")
        all_gaps: dict = {}
        for job in prog["jobs"]:
            for gs in job.get("gap_skills", []):
                all_gaps[gs] = all_gaps.get(gs, 0) + 1
        if all_gaps:
            sorted_gaps = sorted(all_gaps.items(), key=lambda x: x[1], reverse=True)
            for skill_name, count in sorted_gaps[:8]:
                st.markdown(
                    f"<span class='skill-tag' style='background:#fdecea; border-color:#D85A30; color:#b54020;'>"
                    f"❌ {skill_name} ({count}x)</span>",
                    unsafe_allow_html=True,
                )
        else:
            st.success("¡No hay brechas recurrentes en tus trabajos guardados!")

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption(
    "Dashboard generado con Claude · Progreso guardado en progress.json · "
    "Job Tracker: Epic · Datavant · Rhapsody · Redox · Harris Computer · Meta: Remoto · $100k+ · Con beneficios"
)
