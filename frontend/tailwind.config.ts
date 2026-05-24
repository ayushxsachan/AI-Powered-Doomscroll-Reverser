import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        void: "#050506",
        carbon: "#0b0d10",
        blood: "#ff2a3d",
        ember: "#ff8a3d",
        acid: "#b6ff4d",
        cyan: "#22d3ee",
        violet: "#8b5cf6",
      },
      boxShadow: {
        neon: "0 0 30px rgba(255, 42, 61, 0.35)",
        cyan: "0 0 28px rgba(34, 211, 238, 0.25)",
      },
      backgroundImage: {
        "radial-blood": "radial-gradient(circle at 50% 0%, rgba(255,42,61,0.24), transparent 34%)",
      },
      keyframes: {
        scan: {
          "0%": { transform: "translateY(-100%)" },
          "100%": { transform: "translateY(100%)" },
        },
        flicker: {
          "0%, 100%": { opacity: "1" },
          "41%": { opacity: "0.72" },
          "43%": { opacity: "1" },
          "48%": { opacity: "0.55" },
          "50%": { opacity: "1" },
        },
        float: {
          "0%, 100%": { transform: "translateY(0)" },
          "50%": { transform: "translateY(-12px)" },
        },
      },
      animation: {
        scan: "scan 6s linear infinite",
        flicker: "flicker 4s infinite",
        float: "float 7s ease-in-out infinite",
      },
    },
  },
  plugins: [],
};

export default config;

