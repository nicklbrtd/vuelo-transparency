#!/usr/bin/env python3
"""Dependency-free checks for this public documentation repository."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOC_NAMES = {
    "privacy-overview.md", "security-status.md", "e2ee.md", "threat-model.md",
    "data-and-metadata.md", "server-role.md", "device-security.md",
    "local-storage.md", "cryptography.md", "dependencies.md", "audits.md",
    "known-limitations.md", "faq.md", "source-status.md",
    "responsible-disclosure.md",
}
ROOT_PAIRS = (("README.md", "README.ru.md"), ("CHANGELOG.md", "CHANGELOG.ru.md"))
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")
errors: list[str] = []


def fail(path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def slug(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return re.sub(r"\s+", "-", text)


def check_markdown(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    if not content.endswith("\n"):
        fail(path, "missing final newline")
    if "\r" in content:
        fail(path, "use LF line endings")
    fences = 0
    headings: set[str] = set()
    for number, line in enumerate(content.splitlines(), 1):
        if line.startswith("```"):
            fences += 1
        if line.rstrip(" ") != line and len(line) - len(line.rstrip(" ")) != 2:
            fail(path, f"unexpected trailing whitespace on line {number}")
        if line.startswith("#") and not re.match(r"^#{1,6}(\s|$)", line):
            fail(path, f"malformed ATX heading on line {number}")
        heading = HEADING_RE.match(line)
        if heading:
            base = slug(heading.group(1))
            anchor = base
            suffix = 1
            while anchor in headings:
                suffix += 1
                anchor = f"{base}-{suffix}"
            headings.add(anchor)
        if line.startswith("#") and number < len(content.splitlines()) and content.splitlines()[number].strip() and not content.splitlines()[number].startswith("#"):
            # Headings should be followed by a blank line for predictable rendering.
            fail(path, f"heading should be followed by a blank line on line {number}")
    if fences % 2:
        fail(path, "unclosed fenced code block")


def check_links(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    own_anchors: set[str] = set()
    counts: dict[str, int] = {}
    for heading in HEADING_RE.finditer(content):
        base = slug(heading.group(1))
        counts[base] = counts.get(base, 0) + 1
        own_anchors.add(base if counts[base] == 1 else f"{base}-{counts[base]}")
    own_anchors.update(re.findall(r"<(?:a|span)\s+[^>]*id=[\"']([^\"']+)", content, flags=re.IGNORECASE))
    for match in LINK_RE.finditer(content):
        target = match.group(1).strip().strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
            continue
        parts = urlsplit(target)
        fragment = unquote(parts.fragment)
        if not parts.path:
            if fragment and fragment not in own_anchors:
                fail(path, f"broken heading link #{fragment}")
            continue
        candidate = (path.parent / unquote(parts.path)).resolve()
        if ROOT.resolve() not in candidate.parents and candidate != ROOT.resolve():
            fail(path, f"link escapes repository: {target}")
            continue
        if not candidate.is_file():
            fail(path, f"broken internal link: {target}")
            continue
        if fragment and candidate.suffix.lower() == ".md":
            target_text = candidate.read_text(encoding="utf-8")
            anchors: set[str] = set()
            counts = {}
            for heading in HEADING_RE.finditer(target_text):
                base = slug(heading.group(1))
                counts[base] = counts.get(base, 0) + 1
                anchors.add(base if counts[base] == 1 else f"{base}-{counts[base]}")
            anchors.update(re.findall(r"<(?:a|span)\s+[^>]*id=[\"']([^\"']+)", target_text, flags=re.IGNORECASE))
            if fragment not in anchors:
                fail(path, f"broken heading link: {target}")


def main() -> int:
    for en, ru in ROOT_PAIRS:
        if not (ROOT / en).is_file() or not (ROOT / ru).is_file():
            errors.append(f"missing root language pair: {en} / {ru}")
    en_files = {p.name for p in (ROOT / "docs/en").glob("*.md")}
    ru_files = {p.name for p in (ROOT / "docs/ru").glob("*.md")}
    if en_files != ru_files:
        errors.append(f"EN/RU document sets differ: EN-only={sorted(en_files-ru_files)}, RU-only={sorted(ru_files-en_files)}")
    if en_files != DOC_NAMES:
        errors.append(f"unexpected or missing main docs: expected={sorted(DOC_NAMES)}, found={sorted(en_files)}")
    pairs = [*ROOT_PAIRS, *((f"docs/en/{name}", f"docs/ru/{name}") for name in sorted(DOC_NAMES))]
    for en_name, ru_name in pairs:
        en_path, ru_path = ROOT / en_name, ROOT / ru_name
        if en_path.is_file() and ru_path.is_file():
            en_levels = [len(m.group(1)) for line in en_path.read_text(encoding="utf-8").splitlines() if (m := re.match(r"^(#{1,6})\s", line))]
            ru_levels = [len(m.group(1)) for line in ru_path.read_text(encoding="utf-8").splitlines() if (m := re.match(r"^(#{1,6})\s", line))]
            if en_levels != ru_levels:
                errors.append(f"heading structure differs: {en_name} / {ru_name}")
    files = sorted([*ROOT.glob("*.md"), *ROOT.glob("docs/**/*.md")])
    for path in files:
        check_markdown(path)
        check_links(path)
    if errors:
        print("Documentation checks failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Documentation checks passed for {len(files)} Markdown files; EN/RU document sets match and all internal links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
