"use client"

import { useEffect, useState } from "react"

export default function Home() {

  const [stats, setStats] = useState<any>(null)

  useEffect(() => {

    fetch("http://127.0.0.1:8000/dashboard-stats")
      .then(res => res.json())
      .then(data => setStats(data))

  }, [])

  if (!stats) {
    return (
      <main className="p-10">
        Loading Nexus Core...
      </main>
    )
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 p-8">

      <div className="mb-10">

        <h1 className="text-4xl font-bold text-slate-800 tracking-tight">
          Nexus Core
        </h1>

        <p className="text-gray-500 mt-2">
          Autonomous Operations Dashboard
        </p>

        <div className="mt-4 flex gap-3">

  <div className="px-3 py-1 rounded-full bg-green-100 text-green-700 text-sm font-medium">
    System Online
  </div>

  <div className="px-3 py-1 rounded-full bg-blue-100 text-blue-700 text-sm font-medium">
    AI Active
  </div>

</div>

      </div>

      {/* TOP STATS */}

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">

        <Card
          title="Revenue"
          value={`UGX ${stats.total_revenue}`}
        />

        <Card
          title="Clients"
          value={stats.total_clients}
        />

        <Card
          title="Leads"
          value={stats.total_leads}
        />

        <Card
          title="Outreach"
          value={stats.total_outreach}
        />

      </div>

      {/* PAYMENTS */}

      <Section title="Recent Payments">

        {stats.payments.length === 0 ? (
          <Empty text="No payments yet" />
        ) : (
          stats.payments.map((p: any, i: number) => (

            <Row
              key={i}
              title={p.client_name}
              subtitle={p.client_email}
              right={`UGX ${p.amount}`}
            />

          ))
        )}

      </Section>

      {/* LEADS */}

      <Section title="Lead Discovery">

        {stats.businesses.length === 0 ? (
          <Empty text="No leads collected" />
        ) : (
          stats.businesses.map((b: any, i: number) => (

            <Row
              key={i}
              title={b.name}
              subtitle={`${b.type} • ${b.location}`}
              right="Lead"
            />

          ))
        )}

      </Section>

      {/* OUTREACH */}

      <Section title="Outreach Activity">

        {stats.outreach.length === 0 ? (
          <Empty text="No outreach activity" />
        ) : (
          stats.outreach.map((o: any, i: number) => (

            <Row
              key={i}
              title={o.business_name || "Business"}
              subtitle={o.email || "Outreach Sent"}
              right={o.sent ? "Sent" : "Pending"}
            />

          ))
        )}

      </Section>

    </main>
  )
}

function Card({ title, value }: any) {

  return (
    <div className="
      bg-white
      rounded-2xl
      p-6
      shadow-sm
      border
      border-slate-200
      hover:shadow-md
      transition
    ">

      <p className="text-slate-500 text-sm font-medium">
        {title}
      </p>

      <h2 className="text-3xl font-bold mt-3 text-slate-800">
        {value}
      </h2>

    </div>
  )
}

function Section({ title, children }: any) {

  return (
    <div className="
      bg-white
      rounded-2xl
      p-6
      shadow-sm
      border
      border-slate-200
      mb-8
    ">

      <div className="flex items-center justify-between mb-5">

        <h2 className="text-2xl font-bold text-slate-800">
          {title}
        </h2>

        <div className="
          w-12
          h-1
          rounded-full
          bg-blue-500
        "/>

      </div>

      <div className="space-y-3">
        {children}
      </div>

    </div>
  )
}

function Row({ title, subtitle, right }: any) {

  return (
    <div className="
      flex
      items-center
      justify-between
      border
      border-slate-200
      rounded-xl
      p-4
      hover:bg-slate-50
      transition
    ">

      <div>

        <p className="font-semibold text-slate-800">
          {title}
        </p>

        <p className="text-sm text-slate-500">
          {subtitle}
        </p>

      </div>

      <div className="
        text-sm
        font-bold
        px-3
        py-1
        rounded-full
        bg-blue-100
        text-blue-700
      ">
        {right}
      </div>

    </div>
  )
}
function Empty({ text }: any) {

  return (
    <div className="text-gray-400">
      {text}
    </div>
  )
}