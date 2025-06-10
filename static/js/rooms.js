document.addEventListener('DOMContentLoaded', function () {
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