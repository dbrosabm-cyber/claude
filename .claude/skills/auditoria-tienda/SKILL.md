---
name: auditoria-tienda
description: Auditar la tienda Shopify (conversión, velocidad, confianza, SEO y cumplimiento legal España/UE) y devolver un plan priorizado. Úsala para revisar la tienda, antes de lanzar anuncios o si convierte poco.
---

# Auditoría de tienda

Revisa con Shopify (`get-shop-info`, `search_products`, y GraphQL para `shop { shopPolicies }`, páginas y menús, pidiendo campos mínimos) y con lo que el usuario te enseñe. Puntúa cada bloque 0-10.

## 1. Legal España/UE (bloqueante antes de anunciarse)
- Aviso legal (LSSI art. 10): titular, NIF, domicilio, email.
- Privacidad RGPD y banner de cookies con "Rechazar" tan visible como "Aceptar" (criterio AEPD).
- Condiciones de venta: desistimiento 14 días con formulario modelo, quién paga la devolución, garantía legal de 3 años, plazos de entrega reales, precios con IVA y gastos de envío visibles antes del checkout.
- Omnibus: descuento anunciado = referencia al precio más bajo de los 30 días previos; informar de si se verifican las reseñas y cómo; ni reseñas ni urgencias falsas.
- GPSR (desde dic-2024): en cada ficha, fabricante, persona responsable UE, identificación del producto y advertencias en español.
- Accesibilidad (European Accessibility Act, desde jun-2025): exenta la microempresa (<10 empleados y ≤ 2 M€); si no, contraste, alt, navegación por teclado.
- La plataforma ODR de la UE cerró en 2025: quita enlaces viejos a ella.

## 2. Conversión (móvil)
Barra de anuncio con oferta o envío · héroe con el producto estrella y CTA · ficha según la skill `ficha-producto` · carrito lateral con barra de envío gratis y 1 venta cruzada · pagos exprés (Shop Pay, Apple/Google Pay, PayPal; Bizum si el público lo pide) · páginas de contacto (email real, WhatsApp), sobre nosotros, seguimiento de pedido y FAQ.

## 3. Velocidad
LCP móvil < 2,5 s. Máximo 8-10 apps; quita apps desinstaladas que dejan código en el tema. Imágenes ≤ 2048 px, sin carruseles automáticos pesados ni vídeos en autoplay arriba del todo.

## 4. SEO
Título SEO y meta descripción únicos en productos y colecciones, alt en imágenes, handles limpios, colecciones con texto, sin productos de prueba publicados, dominio propio conectado.

## 5. Stack de apps recomendado (mínimo viable)
Proveedor (DSers, CJ Dropshipping o proveedor con almacén UE) · reseñas (Judge.me o Loox) · packs/upsell (Kaching Bundles o similar) · seguimiento (Parcel Panel/Track123) · email (Shopify Email para empezar; Klaviyo al escalar) · traducción (Translate & Adapt) · píxeles oficiales de Meta/TikTok/Google. Todo lo que no sume ventas, fuera.

## Entregable
Nota por bloque, luego las 10 acciones de mayor impacto ordenadas por impacto/esfuerzo, con quién hace cada una (Claude vía Shopify o el usuario en el panel). Pide confirmación antes de cambiar nada.
