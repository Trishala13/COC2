<script type="text/javascript">

jQuery(function ($) {

$("#form01").validate({
        rules: {
            firstname: {
                required: true,
                lettersonly:true
            },
            lastname: {
                required: false,
                lettersonly:true
            },
	    username:{
		required:true,
		alphanumeric:true,
		minWords:8,
		maxWords:20
		},
	    password: {
		required:true,
		alphanumeric:true,
		minWords:8
		},
	    email: {
		required:true,
		email:true
		}
        },

	messages: {
	    email: {
	      required: "You need to enter email address",
	      email:"Enter valid email!!"
		},
	    username:{
		required:"You need to enter username for login",
	        minlength: "At least 8 characters required!"
		    },
	    firstname:{
		required:"You need enter firstname!!"
		},
	    password: {
		minlength:"At least 8 characters required!"
			}
   
	  },
highlight: function (element) {
            $(element).parent().addClass('error')
        },
        unhighlight: function (element) {
            $(element).parent().removeClass('error')
        },
             submitHandler: function(form)
             {
                form.submit();
             }

    });
});

</script>
