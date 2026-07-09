document.addEventListener("DOMContentLoaded", function () {
    const popup = document.getElementById("dynamicPopup");

    if (popup) {
        const popupSeen = sessionStorage.getItem("necPopupSeen");

        if (popupSeen === "yes") {
            popup.style.display = "none";
        } else {
            popup.style.display = "flex";
            sessionStorage.setItem("necPopupSeen", "yes");
        }
    }
});


function closePopup() {
    const popup = document.getElementById("dynamicPopup");
    if (popup) {
        popup.style.display = "none";
        sessionStorage.setItem("necPopupSeen", "yes");
    }
}

// popup code ...

function loadProgramTab(btn) {
    const url = btn.dataset.url;
    console.log("clicked url:", url);

    if (!url) return;

    document.querySelectorAll(".program-tab-link").forEach(function(item){
        item.classList.remove("active");
    });

    btn.classList.add("active");

    fetch(url)
        .then(res => res.text())
        .then(html => {
            const doc = new DOMParser().parseFromString(html, "text/html");
            const newContent = doc.querySelector("#program-detail-area");
            const currentContent = document.querySelector("#program-detail-area");

            if (newContent && currentContent) {
                currentContent.innerHTML = newContent.innerHTML;
                history.pushState({}, "", url);
            }
        });
}

// hero slider code ...

let currentHeroSlide = 0;

function getHeroSlides() {
    return document.querySelectorAll(".hero-slide");
}

function getHeroDots() {
    return document.querySelectorAll(".hero-dot");
}

function showHeroSlide(index) {
    const slides = getHeroSlides();
    const dots = getHeroDots();
    updateEntranceDeadline();


    if (!slides.length) return;

    if (index >= slides.length) {
        currentHeroSlide = 0;
    } else if (index < 0) {
        currentHeroSlide = slides.length - 1;
    } else {
        currentHeroSlide = index;
    }

    slides.forEach((slide, i) => {
        slide.classList.toggle("active", i === currentHeroSlide);
    });

    dots.forEach((dot, i) => {
        dot.classList.toggle("active", i === currentHeroSlide);
    });
}

function moveHeroSlide(step) {
    showHeroSlide(currentHeroSlide + step);
}

function goToHeroSlide(index) {
    showHeroSlide(index);
}

   function updateEntranceDeadline() {
    
    const deadlineDate = new Date("2026-07-09T00:00:00");

    const today = new Date();
    const difference = deadlineDate - today;
    const daysLeft = Math.ceil(difference / (1000 * 60 * 60 * 24));

    const daysLeftElements = document.querySelectorAll(".daysLeft");
    const remainingBoxes = document.querySelectorAll(".remaining-days");

    if (!daysLeftElements.length) return;

    if (daysLeft > 0) {
        daysLeftElements.forEach(function(element) {
            element.innerText = daysLeft;
        });
    } else if (daysLeft === 0) {
        daysLeftElements.forEach(function(element) {
            element.innerText = "Today";
        });
    } else {
        remainingBoxes.forEach(function(box) {
            box.innerText = "Deadline has passed";
        });
    }
} 

function sendMessage() {
    const input = document.getElementById("chat-input");
    const body = document.getElementById("chat-body");

    if (!input || !body) return;

    const msg = input.value.trim();
    if (!msg) return;

    body.innerHTML += `<div class="chat-msg user-msg">${msg}</div>`;
    body.innerHTML += `<div id="bot-typing"><b>necBot:</b> Typing...</div>`;
    body.scrollTop = body.scrollHeight;

    fetch("/chatbot/chat/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: msg })
    })
    .then(async (res) => {
        const data = await res.json();

        if (!res.ok) {
            throw new Error(data.reply || `HTTP ${res.status}`);
        }

        const typing = document.getElementById("bot-typing");
        if (typing) typing.remove();

        body.innerHTML += `<div><b>necBot:</b> ${data.reply}</div>`;
        body.scrollTop = body.scrollHeight;
    })
    .catch((error) => {
        const typing = document.getElementById("bot-typing");
        if (typing) typing.remove();

        body.innerHTML += `<div><b>NecBot:</b> ${error.message}</div>`;
        body.scrollTop = body.scrollHeight;
        console.error("Chat error:", error);
    });

    input.value = "";
}
 document.addEventListener("DOMContentLoaded", function () {
    const counters = document.querySelectorAll(".counter");

    if (!counters.length) return;

    const runCounter = (counter) => {
        const target = Number(counter.getAttribute("data-target"));
        let current = 0;
        const duration = 2500;
        const stepTime = 20;
        const increment = target / (duration / stepTime);

        const timer = setInterval(() => {
            current += increment;

            if (current >= target) {
                counter.innerText = target;
                clearInterval(timer);
            } else {
                counter.innerText = Math.floor(current);
            }
        }, stepTime);
    };

    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                runCounter(entry.target);
                obs.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.5
    });

    counters.forEach((counter) => {
        observer.observe(counter);
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const slides = getHeroSlides();
    if (slides.length) {
        showHeroSlide(0);

        if (slides.length > 1) {
            setInterval(() => {
                showHeroSlide(currentHeroSlide + 1);
            }, 2000);
        }
    }


    const chatbotToggle = document.getElementById("chatbotToggle");
    const chatbotBox = document.getElementById("chatbotBox");
    const chatbotClose = document.getElementById("chatbotClose");
    const chatInput = document.getElementById("chat-input");
    const chatSendBtn = document.getElementById("chat-send-btn");

    if (chatbotToggle && chatbotBox) {
        chatbotToggle.addEventListener("click", function () {
        chatbotBox.classList.add("active");
        });
    }

    if (chatbotClose && chatbotBox) {
        chatbotClose.addEventListener("click", function () {
            chatbotBox.classList.remove("active");
        });
    }

    if (chatSendBtn) {
        chatSendBtn.addEventListener("click", function (e) {
            e.preventDefault();
            sendMessage();
        });
    }

    if (chatInput) {
        chatInput.addEventListener("keydown", function (e) {
            if (e.key === "Enter") {
                e.preventDefault();
                sendMessage();
            }
        });
    }
});
document.addEventListener("DOMContentLoaded", function () {

    // 🔥 chip button logic
    const chips = document.querySelectorAll(".nec-chip");

    chips.forEach(btn => {
        btn.addEventListener("click", function () {
            const msg = this.getAttribute("data-message");

            const input = document.getElementById("chat-input");
            if (input) {
                input.value = msg;
                sendMessage();   // 🔥 auto send
            }
        });
    });

});
document.addEventListener("DOMContentLoaded", function () {
    const scholarshipCards = Array.from(document.querySelectorAll(".scholarship-card"));

    if (!scholarshipCards.length) return;

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            const index = scholarshipCards.indexOf(entry.target);

            entry.target.style.setProperty("--delay", `${index * 0.15}s`);

            if (entry.isIntersecting) {
                entry.target.classList.add("show");
            } else {
                entry.target.classList.remove("show");
            }
        });
    }, {
        threshold: 0.2
    });

    scholarshipCards.forEach(function (card) {
        observer.observe(card);
    });
});