const nav = document.querySelector('nav');

document.addEventListener("scroll", e => {
  if (scrollY > 100) {
    if (scrollY > window.innerHeight) {
      nav.classList.add('invisible');
    } else {
      nav.classList.add('bg-gray-900');
      nav.classList.remove('invisible');
    }
  } else {
    nav.classList.remove('bg-gray-900');
    nav.classList.remove('invisible');
  }
});
