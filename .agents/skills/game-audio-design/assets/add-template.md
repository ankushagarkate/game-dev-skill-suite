# Audio Design Document (ADD): [Project Title]

## I. Outline & Objectives
- **Overview & Aesthetic Pillars**:
- **Music Direction** (Interactive states: General / Action / Special):
- **Sound Effects Direction** (Realism vs. stylization, combat readability):
- **Dialogue & Narration**:
- **UI Audio**:

## II. Technical Research & Standards
- **Target Middleware / Engine**: (e.g., FMOD, Wwise, Unity Audio, Panda3D OpenAL)
- **Source Format**: 48 kHz / 24-bit (or 16-bit) PCM WAV
- **Runtime Compression & Load Strategy**:
  - Short SFX (<200 KB): Decompress on Load (ADPCM)
  - Medium SFX/VO: Compressed in Memory (Vorbis)
  - Music / Long Ambience (>350 KB): Streaming
- **3D Spatialization Rule**: All 3D emitters exported as Mono.

## III. Implementation (6-Layer Architecture)
- **Layer 0 — Ambient Terrain**: (Max 2 simultaneous crossfading beds)
- **Layer 1 — 3D Spatial Emitters**: (Attenuation curves, doppler, occlusion)
- **Layer 2 — Random World One-Shots**: (Min/max interval, pitch/volume randomization)
- **Layer 3 — Gameplay SFX & UI**: (Voice limits, cooldowns)
- **Layer 4 — Interactive Music**: (Transition rules, beat/bar sync)
- **Layer 5 — Dialogue / Narration**: (Ducking bus targets)

## IV. Content List
| Asset ID | Category | Layer | Mono/Stereo | Load Type | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `SFX_Footstep_Stone` | SFX | 3 | Mono | Decompress on Load | Pending |

## V. Schedule & Milestones
- **Prototype Audio**:
- **Vertical Slice Mix**:
- **Final Mastering & Loudness Check**:
