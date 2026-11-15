# Rendering Pipeline, Fresnel & VSD Reference

## Schlick Fresnel Approximation
```cpp
float schlick(float cosine, float ref_idx) {
    float r0 = (1.0f - ref_idx) / (1.0f + ref_idx);
    r0 = r0 * r0;
    return r0 + (1.0f - r0) * powf((1.0f - cosine), 5.0f);
}
```

## Snell's Law Refraction Check
- Given unit incident ray `uv`, unit normal `n`, and ratio `ni_over_nt`:
- `dt = dot(uv, n)`
- `discriminant = 1.0 - ni_over_nt * ni_over_nt * (1.0 - dt * dt)`
- If `discriminant > 0`: `refracted = ni_over_nt * (uv - n * dt) - n * sqrt(discriminant)`
- Else: **Total Internal Reflection** (reflect instead).

## VSD Structure Selection Guide

| Scene Type | Recommended VSD | Why |
| :--- | :--- | :--- |
| **Indoor Rooms / Corridors** | Portals + PVS | Exact room-to-room visibility; skips occluded geometry |
| **Static Architectural Levels** | BSP Tree | Deterministic front-to-back or back-to-front traversal |
| **Open / Dynamic Worlds** | Octree / BVH + Frustum Culling | Fast updates and hierarchical bounding-volume rejection |

## Retro / Software Renderer Checklist
- Precompute trig (`sin`/`cos`/`tan`) tables if targeting constrained CPUs.
- Use 17-bit LFSRs for cheap pseudo-random screen transitions (e.g., fizzle-fade).
- Separate 2D UI/menu, 3D renderer, and audio subsystems behind clean shared-state interfaces.
