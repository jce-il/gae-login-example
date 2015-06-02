$(function() {
    refreshGroups();
    $('#create_group').on('click', createGroup);
});


function createGroup() {
    $('#group_title').css('background', '#FFF');
    var title = $('#group_title').val();
    if(!title) {
        $('#group_title').css('background', '#FAA');
        return;
    }


    $.ajax({
		url:'/api/create_group',
		type:'GET',
		dataType:'json',
        data:{title:title},
		success:function(data, status, xhr) {
            $('#group_title').val('');
            populateGroups(data.groups);
		},
		error:function(xhr, status, error) {
            alert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
}

function refreshGroups() {
    $.ajax({
		url:'/api/get_groups',
		type:'GET',
		dataType:'json',
		success:function(data, status, xhr) {
            populateGroups(data.groups);
		},
		error:function(xhr, status, error) {
            alert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
}

function populateGroups(groups) {
    console.log(groups);
    var groups_str = '';
    for(var group in groups) {
        //console.log(groups[group]);
        groups_str += '<a href="/groups/'+groups[group].id+'">'+groups[group].title+'</a>'+(groups[group].admin ? '<span>(admin)</span>': '')+'<br>';
    }
    //console.log(groups_str)
    $('#groups').html(groups_str);
    //$('#groups').html(groups_str);
}

