-- ============================================================
-- OneShot AI — Supabase setup
-- Run this ONCE in your Supabase Dashboard SQL Editor:
--   https://supabase.com/dashboard -> your project -> SQL Editor
-- ============================================================

-- 1. Create the training data table
create table if not exists public.training_data (
  id         bigint generated always as identity primary key,
  event_id   text unique,   -- idempotent key, prevents duplicate uploads (plan §27)
  user_id    text not null,
  signal     numeric,
  locked     boolean,
  action     text,
  success    boolean,
  reward     numeric,
  quality    numeric,       -- 0..1 derived quality score (plan §7)
  profile    text,
  v          text,   -- oneshot version / model version
  ts         timestamptz not null default now()
);

create index if not exists training_data_user_idx on public.training_data (user_id);
create index if not exists training_data_ts_idx   on public.training_data (ts desc);
create index if not exists training_data_event_idx on public.training_data (event_id);
create index if not exists training_data_quality_idx on public.training_data (quality desc);

-- 2. Row Level Security
--    PRIVACY (plan §32): anon may only INSERT its own events. Cross-user reads
--    (for building the shared community model) must use the SERVICE_ROLE key,
--    which bypasses RLS and is only used in CI (.github/workflows) and never
--    shipped in client code.
alter table public.training_data enable row level security;

drop policy if exists "training_anon_insert" on public.training_data;
create policy "training_anon_insert"
  on public.training_data for insert
  to anon with check (true);

-- NOTE: intentionally NO anon SELECT policy. If you want a fully public
-- read-only mirror for debugging, add one explicitly — but it is discouraged.

-- 3. Optional view: aggregated community stats by user
create or replace view public.training_stats as
  select user_id,
         count(*)                       as attempts,
         count(*) filter (where success) as successes,
         round(avg(reward), 3)          as avg_reward,
         max(ts)                         as last_ts
  from public.training_data
  group by user_id;

-- ============================================================
-- Usage after setup:
--   sudo python3 oneshot.py --sync          # push local + pull community + auto-train + git push
--   sudo python3 oneshot.py --push-data     # only upload local training log
--   sudo python3 oneshot.py --pull-data     # only download community rows
-- ============================================================