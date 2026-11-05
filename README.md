# T05 | Sensibilidad a malla y condiciones de borde
Se entrega un solver NumPy de elementos finitos 1D; se evalúa su análisis, no reescribir el solver ni memorizar APDL.
1. Lea `datos/barra.json` y registre predicciones en `BITACORA.md` antes de ejecutar.
2. Complete `src/analisis.py` (referencia y error entre nodos).
3. Ejecute `python -m pytest -q` y `python src/ejecutar.py`.
4. Contraste tres mallas y el caso BC_ALTERADO; interprete por qué puede cerrar equilibrio y representar otro problema.
5. Prepare el informe de hasta dos páginas y responda el cuestionario individual en Moodle.
Los tests suministrados comprueban el solver base, no certifican su análisis completo.
## Entorno y ejecución
Abra la carpeta de la actividad (no una carpeta superior) en VS Code. Use el intérprete del entorno del laboratorio.
Para un entorno propio: `python -m venv .venv`, active ese entorno y ejecute `python -m pip install -r requirements.txt`.
En Windows puede ejecutar `.venv\Scripts\python.exe` sin cambiar la política de PowerShell. En Linux use `.venv/bin/python`.
Las actividades T06, T07 y H03 necesitan un motor MAPDL instalado y una licencia accesible. El paquete Python no los incluye.
El lanzador suministrado inicia y cierra solo su propia sesión local. Para un servidor del laboratorio utilice el acceso provisto por el docente.
No comparta credenciales ni exponga puertos del solver. No ejecute código recibido sin revisarlo.
Los bloques PENDIENTE/NotImplementedError son trabajo del estudiante, no fallos del entorno.

## Informe y entrega
Reutilice `informe/main.tex`: es la plantilla U1 con el contenido orientador actualizado.
Conserve `README.md`, entradas, código, CSV, logs y versiones. Incluya el PDF compilado y todas sus fuentes.
Complete `entrega.json` y `USO_IA.md`; copie la URL real del repositorio y el hash completo del commit evaluado.
No incluya `.venv`, `.git`, credenciales ni archivos binarios grandes del solver. Los logs textuales sí se entregan.
Las tolerancias comprueban resultados; no confunda un test que pasa con validación experimental.

## Preentrega
Ejecute `python verificar_entrega.py .` para detectar archivos faltantes; no ejecuta el código ni reemplaza la rúbrica. Las advertencias son de estructura, no una nota.
Tras verificar su entorno, registre sus versiones con `python -m pip freeze > requirements-lock.txt`. No incluya `.venv` en la entrega.

## Revisión y reproducción adicional
Los CSV y PNG de salidas conservan la ejecución recibida de Colab.
Ejecute desde la raíz: `python src/verificar_resultados.py` y `python src/comparar_contornos.py`. Las pruebas y la comprobación analítica se repitieron en un entorno de revisión; registros/ identifica sus versiones, sin atribuirlas a Colab.
Compile en informe/: `pdflatex main.tex`, `bibtex main`, `pdflatex main.tex`, `pdflatex main.tex`. En Overleaf suba el proyecto completo y seleccione informe/main.tex.
Antes de entregar, complete URL real y hash completo en entrega.json, compruebe el acceso docente al repositorio y pruebe una copia extraída del ZIP. El PDF mantiene A4, 11 pt y márgenes de 2,4 cm. No se ha creado ni publicado un repositorio.
