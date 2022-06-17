console.log("Handling")

var ac = document.getElementById("anchor");
var val =document.getElementById("email-ef64").value;
console.log(val)
document.getElementById("anchor").addEventListener("click", function() {
var val =document.getElementById("email-ef64").value;
  console.log(val)
  ac.href = "http://localhost:8000/sendemailaddress/"+val
});
