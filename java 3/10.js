<!DOCTYPE html>
<html>
  <head>
    <title>Form Demo</title>
  </head>
  <body>
    <form id="name-form">
      <label for="first-name-input">First Name:</label>
      <input type="text" id="first-name-input" name="first-name">
      <br>
      <label for="last-name-input">Last Name:</label>
      <input type="text" id="last-name-input" name="last-name">
      <br>
      <input type="submit" value="Submit">
    </form>

    <p id="target"></p>

    <script>
      const nameForm = document.getElementById('name-form');
      const firstNameInput = document.querySelector('input[name="first-name"]');
      const lastNameInput = document.querySelector('input[name="last-name"]');
      const target = document.getElementById('target');

      nameForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const firstName = firstNameInput.value;
        const lastName = lastNameInput.value;
        target.textContent = Your name is ${firstName} ${lastName};
      });
    </script>
  </body>
</html>
