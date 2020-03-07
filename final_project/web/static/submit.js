function SubmitFormData() {
	var name = $("#sentence").val();
	
	$.post("submit.php", { sentence: sentence },
	   function(data) {
		 $('#results').html(data);
		 $('#myForm')[0].reset();
	   });
}

