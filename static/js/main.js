const date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();
// Use javascrip lamda function to control message timeout after 5 seconds.
setTimeout(() => $("#message").fadeOut("slow"), 5000);
