console.log("Yugal");

let val = document.getElementById("quantity");
val.addEventListener("input", (e) => {
  e.preventDefault();
  if (val.value == 0) {
    let btn = document.getElementById("button");
    btn.classList.add("disabled");
    btn.type = "button";
  } else if (val.value != 0) {
    let btn = document.getElementById("button");
    btn.classList.remove("disabled");
    btn.type = "submit";
  }
});

let minus = document.getElementById("minus");
minus.addEventListener("click", (e) => {
  e.preventDefault();

  let val = document.getElementById("quantity").value;
  if (val == 1) {
    let newval = 1;
    document.getElementById("quantity").value = newval;
  } else {
    let newval = val - 1;
    document.getElementById("quantity").value = newval;
  }
});
let plus = document.getElementById("plus");
plus.addEventListener("click", (e) => {
  e.preventDefault();
  let vals = document.getElementById("quantity").value;
  let newvals = parseInt(vals) + 1;
  document.getElementById("quantity").value = newvals;
  let btn = document.getElementById("button");
  btn.classList.remove("disabled");
});

let alert = document.getElementById("alert");
alert.innerHTML = ` 

<div class="alert alert-warning alert-dismissible fade show" role="alert">
  Added to cart
  <button
    type="button"
    class="close"
    data-dismiss="alert"
    aria-label="Close"
  >
    <span aria-hidden="true">&times;</span>
  </button>
</div>
`;
setTimeout(() => {
  alert.innerHTML = "";
}, 2000);
