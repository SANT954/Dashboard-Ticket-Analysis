function clearReports(e){
	 
    document.getElementById('image_box').src ="" ;
    document.getElementById('showing_for').innerHTML=""

}

 
function generateReport(e){


 var x = document.getElementById("id_sprint").value;

    console.log(document.getElementById("id_sprint").value);
    if(x!=="Select Sprint"){
    	document.getElementById('showing_for').innerHTML="Showing " +e.value +" for " + x;

    document.getElementById('image_box').src = "/media/" + x +"/"+ e.id+".png";
    
}else{

    document.getElementById('image_box').src ="" ;
    document.getElementById('showing_for').innerHTML=""

}	
}


 
function loadDoc() {
	  var xhttp = new XMLHttpRequest();
	  xhttp.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	     document.getElementById("showing_for").innerHTML = this.responseText;
	    }
	  };
	  xhttp.open("POST", "/sprint_summary/", true);
	  xhttp.send();
	}