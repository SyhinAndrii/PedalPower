
function validateForm() {
  let radios = document.getElementsByName("rating");
  let selected = false;
  for (let i = 0; i < radios.length; i++) {
    if (radios[i].checked) {
      selected = true;
      break;
    }
  }
    if (!selected) {
        return false;
    } else {
        return true;
    }
}

$(document).ready(function () {
    $('#feedback_form').submit(function (event) {
        event.preventDefault();
        if (!validateForm()){
            alert("Please rate the product!");
            return;
        }
        let data = $(this).data()
        console.log(data)
        let formData = $(this).serializeArray();
        formData.push({name: "product_id", value: data['product']})
        $.ajax({
            url: "/feedback/",
            type: 'POST',
            data: formData,
            success: function (data) {
                if (data['success']){
                    location.reload();
                }
                else{
                    window.location.href ="/login/"
                }

            },
            error: function (xhr, status, error) {
                console.log(error)
            }
        });
    });
});