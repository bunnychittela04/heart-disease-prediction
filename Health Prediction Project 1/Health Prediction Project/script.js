const predictionForm = document.getElementById('prediction-form');
const predictionResult = document.getElementById('prediction-result');
const predictionText = document.getElementById('prediction-text');

predictionForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission

  // Gather user input data
  const formData = new FormData(predictionForm);
  const data = Object.fromEntries(formData.entries()); // Convert FormData to object

  // Send data to Flask app using fetch API
  fetch('/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json' // Specify JSON data type
    },
    body: JSON.stringify(data) // Convert data object to JSON string
  })
  .then(response => response.json()) // Parse JSON response from Flask
  .then(data => {
    predictionResult.classList.remove('hidden'); // Show prediction result
    predictionText.textContent = data.prediction; // Update prediction text
  })
  .catch(error => {
    console.error('Error fetching prediction:', error);
    predictionText.textContent = 'An error occurred. Please try again.';
  });
});


// Handle form submission for registration
registerForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission behavior

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirm-password').value;

  // Basic validation (replace with more robust checks as needed)
  if (username === '' || password === '' || confirmPassword === '') {
    message.textContent = 'Please fill in all fields.';
    return;
  }

  if (password !== confirmPassword) {
    message.textContent = 'Passwords do not match.';
    return;
  }

  // Simulate successful registration (replace with actual user registration logic)
  message.textContent = 'Registration successful!';
  registerForm.reset(); // Clear the form after successful registration
});

// Handle form submission for login
loginForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission behavior

  const username = document.getElementById('login-username').value;
  const password = document.getElementById('login-password').value;

  // Simulate successful login (replace with actual user authentication logic)
  if (username === 'user' && password === 'password') {
    message.textContent = 'Login successful!';
    // Redirect to prediction page or show prediction button after successful login
    window.location.href = "predict.html"; // Redirect to predict.html
  } else {
    message.textContent = 'Invalid username or password.';
  }
});

const registerForm = document.getElementById('register-form');
const loginForm = document.getElementById('login-form');
const message = document.getElementById('message');

function handleLogin() {
  const username = document.getElementById('login-username').value;
  const password = document.getElementById('login-password').value;

  // Login validation (replace with actual authentication logic)
  if (username === 'user' && password === 'password') {
    message.textContent = 'Login successful!';

    // Hide login form and display prediction section (replace with your actual implementation)
    loginForm.style.display = 'none';
    const predictionSection = document.getElementById('prediction-section'); // Assuming you have an element with this ID
    predictionSection.style.display = 'block';
  } else {
    message.textContent = 'Invalid username or password.';
  }
}

loginForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission behavior
  handleLogin();
});


