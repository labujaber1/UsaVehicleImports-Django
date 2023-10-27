
// slow down video play in news.html header
document.querySelector('video').defaultPlaybackRate = 1.0;
document.querySelector('video').playbackRate = 0.35;

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


