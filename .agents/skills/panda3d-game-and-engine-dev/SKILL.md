---
name: panda3d-game-and-engine-dev
description: Build 3D games in Python with Panda3D (ShowBase, FSM, Actor, CollisionTraverser, DirectGUI, Audio3DManager, packaging) and debug C++ engine internals (pgraph, DCAST, PointerTo, .bam, PipelineCycler, Bullet). Use when developing or debugging Panda3D projects.
---

# Panda3D Game & C++ Engine Development

Build clean, leak-free Panda3D games in Python while respecting Panda3D's underlying C++ scene-graph and memory architecture.

## 1. Python Game Architecture & Project Layout

Organize indie/3D projects cleanly:

```text
project/
├── design/                 # GDD, concepts, schedules
└── game/
    ├── main.py             # ShowBase entry point
    ├── assets/{characters,levels,gui,audio,fx}/
    └── src/                # Player(FSM), Arena, HUD, networking
```

- **State Management**: Drive player/game states with `direct.fsm.FSM` (`enterIdle`, `exitIdle`, `request("Run")`).
- **Input & Tasks**: Poll held movement keys in `taskMgr.add(self.moveTask, ...)` using `globalClock.getDt()`; bind discrete triggers with `self.accept(event, handler)`.
- **Collisions**: Use `CollisionTraverser` + `CollisionHandlerPusher` (character pushback) + `CollisionSegment` / `CollisionRay` (grounding/hit checks) + event messenger callbacks.
- **Audio & FX**: Use `Audio3DManager` (mono WAV/OGG emitters) and `ParticleEffect` (`enableParticles()`).
- **UI & Debugging**: Build menus/HUD with `DirectGUI`, inspect scene graphs with `PStats`, and test logic with `unittest`.

## 2. Five C++ Engine Patterns (Under the Hood)

1. **RTTI**: `TypeHandle`, `TypedObject`, and `DCAST(TargetType, ptr)` (never raw C-style casts on Panda types).
2. **Smart Pointers**: `ReferenceCount`, `PointerTo<T>` / `PT(T)` (owning), and `WeakPointerTo<T>` / `WPT(T)` (non-owning).
3. **Serialization**: `Datagram`, `BamReader`, `BamWriter` for `.bam` binary scene/asset caching.
4. **Thread-Safe Scene Graph**: `PipelineCycler` and `CycleData` (copy-on-write per pipeline stage).
5. **Python Bindings**: `interrogate` parses `PUBLISHED:` C++ blocks into Python wrappers (`panda3d.core`, `panda3d.bullet`).

## 3. Critical Footguns to Avoid

- **`loadPrcFileData` Timing**: Call `loadPrcFileData("", ...)` **before** instantiating `ShowBase()`, which is a process-wide singleton.
- **`setColor` vs. `setColorScale`**: `setColor` overrides vertex colors; use `setColorScale` to tint textured/colored models.
- **`flattenStrong()` Stops at `ModelNode`**: Clear or reparent `ModelNode`s if you intentionally want static geometry merged.
- **Reference Cycles & Leaks**: `setPythonTag`, `self.accept`, and unremoved `taskMgr` handles keep nodes alive. Always call `Actor.cleanup()`, `ignoreAll()`, and `removeNode()` on teardown.
- **Bullet `doPhysics` Slow-Mo Trap**: `world.doPhysics(dt, max_substeps=1)` drops time if `dt > fixed_timestep`; pass adequate `max_substeps` (e.g., `10`).
- **Single-Precision World Limits**: Keep active coordinates within `~10^5` units to avoid float jitter.
- **3D Audio**: Stereo clips will not spatialize in `Audio3DManager`—use mono.

## References & Assets

- [Panda3D Internals & Footguns Reference](references/panda3d-internals-and-footguns.md)
- [Development Config.prc Template](assets/prc-dev-template.prc)
