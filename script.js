
document.addEventListener('DOMContentLoaded', function() {
    // Get the input element
    const inputElement = document.getElementById('software-input');
    const jsonDisplay = document.getElementById('json-display');

    // Fetch JSON data from the server
    fetch('./software.json')
        .then(response => response.json())
        .then(data => {
            // Store the JSON data
            const softwareData = data;

            // Listen for input event
            inputElement.addEventListener('input', function() {
                // Split the input value by commas or white space
                const softwareNames = this.value.split(/[, ]+/);

                // Clear previous results
                jsonDisplay.innerHTML = '';

                // Loop through the software names
                softwareNames.forEach(name => {
                    // Check if the name is not empty or null
                    if (name && softwareData.hasOwnProperty(name)) {
                        // Create a new element to display the matching software
                        const matchElement = document.createElement('div');
                        matchElement.textContent = `${softwareData} open source alternative to ${name}`;
                        
                        // Append the match element to the display
                        jsonDisplay.appendChild(matchElement);
                    }
                });
            });
        })
        .catch(error => {
            console.error('Error fetching JSON:', error);
        });
});

