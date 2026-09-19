document.addEventListener("DOMContentLoaded", function () {

    const footer = document.querySelector("footer");

    footer.innerHTML = `
        <p>© ${new Date().getFullYear()} Ashwitha Thaluri. All Rights Reserved.</p>
    `;

});