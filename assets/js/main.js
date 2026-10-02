/* TRL v5 — nav, reveal, WhatsApp enquiry builder. No trackers. */
(function(){
  var WA = "923190091457";
  var nav = document.querySelector(".nav"), burger = document.querySelector(".burger");
  if (burger) burger.addEventListener("click", function(){
    var o = nav.classList.toggle("open"); burger.setAttribute("aria-expanded", o);
  });
  document.querySelectorAll(".menu a").forEach(function(a){a.addEventListener("click",function(){nav.classList.remove("open");burger&&burger.setAttribute("aria-expanded","false")})});
  var onS = function(){ nav && nav.classList.toggle("scrolled", window.scrollY > 8); };
  onS(); window.addEventListener("scroll", onS, {passive:true});

  var els = document.querySelectorAll(".rv");
  if ("IntersectionObserver" in window){
    var io = new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}})},{rootMargin:"0px 0px -8% 0px"});
    els.forEach(function(el){io.observe(el)});
  } else els.forEach(function(el){el.classList.add("in")});

  var y = document.getElementById("yr"); if (y) y.textContent = new Date().getFullYear();

  var f = document.getElementById("waform");
  if (f) f.addEventListener("submit", function(ev){
    ev.preventDefault();
    var d = new FormData(f), g = function(k){return (d.get(k)||"").toString().trim()};
    var msg = "Assalam o Alaikum Rashid, I found TRL on the website.\n\n" +
      "Name: " + g("name") + "\nBusiness: " + g("business") + "\nType: " + g("type") +
      "\nInterested in: " + g("interest") + (g("link") ? "\nLink/page: " + g("link") : "") +
      "\n\nWhat takes most of my time:\n" + g("pain");
    window.open("https://wa.me/" + WA + "?text=" + encodeURIComponent(msg), "_blank", "noopener");
  });
})();
