(() => {
    const navbar = document.querySelector("#navbar");
    const threshold = navbar.offsetTop; // Obtén la posición inicial del navbar
    const cart = document.querySelector('#cart')
    console.log("Hola mundo")
    window.addEventListener('scroll', () => {
        if (window.scrollY > threshold) {
            navbar.classList.add('fixed', 'z-50', 'top-0',  'w-full', 'transform','bg-red-600', 'text-white', 'transition-transform', 'duration-300','ease-in-out'); 
            cart.classList.add('text-white')
            cart.classList.remove('text-indigo-600')
        } else {
            navbar.classList.remove('fixed', 'z-50', 'top-0',  'w-full', 'transform','bg-red-600', 'text-white', 'transition-transform', 'duration-300','ease-in-out');
            cart.classList.remove('text-white')
        }
    });
})();