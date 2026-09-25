#!/usr/bin/env python3
"""Calculadora de rentabilidad por pedido para dropshipping (España/UE).

Ejemplos:
  python3 herramientas/rentabilidad.py --pvp 39.95 --coste 9.80 --envio 4.20
  python3 herramientas/rentabilidad.py --coste 9.80 --envio 4.20 --sugerir
  python3 herramientas/rentabilidad.py --pvp 39.95 --coste 9.80 --envio 4.20 --arancel 0 --margen-objetivo 0.20

Supuestos por defecto (ajústalos a tu caso real):
  IVA 21 % incluido en el PVP · pasarela 1,6 % + 0,25 € (Shopify Payments,
  plan Advanced, tarjetas EEE: comprueba tus tarifas en el panel) ·
  arancel fijo UE de 3 € por envío de fuera de la UE (< 150 €), pon 0 si el
  proveedor lo incluye o sale de almacén UE · devoluciones/incidencias 5 %.
El ROAS se calcula sobre el PVP con IVA, que es el valor que suelen ver Meta/TikTok.
"""
import argparse


def calcular(pvp, a):
    neto = pvp / (1 + a.iva)
    pasarela = pvp * a.pasarela_pct + a.pasarela_fijo
    puesto = a.coste + a.envio + a.arancel + a.extra
    devoluciones = neto * a.devoluciones
    margen = neto - puesto - pasarela - devoluciones
    cpa_obj = margen - a.margen_objetivo * neto
    return {
        "pvp": pvp, "neto": neto, "puesto": puesto, "pasarela": pasarela,
        "devoluciones": devoluciones, "margen": margen, "margen_pct": margen / neto,
        "roas_be": pvp / margen if margen > 0 else float("inf"),
        "cpa_obj": cpa_obj,
        "roas_obj": pvp / cpa_obj if cpa_obj > 0 else float("inf"),
        "multiplo": neto / puesto,
    }


def precio_psicologico(p):
    base = int(p)
    return base + 0.95 if p - base <= 0.95 else base + 1.95


def eur(x):
    return f"{x:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")


def num(x, fmt=".2f"):
    return format(x, fmt).replace(".", ",")


def veredicto(r):
    if r["margen"] <= 0:
        return "NO: pierdes dinero antes de publicidad"
    if r["roas_be"] > 2.5 or r["multiplo"] < 2.5:
        return "FLOJO: margen justo, solo si el CPA real es muy bajo o subes AOV (packs)"
    if r["roas_be"] > 2.0:
        return "OK: viable con creatividades fuertes"
    return "BUENO: margen cómodo para testear y escalar"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--pvp", type=float, help="precio de venta con IVA")
    p.add_argument("--coste", type=float, required=True, help="coste del producto al proveedor")
    p.add_argument("--envio", type=float, default=0.0, help="coste de envío al cliente que pagas tú")
    p.add_argument("--arancel", type=float, default=3.0)
    p.add_argument("--extra", type=float, default=0.0, help="embalaje, inserts, etc. por pedido")
    p.add_argument("--iva", type=float, default=0.21)
    p.add_argument("--pasarela-pct", type=float, default=0.016)
    p.add_argument("--pasarela-fijo", type=float, default=0.25)
    p.add_argument("--devoluciones", type=float, default=0.05, help="provisión sobre ventas netas")
    p.add_argument("--margen-objetivo", type=float, default=0.15, help="beneficio neto deseado tras ads, sobre ventas netas")
    p.add_argument("--sugerir", action="store_true", help="propone PVP a 2,5x-4x del coste puesto")
    a = p.parse_args()

    if a.sugerir or a.pvp is None:
        puesto = a.coste + a.envio + a.arancel + a.extra
        print(f"Coste puesto en destino: {eur(puesto)}\n")
        print(f"{'múltiplo':>8} {'PVP':>10} {'margen':>10} {'margen %':>9} {'CPA BE':>9} {'ROAS BE':>8} {'ROAS obj':>9}")
        for m in (2.5, 3.0, 3.5, 4.0):
            pvp = precio_psicologico(puesto * m * (1 + a.iva))
            r = calcular(pvp, a)
            print(f"{num(m, '.1f'):>7}x {eur(pvp):>10} {eur(r['margen']):>10} {r['margen_pct']:>8.0%} "
                  f"{eur(r['margen']):>9} {num(r['roas_be']):>8} {num(r['roas_obj']):>9}")
        print("\nRegla: en frío busca ROAS BE ≤ 2,0 (múltiplo ≥ 3x). Por debajo, sube AOV con packs.")
        return

    r = calcular(a.pvp, a)
    filas = [
        ("PVP (con IVA)", eur(r["pvp"])),
        ("Ingreso neto (sin IVA)", eur(r["neto"])),
        ("Coste puesto (producto+envío+arancel+extra)", eur(r["puesto"])),
        ("Pasarela de pago", eur(r["pasarela"])),
        ("Provisión devoluciones", eur(r["devoluciones"])),
        ("Margen de contribución antes de ads", f"{eur(r['margen'])} ({r['margen_pct']:.0%})"),
        ("CPA máximo (break-even)", eur(r["margen"])),
        ("ROAS break-even", num(r["roas_be"])),
        (f"CPA objetivo (beneficio {a.margen_objetivo:.0%})", eur(r["cpa_obj"])),
        ("ROAS objetivo", num(r["roas_obj"])),
        ("Múltiplo neto / coste puesto", num(r["multiplo"], ".1f") + "x"),
    ]
    ancho = max(len(k) for k, _ in filas)
    for k, v in filas:
        print(f"{k:<{ancho}}  {v}")
    print(f"\nVeredicto: {veredicto(r)}")


if __name__ == "__main__":
    main()
