"use client";

import { usePathname, useRouter } from "next/navigation";

export default function Navbar() {
    const pathname = usePathname();
    const router = useRouter();

    // Define navigation content for each route
    const navbarContent: Record<string, { right: { name: string; link: string }[] }> = {
        "/": {
            right: [
                { name: "About", link: "/about" },
                { name: "How to Contribute", link: "/how-to-contribute" },
            ],
        },
        "/topics": {
            right: [
                { name: "About", link: "/about" },
                { name: "How to Contribute", link: "/how-to-contribute" },
            ],
        },
        "/projects": {
            right: [
                { name: "Projects in SDG", link: "/projects" },
            ],
        },
        "/project-details": {
            right: [
                { name: "Project Details in Organization", link: "/project-details" },
            ],
        },
        "/organization-list": {
            right: [
                { name: "Organization list in SDG", link: "/organization-list" },
            ],
        },
        "/organization": {
            right: [
                { name: "Organization in SDG", link: "/organization" },
            ],
        },
    };

    const currentContent = navbarContent[pathname] || { right: [] };

    return (
        <nav className="flex items-center justify-between bg-white px-8 py-4 shadow-md">
            {/* Left Content: Always "PARD" */}
            <div
                className="text-xl font-bold text-gray-900 cursor-pointer"
                onClick={() => router.push("/")}
            >
                PARD
            </div>

            {/* Right Links */}
            <div className="flex space-x-6">
                {currentContent.right.map((item) => (
                    <button
                        key={item.name}
                        className="text-lg font-medium text-gray-700 hover:text-blue-500"
                        onClick={() => router.push(item.link)}
                    >
                        {item.name}
                    </button>
                ))}
            </div>
        </nav>
    );
}
