$().ready(function () {
  $('#register-form input').tooltipster({ 	  	
        trigger: 'custom', // default is 'hover' which is no good here
        onlyOne: false,    // allow multiple tips to be open at a time
        position: 'right',
	  	animation: 'grow'// display the tips to the right of the element
    });
  
  // validate signup form on keyup and submit
  $("#register-form").validate({
	errorPlacement: function (error, element) {
            var lastError = $(element).data('lastError'),
                newError = $(error).text();

            $(element).data('lastError', newError);

            if(newError !== '' && newError !== lastError){
                $(element).tooltipster('content', newError);
                $(element).tooltipster('show');
            }
        },
        success: function (label, element) {
            $(element).tooltipster('hide');
        },
    rules: {
      password: {               
		pattern: /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/	  
      },
      confirm_password: {       
		pattern: /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/,
        equalTo: "#password"
      }
    },
    messages: {    
      password: {
        pattern: "Your password must be at least 8 characters long including a upper case a lower case and a digit"
      },
      confirm_password: {
        pattern: "Your password must be at least 8 characters long including a upper case a lower case and a digit",
        equalTo: "Please enter the same password as above"
      }
     
    },
	submitHandler: function(form) {
    // do other things for a valid form
    form.submit();
    }
  });

});