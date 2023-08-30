document.addEventListener("DOMContentLoaded", function () {
    const pythonValueContainer = document.getElementById("pythonValueContainer");
    const pythonValue = pythonValueContainer.getAttribute("data-value");

    const gaugeArrow = document.getElementById("gaugeArrow");
    const gaugeValue = pythonValue; // Example value between 0 and 1

    const angle = gaugeValue * 90; // Assuming a half-circle gauge

    gaugeArrow.style.transform = `translateX(-50%) translateY(-100%) rotate(${angle}deg)`;

    const numTicks = 16;

    const tickMarksContainer = document.getElementById("tickMarks");

    for (let i = 0; i < numTicks; i++) {
        const tick = document.createElement("div");
        tick.className = "tick";
        tick.style.transform = `rotate(${(360 / numTicks) * i}deg)`;
        tickMarksContainer.appendChild(tick);
}
});
