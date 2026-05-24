-- Doomscroll Reverser Supabase schema
-- Run this in the Supabase SQL editor.

create extension if not exists pgcrypto;

create table if not exists public.profiles (
  id uuid primary key default gen_random_uuid(),
  clerk_user_id text unique not null,
  email text,
  display_name text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.screen_time_reports (
  id uuid primary key default gen_random_uuid(),
  clerk_user_id text,
  instagram_hours numeric(5, 2) not null default 0,
  youtube_hours numeric(5, 2) not null default 0,
  short_form_hours numeric(5, 2) not null default 0,
  gaming_hours numeric(5, 2) not null default 0,
  sleep_hours numeric(5, 2) not null default 7,
  hourly_value numeric(8, 2) not null default 12,
  daily_goals text not null default '',
  result jsonb not null,
  created_at timestamptz not null default now()
);

create table if not exists public.alternate_realities (
  id uuid primary key default gen_random_uuid(),
  report_id uuid references public.screen_time_reports(id) on delete set null,
  clerk_user_id text,
  prompt_version text not null default 'v1',
  model text not null,
  response jsonb not null,
  created_at timestamptz not null default now()
);

create table if not exists public.focus_missions (
  id uuid primary key default gen_random_uuid(),
  clerk_user_id text not null,
  title text not null,
  difficulty text not null check (difficulty in ('low', 'medium', 'high')),
  completed_at timestamptz,
  created_at timestamptz not null default now()
);

create index if not exists idx_reports_clerk_user_id on public.screen_time_reports(clerk_user_id);
create index if not exists idx_realities_clerk_user_id on public.alternate_realities(clerk_user_id);
create index if not exists idx_focus_missions_clerk_user_id on public.focus_missions(clerk_user_id);

alter table public.profiles enable row level security;
alter table public.screen_time_reports enable row level security;
alter table public.alternate_realities enable row level security;
alter table public.focus_missions enable row level security;

-- Clerk JWT integration can map auth.jwt()->>'sub' to clerk_user_id.
-- Keep service-role backend writes unrestricted by RLS.
create policy "profiles_select_own" on public.profiles
  for select using (auth.jwt() ->> 'sub' = clerk_user_id);

create policy "reports_select_own" on public.screen_time_reports
  for select using (auth.jwt() ->> 'sub' = clerk_user_id);

create policy "realities_select_own" on public.alternate_realities
  for select using (auth.jwt() ->> 'sub' = clerk_user_id);

create policy "missions_select_own" on public.focus_missions
  for select using (auth.jwt() ->> 'sub' = clerk_user_id);

