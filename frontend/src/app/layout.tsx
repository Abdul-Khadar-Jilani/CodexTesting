import type { Metadata } from "next";

import "./globals.css";

export const metadata: Metadata = {
  title: "DecisionGraph",
  description: "Multi-agent decision intelligence platform"
};

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
