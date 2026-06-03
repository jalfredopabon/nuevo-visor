# 📝 Bitácora de Avance — Visor MEAL CARE Colombia

Este archivo registra el progreso, actividades y optimizaciones del desarrollo del **Visor MEAL Interactivo (Teoría del Cambio & Mapa Operativo)** de CARE Colombia.

---

## 🌟 Información del Proyecto
* **Nombre:** Visor MEAL Interactivo
* **Ubicación principal:** `docs/index.html`
* **Estilo visual:** "Humanitarian Clarity" (CARE Orange `#E36F1E`, Inter, bordes suaves).
* **Propósito:** Facilitar la trazabilidad de metas y flujos operacionales a los equipos en territorio.

---

## 📈 Tablero de Control de Actividades
- `[x]` Crear estructura unificada de Teoría del Cambio y Mapa Operativo (Completado: 2026-06-03).
- `[x]` Diseño responsivo y transiciones de pestañas (Completado: 2026-06-03).
- `[x]` Interactividad fluida entre Teoría del Cambio y tarjetas del Mapa (Completado: 2026-06-03).
- `[x]` Integración del Asistente de Carga (Wizard) interactivo de 5 niveles (Completado: 2026-06-03).
- `[ ]` Carga dinámica de links reales desde la carpeta de Drive (Pendiente).

---

## 📌 Historial de Avance y Sesiones

### [2026-06-03] Implementación y Diseño Base
* `[x]` Creación de la estructura del visor interactivo premium unificando la Teoría del Cambio y el Mapa Operativo.
* `[x]` Implementación del diseño visual basado en paleta de colores corporativos e iconografía de Material Symbols.
* `[x]` Programación de la lógica para alternar vistas (Geográfica vs. Estratégica) en el Mapa Operativo.

### [2026-06-03] Optimización de UX e Interactividad Avanzada
* `[x]` **Unificación de JavaScript:** Corrección de la etiqueta de cierre `</script>` prematura que rompía la inicialización de `wizardState` en consola.
* `[x]` **Navegación inteligente (linkToMap):** Al hacer clic en un indicador de la Teoría del Cambio, el visor cambia a Mapa Operativo, localiza y hace scroll hasta la tarjeta correspondiente, iluminándola por 3 segundos.
* `[x]` **Corrección de nombres territoriales:** Corrección del municipio "Harací" a "Hacarí" en el listado de Norte de Santander.
* `[x]` **Botones de retroceso dinámicos:** Actualización en el asistente de carga para que el usuario sepa a qué nivel retrocede exactamente ("Volver a departamento", "Volver a municipio", etc.).
* `[x]` **Identificación de enlaces pendientes:** Reemplazo de links rotos por badges visuales ámbar corporativos con el texto *"Próximamente links de evidencia"*.
* `[x]` **Logo CARE:** Corrección de la URL del logo de la cabecera para cargar desde `care_horizontal.webp`.
