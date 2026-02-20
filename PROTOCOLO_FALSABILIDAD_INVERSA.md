# Test de Confirmación Fuerte
## Protocolo de Falsabilidad Inversa

**Autor:** Juan Pablo Figueroa Torres  
**Versión:** Febrero 2026  
**Complemento de:** Protocolo Operacional v1

---

## Objetivo

El protocolo original confirmó que las galaxias **NON-REGIME** fallan (esa es la mitad del test).  
Este protocolo busca la otra mitad: encontrar galaxias que clasifiquen como **REGIME** (`g_int < a_crit`) y verificar si la predicción acierta.

- Si acierta sistemáticamente → **la hipótesis se fortalece**.
- Si falla en REGIME → **la hipótesis se falsifica**.

---

## Contexto

### ¿Qué cambia respecto al protocolo original?

| Aspecto | Protocolo original | Este protocolo |
|---|---|---|
| Objetivo | Confirmar que NON-REGIME falla | Confirmar que REGIME acierta |
| Galaxias buscadas | Cualquiera del catálogo | Solo con `g_int < a_crit` |
| Resultado esperado | Error > 20% ✓ | Error ≤ 20% ✓ |
| Poder de falsación | Moderado | Máximo — fallo aquí falsifica |

---

## Paso 1: Criterio de búsqueda en SPARC

Para que una galaxia entre en REGIME debe satisfacer la condición `g_int < a_crit` **antes** de calcular predicciones. Esto implica buscar galaxias con las siguientes características en SPARC:

### Velocidad plana
**`V_flat` baja**.  
`V` aparece al cuadrado en `g_int = V² / R`; valores bajos reducen `g_int` de forma drástica.

### Radio de aplanamiento
**`R_flat` grande**.  
`R` aparece en el denominador; radios grandes reducen `g_int`. Combinado con `V` baja, es decisivo.

### Tipo morfológico
**LSB / enanas difusas**.  
Las galaxias de baja superficie brillante (*Low Surface Brightness*) tienden a baja aceleración en su borde.

### Masa bariónica
**`M_bar` baja**.  
Sistemas poco masivos tienden a curvas de rotación lentas y extendidas, favorables para REGIME.

### Umbral que debe cumplirse **antes** del cálculo

```text
g_int = V² / R < 1.0 × 10⁻¹¹ m/s²
```

### Equivalente en unidades observacionales

Si `V = 40 km/s` y `R = 5 kpc`:

```text
g_int = (40000)² / (5 × 3.086×10¹⁹)
      = 1.04 × 10⁻¹² m/s²   ✓ REGIME
```

Si `V = 50 km/s` y `R = 8 kpc`:

```text
g_int = (50000)² / (8 × 3.086×10¹⁹)
      = 1.01 × 10⁻¹¹ m/s²   ✗ borde — NON-REGIME
```

Las galaxias **UGCA444**, **UGCA442** y **UGCA281** ya aparecen en el documento original como casos que convergen al orden `10⁻¹¹`; son candidatos iniciales a verificar.

---

## Paso 2: Candidatos del catálogo SPARC

Galaxias del catálogo SPARC con características que favorecen entrada en REGIME.  
Se listan para verificar con datos exactos del catálogo antes de correr el protocolo.

### Candidatos prioritarios (verificar datos en SPARC antes de usar)

| Galaxia | V_flat est. | R_flat est. | Tipo | Por qué es candidata |
|---|---:|---:|---|---|
| UGCA444 | ~38 km/s | ~2.6 kpc | Enana LSB | Aparece en el documento original con `a_borde ≈ 1.8×10⁻¹¹`. Candidata fuerte. |
| UGCA442 | ~57 km/s | ~6.3 kpc | Enana LSB | `a_borde ≈ 1.6×10⁻¹¹` en documento original. Probable REGIME. |
| UGCA281 | ~30 km/s | ~1.1 kpc | Enana LSB | `a_borde ≈ 2.6×10⁻¹¹`. Está más arriba del umbral; verificar con datos exactos. |
| DDO154 | 50 km/s | 8 kpc | Enana gas | Calculada previamente: `g_int = 1.013×10⁻¹¹`. Borde exacto (1.3% sobre umbral). Probar con `R_flat` real de SPARC. |
| NGC3741 | ~50 km/s | ~3 kpc | Enana LSB | Masa muy baja (`~8×10⁷ M☉`). Posible REGIME si `R_flat` es mayor de lo estimado. |
| F563-1 | ~95 km/s | ~10 kpc | LSB | Galaxia LSB clásica de la muestra SPARC. Verificar si `g_int` cae bajo umbral. |

> **Importante:** los valores de esta tabla son estimaciones para orientar la búsqueda. Los datos reales deben tomarse del catálogo SPARC (Lelli et al., 2016) antes de cualquier cálculo. **No usar estos valores directamente.**

---

## Paso 3: Flujo de ejecución

Una vez obtenidos los datos reales de SPARC, seguir este orden sin saltarse pasos:

1. **Convertir unidades a SI**  
   `V × 1000 → m/s`  
   `R × 3.0857×10¹⁹ → m`  
   `M × 1.989×10³⁰ → kg`

2. **Calcular `g_int = V² / R`**  
   Solo cinemática; sin modelo involucrado.

3. **Clasificar régimen**  
   Si `g_int < 1.0×10⁻¹¹` → REGIME.  
   Si no, descartar para este protocolo.

4. **Calcular `R_T` y `V_pred`**  
   `R_T = sqrt(G·M / a_crit)`  
   `V_pred = (G·M·a_crit)^(1/4)`

5. **Comparar predicción vs observación**  
   `error% = |V_pred − V_obs| / V_obs × 100`  
   `ratio = R_T / R_obs`

6. **Registrar veredicto**  
   `Error ≤ 20%` y `ratio ∈ [0.5, 2.0]` → **CONFIRMA**  
   `Error > 20%` en REGIME → **FALSIFICA**

---

## Paso 4: Criterio de falsación (veredicto final)

Este es el test de máximo poder de falsación. El resultado es binario:

### ✓ Confirma hipótesis
Galaxias REGIME con `error ≤ 20%` de forma consistente.  
La predicción `V⁴ = G·M·a_crit` funciona donde el modelo indica que debe funcionar.

### ✗ Falsifica hipótesis
Galaxias REGIME con `error > 20%` de forma sistemática.  
La predicción falla donde se supone que debe acertar; esto falsifica la hipótesis central.

### Umbral de acuerdo

```text
error% = |V_pred − V_obs| / V_obs × 100

error% ≤ 20%  → CONFIRMA   (mismo orden de magnitud)
error% > 20%  → FALSIFICA  (en galaxia REGIME)

ratio ∈ [0.5, 2.0]  → R_T coherente con R_obs
ratio ∉ [0.5, 2.0]  → R_T no predice R_obs
```

Se requiere un mínimo de **5 galaxias en REGIME** para que el resultado sea estadísticamente significativo.  
Con 1–2 galaxias, el resultado es indicativo pero no concluyente.

---

## Registro

### Tabla de pre-registro

Completar con datos reales de SPARC antes de correr los cálculos.  
La clasificación de régimen debe registrarse antes de ver `V_pred`.

| Galaxia | V_flat | R_flat | M_bar | g_int | Régimen | V_pred | R_T | Error% | Veredicto |
|---|---|---|---|---|---|---|---|---|---|
| UGCA444 | — | — | — | — | — | — | — | — | pendiente |
| UGCA442 | — | — | — | — | — | — | — | — | pendiente |
| UGCA281 | — | — | — | — | — | — | — | — | pendiente |
| NGC3741 | — | — | — | — | — | — | — | — | pendiente |
| F563-1 | — | — | — | — | — | — | — | — | pendiente |

---

**Falsabilidad inversa — test de confirmación fuerte**  
Clasificación de régimen registrada antes de ver predicciones · Febrero 2026.
