var menu = document.getElementById("menuzin");
var btn = document.getElementById("mobilemenu");
var span = document.getElementsByClassName("close")[0];
console.log(menu);

/*
btn.onclick = function () {
  console.log(menu);
  menu.style.display = "flex";
  console.log(menu.style);
};
btn.onclick = function () {
  menu.style.display = "none";
};
window.onclick = function (event) {
  if (event.target == menu) {
    menu.style.display = "none";
  }
};*/

function reveal() {
  console.log("clicked");
  if (menu.style.display === "flex") {
    return (menu.style.display = "none");
  }
  return (menu.style.display = "flex");
}
