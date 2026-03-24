import { ArrowRight, Bot, CheckCircle2, FlaskConical, Search } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";

const pillars = [
  {
    icon: Search,
    title: "Research",
    description: "Collect evidence from trusted sources and document traceability."
  },
  {
    icon: FlaskConical,
    title: "Critique",
    description: "Stress-test assumptions through automated adversarial reviews."
  },
  {
    icon: Bot,
    title: "Synthesize",
    description: "Convert findings into executive-ready recommendations."
  }
];

export default function Home() {
  return (
    <main className="mx-auto flex min-h-screen w-full max-w-6xl flex-col gap-10 px-6 py-14 md:px-8">
      <section className="space-y-6">
        <p className="inline-flex items-center rounded-full border border-slate-300 bg-white px-3 py-1 text-xs font-medium text-slate-600">
          Frontend stack confirmed: Next.js + Tailwind + shadcn/ui
        </p>
        <h1 className="max-w-3xl text-4xl font-semibold tracking-tight text-slate-900 md:text-5xl">
          DecisionGraph gives teams auditable, multi-agent reasoning for high-stakes choices.
        </h1>
        <p className="max-w-2xl text-base text-slate-600 md:text-lg">
          This starter frontend is ready to connect to your FastAPI backend and visualize every stage of planning, research, critique, and final recommendations.
        </p>
        <div className="flex flex-wrap items-center gap-3">
          <Button>Start a new analysis</Button>
          <Button variant="outline">View API status</Button>
        </div>
      </section>

      <section className="grid gap-4 md:grid-cols-3">
        {pillars.map((pillar) => (
          <Card key={pillar.title}>
            <CardHeader>
              <div className="mb-2 inline-flex size-9 items-center justify-center rounded-lg bg-slate-100 text-slate-700">
                <pillar.icon className="size-4" />
              </div>
              <CardTitle>{pillar.title}</CardTitle>
              <CardDescription>{pillar.description}</CardDescription>
            </CardHeader>
            <CardContent>
              <Button variant="ghost" size="sm" className="px-0 text-slate-700">
                Learn more <ArrowRight className="size-4" />
              </Button>
            </CardContent>
          </Card>
        ))}
      </section>

      <section className="rounded-xl border border-slate-200 bg-white p-6">
        <div className="flex items-center gap-2 text-sm font-medium text-slate-700">
          <CheckCircle2 className="size-4 text-emerald-500" />
          Ready for next step
        </div>
        <p className="mt-2 text-sm text-slate-600">
          Next, we can wire this UI to `/api/v1/tasks` and `/api/v1/runs` to submit tasks and stream workflow progress.
        </p>
      </section>
    </main>
  );
}
