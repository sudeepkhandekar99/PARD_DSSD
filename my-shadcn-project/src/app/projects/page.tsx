"use client";

import { useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";

interface SDG {
  name: string;
  code: string;
}

interface Project {
  id: number;
  project_name: string;
  organization_name: string;
  source_name: string;
  project_website: string;
}

export default function Projects() {
  const searchParams = useSearchParams();
  const [sdgs, setSdgs] = useState<SDG[]>([]);
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const tags = searchParams.getAll("tags");

    if (tags.length > 0) {
      const queryString = tags.map((tag) => `tags=${encodeURIComponent(tag)}`).join("&");

      fetch(`http://localhost:8000/get-sdg?${queryString}`)
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to fetch SDGs.");
          }
          return response.json();
        })
        .then((data) => {
          setSdgs(data.sdgs);
          const sdgCodes = data.sdgs.map((sdg: SDG) => sdg.code);
          return sdgCodes;
        })
        .then((sdgCodes) => {
          const projectQueryString = sdgCodes
            .map((code: string) => `sdgs=${encodeURIComponent(code)}`)
            .join("&");

          return fetch(`http://localhost:8000/get-projects-by-sdgs?${projectQueryString}`);
        })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to fetch projects.");
          }
          return response.json();
        })
        .then((data) => {
          setProjects(data.projects);
          setLoading(false);
        })
        .catch((error) => {
          setError(error.message);
          setLoading(false);
        });
    } else {
      setLoading(false);
    }
  }, [searchParams]);

  return (
    <div className="p-6">
      <h1 className="text-4xl font-bold text-center text-black">Projects</h1>
      <p className="mt-4 text-lg text-center text-black">
        Discover various projects aligned with sustainable development goals (SDG).
      </p>

      {loading ? (
        <p className="mt-6 text-center text-black">Loading projects...</p>
      ) : error ? (
        <p className="mt-6 text-center text-red-500">Error: {error}</p>
      ) : projects.length > 0 ? (
        <div className="space-y-4 mt-8">
          {projects.map((project: Project) => (
            <div
              key={project.id}
              className="flex items-center gap-4 p-4 border border-gray-300 rounded-lg shadow-md bg-white"
            >
              <div className="w-16 h-16 bg-green-500 text-white flex items-center justify-center rounded-full text-xl font-bold">
                {project.id}
              </div>
              <div>
                <h2 className="text-2xl font-bold text-black">{project.project_name}</h2>
                <p className="text-black mt-1">{project.organization_name}</p>
                <p className="text-gray-700 mt-1">{project.source_name}</p>
                <a
                  href={project.project_website}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-500 underline mt-2"
                >
                  Visit Project Website
                </a>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <p className="mt-6 text-center text-gray-700">No projects found for the selected SDGs.</p>
      )}
    </div>
  );
}
