'use strict';

let form_being_submitted = false;

const checkForm = function (form) {
	if (form_being_submitted) {
		alert('The form is being submitted, please wait a moment...');
		form.myButton.disabled = true;
		return false;
	}
	// document.querySelector('.output').getElementsByClassName.opacity = 1;

	const dataArr = [...new FormData(document.querySelector('#lap-form'))];
	const data = Object.fromEntries(dataArr);
	console.log(data);

	if (
		data.HDD == '' ||
		data.SSD == '' ||
		data.ScreenSize == '' ||
		data.company == '' ||
		data.cpuname == '' ||
		data.gpuname == '' ||
		data.ram == ''
	) {
		alert('please fill the form');
		form.myButton.disabled = false;
		return false;
	}

	if (data.company == 'apple') {
		if (
			data.cpuname !== 'M1 Max' &&
			data.cpuname !== 'M1 Pro' &&
			data.cpuname !== 'M1 Processor' &&
			data.cpuname !== 'M2 Max' &&
			data.cpuname !== 'M2 Pro' &&
			data.cpuname !== 'M2 Processor'
		) {
			alert('processor must be apple processor and dont tick msoffice');
			form.myButton.disabled = false;
			return false;
		}

		if (data.gpuname != 'Apple') {
			alert('GPU must be apple processor and dont tick msoffice');
			form.myButton.disabled = false;
			return false;
		}

		if (document.querySelector('#ms').checked) {
			alert('apple does not have ms office');
			form.myButton.disabled = false;
			return false;
		}
	}

	form.myButton.value = 'Submitting form...';
	form_being_submitted = true;
	return true; /* submit form */
};

const resetForm = function (form) {
	form.myButton.disabled = false;
	form.myButton.value = 'Submit';
	form_being_submitted = false;
};
