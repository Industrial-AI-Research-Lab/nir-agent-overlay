# nir-agent-overlay

[English version](README.md)

Общие указания, правила и скиллы для LLM-ассистентов в студенческих НИР лаборатории. Проект подключает overlay как submodule, закреплённый на теге; исправленное здесь правило попадает в каждый проект при следующем обновлении версии.

## Что внутри

- [AGENTS.md](AGENTS.md) — общие указания; проект их импортирует.
- [rules/](rules) — по теме на файл: python-style, experiments-mlflow, adr, commits, pr, security.
- [skills/](skills) — write-adr, experiment-issue, meeting-record, pr-describe; pre-ship и review скопированы из набора скиллов лаборатории, см. [skills/VENDORED.md](skills/VENDORED.md).
- [hooks/settings.json](hooks/settings.json) — фрагмент для `.claude/settings.json` проекта: запрет чтения `.env`, запуск `make check` на Stop, пока рабочее дерево не чистое.

## Подключение

Из [шаблона проекта](https://github.com/Industrial-AI-Research-Lab/nir-project-template): `make overlay` (версия закреплена в Makefile). Вручную:

```bash
git submodule add https://github.com/Industrial-AI-Research-Lab/nir-agent-overlay.git .agents/overlay
git -C .agents/overlay checkout v0.1.0
mkdir -p .claude/rules && ln -s ../../.agents/overlay/rules .claude/rules/overlay
printf '\n@.agents/overlay/AGENTS.md\n' >> CLAUDE.md
git add .gitmodules .agents/overlay .claude/rules/overlay CLAUDE.md
```

Клонируйте проект с флагом `--recurse-submodules`, иначе папка overlay останется пустой. На Windows без права создавать символические ссылки обойдитесь без ссылки и подключите правила в CLAUDE.md пофайлово: `@.agents/overlay/rules/<имя>.md`. Скилл становится виден Claude Code через ссылку `.claude/skills/<имя>` → `../../.agents/overlay/skills/<имя>`.

## Какой агент что читает

| Агент | Читает | Как подключить overlay |
|---|---|---|
| Claude Code | CLAUDE.md, `.claude/rules/`, `.claude/skills/` | строка `@.agents/overlay/AGENTS.md` в CLAUDE.md; ссылка `.claude/rules/overlay`; скиллы по ссылкам |
| Codex | AGENTS.md | строка в AGENTS.md проекта: «Также следуй `.agents/overlay/AGENTS.md` и `.agents/overlay/rules/`» |
| Cursor | AGENTS.md, `.cursor/rules/` | та же строка; или копия правил в `.cursor/rules/` файлами `.mdc` |
| GitHub Copilot | AGENTS.md, CLAUDE.md, `.github/copilot-instructions.md` | та же строка в AGENTS.md |

## Версии

Теги `vMAJOR.MINOR.PATCH`, история в [CHANGELOG.md](CHANGELOG.md). Проект переходит на новую версию через PR: переключите submodule на новый тег в ветке `chore/...`.

## Прежде чем подключать чужой overlay

Читайте исходный текст каждого файла, а не только его отображение; ищите в хуках и скиллах команды, которые отправляют что-либо за пределы репозитория; закрепляйте тег или коммит; держите LICENSE в корне.

## Лицензия

MIT.
