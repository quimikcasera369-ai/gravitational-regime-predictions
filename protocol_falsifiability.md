# Protocolo de Falsabilidad Inversa — Emergencia Gravitacional

**Autor:** Juan Pablo Figueroa Torres
**Versión:** Febrero 2026
**Tipo:** Test de confirmación fuerte

---

## Objetivo

El protocolo original confirmó que las galaxias **NON‑REGIME fallan**.
Este protocolo busca la otra mitad del test: encontrar galaxias **REGIME** y verificar si la predicción acierta.

* Si acierta sistemáticamente → la hipótesis se fortalece
* Si falla en REGIME → la hipótesis se falsifica

---

## Diferencia respecto al protocolo original

| Aspecto            | Protocolo original         | Este protocolo           |
| ------------------ | -------------------------- | ------------------------ |
| Objetivo           | Confirmar NON‑REGIME falla | Confirmar REGIME acierta |
| Galaxias buscadas  | Cualquiera                 | Solo g_int < a_crit      |
| Resultado esperado | Error > 20%                | Error ≤ 20%              |
| Poder de falsación | Moderado                   | Máximo                   |

---

## Paso 1 — Criterio de búsqueda en SPARC

Condición previa obligatoria:

```
g_int = V² / R < 1.0 × 10⁻¹¹ m/s²
```

Ejemplo:

```
V = 40 km/s , R = 5 kpc → REGIME
V = 50 km/s , R = 8 kpc → NON‑REGIME
```

Características esperadas:

* V_flat baja
* R_flat grande
* LSB / enanas difusas
* baja masa bariónica

---

## Paso 2 — Candidatos SPARC

| Galaxia | V_flat est | R_flat est | Tipo | Nota             |
| ------- | ---------- | ---------- | ---- | ---------------- |
| UGCA444 | ~38 km/s   | ~2.6 kpc   | LSB  | candidata fuerte |
| UGCA442 | ~57 km/s   | ~6.3 kpc   | LSB  | probable regime  |
| UGCA281 | ~30 km/s   | ~1.1 kpc   | LSB  | verificar        |
| DDO154  | 50 km/s    | 8 kpc      | gas  | borde umbral     |
| NGC3741 | ~50 km/s   | ~3 kpc     | LSB  | posible          |
| F563-1  | ~95 km/s   | ~10 kpc    | LSB  | verificar        |

*Usar siempre valores reales del catálogo SPARC.*

---

## Paso 3 — Flujo de ejecución

1. Convertir unidades a SI
2. Calcular g_int = V² / R
3. Clasificar régimen
4. Calcular predicción
5. Comparar con observación
6. Registrar veredicto

### Predicciones

```
R_T = sqrt(G·M / a_crit)
V_pred = (G·M·a_crit)^(1/4)
```

---

## Paso 4 — Criterio de falsación

```
error% = |V_pred − V_obs| / V_obs × 100
```

* error ≤ 20% → confirma
* error > 20% en REGIME → falsifica

También:

```
ratio = R_T / R_obs
ratio ∈ [0.5 , 2.0] → coherente
```

Se requieren mínimo 5 galaxias REGIME para significancia.

---

## Tabla de preregistro

| Galaxia | V_flat | R_flat | M_bar | g_int | Régimen | V_pred | R_T | Error% | Veredicto |
| ------- | ------ | ------ | ----- | ----- | ------- | ------ | --- | ------ | --------- |
| UGCA444 |        |        |       |       |         |        |     |        |           |
| UGCA442 |        |        |       |       |         |        |     |        |           |
| UGCA281 |        |        |       |       |         |        |     |        |           |
| NGC3741 |        |        |       |       |         |        |     |        |           |
| F563-1  |        |        |       |       |         |        |     |        |           |

---

## Regla de interpretación

* REGIME + acuerdo → apoya hipótesis
* NON‑REGIME + desviación → esperado
* REGIME + fallo → falsificación directa

---

**Clasificación fijada antes de ver resultados observacionales**
