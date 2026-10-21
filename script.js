document.getElementById('year').textContent = new Date().getFullYear();
const root = document.documentElement;
const btn = document.getElementById('theme');
const paint = () => { btn.textContent = root.dataset.theme === 'light' ? '☾' : '☀'; };
paint();
btn.addEventListener('click', () => {
  root.dataset.theme = root.dataset.theme === 'light' ? 'dark' : 'light';
  try { localStorage.setItem('theme', root.dataset.theme); } catch (e) {}
  paint();
});
