---
name: game-audio-design
description: Plan game audio architecture, author Audio Design Documents (ADD), design multi-layer interactive audio engines, and enforce spatial/compression best practices. Use when scoping game sound, music states, dialogue, or optimizing audio memory/CPU.
---

# Game Audio Design

Structure game audio across design, implementation, and engine performance so sound reinforces gameplay clarity without blowing memory or CPU budgets.

## 1. The 4 Audio Categories

1. **Music**: Emotional tone, pacing, interactive state transitions (General, Action, Special).
2. **Sound Effects (SFX)**: World feedback, combat impacts, footsteps, ambient emitters.
3. **Dialogue**: Narration, character barks, story VO (dry vs. environmental reverb).
4. **User Interface (UI)**: Crisp, low-latency menu navigation, confirmations, and alerts.

## 2. Six-Layer Interactive Audio Model

Design your runtime mixer around 6 distinct priority layers:

- **Layer 0 (Terrain Ambient)**: Continuous environment bed; crossfade at most **2** streams simultaneously.
- **Layer 1 (3D Spatial Enhancement)**: Positioned 3D world loops (torches, rivers, machinery).
- **Layer 2 (Random Ambience)**: Randomized one-shots on terrain/buildings (birds, creaks, wind gusts).
- **Layer 3 (SFX, UI & Combat)**: High-priority gameplay feedback and UI responses.
- **Layer 4 (Interactive Music)**: Stem/state-driven music switching smoothly across *General*, *Action*, and *Special* states.
- **Layer 5 (Narration & Dialogue)**: Ducking-enabled voice channels with priority over ambience.

## 3. Technical & Spatial Rules

- **3D Sounds MUST Be Mono**: Stereo clips do not spatialize properly in 3D audio engines (Unity, Panda3D/OpenAL, FMOD); reserve stereo for 2D music and UI.
- **Master in Uncompressed WAV**: Always author and store source masters as PCM `.wav`, then let the engine compress per platform.
- **Compression & Load Types**:
  - **< 200 KB** (short, frequent SFX): *Decompress on Load* (PCM/ADPCM) for zero runtime CPU decode cost.
  - **>= 200 KB** (medium SFX/VO): *Compressed in Memory* (Vorbis/ADPCM) to save RAM.
  - **> 350–400 KB** (music, long ambience): *Streaming* from disk to minimize memory footprint.
- **Voice Limiting & Ducking**: Cap simultaneous voices per category and duck ambience/music slightly during critical dialogue or combat cues.

## 4. Authoring an Audio Design Document (ADD)

Use [the ADD template](assets/add-template.md) to document Objectives, Research/Formats, 6-Layer Implementation, Asset Content List, and Schedule.

## Assets

- [Audio Design Document (ADD) Template](assets/add-template.md)
