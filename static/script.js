// Works for both desktop clicks and mobile touches
function sendClick(x, y) {
  fetch("/api/click", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ x, y })
  })
  .then(res => {
    if (!res.ok) throw new Error("Network error");
    return res.json();
  })
  .then(data => console.log("Saved:", data))
  .catch(err => console.error("Error saving click:", err));
}

function getCoordinates(e) {
  // Support both mouse and touch
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

// Listen for both clicks and touches
document.addEventListener("click", getCoordinates);
document.addEventListener("touchend", getCoordinates);
