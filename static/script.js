document.addEventListener("click", (e) => {
    const x = e.pageX;
    const y = e.pageY;
  
    fetch("/api/click", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({x, y})
    });
  });
  