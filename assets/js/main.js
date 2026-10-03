/* TRL site interactions: accessible navigation and the WhatsApp enquiry form. */
(function () {
  var phone = "923190091457";
  var menu = document.getElementById("menu");
  var burger = document.querySelector(".burger");
  var header = document.querySelector(".nav");

  function closeMenu() {
    if (!menu || !burger) return;
    menu.classList.remove("is-open");
    burger.setAttribute("aria-expanded", "false");
    burger.setAttribute("aria-label", "Open menu");
  }

  if (menu && burger) {
    burger.addEventListener("click", function () {
      var open = burger.getAttribute("aria-expanded") !== "true";
      menu.classList.toggle("is-open", open);
      burger.setAttribute("aria-expanded", String(open));
      burger.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      if (open) {
        var firstLink = menu.querySelector("a");
        if (firstLink) firstLink.focus();
      }
    });

    menu.addEventListener("click", function (event) {
      if (event.target.closest("a")) closeMenu();
    });

    document.addEventListener("click", function (event) {
      if (burger.getAttribute("aria-expanded") === "true" && header && !header.contains(event.target)) closeMenu();
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && burger.getAttribute("aria-expanded") === "true") {
        closeMenu();
        burger.focus();
      }
    });

    window.addEventListener("resize", function () {
      if (window.innerWidth > 900) closeMenu();
    }, { passive: true });
  }

  var year = document.getElementById("yr");
  if (year) year.textContent = new Date().getFullYear();

  var form = document.getElementById("waform");
  if (form) form.addEventListener("submit", function (event) {
    event.preventDefault();
    var data = new FormData(form);
    var value = function (key) { return (data.get(key) || "").toString().trim(); };
    var message = "Assalam o Alaikum Rashid, I found TRL on the website.\n\n" +
      "Name: " + value("name") + "\nBusiness: " + value("business") + "\nType: " + value("type") +
      "\nInterested in: " + value("interest") + (value("link") ? "\nLink/page: " + value("link") : "") +
      "\n\nWhat takes most of my time:\n" + value("pain");
    window.open("https://wa.me/" + phone + "?text=" + encodeURIComponent(message), "_blank", "noopener,noreferrer");
  });
})();
