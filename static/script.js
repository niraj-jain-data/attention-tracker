function sendClick(x, y) {
  fetch("/api/click", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ x, y })
  })
  .then(res => res.json())
  .then(data => console.log("Tap saved:", data))
  .catch(err => console.error("Error:", err));
}

function getCoordinates(e) {
  let x, y;
  if (e.touches && e.touches.length > 0) {
    const touch = e.touches[0];
    x = touch.pageX;
    y = touch.pageY;
  } else {
    x = e.pageX;
    y = e.pageY;
  }
  sendClick(x, y);
}

document.addEventListener("click", getCoordinates);
document.addEventListener("touchend", getCoordinates);
