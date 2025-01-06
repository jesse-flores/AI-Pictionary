import confetti from "https://cdn.skypack.dev/canvas-confetti";

//Triggering confetti
const doItNow = (evt, hard) => {
    const direction = Math.sign(lastX - evt.clientX);
    lastX = evt.clientX;
    const particleCount = hard ? r(122, 245) : r(2, 15);

    const rect = correctButton.getBoundingClientRect(); //Target the correctButton
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;

    const shootConfetti = () => {
        confetti({
            particleCount,
            angle: r(90, 90 + direction * 30),
            spread: r(45, 80),
            origin: {
                x: centerX / window.innerWidth,
                y: centerY / window.innerHeight
            }
        });
    };

    //Trigger confetti multiple times
    for (let i = 0; i < 10; i++) {
        setTimeout(shootConfetti, i * 200);
    }
};

const doItHard = (evt) => {
    doItNow(evt, true);
};

let lastX = 0;

const correctButton = document.querySelector("#correct");

correctButton.addEventListener("click", doItHard);

function r(mi, ma) {
    return parseInt(Math.random() * (ma - mi) + mi);
}



function popupFn() {
    var img = document.getElementById("wrong");

    img.style.display

    setTimeout(function() {
        img.style.display = "none";
    }, 2500); //5000 milliseconds
}
    