console.log("This is the new project.");
const name = document.getElementById("username");
const email = document.getElementById("email");
const pass1 = document.getElementById("pass1");
const pass2 = document.getElementById("pass2");

// console.log(name, email, phone);
name.addEventListener("blur", (e) => {
  e.preventDefault();
  console.log("name is blurred");
  let regex = /^[a-zA-Z0-9]([0-9a-zA-Z]){2,19}$/;
  let str = name.value;
  console.log(regex, str);
  if (regex.test(str)) {
    console.log("Your name is valid.");
    name.classList.remove("is-invalid");
  } else {
    console.log("Your name is not valid.");
    name.classList.add("is-invalid");
  }
});
email.addEventListener("blur", () => {
  console.log("email is blurred");
  let regex = /^([_\-\.0-9a-zA-Z]+)@([_\-\.*0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
  let str = email.value;
  console.log(regex, str);
  if (regex.test(str)) {
    console.log("Your email is valid.");
    email.classList.remove("is-invalid");
  } else {
    console.log("Your email is not valid.");
    email.classList.add("is-invalid");
  }
});
pass1.addEventListener("blur", () => {
  if (pass1.value.length <= 8) {
    pass1.classList.add("is-invalid");
  } else {
    console.log("Your email is not valid.");
    pass1.classList.remove("is-invalid");
  }
});
pass2.addEventListener("blur", () => {
  console.log("The value is : ", pass2.value.length);
  if (pass1.value != pass2.value) {
    pass2.classList.add("is-invalid");
  } else {
    pass2.classList.remove("is-invalid");
  }
});
