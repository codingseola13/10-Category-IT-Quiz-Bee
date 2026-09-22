-- IT Quiz Bee Trainer: cloud progress storage
-- Run this once in the Supabase SQL Editor.

create table if not exists public.quiz_progress (
  user_id uuid primary key references auth.users(id) on delete cascade,
  progress jsonb not null default '{}'::jsonb,
  study_marks jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);

alter table public.quiz_progress enable row level security;

revoke all on table public.quiz_progress from anon;
grant select, insert, update, delete on table public.quiz_progress to authenticated;

drop policy if exists "Users can read their own quiz progress" on public.quiz_progress;
create policy "Users can read their own quiz progress"
on public.quiz_progress
for select
to authenticated
using ((select auth.uid()) = user_id);

drop policy if exists "Users can create their own quiz progress" on public.quiz_progress;
create policy "Users can create their own quiz progress"
on public.quiz_progress
for insert
to authenticated
with check ((select auth.uid()) = user_id);

drop policy if exists "Users can update their own quiz progress" on public.quiz_progress;
create policy "Users can update their own quiz progress"
on public.quiz_progress
for update
to authenticated
using ((select auth.uid()) = user_id)
with check ((select auth.uid()) = user_id);

drop policy if exists "Users can delete their own quiz progress" on public.quiz_progress;
create policy "Users can delete their own quiz progress"
on public.quiz_progress
for delete
to authenticated
using ((select auth.uid()) = user_id);
