const menuToggle = document.getElementById('menuToggle');
const mainNav = document.getElementById('mainNav');

if (menuToggle && mainNav) {
  menuToggle.addEventListener('click', () => mainNav.classList.toggle('open'));
  mainNav.querySelectorAll('.nav-link, .nav-cta').forEach(link => {
    link.addEventListener('click', () => mainNav.classList.remove('open'));
  });
}

document.addEventListener('click', (e) => {
  if (mainNav && menuToggle && !mainNav.contains(e.target) && !menuToggle.contains(e.target)) {
    mainNav.classList.remove('open');
  }
});
