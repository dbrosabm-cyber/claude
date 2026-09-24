# Proyecto Bar del Abuelo (Parla)

Este repositorio es el proyecto digital del Bar del Abuelo, un bar de raciones
y tapas en Parla (Madrid): diseño, redes sociales, automatizaciones, web y
llamadas con IA para tomar pedidos.

Datos del bar, canales, marca y decisiones tomadas:

@docs/ficha-del-bar.md

## Cómo trabajar

- Habla siempre en español de España, de forma sencilla y sin tecnicismos.
  Quien lleva el proyecto no es programador.
- Cuando te den datos nuevos del bar, actualiza `docs/ficha-del-bar.md` y
  añade las decisiones importantes a su tabla de decisiones.
- **Nunca publiques, programes ni envíes nada** (posts, historias, respuestas a
  reseñas, correos, mensajes de WhatsApp) sin un visto bueno explícito para ese
  contenido concreto. Enséñalo antes.
- **Pregunta antes de contratar o activar cualquier servicio de pago.** Las
  llamadas con IA tienen un tope de 10–20 €/mes.
- No inventes precios ni platos: usa solo la carta confirmada. Si falta un
  dato, pídelo.
- El entorno de nube bloquea muchas webs externas. Si una página no carga,
  dilo y pide que se añada el dominio a la red permitida del entorno.

## Estructura

- `docs/`: documentación del proyecto (empieza por la ficha del bar)
- `herramientas/revision-chatgpt/`: script independiente para que ChatGPT
  revise lo que genera Claude; no forma parte del bar
