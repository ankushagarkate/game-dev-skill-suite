# Game Development Suite — Standing Rules

These rules are active for all game development tasks within the workspace or when the plugin is enabled.

## General Game Development Standards

- **Ground Advice in Established Principles**: Always ground answers in recognized game design, interactive media, software engineering, and computer graphics theory.
- **Actionable Over Abstract**: Prefer concrete, copy-paste-ready or directly testable implementation over vague theoretical descriptions.
- **Platform & Pipeline First**: When advising on performance, always state the target hardware (Mobile, XR/VR, PC, Console, WebGL) and rendering pipeline (Forward, Deferred, Forward+, URP, HDRP, custom) before recommending solutions.
- **Explicit Trade-Offs**: Never recommend an architecture or design pattern without explicitly weighing its trade-offs for games (memory bandwidth, latency, garbage collection pressure, cache misses, draw call overhead).

## Code Quality & Engineering Standards

- **Unity C#**:
  - Prefer `struct` over `class` for small, frequently-allocated data (value types, vectors, state snapshots).
  - Eliminate per-frame heap allocations in `Update()`, `FixedUpdate()`, and coroutines (`ObjectPool`, `StringBuilder`, non-alloc physics queries).
  - Use `[SerializeField] private` instead of `public` fields for Inspector exposure.
  - Cache component lookups (`TryGetComponent`) and string/property hashes (`Shader.PropertyToID`, `Animator.StringToHash`).
- **GLSL / HLSL Shaders**:
  - Always declare the shader stage explicitly (Vertex, Fragment, Compute, Geometry, RayGen).
  - Use explicit float literals (`0.0`, `1.0`) to avoid compilation failure on strict GLSL ES drivers.
  - Prefer `mediump` on mobile GPUs for color and UV calculations; reserve `highp` for world-space positions and time accumulators.
- **C++ Engine & Systems Code**:
  - Practice Data-Oriented Design (DOD). Prefer Structure of Arrays (SoA) over Array of Structures (AoS) for high-frequency iteration loops.
  - Document memory ownership explicitly (`unique_ptr`, `shared_ptr`, or specialized pool/frame allocators). Avoid naked raw `new`/`delete` in gameplay code.
  - Decouple simulation ticks from presentation render ticks with fixed-timestep accumulators.

## Design, GDD & QA Quality Gates

- **Game Design Documents (GDDs)**: Must clearly articulate Vision Statement, 3Cs (Character, Camera, Controls), Core Loop, Platform Target, Win/Loss States, and Production Milestones.
- **Level Design**: Always validate gameplay in greybox primitives before authorizing production art. Ensure pacing features alternating tension and release beats.
- **Game QA**: Classify all reported defects into the 9 standard game bug categories (Stability, Level-design, Audio, Visual, AI, Physics, Compatibility, Networking, Performance) with exact reproduction steps and telemetry evidence.
