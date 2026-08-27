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
  ts         TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ──────────────────────────────────────────────────────────────
-- 2. Indexes (safe: create if missing, skip if exists)
-- ──────────────────────────────────────────────────────────────
CREATE INDEX IF NOT EXISTS training_data_user_idx    ON public.training_data (user_id);
CREATE INDEX IF NOT EXISTS training_data_ts_idx      ON public.training_data (ts DESC);
CREATE INDEX IF NOT EXISTS training_data_event_idx   ON public.training_data (event_id);
CREATE INDEX IF NOT EXISTS training_data_quality_idx ON public.training_data (quality DESC);

-- ──────────────────────────────────────────────────────────────
-- 3. Row Level Security (idempotent — safe to re-run)
-- ──────────────────────────────────────────────────────────────
-- Enable RLS (Postgres skips silently if already enabled)
ALTER TABLE public.training_data ENABLE ROW LEVEL SECURITY;

-- Force RLS for table owner too (prevents accidental bypass)
ALTER TABLE public.training_data FORCE ROW LEVEL SECURITY;

-- Drop ALL existing policies on this table to start clean
DO $$
DECLARE
  pol RECORD;
BEGIN
  FOR pol IN
    SELECT policyname
    FROM pg_policies
    WHERE schemaname = 'public'
      AND tablename  = 'training_data'
  LOOP
    EXECUTE format(
      'DROP POLICY IF EXISTS %I ON public.training_data',
      pol.policyname
    );
  END LOOP;
END
$$;

-- Policy: anon can INSERT (upload training events)
CREATE POLICY "training_anon_insert"
  ON public.training_data
  FOR INSERT
  TO anon
  WITH CHECK (true);

-- Policy: anon can SELECT own rows only (for local verification)
-- Uncomment below if you want users to read their own rows:
-- CREATE POLICY "training_anon_select_own"
--   ON public.training_data
--   FOR SELECT
--   TO anon
--   USING (user_id = current_setting('request.jwt.claims', true)::json->>'sub');

-- NOTE: Cross-user reads (for building the shared community model)
-- use the SERVICE_ROLE key which bypasses RLS.
-- It is injected via SUPABASE_SERVICE_ROLE_KEY GitHub secret only.

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
-- 5. Verify setup (run this to confirm everything is correct)
-- ──────────────────────────────────────────────────────────────
-- Uncomment and run to verify:
-- SELECT schemaname, tablename, policyname, cmd, with_check
-- FROM pg_policies
-- WHERE tablename = 'training_data';

-- ============================================================
-- DONE! This script is fully idempotent — run it again anytime.
--
-- Usage:
--   python3 oneshot.py --sync      # push local + pull + retrain + git push
--   python3 oneshot.py --push-data  # upload local training log
--   python3 oneshot.py --pull-data  # download community rows
-- ============================================================