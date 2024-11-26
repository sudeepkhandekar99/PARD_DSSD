"use client";

import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();

  return (
    <div className="text-center">
      <h1 className="text-4xl font-bold text-gray-900">Welcome to PARD</h1>
      <p className="mt-4 text-lg text-gray-700">
        Explore sustainable development projects and organizations.
      </p>
      <button
        onClick={() => router.push("/topics")}
        className="mt-6 px-6 py-3 bg-blue-500 text-white text-lg font-medium rounded-md shadow hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-offset-2"
      >
        Explore Topics
      </button>
    </div>
  );
}
