console.log("This is yugals.");

$(".carousel").carousel({
  interval: 1000,
});
let btn = document.getElementById("yugalbar");
btn.addEventListener("input", function () {
  console.log("Button is clicked");

  let bar = document.getElementById("yugalbar");
  let inputVal = bar.value.toLowerCase();

  let noteCards = document.getElementsByClassName("noteCards");

  Array.from(noteCards).forEach(function (elements, index) {
    let cardTxt = elements.getElementsByTagName("p")[0].innerText;

    cardTxts = cardTxt.toLowerCase();
    if (cardTxts.includes(inputVal)) {
      elements.style.display = "block";
    } else {
      elements.style.display = "none";
    }
  });

  let get_class = document.getElementById("itemlist");
  height = get_class.clientHeight;
  let search_result = document.getElementById("get_search_result");
  if (height <= 40) {
    search_result.innerHTML = `The product you searched for is not available`;
  } else {
    search_result.innerHTML = "";
  }
});

let get_item = document.getElementById("itemlist");
heights = get_item.clientHeight;
let filter_result = document.getElementById("get_filter_result");
if (heights <= 40) {
  filter_result.innerHTML = `The product in this price range doesnot exist`;
}

let alert = document.getElementById("alert");
setTimeout(() => {
  alert.innerHTML = "";
}, 3000);

let cartnumbers = document.getElementById("cartvaluehome").value;
console.log(cartnumbers);
console.log($("#cartnumber").text(cartnumbers));
