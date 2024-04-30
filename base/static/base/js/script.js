/* 
Author:
- Anthony
*/

// login.html scripts
function validateLogin() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const errorMessage = document.getElementById("error-message");

  // Check if username length is less than 3 characters and prevent form submission
  if (username.length < 3) {
    errorMessage.textContent = "Username must be at least 3 characters long.";
    errorMessage.style.display = "block";
    return false;
  }

  // Check if password length is less than 6 characters and prevent form submission
  if (password.length < 6) {
    errorMessage.textContent = "Password must be at least 6 characters long.";
    errorMessage.style.display = "block";
    return false; // Prevent form submission
  }

  return true;
}


// equipment-list.html scripts 
const bookBtns = document.querySelectorAll(".book-equipment");
const generalFilterSelect = document.getElementById('general-filter');
const typeFilterSelect = document.getElementById('type-filter');
const locationFilterSelect = document.getElementById('location-filter');
const statusFilterSelect = document.getElementById('status-filter'); 
const filterButton = document.getElementById('filter');
const filters = document.querySelector('.filters');

// Change button styling and disable button if item.status is "Out of Service" or "On Loan"
bookBtns.forEach(button => {
  if (button.textContent.trim() === "Out") {
    button.style.backgroundColor = "grey";
    button.style.cursor = "default";
    button.disabled = true;
  }
});

// Submit form based on the filter selected
generalFilterSelect.addEventListener('change', function() {
  document.getElementById('generalFilterForm').submit();
});

typeFilterSelect.addEventListener('change', function() {
  document.getElementById('typeFilterForm').submit();
});
locationFilterSelect.addEventListener('change', function() {
  document.getElementById('locationFilterForm').submit();
});
statusFilterSelect.addEventListener('change', function() {
  document.getElementById('statusFilterForm').submit();
});

// Toggle the visibility of the filters section
filterButton.addEventListener('click', function() { 
  if (filters) {
    filters.classList.toggle('hidden');
  }
});

