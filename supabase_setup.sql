-- ============================================================
-- OneShot AI — Supabase setup (IDEMPOTENT)
-- Safe to run MULTIPLE times — creates or overwrites cleanly.
--   https://supabase.com/dashboard -> your project -> SQL Editor
-- ============================================================

-- ──────────────────────────────────────────────────────────────
-- 1. Training data table (safe: create if missing)
-- ──────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS public.training_data (
  id         BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  event_id   TEXT UNIQUE,
  user_id    TEXT NOT NULL,
  signal     NUMERIC,
  locked     BOOLEAN,
  action     TEXT,
  success    BOOLEAN,
  reward     NUMERIC,
  quality    NUMERIC,
  profile    TEXT,
  v          TEXT,
  ts         TIMESTAMPTZ NOT NULL DEFAULT now(),
  -- Device identity fields (added for full brain memory)
  bssid      TEXT DEFAULT '',
  essid      TEXT DEFAULT '',
  pin        TEXT DEFAULT '',
  firmware   TEXT DEFAULT '',
  chipset    TEXT DEFAULT '',
  mac        TEXT DEFAULT ''
);

-- Migration: add columns if table already exists (idempotent)
ALTER TABLE public.training_data ADD COLUMN IF NOT EXISTS bssid    TEXT DEFAULT '';
ALTER TABLE public.training_data ADD COLUMN IF NOT EXISTS essid    TEXT DEFAULT '';
ALTER TABLE public.training_data ADD COLUMN IF NOT EXISTS pin      TEXT DEFAULT '';
ALTER TABLE public.training_data ADD COLUMN IF NOT EXISTS firmware TEXT DEFAULT '';
ALTER TABLE public.training_data ADD COLUMN IF NOT EXISTS chipset  TEXT DEFAULT '';
ALTER TABLE public.training_data ADD COLUMN IF NOT EXISTS mac      TEXT DEFAULT '';

-- ──────────────────────────────────────────────────────────────
-- 2. Indexes (safe: create if missing, skip if exists)
-- ──────────────────────────────────────────────────────────────
CREATE INDEX IF NOT EXISTS training_data_user_idx    ON public.training_data (user_id);
CREATE INDEX IF NOT EXISTS training_data_ts_idx      ON public.training_data (ts DESC);
CREATE INDEX IF NOT EXISTS training_data_event_idx   ON public.training_data (event_id);
CREATE INDEX IF NOT EXISTS training_data_quality_idx ON public.training_data (quality DESC);

-- ──────────────────────────────────────────────────────────────
-- 3. Row Level Security — DISABLED for anon INSERT support
-- ──────────────────────────────────────────────────────────────
-- RLS is disabled because the anon key needs to INSERT training
-- events from any user. Security is maintained at the Supabase
-- API gateway level (API key validation) — not at the DB level.
--
-- If you want to re-enable RLS later, run:
--   ALTER TABLE public.training_data ENABLE ROW LEVEL SECURITY;
-- and create INSERT/SELECT policies as needed.
ALTER TABLE public.training_data DISABLE ROW LEVEL SECURITY;

-- ──────────────────────────────────────────────────────────────
-- 4. Stats view (safe: replace if exists)
-- ──────────────────────────────────────────────────────────────
CREATE OR REPLACE VIEW public.training_stats AS
  SELECT
    user_id,
    COUNT(*)                             AS attempts,
    COUNT(*) FILTER (WHERE success)      AS successes,
    ROUND(AVG(reward), 3)                AS avg_reward,
    MAX(ts)                              AS last_ts
  FROM public.training_data
  GROUP BY user_id;

-- ──────────────────────────────────────────────────────────────
-- 5. Verify (uncomment to check table status)
-- ──────────────────────────────────────────────────────────────
-- SELECT tablename, rowsecurity FROM pg_tables WHERE tablename = 'training_data';
-- SELECT COUNT(*) FROM public.training_data;

-- ============================================================
-- DONE! This script is fully idempotent — run it again anytime.
--
-- Usage:
--   python3 oneshot.py --sync      # push local + pull + retrain + git push
--   python3 oneshot.py --push-data  # upload local training log
--   python3 oneshot.py --pull-data  # download community rows
-- ============================================================