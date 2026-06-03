# 🇨🇴 Sistema MEAL — SSR & Espacios Protectores
## CARE Colombia

Este espacio de trabajo es el centro de control técnico y operativo del sistema de Monitoreo, Evaluación, Rendición de Cuentas y Aprendizaje (MEAL) para el proyecto de Salud Sexual y Reproductiva (SSR) y Entornos Protectores en Colombia. Su objetivo es mapear, procesar y controlar la información de las atenciones territoriales en los 6 municipios prioritarios, garantizando la calidad del dato y la toma de decisiones basada en evidencia.

---

### 📂 Estructura del Repositorio
Para asegurar que **nada se escape**, cada archivo y carpeta tiene un rol estrictamente definido:

* 📄 **[README.md](file:///C:/Users/Alfredo%20Pabón/Documents/Proyectos%20antigravity/proyecto_CARE_MEAL/README.md)**: Vista general, arquitectura del workspace, seguridad y glosario (este archivo).
* 📄 **[bitacora_avance.md](file:///C:/Users/Alfredo%20Pabón/Documents/Proyectos%20antigravity/proyecto_CARE_MEAL/bitacora_avance.md)**: Bitácora viva de sesiones, estado de tareas (`[ ]` / `[x]`), lecciones aprendidas y registro histórico de errores/soluciones.
* 📁 **[docs/](file:///C:/Users/Alfredo%20Pabón/Documents/Proyectos%20antigravity/proyecto_CARE_MEAL/docs)**: Documentos metodológicos, conceptuales y visualizadores interactivos.
  * 🖥️ **[docs/index.html](file:///C:/Users/Alfredo%20Pabón/Documents/Proyectos%20antigravity/proyecto_CARE_MEAL/docs/index.html)**: Visor web interactivo premium del Marco Lógico y el Mapa Operativo del proyecto (diseño adaptado de Stitch).
  * 📄 **[docs/arquitectura_procesos.md](file:///C:/Users/Alfredo%20Pabón/Documents/Proyectos%20antigravity/proyecto_CARE_MEAL/docs/arquitectura_procesos.md)**: Mapeo de herramientas (KoboToolbox, Power BI, Jira) y flujos operativos del equipo MEAL.
  * 📄 **[docs/marco_logico.md](file:///C:/Users/Alfredo%20Pabón/Documents/Proyectos%20antigravity/proyecto_CARE_MEAL/docs/marco_logico.md)**: Indicadores de impacto, fórmulas de cálculo, metas y matriz de cobertura municipal.
  * 📊 **1. POA_Seguimiento.xlsx**: Plan de Trabajo Operativo Anual y monitoreo físico-financiero del proyecto.
* 📁 **[datos_municipios/](file:///C:/Users/Alfredo%20Pabón/Documents/Proyectos%20antigravity/proyecto_CARE_MEAL/datos_municipios)**: Repositorio de bases de datos mensuales limpias reportadas por el personal de campo (Nomenclatura recomendada: `Datos_Municipio_AAAA_MM.xlsx`).
* 📁 **[scripts_procesamiento/](file:///C:/Users/Alfredo%20Pabón/Documents/Proyectos%20antigravity/proyecto_CARE_MEAL/scripts_procesamiento)**: Código en Python, macros o flujos de ETL para la limpieza, consolidación y desduplicación automática de beneficiarios.
* 📁 **[reportes_powerbi/](file:///C:/Users/Alfredo%20Pabón/Documents/Proyectos%20antigravity/proyecto_CARE_MEAL/reportes_powerbi)**: Archivos fuente de Power BI (`.pbip`) y control de versiones del tablero UX/UI.

---

### 🛡️ Protocolo de Seguridad y Confidencialidad de Datos
Debido a la extrema sensibilidad de los datos de Salud Sexual y Reproductiva (SSR) y Gestión de Casos de violencia basada en género (VBG):
1. **Anonimización Estricta:** Queda estrictamente prohibido guardar nombres completos, cédulas o datos de contacto directo en las bases de datos de esta carpeta.
2. **Identificadores Únicos (UID):** Toda persona atendida debe contar con un código anónimo desduplicado generado por sistema o fórmula MEAL para control de atenciones únicas.
3. **Cifrado de Casos:** Las carpetas o registros detallados de Gestión de Casos deben guardarse de forma cifrada y con accesos restringidos sólo a personal autorizado.

---

### 📖 Glosario de Conceptos Clave
* **MEAL:** *Monitoring, Evaluation, Accountability and Learning* (Monitoreo, Evaluación, Rendición de Cuentas y Aprendizaje).
* **SSR:** Salud Sexual y Reproductiva.
* **APS:** Atención Psicosocial (acompañamiento psicológico/emocional).
* **Gestión de Casos (Case Management):** Proceso estructurado de acompañamiento individual a sobrevivientes de violencia o vulneraciones de derechos.
* **OBP:** Observación Basada en Participantes.
* **PQR / PQRS:** Peticiones, Quejas, Reclamaciones y Sugerencias (mecanismo para Rendición de Cuentas o Accountability).
