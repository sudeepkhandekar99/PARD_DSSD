/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./src/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#1d4ed8", // Adjust primary color for links/buttons
      },
    },
  },
  plugins: [],
  darkMode: false, // Disable dark mode
};
