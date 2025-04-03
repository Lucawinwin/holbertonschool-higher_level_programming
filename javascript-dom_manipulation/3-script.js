// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Select the element with id 'toggle_header'
  const toggleButton = document.querySelector('#toggle_header');
  
  // Add a click event listener to this element
  toggleButton.addEventListener('click', function() {
    // When clicked, select the header element
    const header = document.querySelector('header');
    
    // Check current class and toggle between red and green
    if (header.classList.contains('red')) {
      header.classList.remove('red');
      header.classList.add('green');
    } else {
      header.classList.remove('green');
      header.classList.add('red');
    }
  });
});
