function go() {
  var a;

  // a = 10
  // alert(a)
  // alert(typeof (a))

  //
  // document.write(a)
  // a += 10
  // console.log(a)
  // a *= 10
  // console.log(a)
  // a -= 10
  // console.log(a)
  // a /= 10
  // console.log(a)
  // document.write(a
  // )

  a = document.getElementById("input").value
  if (a%2==0){
    document.getElementById("output").innerHTML = "<div class='alert alert-success'> even No</div>";
    // alert(document.getElementById("output"))
    // console.log("Even No")
  }
  else
  {
    document.getElementById("output").innerHTML = "<div class='alert alert-danger'>Odd No</div >"
  }
  // console.log(a)
}

function go1(){
  var a;
  a = parseInt(document.getElementById("input").value)
  switch(a){
    case 1:
      alert("one")
      break;
    case 2:
      alert("two")
      break
  }
}
