# Note-Taking App

A note-taking app in a similar style to Obsidian.

## Tech Stack

- HTMX
- TailwindCSS
- FastAPI
- SQLModel
- Postgres
- Docker
- AWS ECS

## Recompiling CSS

The `output.css` file can be recompiled by running the following command from the root directory:

```bash
tailwindcss -i ./src/assets/css/input.css -o ./src/assets/css/output.css --watch
```
