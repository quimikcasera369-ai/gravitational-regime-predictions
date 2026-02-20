# Línea Temporal de Sucesos y Cambios (Ramificada)

Este documento organiza los cambios en forma jerárquica, sin tocar el contenido original del protocolo base.

## Regla aplicada
- El original se conserva en: `PROTOCOLO_FALSABILIDAD_INVERSA.md`.
- Cada cambio adicional se separa en su propia "rama" documental con commit independiente.

## Árbol jerárquico

```text
Rama 00 (base)
└── Protocolo original en Markdown
    └── commit: f6a3afa  (histórico previo)

Rama 01 (derivación de base)
└── Documento guía para formato Markdown base
    └── commit: a0bf42f

Rama 02 (derivación de base)
└── Documento guía para formato HTML completo
    └── commit: e5b2d32

Rama 03 (derivación de base)
└── Documento guía para tablas separadas
    └── commit: c4182a6
```

## Rutas por rama
- Rama 01 (Markdown): `ramas/01_origen_markdown/README.md`
- Rama 02 (HTML): `ramas/02_presentacion_html/README.md`
- Rama 03 (Tablas): `ramas/03_tablas_separadas/README.md`

## Secuencia temporal resumida
1. Se fija el protocolo original (base canónica).
2. Se crea rama documental para baseline Markdown.
3. Se crea rama documental para versión HTML.
4. Se crea rama documental para versión de tablas aisladas.

> Nota: la separación por ramas se implementa como estructura documental y commits independientes en la línea de tiempo del repositorio.
