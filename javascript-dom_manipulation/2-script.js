// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Select the element with id 'red_header'
  const redHeaderButton = document.querySelector('#red_header');
  
  // Add a click event listener to this element
  redHeaderButton.addEventListener('click', function() {
    // When clicked, select the header element and add the 'red' class to it
    const header = document.querySelector('header');
    header.classList.add('red');
  });
});
