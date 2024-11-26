import "./globals.css";
import Navbar from "@/components/ui/Navbar";

export const metadata = {
  title: "PARD",
  description: "Platform for sustainable development",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-gray-50">
        <Navbar />
        <main className="container mx-auto mt-8 px-4">{children}</main>
      </body>
    </html>
  );
}
