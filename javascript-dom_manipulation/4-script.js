document.getElementById("add_item").addEventListener("click", function() {
    // Create a new list item element
    let newItem = document.createElement("li");
    newItem.textContent = "Item";
    
    // Append the new item to the list with class 'my_list'
    document.querySelector(".my_list").appendChild(newItem);
});

