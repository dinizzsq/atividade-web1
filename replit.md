# Workspace

## Overview

pnpm workspace monorepo using TypeScript. Each package manages its own dependencies.
Also contains a standalone Django project for a beginner academic assignment.

## Stack

- **Monorepo tool**: pnpm workspaces
- **Node.js version**: 24
- **Package manager**: pnpm
- **TypeScript version**: 5.9
- **API framework**: Express 5
- **Database**: PostgreSQL + Drizzle ORM
- **Validation**: Zod (`zod/v4`), `drizzle-zod`
- **API codegen**: Orval (from OpenAPI spec)
- **Build**: esbuild (CJS bundle)
- **Python**: 3.11 with Django 5.x (standalone Django project)

## Key Commands

- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- `pnpm --filter @workspace/api-server run dev` — run API server locally

See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details.

## Django Project — Área Restrita de Funcionários

Location: `artifacts/django-app/`

### Structure

```
artifacts/django-app/
  manage.py
  db.sqlite3
  projeto/
    settings.py
    urls.py
    wsgi.py
  funcionarios/
    views.py
    urls.py
    admin.py
    apps.py
  templates/
    home.html
    login.html
    painel.html
    perfil.html
```

### Pages

- `/` — Home (public)
- `/login/` — Login page
- `/logout/` — Logout (POST)
- `/painel/` — Painel (protected with LoginRequiredMixin)
- `/perfil/` — Perfil (protected with LoginRequiredMixin)
- `/admin/` — Django admin

### Pre-created Users

- **admin** / admin123 (superusuário)
- **funcionario1** / senha123

### Run

```bash
cd artifacts/django-app
python manage.py runserver 0.0.0.0:8000
```
