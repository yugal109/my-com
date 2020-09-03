$(".carousel").carousel({
  interval: 3000,
});
let btn = document.getElementById("yugbtn");
btn.addEventListener("click", function () {
  console.log("Button clicked");
  let bar = document.getElementById("yugalbar");
  let inputVal = bar.value.toLowerCase();
  console.log(inputVal);
  let noteCards = document.getElementsByClassName("noteCards");

  Array.from(noteCards).forEach(function (elements, index) {
    let cardTxt = elements.getElementsByTagName("p")[0].innerText;
    console.log(cardTxt);
    console.log(index);
    cardTxts = cardTxt.toLowerCase();
    if (cardTxts.includes(inputVal)) {
      elements.style.display = "block";
    } else {
      elements.style.display = "none";
    }
  });
});

let cartnumbers = document.getElementById("cartvalue").value;
console.log(cartnumbers);
console.log($("#cartnumber").text(cartnumbers));

let alert = document.getElementById("alert");
setTimeout(() => {
  alert.innerHTML = "";
}, 3000);
