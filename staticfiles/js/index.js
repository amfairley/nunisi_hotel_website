document.addEventListener('DOMContentLoaded', function () {
  // About us Carousel Logic //
  const carousel = document.getElementById('aboutUsCarousel');
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');

  const toggleButtons = () => {
      const activeIndex = Array.from(carousel.querySelectorAll('.carousel-item-desktop')).findIndex(item =>
      item.classList.contains('active')
      );
      prevBtn.classList.toggle('d-none', activeIndex === 0);
      nextBtn.classList.toggle('d-none', activeIndex === 1);
  };

  carousel.addEventListener('slid.bs.carousel', toggleButtons);
  toggleButtons();

  // Navbar burger menu hiding functionality
  const navLinks = document.querySelectorAll('.navbar .nav-link');
  navLinks.forEach(link => {
    link.addEventListener("click", function () {
      const navbarCollapse = new bootstrap.Collapse(
        document.getElementById("navbarSupportedContent"),
        { toggle: false }
      );
      navbarCollapse.hide();
    });
  });
});