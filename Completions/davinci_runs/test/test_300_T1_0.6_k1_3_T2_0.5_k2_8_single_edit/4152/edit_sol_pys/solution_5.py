// Your JS goes here


for (var i = 0; i < 81; i++) {
  var div = document.createElement('div');
  div.style.width = "11.1%";
  div.style.float = "left";
  div.style.paddingBottom = "11.1%";
  if (i % 2 === 0) {
    div.style.backgroundColor = "red";
  }
  else {
    div.style.backgroundColor = "black";
  }
  document.body.appendChild(div);
}
