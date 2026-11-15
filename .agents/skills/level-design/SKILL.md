---
name: level-design
description: Design 3D and 2D level layouts, graybox blocking, pacing and tension curves, encounter staging (solo, reinforced, mastery, twist), non-diegetic navigation, and playtesting protocols. Use when planning maps, combat spaces, level flow, or spatial environmental storytelling.
---

# Level Design & Spatial Architecture

Structure level geometry, spatial navigation, encounter density, and intensity pacing so levels feel intuitive to navigate and rewarding to explore.

## 1. The 3Cs Ruler Principle (Character, Camera, Controls)

Every metric in level design originates from the **3Cs**:
- **Character Metrics**: Measure walking/sprint speeds, jump apex/distance, crouch height, mantle reach, and combat weapon ranges. Treat these numbers as fixed architectural constraints.
- **Doorways & Corridors**: Door heights must exceed character height by at least 25-30% to prevent camera clipping; corridor widths must accommodate character width plus side-strafe room.
- **Camera Clearances**: Ensure ceilings and tight corners do not trigger aggressive spring-arm camera clipping or inverted orientation.

## 2. Greybox / Blockout Workflow

Never invest in final art assets before validating layout in graybox:

1. **2D Bubble / Flow Diagram**: Map key beats, choke points, hubs, and encounter spaces on paper.
2. **Greybox Modeling**: Assemble geometry using primitive solids (cubes, cylinders, ramps) with standard grid units.
3. **Scale Validation**: Place character scale dummies throughout every room and corridor.
4. **Sightline & Occlusion Check**: Verify that points of interest and landmarks are framed naturally through doorways and arches.
5. **Mechanics Playtest**: Test movement mechanics (jumping, sliding, shooting, cover) in the blockout before texturing.

## 3. Guiding Players Without UI Arrows

Use environmental architecture and human perceptual tendencies to guide flow:

- **Light Over Darkness**: The human eye instinctively tracks high contrast. Light the critical path; leave dead ends in shadow.
- **Lines of Convergence**: Floor patterns, road ruts, piping, ceiling beams, and wires point in the direction of progression.
- **Landmark Anchors (Weenie Principle)**: Position a tall, unmistakable visual landmark (tower, spire, mountain peak) visible across districts to ground player orientation.
- **Framing & Apertures**: Frame upcoming objectives through archways, broken windows, or valley gaps as rewards for completing sections.
- **Color Accent Signifiers**: Use consistent, saturated accent colors (e.g., yellow ledges for climbing, red valves for interaction).

## 4. Encounter Architecture (4 Encounter Archetypes)

Structure combat arenas through deliberate encounter phases:
1. **Solo Encounter (Introduction)**: Introduce a single new enemy type or mechanic in a controlled, low-pressure space.
2. **Reinforced Encounter (Escalation)**: Combine the new enemy with familiar support units or environmental hazards.
3. **Mastery Encounter (Peak Challenge)**: Require precise synergy of multiple skills under spatial or temporal pressure (e.g., shrinking arena, flanking waves).
4. **Twist Encounter (Subversion)**: Invert the established pattern (e.g., player loses weapon, terrain collapses, enemies fight each other).

## 5. Pacing & Intensity Curves

Structure levels as an undulating waveform of **Tension and Release**:

```
Intensity
  ▲         [Climax]
  │           ▲
  │   [Peak]  │
  │     ▲     │
  │  ▲  │  ░  │  ░
  └──┴──┴──┴──┴──┴──► Time (Level Duration)
    Int Build Drop Boss Outro
```

- **Intensity Caps**: Never sustain maximum combat intensity for more than **60–90 seconds** without fatigue setting in.
- **Breather Beats**: Follow every intense encounter with safe exploration, narrative exposition, resource restocking, or environmental vistas.

## References

- [Encounter Pacing & Level Design Reference](references/encounter-and-pacing-guide.md)
