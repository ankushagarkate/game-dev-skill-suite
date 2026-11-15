# Game QA Test Matrix & Bug Taxonomy

## 9 Game Bug Categories & Examples

| Category | Common Failure Examples |
| :--- | :--- |
| **Stability** | Crashes, freezes, infinite loading screens, unhandled exceptions |
| **Level-design** | Stuck spots, out-of-bounds map holes, missing collision, unreachable objectives |
| **Audio** | Missing SFX, looping cutoffs, 3D panning inverted, clipping/distortion |
| **Visual** | Z-fighting, mesh clipping, missing textures, LOD pop-in, UI overlap |
| **AI** | Pathfinding stuck on corners, passive enemies, wall-hack aggro |
| **Physics** | Ragdoll explosions, tunneling through walls, floating props |
| **Compatibility** | Driver-specific artifacts, ultrawide UI stretching, gamepad disconnect hang |
| **Networking** | Desync, rubber-banding, ghost hits, lobby/matchmaking timeout |
| **Performance** | Frame-time spikes, shader compilation stutter, memory leaks over long sessions |

## Multiplayer / Asymmetrical QA Focus
- Test **host/server authority** vs. client prediction under simulated packet loss (1–5%) and latency (100–250ms).
- Verify **disconnect/reconnect** mid-match does not soft-lock remaining players.
- Validate **role-specific states** (e.g., survivor vs. hunter abilities, cooldowns, and win/loss triggers).
