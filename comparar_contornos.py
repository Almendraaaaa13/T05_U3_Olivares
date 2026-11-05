import json
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from barra_mef import resolver_barra
from analisis import desplazamiento_referencia

ROOT = Path(__file__).resolve().parents[1]
p = json.loads((ROOT / "datos/barra.json").read_text())

parametros = dict(
    L=p["L_mm"], E=p["E_MPa"], A=p["A_mm2"],
    P=p["P_N"], q=p["q_N_mm"]
)

base = resolver_barra(8, **parametros)
alterado = resolver_barra(
    8, **parametros, extremo_derecho_fijo=True
)

salidas = ROOT / "salidas"
salidas.mkdir(exist_ok=True)

# Guardar los desplazamientos nodales de ambos modelos.
tabla = np.column_stack((base.x, base.u, alterado.u))
np.savetxt(
    salidas / "comparacion_contornos.csv",
    tabla,
    delimiter=",",
    header="x_mm,u_base_mm,u_alterado_mm",
    comments=""
)

# Referencias analíticas de cada problema de borde.
x = np.linspace(0, parametros["L"], 401)
u_base_ref = desplazamiento_referencia(x, **parametros)
u_alterado_ref = (
    parametros["q"] * x * (parametros["L"] - x)
    / (2 * parametros["E"] * parametros["A"])
)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, u_base_ref, "-", label="Referencia: contorno original")
ax.plot(base.x, base.u, "o--", label="MEF: contorno original")
ax.plot(x, u_alterado_ref, "-", label="Referencia: ambos extremos fijos")
ax.plot(alterado.x, alterado.u, "s--", label="MEF: ambos extremos fijos")

ax.set(xlabel="Posición x [mm]", ylabel="Desplazamiento u [mm]")
ax.grid(True, alpha=0.3)
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig(salidas / "comparacion_contornos.png", dpi=180)
plt.close(fig)

print("Comparación guardada en CSV y PNG.")
