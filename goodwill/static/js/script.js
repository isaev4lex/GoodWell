document.addEventListener('DOMContentLoaded', () => {
  const swiper = new Swiper('.swiper-container', {
    loop: true,
    pagination: {
      el: '.swiper-pagination',
      bulletClass: 'dots',
      bulletActiveClass: 'dots-active',
      clickable: 'true',
    },
  });

  const mobileProducts = document.querySelector('#products');
  const mobileSubmenu = document.querySelector('.submenu-mobile');
  mobileProducts.addEventListener('click', () => {
    mobileProducts.classList.toggle('menu__item-rotate');
    mobileSubmenu.classList.toggle('submenu-mobile-active');
  });
});
