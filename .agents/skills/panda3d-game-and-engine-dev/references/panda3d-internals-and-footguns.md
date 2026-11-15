# Panda3D C++ Internals & Footguns Reference

## Core C++ Subsystem Map

| Module | Responsibility |
| :--- | :--- |
| `dtool` (`dtoolbase`, `prc`, `interrogatedb`) | Base types, Config.prc system, Python binding metadata |
| `pgraph`, `pgraphnodes`, `cull` | `PandaNode`, `NodePath`, LOD/Switch/Camera nodes, cull traversal |
| `gobj`, `gsgbase`, `display`, `glstuff` | `Geom`, `Texture`, `Shader`, `GraphicsStateGuardian`, OpenGL/TinyDisplay |
| `char`, `chan` | Skeletal `Character`, `PartBundle`, animation channels |
| `collide`, `physics`, `bullet`, `ode` | Built-in collision system + Bullet/ODE physics wrappers |
| `direct` (`showbase`, `actor`, `fsm`, `gui`, `task`) | High-level Python framework |

## Teardown Checklist (Preventing Memory Leaks)
1. `self.ignoreAll()` to detach `DirectObject` messenger listeners.
2. `taskMgr.remove(task_name)` for all owned tasks.
3. `actor.cleanup()` before `actor.removeNode()` on `Actor` instances.
4. `node.clearPythonTag(...)` if storing circular Python object references on `NodePath`s.

## Common Bugs & Fixes
- **DirectGUI Keyboard Navigation**: `DirectGUI` is mouse-centric by default; implement explicit focus/key navigation for gamepad/keyboard menus.
- **TransformState Cache Bloat**: Avoid generating thousands of unique micro-transforms on static nodes; batch or flatten static props.
- **PStats Profiling**: Set `want-pstats 1` in `Config.prc` and run `pstats` to inspect App, Cull, and Draw stage timings.
