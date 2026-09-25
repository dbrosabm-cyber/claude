# Guía de puesta en marcha: tu ordenador y la tienda en piloto automático

Objetivo: que la IA haga el máximo trabajo y tú solo decidas, pongas contraseñas y apruebes pagos.
Tiempo total: 3-4 horas repartidas en 2-3 días.

## Fase A · Tu ordenador (1 hora)

1. **Perfil de Chrome "Tienda"**: Chrome → tu foto → Añadir perfil. Todo lo de la tienda, solo aquí.
2. **Extensión Claude in Chrome** en ese perfil (claude.ai/chrome) y fíjala con la chincheta.
3. **Claude Desktop**: claude.ai/download → instalar → iniciar sesión → Ajustes → Conectores → activar Claude in Chrome.
4. **Limpia conectores de tu cuenta** en claude.ai/customize/connectors: desactiva Spotify, Vercel, Gamma, Apollo, Google Calendar y Supermetrics. Así ahorras tokens en todos los chats, no solo en este proyecto.
5. **Crea un Proyecto en Claude** (claude.ai → Proyectos → Nuevo) llamado como la tienda:
   - En "Instrucciones" pega el contenido de `CLAUDE.md`.
   - En "Conocimiento" sube `negocio/perfil.md` y `negocio/registro-productos.md`.
   - Cada chat que abras dentro del proyecto sabrá ya quién eres, el nicho, las reglas y los márgenes.
6. **Sube las habilidades a tu cuenta**: comprime cada carpeta de `.claude/skills/` (por ejemplo `ficha-producto`) en un .zip y súbelo en claude.ai → Ajustes → Capacidades → Skills. Así las tendrás también en los chats normales.
7. **Carpeta en Google Drive** "Tienda" con subcarpetas: Productos, Creatividades, Proveedores, Legal, Informes. Claude guarda ahí lo que genere.

## Fase B · Cuentas (1-2 horas; las contraseñas las pones tú)

Deja la sesión iniciada en el perfil "Tienda" de Chrome en cada una:

1. **Shopify**: baja el plan a Basic (Ajustes → Plan).
2. **CJ Dropshipping**: crea la cuenta e instala su app en Shopify.
3. **Apps gratis de Shopify**: Google & YouTube (Google Shopping gratis), Pinterest, TikTok, Judge.me (reseñas), Shopify Inbox (chat con clientes), Klaviyo (email; ya está conectado a Claude).
4. **Redes de la marca**: TikTok, Instagram (cuenta profesional), YouTube y Pinterest Business, todas con el mismo nombre.
5. **Metricool**: vincula esas 4 redes (Conexiones).
6. **Google Merchant Center**: se crea desde la app Google & YouTube.
7. **Alta de autónomo** (gestoría online) y **cuenta bancaria solo para la tienda**. Lo necesitas para TikTok Shop y para cobrar legalmente.

## Fase C · Automatizaciones (Claude las monta contigo)

| Qué se automatiza | Herramienta | Resultado |
|---|---|---|
| Pedidos al proveedor | App CJ con pedido y pago automáticos (con saldo precargado) | El pedido llega a CJ y se envía sin que toques nada |
| Seguimiento al cliente | CJ + Shopify (números de seguimiento automáticos) | El cliente recibe el tracking solo |
| Emails de venta | Klaviyo: bienvenida, carrito abandonado, post-compra, reseñas | Ventas extra mientras duermes |
| Reglas internas | Shopify Flow (gratis): etiquetar clientes, avisos de stock o de pedidos atascados | Menos revisiones manuales |
| Registro y avisos | Zapier: cada pedido a una hoja de Google, aviso de reseñas malas | Todo anotado sin copiar y pegar |
| Publicaciones | Metricool: Claude prepara 14 días de vídeos y textos y los programa tras tu OK | Redes activas a diario |
| Atención al cliente | Shopify Inbox con respuestas sugeridas + Sidekick (IA de Shopify) | Respuestas en segundos |
| Informe semanal | Rutina programada de Claude cada lunes (`/informe`) | Números y 3 acciones sin pedirlo |

## Fase D · El encargo para montar la tienda al 100 %

Ábrelo en una sesión de Claude Code sobre este repositorio (rama con esta configuración) y pega:

> Monta la tienda de Shopify al 100 % siguiendo CLAUDE.md y negocio/perfil.md. Orden:
> 1. Confírmame nombre y marca (skill marca) y guárdalo en el perfil.
> 2. Busca en CJ los 6 productos de la idea con stock en almacén UE y pásalos por herramientas/rentabilidad.py. Descarta los que no den ROAS break-even ≤ 2,5.
> 3. Crea colecciones y las fichas completas en DRAFT con la skill ficha-producto, más el pack.
> 4. Crea páginas: Sobre nosotros, Envíos, Devoluciones, Preguntas frecuentes, Contacto, y textos de políticas (aviso legal, privacidad, términos) con los datos que te dé.
> 5. Menús principal y de pie, código BIENVENIDA10 y SEO de todo.
> 6. Pasa la skill auditoria-tienda y dame la lista de lo que me toca hacer a mí en el panel.
> No publiques nada ni gastes dinero sin preguntarme.

Ten a mano antes de empezar: nombre de la tienda, tu nombre o empresa y NIF, dirección, email de contacto, logo (o pide que te lo diseñe con Canva) y la persona responsable en la UE de cada producto (la da el proveedor).
