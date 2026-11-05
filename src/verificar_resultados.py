"""Reproduce la verificación de Colab; conserva sus CSV originales."""
import csv
import json
from pathlib import Path
import numpy as np
from barra_mef import resolver_barra
from analisis import desplazamiento_referencia, error_puntos_medios
ROOT = Path(__file__).resolve().parents[1]
p = json.loads((ROOT/'datos/barra.json').read_text())
kw = dict(L=p['L_mm'], E=p['E_MPa'], A=p['A_mm2'], P=p['P_N'], q=p['q_N_mm'])
for n, fijo in [(2,False),(4,False),(8,False),(8,True)]:
    r = resolver_barra(n, **kw, extremo_derecho_fijo=fijo)
    residuo = r.K@r.u-r.f
    relativo = abs(residuo[r.fijos].sum()+r.f.sum())/abs(kw['P']+kw['q']*kw['L'])
    assert relativo <= 1e-8
    assert np.max(abs(residuo[r.libres]))/abs(kw['P']+kw['q']*kw['L']) <= 1e-8
    if not fijo:
        esperado = abs(kw['q'])*(kw['L']/n)**2/(8*kw['E']*kw['A'])
        assert np.isclose(error_puntos_medios(r,**kw), esperado, rtol=1e-10,atol=1e-14)
        assert np.allclose(r.u, desplazamiento_referencia(r.x,**kw),rtol=1e-10,atol=1e-14)
    else:
        assert np.allclose(r.reacciones[r.fijos], [-10000,-30000])
    print(f'n={n}, fijo_derecho={fijo}, residuo_libre_N={np.max(abs(residuo[r.libres])):.12e}, balance_relativo={relativo:.12e}: OK')
print('Referencia, error, residuos y reacciones verificados.')
