document.addEventListener('DOMContentLoaded', function() {
    var content = document.querySelector('.content');

    // Add animation class when scrolled into view
    window.addEventListener('scroll', function() {
        if (isInViewport(content)) {
            content.classList.add('animate-fadeIn');
        }
    });

    // Check if an element is in the viewport
    function isInViewport(element) {
        var rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }
});
