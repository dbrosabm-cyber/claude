---
name: campanas-ads
description: Lanzar, testear, diagnosticar y escalar campañas de Meta Ads, TikTok Ads y Google Shopping para la tienda, con reglas de apagado y escalado y datos vía Windsor.ai. Úsala para campañas, presupuestos, ROAS, CPA o anuncios que no funcionan.
---

# Campañas de pago

## Antes de gastar 1 €
- Píxel + API de conversiones con las apps oficiales de Shopify (Facebook & Instagram, TikTok, Google & YouTube) con compartición de datos máxima. Dominio verificado en Meta.
- Eventos con valor: ViewContent, AddToCart, InitiateCheckout, Purchase. Compra de prueba hecha.
- CPA y ROAS break-even calculados con `herramientas/rentabilidad.py`. Presupuesto de test por producto ≥ 3 × CPA BE.

## Estructura Meta (test)
Campaña de ventas, objetivo compra, España, público amplio (Advantage+), ubicaciones Advantage+. 1 conjunto por ángulo con 3-5 creatividades, o una campaña Advantage+ de ventas con todas. No se toca en 72 h salvo reglas de apagado.

## Reglas de apagado
- Gasto ≥ 1 × CPA BE sin ningún añadido al carrito → apagar anuncio.
- Gasto ≥ 2 × CPA BE sin compra → apagar.
- CTR de enlace < 0,8 % con > 2.000 impresiones → creatividad floja.
- Hook rate (reproducciones 3 s / impresiones) < 25 % → cambiar los 3 primeros segundos.
- Producto sin compras tras 3 ángulos distintos → producto muerto, no insistas.

## Escalado
- ROAS ≥ objetivo 3 días seguidos → +20-30 % de presupuesto cada 48-72 h.
- Ganadores a una campaña de escalado (Advantage+/CBO) y nuevos ángulos cada semana: la fatiga llega en 2-4 semanas (TikTok antes).
- TikTok: Spark Ads con contenido de creadores, refresco semanal. Google: Shopping/PMax con feed de Merchant Center solo si hay volumen de búsqueda.

## Diagnóstico del embudo
CPM alto → creatividad o público pequeño · CTR bajo → gancho · CTR alto y pocas conversiones → página de producto, precio o confianza · muchos carritos y pocas compras → envío/pagos en el checkout. Referencias ES frío: CTR enlace 1-2 %, conversión 1-2,5 %, añadido al carrito 5-10 % de sesiones.

## Datos
Windsor `get_data` (facebook / tiktok / google_ads): spend, impressions, clicks, ctr, cpc, purchases, purchase value por campaña/anuncio. Cruza con ventas reales de Shopify y calcula MER. Cambios (pausar, presupuestos) con `execute_action` solo tras confirmación explícita del cambio concreto.

## Políticas
Sin atributos personales, sin claims de salud, antes/después corporal ni escasez falsa. Cuenta publicitaria con 2FA y administrador de respaldo.
