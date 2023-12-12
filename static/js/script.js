// script.js

document.addEventListener("DOMContentLoaded", function() {
    // Add event listener to the Predict button
    const predictButton = document.querySelector("#predictButton");
    if (predictButton) {
        predictButton.addEventListener("click", function() {
            alert("Prediction button clicked!");
            // Add more JavaScript logic here as needed
        });
    }
});
