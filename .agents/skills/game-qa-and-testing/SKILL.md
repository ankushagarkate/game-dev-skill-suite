---
name: game-qa-and-testing
description: Plan game QA across the Game Development Life Cycle (GDLC), write Test Plans/Cases/Checklists, execute 11 game testing types, and file structured bug reports across 9 game bug categories. Use when setting up game QA, writing test suites, or triaging game bugs.
---

# Game QA & Testing

Integrate structured QA across every GDLC milestone—dedicating ~40% of total development effort to testing and maintaining independent tester objectivity.

## 1. QA Across the GDLC

- **Concept & Prototype**: Smoke testing and core capability checks.
- **Vertical Slice**: Verify end-to-end loop, asset pipeline, and target frame rate.
- **Alpha (Internal QA)**: Feature-complete functional, progression, and level-design testing.
- **Beta (External Users)**: Load/network stress, compatibility matrix, and balance telemetry.
- **Gold Master**: Strict regression, compliance/TRC/XR certification, and localization sign-off.
- **Post-Launch**: Live-ops regression, patch verification, and crash telemetry triage.

## 2. Core QA Documentation

- **Test Plan**: Scope, target hardware/OS matrix, tools, entry/exit criteria, and risks.
- **Test Cases**: Both **Positive** (valid player paths) and **Negative** (invalid inputs, disconnects, boundary abuse).
- **Checklists**: Track status using `Passed`, `Failed`, `Blocked`, `In Progress`, `Not Run`, `Skipped`.

## 3. Eleven Game Testing Techniques

1. **Functional** (use QA cheat codes/debug menus to reach late-game states fast)
2. **Playtesting** (fun, pacing, onboarding clarity)
3. **Ad-hoc / Exploratory** (trying unexpected player combos)
4. **Progression** (soft-locks, economy/XP curves, save/load integrity)
5. **Balance** (weapons, matchmaking, difficulty spikes)
6. **Usability** (HUD readability, input ergonomics)
7. **Compatibility** (GPUs, OS versions, resolutions, aspect ratios)
8. **Performance** (FPS, frame-time spikes, memory leaks, load times)
9. **Localization** (LocKit strings, text overflow, RTL/font glyphs)
10. **Compliance** (platform store rules, age ratings, controller prompts)
11. **Security & Regression** (anti-cheat/server authority + verifying fixes don't break existing features)

## 4. Bug Reporting & 9 Bug Categories

Always classify bugs into one of the 9 standard categories using [the Bug Report Template](assets/bug-report-template.md):
**Stability**, **Level-design** (stuck spots, map holes, missing geometry), **Audio**, **Visual** (clipping, z-fighting), **AI**, **Physics**, **Compatibility**, **Networking**, **Performance**.

## References & Assets

- [Game QA Test Matrix & GDLC Checklist](references/qa-test-matrix.md)
- [Game Bug Report Template](assets/bug-report-template.md)
