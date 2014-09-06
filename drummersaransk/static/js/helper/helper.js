$(document).ready(function(){		
	////active menu punkt
	var	pathname = location.pathname;
	var	pathnameList = pathname.split('/');
	var	slug1 = '/' + pathnameList[1];
	var	slug2 = '/' + pathnameList[2];

	console.log('pathname::' + pathname);
	console.log('pathnameList::' + pathnameList);
	console.log('slug1::' + slug1);
	console.log('slug2::' + slug2);
	console.log('slug1 + slug2 + slash::' + slug1 + slug2 + '/');

	$('.nav_edit_outer a').each(function(){
		var	href = $(this).attr('href');
		
		$(this).closest('li').removeClass('active');
		
		if(href == slug1 + slug2 + '/'){
			$(this).closest('li').addClass('active');
		}
	});	
	
	$('.nav_basic a').each(function(){
		var	href = $(this).attr('href');
		
		$(this).closest('li').removeClass('active');
		
		if(href == slug1 + slug2 + '/'){
			$(this).closest('li').addClass('active');
		}
		else if(slug2 == '/'){
			$('.nav_basic li').eq(0).addClass('active');
		}
	});	

	////teacher_fio
	var teacher_fio_elem = $('#teacher_fio');
	var id_teacher_fio_elem = $('#id_teacher_fio');	
	var	selected_num = $("#id_teacher :selected").val();
	
	if(selected_num == 2){
		teacher_fio_elem.removeClass('hide');
	};
	
	$('#id_teacher').on('change', function(){		
		$(this).find("option:selected").each(function(){
			num = $(this).val();
		});	
		
		//console.log(num);
		
		if(num == 2){
			teacher_fio_elem.removeClass('hide');
		}
		else{
			//console.log('else');
			teacher_fio_elem.addClass('hide');
			id_teacher_fio_elem.val('');
		}
	});
	
	//// hacks for image load widget. костыли блять((
	// path glory form
	var	label = $('.pathglory_item_form .image_outer .label');
	var	thumb = $('.pathglory_item_form .image_outer .box_common_outer');
	var	label2 = $('.pathglory_item_form .image_outer label[for="path_glory_photo-clear_id"]');
	var	photo_input = $('#id_path_glory_photo');
	var	checkbox = $('#path_glory_photo-clear_id');
	$('.pathglory_item_form .image_outer').empty().append(label).append(thumb).append(photo_input).append($('<div class="del" />')).append(checkbox).append(label2);
	
	// drum data form
	var	label = $('.drum_data_form .image_outer .label');
	var	thumb = $('.drum_data_form .image_outer .box_common_outer');
	var	label2 = $('.drum_data_form .image_outer label[for="drum_photo-clear_id"]');
	var	photo_input = $('#id_drum_photo');
	var	checkbox = $('#drum_photo-clear_id');
	$('.drum_data_form .image_outer').empty().append(label).append(thumb).append(photo_input).append($('<div class="del" />')).append(checkbox).append(label2);	
	
	// avatar change form
	var	label = $('.avatar_form .image_outer .label');
	var	thumb = $('.avatar_form .image_outer .box_common_outer');
	var	label2 = $('.avatar_form .image_outer label[for="avatar-clear_id"]');
	var	photo_input = $('#id_avatar');
	var	checkbox = $('#avatar-clear_id');
	$('.avatar_form .image_outer').empty().append(label).append(thumb).append(photo_input).append($('<div class="del" />')).append(checkbox).append(label2);		
});