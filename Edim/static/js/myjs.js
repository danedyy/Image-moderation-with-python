//  <!-- script to update image holder to selected image -->

 function readURL(input) {
     if (input.files && input.files[0]) {
         var reader = new FileReader();
         reader.onload = function (e) {
             $('#image_view').attr('src', e.target.result)
         };
         reader.readAsDataURL(input.files[0]);
     }
 }
 // $("#file-2").onchange(function () {
 //    readURL(this); 
 // });

 // <!-- end of script  -->


 // <!-- script to update select image button after selection -->

 'use strict';

 ;
 (function (document, window, index) {
     var inputs = document.querySelectorAll('.inputfile');
     Array.prototype.forEach.call(inputs, function (input) {
         var label = input.nextElementSibling,
             labelVal = label.innerHTML;

         input.addEventListener('change', function (e) {
             var fileName = e.target.value.split('\\').pop();

             if (fileName)
                 label.querySelector('span').innerHTML = fileName;
             else
                 label.innerHTML = labelVal;
         });

         // Firefox bug fix
         input.addEventListener('focus', function () {
             input.classList.add('has-focus');
         });
         input.addEventListener('blur', function () {
             input.classList.remove('has-focus');
         });
     });
 }(document, window, 0));

 // <!-- end iof script -->

