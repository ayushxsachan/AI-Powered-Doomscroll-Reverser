# Doomscroll Reverser

A full-stack AI-powered web app that turns social media usage into a cinematic opportunity-cost report.

## Stack

- Frontend: Next.js 15, TypeScript, Tailwind CSS, Framer Motion, Recharts, Clerk
- Backend: FastAPI, Pydantic, OpenAI Responses API, Supabase service-role persistence
- Database: Supabase Postgres
- Deploy: Vercel for `frontend`, Render/Fly.io for `backend`

## Features

- Screen time analyzer for Instagram, YouTube, short-form video, gaming, sleep, and goals
- Animated yearly cost metrics: hours wasted, money lost, books, workouts, projects, interview prep
- Cyberpunk doom meter with five categories
- AI alternate reality generator with realistic motivational prompts
- Future timeline comparison between current and disciplined behavior
- Brain rot analytics with radial and chart visualizations
- Shareable dark meme-style result card exported as PNG
- Touch Grass mode with fullscreen reset and optional ambient tone
- Clerk-ready auth, Supabase-ready persistence, local demo fallbacks

## Local Setup

### 1. Frontend

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000`.

### 2. Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Open `http://localhost:8000/api/health`.

## Environment Variables

Copy `.env.example` to `.env.local` for frontend work and `backend/.env.example` to `backend/.env` for the API.

Frontend:

```bash
NEXT_PUBLIC_API_URL=
BACKEND_API_URL=http://127.0.0.1:8000
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=
```

Backend:

```bash
BACKEND_CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
OPENAI_API_KEY=
OPENAI_MODEL=gpt-5.4-mini
SUPABASE_URL=
SUPABASE_SERVICE_ROLE_KEY=
```

The app runs without keys in demo mode. Locally, the frontend proxies `/api/*` to `BACKEND_API_URL`. In production, set `BACKEND_API_URL` to the deployed FastAPI URL or set `NEXT_PUBLIC_API_URL` if you prefer direct browser calls.

## Database

Run `database/schema.sql` in Supabase SQL editor. The schema includes:

- `profiles`
- `screen_time_reports`
- `alternate_realities`
- `focus_missions`

The FastAPI backend writes with the Supabase service role key. Frontend reads can use Clerk JWT mapping where `auth.jwt()->>'sub'` matches `clerk_user_id`.

## API

- `GET /api/health`
- `POST /api/analyze`
- `POST /api/alternate-reality`
- `POST /api/share-card`

Example analysis payload:

```json
{
  "instagram_hours": 1.5,
  "youtube_hours": 1,
  "short_form_hours": 2.5,
  "gaming_hours": 0.5,
  "sleep_hours": 6.5,
  "hourly_value": 12,
  "daily_goals": "coding projects, gym, interview prep"
}
```

## AI Prompting

The backend prompt is in `backend/app/prompts.py`. It is designed to:

- connect emotionally without shaming the user
- show realistic 12-month upside
- keep the tone cinematic, motivational, and slightly scary
- return a structured JSON report for stable frontend rendering

The OpenAI integration uses the Responses API via `client.responses.create(...)`, with `instructions` for tone and `response.output_text` parsing.

## Deployment

### Vercel Frontend

1. Import the repo in Vercel.
2. Set the project root to `frontend`.
3. Add frontend environment variables.
4. Deploy with the default Next.js build command.

### Render Backend

1. Create a Web Service from the repo.
2. Set root directory to `backend`.
3. Build command:

```bash
pip install -r requirements.txt
```

4. Start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

5. Add backend environment variables.

### Fly.io Backend

Use a Python app with the same start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

Set `BACKEND_CORS_ORIGINS` to your Vercel domain.

## Production Notes

- Use `OPENAI_MODEL=gpt-5.5` for highest quality or `gpt-5.4-mini` for lower latency/cost.
- Restrict CORS to production domains.
- Keep `SUPABASE_SERVICE_ROLE_KEY` only on the backend.
- Add Clerk webhook syncing if you want profile rows created immediately after signup.
- Add rate limiting around `/api/alternate-reality` before public launch.
