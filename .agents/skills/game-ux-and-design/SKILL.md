---
name: game-ux-and-design
description: Design player-centric game UX, evaluate usability and engage-ability, audit dark patterns, scope prototypes, and draft Game Design Documents (GDD). Use when designing mechanics, HUDs, onboarding/tutorials, progression loops, or GDDs.
---

# Game UX & Design

Apply cognitive science, Game UX heuristics, and disciplined scoping so players understand your game effortlessly and stay intrinsically motivated.

## Core Cognitive Pillars

Design every mechanic, HUD element, and tutorial around three human brain constraints:

1. **Perception is Subjective**: Players interpret visuals through prior experience and expectations. Use **affordances** and **signifiers** so interactive elements look and behave the way players expect (*Form Follows Function*).
2. **Attention is Scarce**: Working attention handles roughly one active focus at a time. Never force players to read tutorial popups while dodging enemies or managing complex inputs.
3. **Memory is Fallible**: Humans suffer from change blindness and limited short-term recall. Minimize memory load with persistent visual cues, clear icons, and contextual reminders instead of front-loading walls of text.

## Game UX Framework: Usability + Engage-ability

### 1. Usability (7 Pillars)

- **Signs & Feedback**: Every player action needs immediate, unmistakable visual/audio feedback; every system state needs a clear sign.
- **Clarity**: Keep HUD, icons, typography, and combat readability unambiguous at target resolution.
- **Form Follows Function**: Visual design must communicate function (e.g., cover looks solid, hazards look dangerous).
- **Consistency**: Reuse controls, color coding, and UI metaphors across menus and gameplay.
- **Minimum Workload**: Reduce physical clicks/inputs and cognitive friction in menus and core loops.
- **Error Prevention & Recovery**: Confirm destructive actions; allow undo/respec where reasonable.
- **Flexibility & Accessibility**: Support remappable controls, subtitles, colorblind-safe palettes, and difficulty options.

### 2. Engage-ability (3 Pillars)

- **Motivation (Self-Determination Theory)**: Balance **extrinsic** rewards (loot, XP, badges) with **intrinsic** needs:
  - *Competence*: Clear progression, skill mastery, fair challenge.
  - *Autonomy*: Meaningful choices, build/playstyle expression.
  - *Relatedness*: Cooperative or competitive social connection.
- **Emotion**: Craft tactile **game feel** (responsive controls, hit-stop, audio punch), **presence**, and controlled **surprises**.
- **Game Flow**: Tune the **learning curve**, **difficulty curve**, and **pacing** (tension vs. release) to keep players in flow without boredom or frustration.

## Dark Patterns Audit

Reject manipulative patterns that erode player trust:

- Guilt-tripping, loss aversion traps, or coercive FoMO timers.
- Pay-to-win or artificial friction sold back as convenience.
- Forced social obligation loops or predatory lootboxes.
- Never design around "addiction" metrics or punish players for taking breaks.

## Scoping & GDD Workflow

1. **Idea Splitting**: Separate core playable loop ("must-have vertical slice") from stretch features ("nice-to-have").
2. **Rapid Prototyping**: Prove the fun of the core mechanic in a graybox prototype before investing in final art.
3. **GDD Authoring**: Use [the GDD template](assets/gdd-template.md) to document core loop, controls, progression, and technical scope.
4. **Scientific UX Playtesting**: Combine **telemetry** (where players drop off) with **moderated playtesting** (why they got confused).

## References & Assets

- [UX Heuristics & Playtest Checklist](references/ux-heuristics-checklist.md)
- [Game Design Document (GDD) Template](assets/gdd-template.md)
