# Antigravity Game Development Skill Suite

A unified, modular, progressive-disclosure skill suite for **Google Antigravity** (IDE and CLI), synthesizing core engineering and design disciplines from foundational game development literature into 12 actionable, battle-tested skills.

Designed to work both as a **workspace-level skill suite** (`.agents/skills/`) and as a **global Antigravity plugin** (`~/.gemini/config/plugins/gamedev-suite/`).

---

## Suite Architecture & Skills

The suite organizes game development across 12 specialized domains:

| # | Skill Name | Primary Domain | Core Coverage | Key Sources |
|---|---|---|---|---|
| 1 | `game-design-theory` | Game Design & Psychology | Crawford tenets, MDA framework, Flow channel, Bartle taxonomy, design anti-patterns | *Art of Computer Game Design* |
| 2 | `game-ux-and-design` | UX & Onboarding | Usability (7 pillars), Engage-ability, SDT, Dark patterns audit, GDD workflow | *GameUX* (Celia Hodent) |
| 3 | `level-design` | Spatial Design & Flow | 3Cs metrics, greybox methodology, pacing/tension curves, 4 encounter archetypes | *Level Design: Better Levels* |
| 4 | `game-math-and-geometry` | 3D Math & Transforms | Left/Right handedness, vectors, matrices, quaternions, SLERP, ray/AABB tests | *3D Math Primer* |
| 5 | `glsl-shaders-and-sdf` | Shaders & Procedural Art | GLSL fragment shaders, shaping, 2D SDFs, fBM noise, domain warping, blending | *The Book of Shaders* |
| 6 | `raytracing-and-rendering-pipeline` | Rendering & Light Transport | Ray/path tracing, Lambertian/Metal/Dielectric, Schlick Fresnel, BVH, VSD culling | *Ray Tracing in a Weekend* |
| 7 | `game-audio-design` | Interactive Audio Systems | 6-layer audio model, ADD authoring, mono 3D emitters, load/compression rules | *Audio Design Document* |
| 8 | `game-engine-architecture` | Low-Level Systems | Decoupled game loops, DDA raycasting, ECS/DOTS (SoA), custom allocators | *Wolfenstein 3D Black Book* |
| 9 | `unity-performance-optimization` | Engine Performance | Unity 6 profiling, Mobile 65% thermal rule, GC avoidance, URP, draw calls | *Optimize Performance (Unity 6)* |
| 10 | `panda3d-game-and-engine-dev` | Python & C++ Engine Dev | `ShowBase`, Actor animation, FSM, collisions, Bullet physics, C++ internals | *Panda3D Manual & Book 1* |
| 11 | `game-ai` | AI, Pathfinding & PCG | FSM, Behavior Trees, A*, Reynolds steering/flocking, DDA, WFC/PCG | *Game AI & Procedural Systems* |
| 12 | `game-qa-and-testing` | QA & Defect Triage | GDLC QA milestones, 11 testing types, 9 bug categories, bug reporting | *Game Testing Guide* |

---

## Directory Structure

```text
game-dev-skill-suite/
├── .github/
│   └── workflows/
│       └── validate.yml                 # Automated CI skill validation
├── .agents/
│   ├── rules/
│   │   └── AGENTS.md                    # Standing game engineering rules
│   └── skills/
│       ├── game-ai/
│       ├── game-audio-design/
│       ├── game-design-theory/
│       ├── game-engine-architecture/
│       ├── game-math-and-geometry/
│       ├── game-qa-and-testing/
│       ├── game-ux-and-design/
│       ├── glsl-shaders-and-sdf/
│       ├── level-design/
│       ├── panda3d-game-and-engine-dev/
│       ├── raytracing-and-rendering-pipeline/
│       └── unity-performance-optimization/
├── rules/
│   └── AGENTS.md                        # Standing rules (for plugin mode)
├── scripts/
│   ├── install.py                       # Cross-platform installer
│   └── validate_skills.py               # Frontmatter and link validator
├── .gitignore
├── plugin.json                          # Antigravity plugin manifest
└── README.md
```

---

## Installation

### Option 1: Install to Your Current Project Workspace (Recommended)
This makes the skills and rules available specifically to your current game project repository:

```bash
# In your target game project directory:
python /path/to/game-dev-skill-suite/scripts/install.py
```

Or manually copy:
```bash
mkdir -p <your-project>/.agents/skills
cp -r .agents/skills/* <your-project>/.agents/skills/
cp -r .agents/rules/* <your-project>/.agents/rules/
```

### Option 2: Install as Global Antigravity Plugin
This makes the entire suite available across all your Antigravity sessions and workspaces:

```bash
python scripts/install.py --global-plugin
```

---

## Validation & Quality Checks

Run the automated validation script before committing changes:

```bash
python scripts/validate_skills.py
```

The validator verifies:
- YAML frontmatter presence and valid `name` (kebab-case) and `description`.
- `SKILL.md` length limits (under 500 lines for progressive disclosure efficiency).
- All relative links to `references/` and `assets/` point to real, existing files.

---

## GitHub Deployment Guide

To push this repository to GitHub:

```bash
# 1. Initialize git repository (if not already initialized)
git init

# 2. Add files and make initial commit
git add .
git commit -m "feat: initial release of Antigravity Game Dev Skill Suite"

# 3. Create a new GitHub repo and link it
git remote add origin https://github.com/<your-username>/<your-repo-name>.git

# 4. Push to main branch
git branch -M main
git push -u origin main
```

The included `.github/workflows/validate.yml` will automatically validate all skills on every push and pull request.

---

## Example Prompts

Once installed, the agent activates relevant skills automatically when you prompt:

- **Game Design**: *"Design the core loop, meta loop, and progression mechanics for a tactical roguelike."*
- **Level Design**: *"Analyze my combat arena blockout for player sightlines and flanking routes."*
- **Shaders**: *"Write a GLSL fragment shader for procedural water with caustic distortion and foam edges."*
- **Performance**: *"Diagnose Unity 6 frame drops on Quest 3 and suggest zero-allocation alternatives."*
- **Engine Architecture**: *"Explain how a DDA raycaster calculates perpendicular wall distances without fisheye distortion."*
- **AI & Navigation**: *"Implement a Behavior Tree in C# with Selector and Sequence composites for a patrolling enemy."*
- **QA & Testing**: *"Draft a structured bug report and test checklist for an inventory item duplication glitch."*
