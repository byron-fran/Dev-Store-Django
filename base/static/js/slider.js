

const swiper = new Swiper('.mySwiper', {
    slidesPerView: 1,
    spaceBetween: 30,
    effect : 'flip',
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,

    },
    autoplay : {
        delay : 1500
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
})