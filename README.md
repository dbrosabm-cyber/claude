# Revisión de trabajos de Claude con ChatGPT

Script que toma un archivo (código o texto generado por Claude) y lo envía a
la API de ChatGPT (OpenAI) para obtener una revisión crítica.

## 1. Conseguir una API key de OpenAI

1. Crea una cuenta en https://platform.openai.com/
2. Genera una key en https://platform.openai.com/api-keys
3. Activa facturación en https://platform.openai.com/account/billing
   (el uso de la API se cobra por tokens).

## 2. Instalación

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-tu-key-aqui
```

## 3. Uso

```bash
python3 review_with_chatgpt.py ruta/al/archivo.py
```

Opciones:

```bash
python3 review_with_chatgpt.py ruta/al/archivo.py \
  --model gpt-4o \
  --instructions "Enfócate en problemas de seguridad y rendimiento"
```
