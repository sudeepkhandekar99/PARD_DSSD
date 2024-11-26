"use client";

import { useState } from "react";

const topics = [
    {
      id: 1,
      title: "No Poverty",
      description: "Access to basic human needs of health, education, sanitation",
      tags: ["income inequality", "education", "health"],
      img: "/images/Sustainable_Development_Goal_01NoPoverty.svg.png",
    },
    {
      id: 2,
      title: "Zero Hunger",
      description: "Providing food relief, humanitarian relief, and sustainable food production",
      tags: ["sustainability", "food", "health"],
      img: "/images/E_SDG-goals_icons-individual-rgb-02.png",
    },
    {
      id: 3,
      title: "Good Health & Well-being",
      description: "Better, more accessible health systems to increase life expectancy",
      tags: ["health"],
      img: "/images/E_SDG-goals_icons-individual-rgb-03.png",
    },
    {
      id: 4,
      title: "Quality Education",
      description: "Inclusive education to enable upward social mobility and end poverty",
      tags: ["education", "income inequality"],
      img: "/images/E_SDG goals_icons-individual-rgb-04.png",
    },
    {
      id: 5,
      title: "Gender Equality",
      description: "Education regardless of gender and advancement of equality laws",
      tags: ["education", "gender"],
      img: "/images/E_SDG-goals_icons-individual-rgb-05.png",
    },
    {
      id: 6,
      title: "Clean Water & Sanitation",
      description: "Improving access for billions of people who lack these basic facilities",
      tags: ["water", "income inequality", "health"],
      img: "/images/E_SDG-goals_icons-individual-rgb-06.png",
    },
    {
      id: 7,
      title: "Affordable and Clean Energy",
      description: "Access to renewable, safe, and available energy sources for all",
      tags: ["sustainability", "energy"],
      img: "/images/E_SDG-goals_icons-individual-rgb-07.png",
    },
    {
      id: 8,
      title: "Decent Work & Economic Growth",
      description: "Creating jobs for all to improve living standards",
      tags: ["jobs"],
      img: "/images/E_SDG goals_icons-individual-rgb-08.png",
    },
    {
      id: 9,
      title: "Industry, Innovation, & Infrastructure",
      description: "Generating employment and income through innovation",
      tags: ["jobs", "infrastructure"],
      img: "/images/E_SDG goals_icons-individual-rgb-09.png",
    },
    {
      id: 10,
      title: "Reduced Inequalities",
      description: "Reducing income and other inequalities, within and between countries",
      tags: ["income inequality"],
      img: "/images/Sustainable_Development_Goal_10ReducedInequalities.svg.png",
    },
    {
      id: 11,
      title: "Sustainable Cities & Communities",
      description: "Making cities safe, inclusive, resilient, and sustainable",
      tags: ["sustainability", "infrastructure"],
      img: "/images/E_SDG-goals_icons-individual-rgb-11.png",
    },
    {
      id: 12,
      title: "Climate Action",
      description: "Regulating and reducing emissions and promoting renewable energy",
      tags: ["sustainability", "climate"],
      img: "/images/E_SDG-goals_icons-individual-rgb-13.png",
    },
    {
      id: 13,
      title: "Life on Land",
      description: "Reversing man-made deforestation and desertification to sustain life on earth",
      tags: ["sustainability", "climate"],
      img: "/images/E_SDG goals_icons-individual-rgb-15.png",
    },
    {
      id: 14,
      title: "Peace, Justice & Strong Institutions",
      description: "Inclusive societies, strong institutions & access to justice",
      tags: ["peace, love, and happiness"],
      img: "/images/E_SDG-goals_icons-individual-rgb-16.png",
    },
    {
      id: 15,
      title: "Partnerships for the Goals",
      description: "Revitalize strong global partnerships for development",
      tags: ["peace, love, and happiness"],
      img: "/images/E_SDG-goals_icons-individual-rgb-17.png",
    },
  ];

// Unique tags from all topics
const uniqueTags = Array.from(
  new Set(topics.flatMap((topic) => topic.tags))
);

function toTitleCase(text: string): string {
  return text.replace(/\w\S*/g, (word) => word.charAt(0).toUpperCase() + word.substring(1).toLowerCase());
}

export default function Topics() {
  const [isSidebarOpen, setSidebarOpen] = useState(false);
  const [selectedTag, setSelectedTag] = useState<string | null>(null);

  // Filter topics based on the selected tag
  const filteredTopics = selectedTag
  ? topics.filter((topic) =>
      topic.tags.some((tag) => tag.toLowerCase() === selectedTag.toLowerCase())
    )
  : topics;

  return (
    <div className="flex">
      {/* Sidebar */}
      <div
        className={`fixed inset-y-0 left-0 transform ${
          isSidebarOpen ? "translate-x-0" : "-translate-x-full"
        } bg-gray-100 p-4 shadow-md transition-transform duration-300 lg:translate-x-0 lg:static lg:w-[20%]`}
      >
        <button
          className="lg:hidden mb-4 text-blue-500 font-medium"
          onClick={() => setSidebarOpen(false)}
        >
          Close Tags
        </button>
        <h2 className="text-xl font-bold mb-4 text-gray-800">Tags</h2>
        <div className="space-y-2">
          <button
            className={`w-full text-left px-3 py-2 ${
              selectedTag === null ? "bg-blue-600 text-white" : "bg-blue-500 text-white"
            } text-sm rounded-md hover:bg-blue-600`}
            onClick={() => setSelectedTag(null)}
          >
            Show All
          </button>
          {uniqueTags.map((tag) => (
            <button
              key={tag}
              className={`w-full text-left px-3 py-2 ${
                selectedTag === tag ? "bg-blue-600 text-white" : "bg-blue-500 text-white"
              } text-sm rounded-md hover:bg-blue-600`}
              onClick={() => setSelectedTag(tag)}
            >
              {toTitleCase(tag)}
            </button>
          ))}
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 p-4 lg:ml-4">
        <div className="flex items-center justify-between">
          <h1 className="text-4xl font-bold text-gray-900">Topics</h1>
          <button
            className="lg:hidden text-blue-500 font-medium"
            onClick={() => setSidebarOpen(true)}
          >
            Explore Tags
          </button>
        </div>
        <p className="text-lg text-gray-600 text-center mt-4">
          {selectedTag
            ? `Topics related to "${toTitleCase(selectedTag)}"`
            : "Explore various topics related to Sustainable Development Goals (SDGs)."}
        </p>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-8">
          {filteredTopics.map((topic) => (
            <div
              key={topic.id}
              className="rounded-lg shadow-lg overflow-hidden bg-white"
            >
              <div className="flex items-center justify-center bg-gray-100">
                <img
                  src={topic.img}
                  alt={topic.title}
                  className="h-full w-full object-contain p-4"
                />
              </div>
              <div className="p-4">
                <h2 className="text-2xl font-bold text-gray-800">{topic.title}</h2>
                <p className="text-gray-600 mt-2">{topic.description}</p>
                <div className="flex flex-wrap gap-2 mt-4">
                  {topic.tags.map((tag) => (
                    <span
                      key={tag}
                      className="px-3 py-1 bg-blue-100 text-blue-500 text-sm rounded-md"
                    >
                      {toTitleCase(tag)}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}