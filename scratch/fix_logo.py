import os

docs_dir = r"c:\Users\Alfredo Pabón\Documents\Proyectos antigravity\proyecto_CARE_MEAL\docs"
targets = ["index.html", "visor_meal.html"]

for filename in targets:
    file_path = os.path.join(docs_dir, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Define replacements for Level 1 Tags with tooltip spans
        content = content.replace(
            '<span onclick="linkToMap(\'proteccion\')" class="cursor-pointer bg-[#FFF5F0] text-[#be5600] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#FFE4D6] hover:bg-[#FFE4D6] transition-colors">Atenciones Psicosociales (APS)</span>',
            '<span onclick="linkToMap(\'proteccion\')" class="relative group cursor-pointer bg-[#FFF5F0] text-[#be5600] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#FFE4D6] hover:bg-[#FFE4D6] transition-colors">Atenciones Psicosociales (APS)<span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 hidden group-hover:block w-56 bg-inverse-surface text-inverse-on-surface text-[11px] leading-relaxed p-2 rounded shadow-lg text-center z-30 font-normal">Acompañamiento psicológico individual o en crisis ante vulneraciones de derechos.</span></span>'
        )
        content = content.replace(
            '<span onclick="linkToMap(\'proteccion\')" class="cursor-pointer bg-[#FFF5F0] text-[#be5600] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#FFE4D6] hover:bg-[#FFE4D6] transition-colors">Gestión de Casos VBG</span>',
            '<span onclick="linkToMap(\'proteccion\')" class="relative group cursor-pointer bg-[#FFF5F0] text-[#be5600] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#FFE4D6] hover:bg-[#FFE4D6] transition-colors">Gestión de Casos VBG<span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 hidden group-hover:block w-56 bg-inverse-surface text-inverse-on-surface text-[11px] leading-relaxed p-2 rounded shadow-lg text-center z-30 font-normal">Acompañamiento continuo y especializado a personas sobrevivientes de violencias basadas en género.</span></span>'
        )
        content = content.replace(
            '<span onclick="linkToMap(\'salud\')" class="cursor-pointer bg-[#FFF5F0] text-[#be5600] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#FFE4D6] hover:bg-[#FFE4D6] transition-colors">Kits de Dignidad SSR</span>',
            '<span onclick="linkToMap(\'salud\')" class="relative group cursor-pointer bg-[#FFF5F0] text-[#be5600] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#FFE4D6] hover:bg-[#FFE4D6] transition-colors">Kits de Dignidad SSR<span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 hidden group-hover:block w-56 bg-inverse-surface text-inverse-on-surface text-[11px] leading-relaxed p-2 rounded shadow-lg text-center z-30 font-normal">Suministro de kits de higiene, salud reproductiva u otros insumos esenciales de dignidad.</span></span>'
        )
        content = content.replace(
            '<span onclick="linkToMap(\'juridico\')" class="cursor-pointer bg-[#FFF5F0] text-[#be5600] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#FFE4D6] hover:bg-[#FFE4D6] transition-colors">Remisiones a Derechos</span>',
            '<span onclick="linkToMap(\'juridico\')" class="relative group cursor-pointer bg-[#FFF5F0] text-[#be5600] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#FFE4D6] hover:bg-[#FFE4D6] transition-colors">Remisiones a Derechos<span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 hidden group-hover:block w-56 bg-inverse-surface text-inverse-on-surface text-[11px] leading-relaxed p-2 rounded shadow-lg text-center z-30 font-normal">Enlace efectivo de pacientes a la red de salud local o entidades de protección del Estado.</span></span>'
        )

        # Level 2 Tags
        content = content.replace(
            '<span onclick="linkToMap(\'conesperanza\')" class="cursor-pointer bg-[#F0FAFA] text-[#006666] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#D1F0F0] hover:bg-[#D1F0F0] transition-colors">Personas Únicas Atendidas</span>',
            '<span onclick="linkToMap(\'conesperanza\')" class="relative group cursor-pointer bg-[#F0FAFA] text-[#006666] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#D1F0F0] hover:bg-[#D1F0F0] transition-colors">Personas Únicas Atendidas<span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 hidden group-hover:block w-56 bg-inverse-surface text-inverse-on-surface text-[11px] leading-relaxed p-2 rounded shadow-lg text-center z-30 font-normal">Número total de beneficiarios únicos atendidos (desduplicados) en el período de reporte.</span></span>'
        )
        content = content.replace(
            '<span onclick="linkToMap(\'salud\')" class="cursor-pointer bg-[#F0FAFA] text-[#006666] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#D1F0F0] hover:bg-[#D1F0F0] transition-colors">Kits Entregados con Firma</span>',
            '<span onclick="linkToMap(\'salud\')" class="relative group cursor-pointer bg-[#F0FAFA] text-[#006666] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#D1F0F0] hover:bg-[#D1F0F0] transition-colors">Kits Entregados con Firma<span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 hidden group-hover:block w-56 bg-inverse-surface text-inverse-on-surface text-[11px] leading-relaxed p-2 rounded shadow-lg text-center z-30 font-normal">Total de kits de dignidad y SSR distribuidos físicamente con planilla de entrega firmada.</span></span>'
        )
        content = content.replace(
            '<span onclick="linkToMap(\'proteccion\')" class="cursor-pointer bg-[#F0FAFA] text-[#006666] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#D1F0F0] hover:bg-[#D1F0F0] transition-colors">Casos con Seguimiento Activo</span>',
            '<span onclick="linkToMap(\'proteccion\')" class="relative group cursor-pointer bg-[#F0FAFA] text-[#006666] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#D1F0F0] hover:bg-[#D1F0F0] transition-colors">Casos con Seguimiento Activo<span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 hidden group-hover:block w-56 bg-inverse-surface text-inverse-on-surface text-[11px] leading-relaxed p-2 rounded shadow-lg text-center z-30 font-normal">Número de carpetas de gestión de casos abiertas con un plan de seguimiento actualmente activo.</span></span>'
        )
        content = content.replace(
            '<span onclick="linkToMap(\'juridico\')" class="cursor-pointer bg-[#F0FAFA] text-[#006666] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#D1F0F0] hover:bg-[#D1F0F0] transition-colors">Derivaciones Efectivas</span>',
            '<span onclick="linkToMap(\'juridico\')" class="relative group cursor-pointer bg-[#F0FAFA] text-[#006666] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#D1F0F0] hover:bg-[#D1F0F0] transition-colors">Derivaciones Efectivas<span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 hidden group-hover:block w-56 bg-inverse-surface text-inverse-on-surface text-[11px] leading-relaxed p-2 rounded shadow-lg text-center z-30 font-normal">Tasa de efectividad de las derivaciones canalizadas que resultaron en citas confirmadas.</span></span>'
        )

        # Level 3 Tags
        content = content.replace(
            '<span onclick="linkToMap(\'conesperanza\')" class="cursor-pointer bg-[#F0F5FF] text-[#0040C1] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#D6E4FF] hover:bg-[#D6E4FF] transition-colors">6 Municipios Clave</span>',
            '<span onclick="linkToMap(\'conesperanza\')" class="relative group cursor-pointer bg-[#F0F5FF] text-[#0040C1] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#D6E4FF] hover:bg-[#D6E4FF] transition-colors">6 Municipios Clave<span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 hidden group-hover:block w-56 bg-inverse-surface text-inverse-on-surface text-[11px] leading-relaxed p-2 rounded shadow-lg text-center z-30 font-normal">Municipios prioritarios del proyecto ConEsperanza en Cauca y Norte de Santander.</span></span>'
        )
        content = content.replace(
            '<span onclick="linkToMap(\'conesperanza\')" class="cursor-pointer bg-[#F0F5FF] text-[#0040C1] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#D6E4FF] hover:bg-[#D6E4FF] transition-colors">6 Espacios Protectores Activos</span>',
            '<span onclick="linkToMap(\'conesperanza\')" class="relative group cursor-pointer bg-[#F0F5FF] text-[#0040C1] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#D6E4FF] hover:bg-[#D6E4FF] transition-colors">6 Espacios Protectores Activos<span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 hidden group-hover:block w-56 bg-inverse-surface text-inverse-on-surface text-[11px] leading-relaxed p-2 rounded shadow-lg text-center z-30 font-normal">Puntos físicos y seguros de atención humanitaria y protección integral en funcionamiento.</span></span>'
        )
        content = content.replace(
            '<span onclick="linkToMap(\'salud\')" class="cursor-pointer bg-[#F0F5FF] text-[#0040C1] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#D6E4FF] hover:bg-[#D6E4FF] transition-colors">Puntos de Atención SSR</span>',
            '<span onclick="linkToMap(\'salud\')" class="relative group cursor-pointer bg-[#F0F5FF] text-[#0040C1] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#D6E4FF] hover:bg-[#D6E4FF] transition-colors">Puntos de Atención SSR<span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 hidden group-hover:block w-56 bg-inverse-surface text-inverse-on-surface text-[11px] leading-relaxed p-2 rounded shadow-lg text-center z-30 font-normal">Espacios comunitarios adecuados para la consulta, orientación e insumos de salud sexual y reproductiva.</span></span>'
        )

        # Level 4 Tags
        content = content.replace(
            '<span onclick="linkToMap(\'cauca\')" class="cursor-pointer bg-[#F8F0FF] text-[#5300B3] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#EED6FF] hover:bg-[#EED6FF] transition-colors">Incidencia en Cauca</span>',
            '<span onclick="linkToMap(\'cauca\')" class="relative group cursor-pointer bg-[#F8F0FF] text-[#5300B3] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#EED6FF] hover:bg-[#EED6FF] transition-colors">Incidencia en Cauca<span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 hidden group-hover:block w-56 bg-inverse-surface text-inverse-on-surface text-[11px] leading-relaxed p-2 rounded shadow-lg text-center z-30 font-normal">Acciones de articulación e influencia política con autoridades del departamento del Cauca.</span></span>'
        )
        content = content.replace(
            '<span onclick="linkToMap(\'norte-de-santander\')" class="cursor-pointer bg-[#F8F0FF] text-[#5300B3] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#EED6FF] hover:bg-[#EED6FF] transition-colors">Incidencia en Norte de Santander</span>',
            '<span onclick="linkToMap(\'norte-de-santander\')" class="relative group cursor-pointer bg-[#F8F0FF] text-[#5300B3] text-xs font-semibold px-3 py-1.5 rounded-lg border border-[#EED6FF] hover:bg-[#EED6FF] transition-colors">Incidencia en Norte de Santander<span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 hidden group-hover:block w-56 bg-inverse-surface text-inverse-on-surface text-[11px] leading-relaxed p-2 rounded shadow-lg text-center z-30 font-normal">Acciones de articulación e influencia política en zonas de frontera en Norte de Santander.</span></span>'
        )

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"SUCCESS: Applied Step 3 Tooltips in {filename}")
