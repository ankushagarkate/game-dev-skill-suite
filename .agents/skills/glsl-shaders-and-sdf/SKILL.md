---
name: glsl-shaders-and-sdf
description: Write GLSL fragment shaders, shaping functions, color spaces (HSB/YUV), 2D Signed Distance Fields (SDFs), procedural tiling, noise/fBM, and image blending/convolutions. Use when building custom shaders, procedural textures, UI effects, or post-processing.
---

# GLSL Shaders & 2D SDFs

Design fast, parallel GPU fragment shaders using normalized coordinates, analytical shaping functions, and Signed Distance Fields.

## GPU Execution Model & Boilerplate

- Fragment shaders run **in parallel, blindly, and memorylessly** per pixel (`gl_FragCoord.xy`).
- Normalize coordinates first: `vec2 st = gl_FragCoord.xy / u_resolution.xy;` (aspect-correct with `st.x *= u_resolution.x / u_resolution.y;`).
- Use explicit float literals (`0.0`, `1.0`)—implicit `int`-to-`float` casts fail in GLSL ES.
- Set appropriate precision (`mediump` for mobile UVs/colors where possible, `highp` for world positions/time).

## Core Toolkit

1. **Shaping Functions**:
   - `step(edge, x)`: Hard binary threshold (beware aliasing; prefer `smoothstep` for anti-aliased edges).
   - `smoothstep(edge0, edge1, x)`: Hermite interpolation for soft masks and AA borders.
   - `fract()`, `mod()`, `abs()`, `pow()`, `sin()`, `cos()`: Periodic pulses, symmetry, and curves.
2. **Color Spaces**:
   - Use `mix(colorA, colorB, t)` for linear blending.
   - Convert **HSB -> RGB** for intuitive hue cycling and polar color wheels.
   - Use **YUV** matrices for luminance/chrominance separation.
3. **2D Transforms**:
   - Translate `st` before rotating/scaling (`st -= 0.5; st = rot2d(angle) * st; st += 0.5;`).
4. **2D Signed Distance Fields (SDFs)**:
   - Circle: `length(st - center) - radius`
   - Box, rounded box, and polygon SDFs via `max`/`min`/`abs`.
   - Combine shapes with `min(d1, d2)` (union), `max(d1, d2)` (intersection), `max(d1, -d2)` (subtraction).
5. **Patterns & Procedural Noise**:
   - **Tiling**: `vec2 ipos = floor(st); vec2 fpos = fract(st);`
   - **Brick/Offset Grids & Truchet Tiles**: Offset odd rows/columns, then rotate tiles per cell hash.
   - **Deterministic Random**: `fract(sin(dot(st, vec2(12.9898, 78.233))) * 43758.5453123)`
   - **Value/Gradient Noise & fBM**: Sum octaves with halving amplitude (`gain = 0.5`) and doubling frequency (`lacunarity = 2.0`). Apply **domain warping** (`fbm(p + fbm(p))`) for organic clouds/marble/fire.
6. **Textures & Post-Processing**:
   - Sample `sampler2D` with `texture2D(u_tex, st)` / `texture(u_tex, st)`.
   - Apply blend modes (Multiply, Screen, Overlay) and 3×3 convolution kernels (blur, sharpen, Sobel edge detection) via texel offsets (`1.0 / u_resolution`).

## References

- [GLSL Patterns, SDFs & Blend Modes](references/glsl-patterns-and-blending.md)
