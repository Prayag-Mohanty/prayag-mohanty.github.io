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
const burger = document.getElementById('burger');
const menu = document.getElementById('menu');
burger.addEventListener('click', () => {
  const open = menu.classList.toggle('open');
  burger.setAttribute('aria-expanded', open);
  burger.textContent = open ? '✕' : '☰';
});
const bar = document.querySelector('.progress');
let ticking = false;
const progress = () => {
  const max = document.documentElement.scrollHeight - innerHeight;
  bar.style.transform = `scaleX(${max > 0 ? Math.min(scrollY / max, 1) : 0})`;
  ticking = false;
};
addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(progress); } }, { passive: true });
addEventListener('resize', progress);
progress();
// Fade content in as it scrolls into view; anything already on screen shows immediately.
if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const io = new IntersectionObserver(entries => entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }), { rootMargin: '0px 0px -8% 0px' });
  const watch = el => {
    if (el.getBoundingClientRect().top < innerHeight) return;
    el.classList.add('reveal');
    io.observe(el);
  };
  document.querySelectorAll('main h2, .card, .news li, .list li').forEach(watch);
  // Blog posts arrive after load
  const posts = document.getElementById('posts');
  if (posts) new MutationObserver(() => posts.querySelectorAll('.card:not(.reveal)').forEach(watch)).observe(posts, { childList: true });
}
