/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit', // Ativar JIT mode
  content: [
    "./templates/**/*.html", // Adicione o caminho para os seus arquivos HTML
    "./src/**/*.{js,jsx,ts,tsx}", // Se você tiver arquivos JS, adicione aqui
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}