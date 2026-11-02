/* Plays the muted, looping videos rendered by _includes/img.html (converted
   animated GIFs) only while they are on screen, so they don't download until
   needed. Visitors who prefer reduced motion get the normal video controls. */
(function () {
  var videos = document.querySelectorAll("video[data-autoplay]");
  if (!videos.length) return;
  if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  function play(video) {
    var p = video.play();
    if (p && p.catch) p.catch(function () { video.controls = true; });
  }

  for (var i = 0; i < videos.length; i++) videos[i].controls = false;

  if (!("IntersectionObserver" in window)) {
    for (var j = 0; j < videos.length; j++) play(videos[j]);
    return;
  }
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) play(entry.target);
      else entry.target.pause();
    });
  }, { rootMargin: "200px 0px" });
  for (var k = 0; k < videos.length; k++) observer.observe(videos[k]);
})();
