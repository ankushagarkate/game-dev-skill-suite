---
name: raytracing-and-rendering-pipeline
description: Architect ray/path tracers, 3D rasterization pipelines, Visible Surface Determination (VSD), and low-level software rendering optimizations. Use when building custom renderers, culling systems, lighting models, or retro/software 3D engines.
---

# Ray Tracing & Rendering Pipeline

Understand both physically based path tracing and real-time rasterization/visibility pipelines.

## 1. Path / Ray Tracing Architecture

Follow a clean modular pipeline:

1. **Core Primitives**: `vec3` math, `ray(origin, direction)` (`p(t) = A + t*B`), `hitable` interface (`hit(ray, t_min, t_max, rec)`), and `hitable_list`.
2. **Shadow Acne Fix**: Always set `t_min = 0.001` on secondary rays to prevent self-intersection from floating-point error.
3. **Antialiasing & Gamma**: Jitter sub-pixel samples per pixel, average radiance, and apply gamma-2 correction (`sqrt(color)`) before 8-bit output.
4. **Materials (BRDFs)**:
   - **Lambertian Diffuse**: Scatter toward `hit_point + normal + random_in_unit_sphere()`.
   - **Metal**: Reflect `v - 2*dot(v, n)*n`, add `fuzz * random_in_unit_sphere()` (`fuzz in [0, 1]`).
   - **Dielectric (Glass/Water)**: Snell's law refraction (`etai_over_etat`), handle **total internal reflection**, and blend reflection vs. refraction using **Schlick's Fresnel approximation**. Use a negative sphere radius for hollow glass bubbles.
5. **Camera & Depth of Field**: Construct orthonormal basis `(u, v, w)` from `lookfrom`, `lookat`, `vup`, `vfov`, `aspect`. Simulate thin-lens DoF by offsetting ray origins on a disk of radius `aperture / 2` aimed at `focus_dist`.

## 2. Rasterization Pipeline & Visibility (VSD)

- **Pipeline Stages**: Vertex Transform -> Lighting (e.g., Blinn-Phong) -> Backface Culling -> Clipping (Sutherland-Hodgman against 6 frustum planes) -> Perspective Divide & Viewport -> Rasterization & Z-Buffer.
- **Visible Surface Determination (VSD)**:
  - **Frustum Outcodes**: Reject bounding volumes outside all 6 frustum planes early.
  - **Spatial Partitioning**: Regular Grids, Quadtrees/Octrees, **BSP Trees** (painter's order or solid-leaf collision), **Portals & PVS** (Potentially Visible Sets) for indoor levels.

## 3. Low-Level & Retro Engine Craft

- **Fixed-Point Math**: Represent fractions with integer bit-shifts when FPU hardware is absent or deterministic lockstep is needed.
- **Deferred Column Rendering & Compiled Scalers**: Minimize overdraw and per-pixel branch overhead in raycasters.
- **Tick Rate Discipline**: Decouple simulation ticks from variable render frame rates (or clamp `dt`) to prevent physics instability.
- **Memory & Asset Paging**: Manage strict RAM budgets via explicit page/cache managers and lookup tables.

## References

- [Rendering Pipeline, Fresnel & VSD Reference](references/rendering-and-vsd-reference.md)
