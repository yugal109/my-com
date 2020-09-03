//CATEGORIES
let category = [
  "Clothing",
  "Electronics",
  "MobilePhones",
  "Accessories",
  "BathroomItems",
  "HouseholdItems",
  "StationeryItems",
];
for (let Category of category) {
  $(".dropdown-btn-" + Category).click(function () {
    $("aside ul .dropdown-show" + Category.toLowerCase()).toggleClass("show");
    $("aside ul .ROTATE" + Category.toLowerCase()).toggleClass("rotate");
  });
}

//CLOTHING
let sub_category_clothing = [
  "Shirt",
  "Pant",
  "Belt",
  "Shoes",
  "Jacket",
  "T-Shirt",
  "Coat",
];

console.log("T-Shirt".toLowerCase());

for (let categ of sub_category_clothing) {
  console.log(categ);

  $(".dropdown-btn-Clothing-" + categ).click(function () {
    $("aside ul .dropdown-showclothing-" + categ.toLowerCase()).toggleClass(
      "show"
    );
    $("aside ul .ROTATE" + categ.toLowerCase()).toggleClass("rotate");
  });

  $(".dropdown-btn-Clothing-" + categ + "-Brand").click(function () {
    $(
      "aside ul .dropdown-showclothing-" + categ.toLowerCase() + "-brand"
    ).toggleClass("show");
    $("aside ul .ROTATE+" + categ.toLowerCase() + "brand").toggleClass(
      "rotate"
    );
  });
  $(".dropdown-btn-Clothing-" + categ + "-Material").click(function () {
    $(
      "aside ul .dropdown-showclothing-" + categ.toLowerCase() + "-material"
    ).toggleClass("show");
    $("aside ul .ROTATE" + categ.toLowerCase() + "material").toggleClass(
      "rotate"
    );
  });
}

//ELECTRONICS

let sub_category_electronics = ["Camera", "Laptop", "PC", "TV"];

for (let categ_electronics of sub_category_electronics) {
  $(".dropdown-btn-Electronics-" + categ_electronics).click(function () {
    $(
      "aside ul .dropdown-showelectronics-" + categ_electronics.toLowerCase()
    ).toggleClass("show");
    $("aside ul .ROTATE" + categ_electronics.toLowerCase()).toggleClass(
      "rotate"
    );
  });
}

//ACCESSORIES
let sub_category_accessories = ["Watch"];

for (let categ_accessories of sub_category_accessories) {
  $(".dropdown-btn-Accessories-" + categ_accessories).click(function () {
    $(
      "aside ul .dropdown-showaccessories-" + categ_accessories.toLowerCase()
    ).toggleClass("show");
    $("aside ul .ROTATE" + categ_accessories.toLowerCase()).toggleClass(
      "rotate"
    );
  });
  $(".dropdown-btn-Accessories-" + categ_accessories + "-Brand").click(
    function () {
      $(
        "aside ul .dropdown-showaccessories-" +
          categ_accessories.toLowerCase() +
          "-brand"
      ).toggleClass("show");
      $(
        "aside ul .ROTATE" + categ_accessories.toLowerCase() + "brand"
      ).toggleClass("rotate");
    }
  );
}
