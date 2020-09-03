console.log("Yugal");
console.log("Yugal");
let minus = document.getElementById("minus");
minus.addEventListener("click", (e) => {
  e.preventDefault();

  let val = document.getElementById("quantity").value;
  if (val == 1) {
    let newval = 1;
    document.getElementById("quantity").value = newval;
  } else {
    let newval = parseInt(val) - 1;
    document.getElementById("quantity").value = newval;
  }
});

let plus = document.getElementById("plus");
plus.addEventListener("click", (e) => {
  e.preventDefault();
  let vals = document.getElementById("quantity").value;
  let newvals = parseInt(vals) + 1;
  document.getElementById("quantity").value = newvals;
});

let alert = document.getElementById("alert");
setTimeout(() => {
  alert.innerHTML = "";
}, 10000);


