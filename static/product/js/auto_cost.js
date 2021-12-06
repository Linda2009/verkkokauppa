// if (!$) {
//     $ = django.jQuery;
// }
// $(document).ready(function(){
//     // Add event listener to "price" input
//     $("#id_regular_price").change(function(e){
//         // Get entered value
//         let regular_price = parseFloat($(this).val());

//         // Get discount value from another field 
//         let discount_percent = parseFloat($("#id_discount_percent").val())

//         // Compute cost in whatever way you want
//         let cost = regular_price - regular_price * (discount_percent/100);
//         let discounted_price= regular_price * (discount_percent /100)
//          // Set value in read-only "discounted_price" field.
//         $("div.field-discounted_price").find("div.readonly").text(discounted_price);
//          // Set value in read-only "cost" field.
//         $("div.field-cost").find("div.readonly").text(cost);
//     });
// })