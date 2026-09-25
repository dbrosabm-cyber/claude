---
name: producto-ganador
description: Buscar y validar productos ganadores para dropshipping en España (tendencias TikTok/IG, anuncios activos, márgenes, riesgos UE) y decidir GO/NO GO. Úsala al buscar nicho, producto nuevo o evaluar uno concreto.
---

# Producto ganador

## 1. Buscar (señales de demanda, no opiniones)
- vidIQ `vidiq_instagram_tiktok_outlier_search`: vídeos muy por encima de la media de su cuenta, últimos 60 días. Palabras: nicho + "tiktok made me buy it", "gadget", "amazon finds", "producto viral", "problema que resuelve".
- Meta Ad Library España (dáselo al usuario como enlace): `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ES&q=<producto>`. Anuncio activo >30 días con varias variantes = alguien lo está rentabilizando.
- Ahrefs `keywords-explorer-overview` (country `es`): volumen de búsqueda = canal Google Shopping/SEO posible.
- Precio de referencia: Amazon.es y competidores ES. Si Amazon lo vende a <1,5x tu coste puesto con entrega en 24 h, descártalo.

## 2. Puntuar (0-2 cada criterio; GO ≥ 15/20)
1. Wow visual: se entiende y sorprende en 3 s de vídeo sin sonido.
2. Resuelve un dolor o deseo fuerte (dolor, ahorro de tiempo, estatus, mascota, bebé, hogar).
3. Difícil de encontrar barato en tienda física o Amazon.es.
4. Margen: coste puesto ≤ 1/3 del PVP neto; PVP ideal 25-80 €.
5. Logística: ligero, no frágil, sin tallas, entrega ≤ 8 días laborables (mejor almacén UE).
6. Demanda probada: outliers recientes + anuncios activos >30 días.
7. Saturación baja en ES, o un ángulo nuevo claro frente a la competencia.
8. AOV: admite packs, complementos o recompra.
9. Políticas de ads: sin claims médicos/adelgazar, sin marcas registradas ni copias, sin antes/después corporal.
10. Cumplimiento UE: CE/RoHS si es eléctrico, enchufe UE, instrucciones en español, fabricante identificado y persona responsable en la UE (GPSR).

Descarte directo: cosmética (exige notificación CPNP), suplementos y alimentos, juguetes sin EN71, baterías sueltas, líquidos, réplicas de marca, productos sanitarios.

## 3. Números
`python3 herramientas/rentabilidad.py --coste <c> --envio <e> --sugerir` y luego con el PVP elegido. Arancel: 3 € si sale de fuera de la UE salvo que el proveedor lo incluya (verifica con WebSearch si hay cambios).

## 4. Entregable
Tabla de puntuación · rentabilidad (PVP, ROAS BE, CPA BE) · 3 ángulos de venta con su gancho · riesgos · veredicto GO/NO GO · siguiente paso (muestra física antes de escalar). Añade una fila en `negocio/registro-productos.md`.
