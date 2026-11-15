---
name: unity-performance-optimization
description: Profile and optimize Unity 6 games for Mobile, XR, and Web targets across CPU, GPU, memory/GC, assets, URP, UGUI/UI Toolkit, physics, animation, and audio. Use when diagnosing frame drops, GC spikes, draw calls, or build size in Unity.
---

# Unity 6 Performance Optimization (Mobile, XR & Web)

Always **profile first, optimize second**. Never guess bottlenecks without Unity Profiler or Frame Debugger evidence.

## 1. Frame Budgets & Bottleneck Triage

- **Target Frame Times**: `30 fps = 33.33 ms`, `60 fps = 16.66 ms`, `90 fps (VR) = 11.11 ms`.
- **Mobile Thermal Rule (65%)**: Budget `~22 ms` for 30 fps and `~11 ms` for 60 fps to prevent thermal throttling.
- **CPU vs. GPU Bound**:
  - High `Gfx.WaitForCommands` -> **CPU-bound** (scripts, culling, draw-call submission).
  - High `Gfx.WaitForPresent` -> **GPU-bound** (fill rate, overdraw, heavy shaders, shadow maps).
- **Tools**: Unity Profiler, Profile Analyzer (compare captures), Memory Profiler, Frame Debugger.

## 2. Memory & Garbage Collection (GC)

- Enable **Incremental GC** to spread collection across frames.
- Pool frequently spawned objects with `UnityEngine.Pool.ObjectPool<T>`.
- Eliminate per-frame allocations: avoid LINQ, `Regex`, string concatenation in `Update()`, `new WaitForSeconds()` inside coroutines (cache it), boxing, and `GameObject.tag ==` (use `CompareTag()`).
- Manage large assets with **Addressables** and unload unused bundles cleanly.

## 3. C# & Engine Scripting

- Cache `GetComponent<T>()` references in `Awake()`/`Start()`.
- Pre-hash IDs with `Animator.StringToHash` and `Shader.PropertyToID`.
- Use `Transform.SetPositionAndRotation()` instead of setting both separately.
- Use `Renderer.sharedMaterial` when reading/sharing materials to avoid accidental material instancing leaks.
- Store shared immutable config in `ScriptableObject` (Flyweight pattern).
- Time-slice heavy AI/pathfinding across frames via `PlayerLoop` or Jobs/Burst.

## 4. URP, GPU & Assets

- **Batching**: Enable **SRP Batcher** (compatible URP shaders), **GPU Instancing**, and **GPU Resident Drawer** (Forward+ in Unity 6).
- **Culling & Upscaling**: Use LODs, **GPU Occlusion Culling**, and **STP (Spatial-Temporal Post-processing)** upscaling on GPU-bound targets.
- **Textures**: Use **ASTC** compression on mobile, power-of-two (POT) dimensions, **Sprite Atlases** for 2D/UI, disable **Read/Write Enabled**, disable mipmaps on UI textures, and combine PBR channels into **ORM** (Occlusion/Roughness/Metallic) maps. Enforce via `AssetPostprocessor`.

## 5. UI, Animation, Physics, Web & XR

- **UGUI**: Split static vs. dynamic elements into separate `Canvas` components; disable `Raycast Target` on non-interactive text/images; avoid deeply nested `LayoutGroup`s; consider **UI Toolkit** for complex HUDs.
- **Animation**: Prefer **Generic** rigs over Humanoid (30–50% CPU savings when retargeting isn't needed); strip unused scale curves.
- **Physics**: Use **Box Pruning** broadphase, `NonAlloc` / `List` 2D queries, `RaycastCommand` batches, and disable `Physics.autoSyncTransforms`.
- **Web**: Use **Brotli** compression, **Strip Engine Code**, and **WebAssembly 2023**.
- **XR**: Enable **Single Pass Instanced** rendering and **Foveated Rendering**.

## References

- [Unity 6 Performance Budgets & Subsystem Checklists](references/unity-perf-budgets-and-checklists.md)
