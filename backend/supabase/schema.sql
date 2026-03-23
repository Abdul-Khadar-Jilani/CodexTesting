create extension if not exists vector;

create table if not exists projects (
    id uuid primary key default gen_random_uuid(),
    user_id uuid,
    name text not null,
    description text,
    created_at timestamptz not null default now()
);

create table if not exists tasks (
    id uuid primary key default gen_random_uuid(),
    project_id uuid references projects(id) on delete cascade,
    title text not null,
    question text not null,
    constraints_json jsonb not null default '{}'::jsonb,
    preferred_output text not null default 'memo',
    status text not null default 'queued',
    created_at timestamptz not null default now()
);

create table if not exists task_runs (
    id uuid primary key default gen_random_uuid(),
    task_id uuid not null references tasks(id) on delete cascade,
    status text not null default 'queued',
    started_at timestamptz not null default now(),
    completed_at timestamptz,
    final_summary text,
    final_recommendation text,
    confidence_score double precision
);

create table if not exists plan_items (
    id uuid primary key default gen_random_uuid(),
    task_run_id uuid not null references task_runs(id) on delete cascade,
    title text not null,
    description text not null,
    priority int not null default 3,
    status text not null default 'pending'
);

create table if not exists evidence (
    id uuid primary key default gen_random_uuid(),
    task_run_id uuid not null references task_runs(id) on delete cascade,
    subtask_title text not null,
    claim text not null,
    supporting_text text not null,
    source_label text not null,
    confidence double precision not null,
    embedding vector(1536)
);

create table if not exists agent_outputs (
    id uuid primary key default gen_random_uuid(),
    task_run_id uuid not null references task_runs(id) on delete cascade,
    node_name text not null,
    agent_type text not null,
    model_name text not null,
    summary text not null,
    output_json jsonb not null default '{}'::jsonb,
    created_at timestamptz not null default now()
);
