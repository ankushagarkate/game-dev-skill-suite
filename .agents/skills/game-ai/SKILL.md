---
name: game-ai
description: Design and implement game AI systems, Finite State Machines (FSM), Behavior Trees (BT), Goal-Oriented Action Planning (GOAP), A* & NavMesh pathfinding, Reynolds steering behaviors (flocking), Dynamic Difficulty Adjustment (DDA), and Procedural Content Generation (PCG). Use when authoring NPC behavior, tactical combat AI, or generative level logic.
---

# Game AI, Pathfinding & Behavioral Systems

Design intelligent, reactive, and performant AI agents that prioritize player engagement and perceived intelligence over brute-force perfection.

## 1. Selecting an AI Decision Architecture

| Architecture | Best Use Case | Implementation Overhead | Key Limitation |
| :--- | :--- | :--- | :--- |
| **Finite State Machine (FSM)** | Simple enemies, scripted bosses, UI states | Minimal (enum + switch or state classes) | Combinatorial state explosion when scaling |
| **Hierarchical FSM (HFSM)** | Distinct combat vs. non-combat mode layering | Moderate | Rigid transition boundaries |
| **Behavior Tree (BT)** | Tactical NPCs, stealth games, prioritized tasks | Moderate (Selectors, Sequences, Decorators) | Requires blackboard for shared memory |
| **Utility AI** | Soft multi-goal ranking (The Sims, ambient crowds) | Moderate (mathematical response curves) | Hard to tune weight interactions |
| **GOAP (Goal-Oriented Action Planning)**| Emergent tactical agents (F.E.A.R.) | High (A* search over world states) | High runtime cost per plan search |

## 2. Behavior Tree (BT) Core Anatomy

BTs tick from the root down every AI update cycle, returning `Success`, `Failure`, or `Running`:

- **Composites**:
  - **Selector (`?`)**: Ticks children left-to-right; returns `Success` on the first child that succeeds (Logical OR). Ideal for prioritizing fallback strategies.
  - **Sequence (`→`)**: Ticks children left-to-right; returns `Failure` on the first child that fails (Logical AND). Ideal for step-by-step actions (e.g., `HasAmmo -> Aim -> Fire`).
  - **Parallel (`⇉`)**: Runs multiple branches concurrently (e.g., moving while aiming).
- **Decorators (`◇`)**: Wraps a single child to invert results, enforce cooldowns, limit repeat counts, or check blackboard preconditions.
- **Leaf Nodes**:
  - **Action**: Executes game logic (`MoveTo`, `PlayAnimation`, `Attack`).
  - **Condition**: Read-only queries against blackboard (`IsTargetVisible`, `HealthBelowThreshold`).

## 3. Pathfinding & Navigation

### A* Graph Search Principles
`f(n) = g(n) + h(n)`
- `g(n)`: Exact cost from start to node `n`.
- `h(n)`: Admissible heuristic estimate from `n` to target.
  - **Manhattan**: Grid maps with 4-direction movement (`|dx| + |dy|`).
  - **Octile / Chebyshev**: Grid maps with diagonal movement (`max(dx, dy) + (sqrt(2)-1)*min(dx, dy)`).
  - **Euclidean**: Free-angle or 3D navigation mesh node centers (`sqrt(dx² + dy² + dz²)`).

### Navigation Meshes (NavMesh) & Smoothing
- Represent walkable terrain as convex 2D/3D polygons rather than dense point grids.
- Guarantee that any two points inside a convex polygon have an unblocked line of sight.
- Apply the **Funnel Algorithm (String Pulling)** to convert raw node-to-node path lists into smooth, natural trajectories without angular zigzagging.

## 4. Reynolds Steering Behaviors & Flocking

Combine independent vector forces to create lifelike locomotion:
- **Seek / Flee**: Desired velocity points directly toward / away from target at maximum speed; steering force is `desired_velocity - current_velocity`.
- **Arrive**: Scale desired speed linearly down to zero once inside a designated `slowing_radius` to prevent overshoot oscillations.
- **Boid Flocking (Emergent Swarms)**:
  - **Separation**: Steer away from crowded nearby neighbors (inversely proportional to distance).
  - **Alignment**: Steer to match average heading/velocity of neighbors.
  - **Cohesion**: Steer toward center of mass of local flock mates.

## 5. Dynamic Difficulty Adjustment (DDA)

Keep players in the flow state without overt rubber-banding:
- **Telemetry Window**: Track player death rates, time-to-clear, and ammo consumption over rolling 3-5 minute windows.
- **Micro-Adjustments**: Scale subtle parameters (enemy reaction delay, projectile speed, health drop frequency) rather than raw damage multipliers.
- **Player Perception**: Never adjust difficulty in the middle of an active encounter; apply modifiers during zone transitions or respawns to preserve fair play.

## 6. Procedural Content Generation (PCG)

- **Wave Function Collapse (WFC)**: Propagate adjacency tile constraints from a prototype grid to generate deterministic, contradiction-free procedural layouts.
- **Cellular Automata**: Simulate cave/organic terrain using 4-5 rule smoothing over random binary matrices.
- **Perlin / Simplex Noise**: Multi-octave fBM noise for heightmaps, biome distribution, and resource spawning.

## References

- [Behavior Tree & Steering Behaviors Implementation](references/behavior-tree-and-steering-code.md)
