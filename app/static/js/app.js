$(function(){


	var timeoutID = null;

	function findMember(str) {
		console.log("search");
		$.ajax({
			type: 'POST',
			url: '/item/search/' + $("#search").val(),
			data: {},
			success: function(resp) {;
				$("#items-list").html(resp);
			},
			error: function() {
			}
		});
	}

	$('#search').keyup(function() {
		clearTimeout(timeoutID);
		var $target = $(this);
		timeoutID = setTimeout(function() { findMember($target.val()); }, 300);
	});

});