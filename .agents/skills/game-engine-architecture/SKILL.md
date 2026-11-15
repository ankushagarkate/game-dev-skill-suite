---
name: game-engine-architecture
description: Architect game loops (fixed vs. variable timestep), DDA raycasting engines, Entity-Component-System (ECS) data-oriented designs, asset/baking pipelines, and custom low-level memory allocators (frame/pool/stack). Grounded in classic Wolfenstein 3D engine craft and modern C++ game systems.
---

# Game Engine Architecture & Systems Engineering

Ground engine architectures in data-oriented design, predictable cache locality, deterministic update lifecycles, and low-overhead memory allocators.

## 1. Game Loop Architecture & Timestep Models

Decouple physical simulation from presentation rendering to prevent simulation instability and stutter:

```cpp
// Semi-fixed timestep with interpolation
double t = 0.0;
const double dt = 0.016666; // 60 Hz fixed simulation tick
double currentTime = hires_time();
double accumulator = 0.0;

while (!quit) {
    double newTime = hires_time();
    double frameTime = newTime - currentTime;
    if (frameTime > 0.25) frameTime = 0.25; // Clamp spiral-of-death
    currentTime = newTime;
    accumulator += frameTime;

    while (accumulator >= dt) {
        previousState = currentState;
        integrate(currentState, t, dt); // Deterministic physics/logic
        t += dt;
        accumulator -= dt;
    }

    const double alpha = accumulator / dt;
    State renderState = interpolate(previousState, currentState, alpha);
    render(renderState);
}
```

## 2. Wolfenstein 3D Raycasting Engine Craft

Wolfenstein 3D pioneered real-time faux-3D on 286/386 hardware through columnar raycasting:
- **DDA Grid Traversal**: Trace rays across integer grid boundaries using Digital Differential Analysis (DDA), stepping only in `X` or `Y` grid cells per iteration.
- **Fisheye Correction**: Never use Euclidean distance for column height. Use **perpendicular wall distance** (`perpWallDist = (side == 0) ? (sideDistX - deltaDistX) : (sideDistY - deltaDistY)`).
- **Column-Major Scaler**: Draw vertical texture strips directly to linear VGA framebuffers, maximizing sequential cache hits and loop unrolling.
- **Precomputed Lookup Tables (LUTs)**: Replace costly runtime transcendentals (`sin`, `cos`, `tan`, `1/x`) with fixed-point lookup arrays.

## 3. Data-Oriented Design & ECS (Entity-Component-System)

Reject deep object-oriented inheritance hierarchies (`GameObject -> Actor -> Monster -> Boss`) in favor of cache-coherent Data-Oriented Design (DOD):

- **Entity**: An opaque numeric identifier (`uint32_t ID`).
- **Component**: Pure plain-old-data (POD) structs containing zero logic.
- **System**: Pure functions that transform contiguous component arrays.
- **SoA over AoS**: Structure of Arrays (`positions[N]`, `velocities[N]`) outperforms Array of Structures (`struct { pos, vel, name, hp } entities[N]`) by pulling only queried fields into CPU L1/L2 caches.

```cpp
// Cache-friendly continuous processing
struct TransformComponent { float x[MAX_ENTITIES], y[MAX_ENTITIES], z[MAX_ENTITIES]; };
struct VelocityComponent  { float vx[MAX_ENTITIES], vy[MAX_ENTITIES], vz[MAX_ENTITIES]; };

void MovementSystem(TransformComponent& trans, const VelocityComponent& vel, size_t count, float dt) {
    for (size_t i = 0; i < count; ++i) {
        trans.x[i] += vel.vx[i] * dt;
        trans.y[i] += vel.vy[i] * dt;
        trans.z[i] += vel.vz[i] * dt;
    }
}
```

## 4. Custom Memory Allocators for Games

General-purpose heap allocation (`malloc` / `new`) introduces unbounded latency, OS locks, and memory fragmentation. Use specialized game allocators:

1. **Linear / Frame Allocator**: Single pointer bump allocation. Reset pointer to zero at end of frame (`O(1)` reset, zero fragmentation). Ideal for per-frame scratch buffers.
2. **Stack Allocator**: LIFO allocation allowing local unwind points (markers). Ideal for level loading and scene transitions.
3. **Pool Allocator**: Divides a block of memory into fixed-size chunks using a free list. `O(1)` allocation and `O(1)` deallocation. Ideal for bullets, particles, and components.

## 5. Asset Pipeline & Cooking Architecture

Separate authoring formats from runtime engine representations:
- **Source Assets**: Uncompressed, editable formats (FBX, PSD, WAV, GLTF).
- **Asset Cooker**: Offline CLI tool that converts source files into platform-native optimized blobs (e.g., ASTC/BC textures, stripped index-buffered meshes, compressed audio banks).
- **Engine Runtime**: Loads baked binary blobs with minimal serialization overhead (direct memory-mapped pointer patching).

## References

- [DDA Raycaster, ECS & Allocator Internals](references/dda-raycaster-and-allocators.md)
