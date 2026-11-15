# Unity 6 Performance Budgets & Subsystem Checklists

## Frame Time & Thermal Budgets

| Target | Raw Frame Budget | Mobile 65% Thermal Target |
| :--- | :--- | :--- |
| **30 fps** | 33.33 ms | ~21.6 ms |
| **60 fps** | 16.66 ms | ~10.8 ms |
| **90 fps (XR)** | 11.11 ms | N/A (active/headset cooling varies) |

## Quick Triage Matrix

| Profiler Symptom | Likely Cause | First Fixes |
| :--- | :--- | :--- |
| `Gfx.WaitForPresent` | GPU-bound (fill rate / shaders / MSAA) | Lower render scale/STP, reduce overdraw, check Frame Debugger |
| `Gfx.WaitForCommands` | CPU-bound (draw calls / scripts) | Enable SRP Batcher, GPU Resident Drawer, optimize `Update()` |
| `GC.Alloc` spikes | Per-frame heap allocations | `ObjectPool`, cache `WaitForSeconds`, `CompareTag`, remove LINQ |
| `Canvas.BuildBatch` | UGUI dirtying entire canvas | Split static/dynamic canvases, remove nested `LayoutGroup`s |
| `Physics.Simulate` | High collision/raycast cost | Simplify colliders, `autoSyncTransforms = false`, `NonAlloc` APIs |

## Asset Import Enforcement (`AssetPostprocessor`)
- Textures: `isReadable = false`, `mipmapEnabled = false` for UI, ASTC `6x6` or `8x8` (mobile).
- Meshes: Enable mesh compression where precision allows; disable `Read/Write` unless modifying at runtime.
- Audio: Force Mono for 3D emitters; set Load Type by clip size (`<200KB` Decompress on Load, `>=200KB` Compressed in Memory, `>350KB` Streaming).
