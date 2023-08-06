const handleScroll = (event) => {
    const scrollPosition = event.target.scrollingElement.scrollTop;

    const images = document.querySelectorAll("img");

    images.forEach((element) => {
        element.style.transform = `translate(0, ${scrollPosition / 10}px)`;
    });
};

window.addEventListener("scroll", handleScroll);