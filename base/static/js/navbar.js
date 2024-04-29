const navbar = document.querySelector("#navbar");
const threshold = navbar.offsetTop;
const cart = document.querySelector('#cart')
const logout = document.querySelector('#logout')
const profile = document.querySelector("#profile")
const fav = document.querySelector("#fav")
const quantity = document.querySelector("#quantity")

window.addEventListener('scroll', () => {
    if (window.scrollY > threshold) {
        navbar.classList.add('fixed', 'z-50', 'top-0', 'w-full', 'transform', 'bg-indigo-800', 'text-white', 'transition-transform', 'duration-300', 'ease-in-out');
        if (cart) {

            cart.classList.add('text-white')
            cart.classList.remove('text-indigo-600')
        }
        if (quantity) {

            quantity.classList.add('bg-indigo-800', 'text-white')
        }

        if (logout) {

            logout.classList.add('text-white')
            logout.classList.remove('text-indigo-600')

        }
        if (profile) {

            profile.classList.add('text-white')
            profile.classList.remove('text-indigo-600')
        }
    } else {
        navbar.classList.remove('fixed', 'z-50', 'top-0', 'w-full', 'transform', 'bg-indigo-800', 'text-white', 'transition-transform', 'duration-300', 'ease-in-out');
        if (cart) {

            cart.classList.remove('text-white')
        }
        if (logout) {

            logout.classList.remove('text-white')
        }
        if (profile) {

            profile.classList.remove('text-white')
        }
        if (quantity) {

            quantity.classList.remove('bg-white', 'text-indigo-800')
        }

    }
})