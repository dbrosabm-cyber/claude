# Centro de mando de la tienda (Claude + Shopify)

Configuración para que Claude trabaje como director de e-commerce de la tienda
de dropshipping (España, EUR). Se carga sola al abrir una sesión en este repo.

| Pieza | Qué hace |
|---|---|
| `CLAUDE.md` | Rol, reglas de oro y qué conector usar. Corto a propósito: se lee en cada mensaje. |
| `.claude/settings.json` | Bloquea conectores que no aportan a la tienda (Vercel, Spotify, Gamma, Calendar, Supermetrics, Apollo) para ahorrar tokens. |
| `.claude/skills/` | Conocimiento experto que solo se carga cuando hace falta: `/producto-ganador`, `/ficha-producto`, `/creativos`, `/campanas-ads`, `/auditoria-tienda`, `/email-retencion`, `/informe`, `/marca`, `/contenido-organico`. |
| `negocio/` | Perfil del negocio, registro de productos , `guia-puesta-en-marcha.md` (ordenador y automatizaciones) y `plan-lanzamiento.md` (checklist hasta la primera venta). |
| `herramientas/rentabilidad.py` | Márgenes, CPA y ROAS break-even, precio sugerido. |
| `herramientas/tokens.py` | Consumo de tokens por pregunta. |

```bash
python3 herramientas/rentabilidad.py --pvp 39.95 --coste 9.80 --envio 4.20
python3 herramientas/rentabilidad.py --coste 9.80 --envio 4.20 --sugerir
python3 herramientas/tokens.py
```

Para volver a activar un conector bloqueado, quítalo de `deny` en `.claude/settings.json`.

---

## Revisión de trabajos de Claude con ChatGPT

Script que toma un archivo (código o texto generado por Claude) y lo envía a
la API de ChatGPT (OpenAI) para obtener una revisión crítica.

### 1. Conseguir una API key de OpenAI

1. Crea una cuenta en https://platform.openai.com/
2. Genera una key en https://platform.openai.com/api-keys
3. Activa facturación en https://platform.openai.com/account/billing
   (el uso de la API se cobra por tokens).

### 2. Instalación

#### Windows (automático)

Con Git y Python ya instalados, dentro de la carpeta del repo:

```powershell
.\setup.ps1
```

El script verifica los requisitos, instala las dependencias y te pide la API
key una sola vez (queda guardada de forma permanente para tu usuario de
Windows, no se pide de nuevo en futuras terminales).

#### Manual (cualquier sistema)

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-tu-key-aqui
```

### 3. Uso

```bash
python3 review_with_chatgpt.py ruta/al/archivo.py
```

Opciones:

```bash
python3 review_with_chatgpt.py ruta/al/archivo.py \
  --model gpt-4o \
  --instructions "Enfócate en problemas de seguridad y rendimiento"
```
