function closePopup() {
    const popup = document.getElementById("dynamicPopup");
    if (popup) {
        popup.style.display = "none";
    }
}

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

function sendMessage() {
    const input = document.getElementById("chat-input");
    const body = document.getElementById("chat-body");

    if (!input || !body) return;

    const msg = input.value.trim();
    if (!msg) return;

    body.innerHTML += `<div class="chat-msg user-msg">${msg}</div>`;
    body.innerHTML += `<div id="bot-typing"><b>NecBot:</b> Typing...</div>`;
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

        body.innerHTML += `<div><b>NecBot:</b> ${data.reply}</div>`;
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
            }, 5000);
        }
    }

    const tabs = document.querySelectorAll("[data-program-tab]");
    const panels = document.querySelectorAll("[data-program-panel]");

    if (tabs.length && panels.length) {
        tabs.forEach((tab) => {
            tab.addEventListener("click", function () {
                const slug = this.getAttribute("data-program-tab");

                tabs.forEach((t) => t.classList.remove("active"));
                panels.forEach((p) => p.classList.remove("active"));

                this.classList.add("active");

                const activePanel = document.querySelector(`[data-program-panel="${slug}"]`);
                if (activePanel) {
                    activePanel.classList.add("active");
                }
            });
        });
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
