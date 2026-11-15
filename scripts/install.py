#!/usr/bin/env python3
"""
Installer script for Antigravity Game Dev Skill Suite.
Installs skills and rules to either workspace-level (.agents/) or global Antigravity config.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_SRC = ROOT / ".agents" / "skills"
RULES_SRC = ROOT / ".agents" / "rules" / "AGENTS.md"


def get_global_paths():
    home = Path.home()
    gemini_config = home / ".gemini" / "config"
    plugin_dest = gemini_config / "plugins" / "gamedev-suite"
    skills_dest = gemini_config / "skills"
    return plugin_dest, skills_dest


def install_workspace(target_dir: Path):
    agents_dir = target_dir / ".agents"
    dest_skills = agents_dir / "skills"
    dest_rules = agents_dir / "rules"

    dest_skills.mkdir(parents=True, exist_ok=True)
    dest_rules.mkdir(parents=True, exist_ok=True)

    print(f"[+] Installing workspace skills into {dest_skills}...")
    for skill in SKILLS_SRC.iterdir():
        if skill.is_dir():
            target_skill = dest_skills / skill.name
            if target_skill.exists():
                shutil.rmtree(target_skill)
            shutil.copytree(skill, target_skill)
            print(f"    - {skill.name}")

    if RULES_SRC.exists():
        shutil.copy2(RULES_SRC, dest_rules / "AGENTS.md")
        print(f"[+] Installed standing rules into {dest_rules / 'AGENTS.md'}")

    print("\n[✓] Workspace installation complete.")


def install_global_plugin():
    plugin_dest, _ = get_global_paths()
    skills_dest = plugin_dest / "skills"
    rules_dest = plugin_dest / "rules"

    skills_dest.mkdir(parents=True, exist_ok=True)
    rules_dest.mkdir(parents=True, exist_ok=True)

    print(f"[+] Installing global Antigravity plugin into {plugin_dest}...")
    for skill in SKILLS_SRC.iterdir():
        if skill.is_dir():
            target_skill = skills_dest / skill.name
            if target_skill.exists():
                shutil.rmtree(target_skill)
            shutil.copytree(skill, target_skill)
            print(f"    - {skill.name}")

    if RULES_SRC.exists():
        shutil.copy2(RULES_SRC, rules_dest / "AGENTS.md")
        print(f"[+] Copied rules to {rules_dest / 'AGENTS.md'}")

    plugin_json_src = ROOT / "plugin.json"
    if plugin_json_src.exists():
        shutil.copy2(plugin_json_src, plugin_dest / "plugin.json")
        print(f"[+] Copied plugin.json to {plugin_dest / 'plugin.json'}")

    print("\n[✓] Global plugin installation complete.")


def main():
    parser = argparse.ArgumentParser(description="Install Antigravity Game Dev Skill Suite")
    parser.add_argument(
        "--global-plugin",
        action="store_true",
        help="Install as global Antigravity plugin (~/.gemini/config/plugins/gamedev-suite)",
    )
    parser.add_argument(
        "--workspace",
        type=str,
        default=None,
        help="Install into specified workspace directory (default: current directory)",
    )

    args = parser.parse_args()

    if not SKILLS_SRC.exists():
        print(f"[!] Error: source skills folder not found at {SKILLS_SRC}", file=sys.stderr)
        sys.exit(1)

    if args.global_plugin:
        install_global_plugin()
    else:
        target = Path(args.workspace) if args.workspace else Path.cwd()
        install_workspace(target)


if __name__ == "__main__":
    main()
