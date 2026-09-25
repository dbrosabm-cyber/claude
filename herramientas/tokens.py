#!/usr/bin/env python3
"""Escáner de consumo de tokens de Claude Code, pregunta a pregunta.

Lee los transcripts (~/.claude/projects/*/*.jsonl) y muestra, por cada
mensaje tuyo, cuántas llamadas al modelo hizo Claude y cuántos tokens movió.

Uso:
  python3 herramientas/tokens.py            # sesión más reciente
  python3 herramientas/tokens.py --todas    # resumen de todas las sesiones
  python3 herramientas/tokens.py ruta.jsonl # un transcript concreto

"Peso" = tokens equivalentes a entrada normal, con las proporciones de
precio estándar de Anthropic (lectura de caché 0,1x, escritura de caché
1h 2x, salida 5x). Es una aproximación para comparar, no una factura.
"""
import glob
import json
import os
import sys

PESOS = {"input": 1.0, "cache_write": 2.0, "cache_read": 0.1, "output": 5.0}


def es_pregunta(entrada):
    if entrada.get("type") != "user" or entrada.get("isMeta"):
        return False
    contenido = (entrada.get("message") or {}).get("content")
    if isinstance(contenido, str):
        return True
    return isinstance(contenido, list) and any(
        isinstance(b, dict) and b.get("type") == "text" for b in contenido
    )


def texto_pregunta(entrada):
    contenido = entrada["message"]["content"]
    if isinstance(contenido, list):
        contenido = " ".join(b.get("text", "") for b in contenido if b.get("type") == "text")
    return " ".join(contenido.split())[:48]


def analizar(ruta):
    turnos, vistos = [], set()
    for linea in open(ruta, encoding="utf-8"):
        try:
            entrada = json.loads(linea)
        except json.JSONDecodeError:
            continue
        if es_pregunta(entrada):
            turnos.append({"pregunta": texto_pregunta(entrada), "llamadas": 0, "contexto": 0,
                           "input": 0, "cache_write": 0, "cache_read": 0, "output": 0})
            continue
        msg = entrada.get("message")
        if entrada.get("type") != "assistant" or not isinstance(msg, dict) or not turnos:
            continue
        uso, mid = msg.get("usage"), msg.get("id")
        if not uso or mid in vistos:
            continue
        vistos.add(mid)
        t = turnos[-1]
        t["llamadas"] += 1
        t["input"] += uso.get("input_tokens", 0)
        t["cache_write"] += uso.get("cache_creation_input_tokens", 0)
        t["cache_read"] += uso.get("cache_read_input_tokens", 0)
        t["output"] += uso.get("output_tokens", 0)
        if t["llamadas"] == 1:
            t["contexto"] = (uso.get("input_tokens", 0) + uso.get("cache_creation_input_tokens", 0)
                             + uso.get("cache_read_input_tokens", 0))
    for t in turnos:
        t["peso"] = round(sum(t[k] * PESOS[k] for k in PESOS))
    return turnos


def fmt(n):
    return f"{n:,}".replace(",", ".")


def informe(ruta):
    turnos = analizar(ruta)
    print(f"\nSesión: {os.path.basename(ruta)}")
    cab = f"{'#':>2} {'pregunta':<48} {'llam':>4} {'contexto':>9} {'caché leída':>12} {'caché escr.':>11} {'salida':>7} {'peso':>9}"
    print(cab + "\n" + "-" * len(cab))
    for i, t in enumerate(turnos, 1):
        print(f"{i:>2} {t['pregunta']:<48} {t['llamadas']:>4} {fmt(t['contexto']):>9} "
              f"{fmt(t['cache_read']):>12} {fmt(t['cache_write']):>11} {fmt(t['output']):>7} {fmt(t['peso']):>9}")
    if turnos:
        print(f"\nBase fija al empezar (prompt de sistema + herramientas + CLAUDE.md): {fmt(turnos[0]['contexto'])} tokens")
        print(f"Peso total de la sesión: {fmt(sum(t['peso'] for t in turnos))}")
    return turnos


def main():
    args = sys.argv[1:]
    base = os.path.expanduser("~/.claude/projects")
    rutas = sorted(glob.glob(f"{base}/*/*.jsonl"), key=os.path.getmtime)
    if args and args[0] != "--todas":
        rutas = [args[0]]
    elif not args:
        rutas = rutas[-1:]
    if not rutas:
        sys.exit("No hay transcripts en ~/.claude/projects")
    for ruta in rutas:
        informe(ruta)


if __name__ == "__main__":
    main()
