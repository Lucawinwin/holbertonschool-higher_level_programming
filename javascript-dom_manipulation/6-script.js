document.getElementById("add_item").addEventListener("click", function() {
    // Create a new list item element
    let newItem = document.createElement("li");
    newItem.textContent = "Item";
    
    // Append the new item to the list with class 'my_list'
    document.querySelector(".my_list").appendChild(newItem);
});

document.getElementById("update_header").addEventListener("click", function() {
    // Update the text of the header element
    document.querySelector("header").textContent = "New Header!!!";
});

// Fetch character name from API and display it in the element with id 'character'
fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
    .then(response => response.json())
    .then(data => {
        document.getElementById("character").textContent = data.name;
    })
    .catch(error => console.error("Error fetching character:", error));

