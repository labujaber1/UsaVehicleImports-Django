
// slow down video play in news.html header
const video = document.querySelector('video');
if (video) {
  video.defaultPlaybackRate = 1.0;
  video.playbackRate = 0.35;
}
//bootstrap5 toasts for alert messages
// used with a button
document.addEventListener("DOMContentLoaded", function(){ 
    var toast = document.getElementById("showToast");
    // Create toast instance
    var myToast = new bootstrap.Toast(toast);    
        myToast.show();
});

// used after form submission
 function showToast(){
    var myToastEl = document.getElementById('showToast')
    var myToast = bootstrap.Toast.getInstance(myToastEl) 
    myToast.show();
}

//copy to clipboard

const copyUrlElement = document.getElementById("copy-url");
if (copyUrlElement) {
  copyUrlElement.addEventListener("click", function() {
    var url = window.location.href; // Get the current URL
    navigator.clipboard.writeText(url).then(function() {
      console.log("URL copied to clipboard!");
      alert("URL copied to clipboard");
    }, function(err) {
      console.error("Failed to copy URL to clipboard:", err);
      alert("Try again\nInitially failed to copy URL to clipboard:", err);
    });
  });
}
