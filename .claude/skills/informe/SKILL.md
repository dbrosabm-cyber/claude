---
name: informe
description: Informe de resultados de la tienda (ventas, pedidos, AOV, conversión, gasto en ads, MER, CPA, margen) con comparativa y acciones. Úsala para "cómo vamos", informe semanal/mensual, KPIs o análisis de ventas.
---

# Informe de resultados

## Datos
1. Shopify `run-analytics-query` (ShopifyQL) para el periodo y el anterior: ventas totales, pedidos, AOV, sesiones, tasa de conversión, productos top. Si una consulta falla, busca la sintaxis con `search_docs_chunks` en vez de probar a ciegas.
2. Gasto y resultados por plataforma: Windsor `get_data` (facebook, tiktok, google_ads): spend, purchases, purchase value, ctr, cpm.
3. Costes: coste puesto medio desde `negocio/registro-productos.md` o `herramientas/rentabilidad.py`.

## KPIs (siempre en este orden)
MER (ventas / gasto ads) · beneficio de contribución (ventas netas − coste producto/envío − pasarela − ads) · CPA real (gasto / pedidos Shopify) vs CPA BE · AOV · tasa de conversión · % ventas de email · reembolsos y contracargos.

## Formato
Tabla compacta con periodo actual, anterior y variación %. Luego 3 conclusiones y 3 acciones concretas para la semana siguiente, con responsable. Si lo piden visual, un artifact con la skill dataviz.

## Alertas automáticas
MER < ROAS BE de la tienda → perdiendo dinero · conversión cae > 30 % → revisar web, checkout y stock del proveedor · reembolsos > 5 % → problema de producto o plazos.
