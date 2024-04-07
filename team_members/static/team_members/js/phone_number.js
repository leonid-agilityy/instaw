// JavaScript to format phone number property
function format_phone_number() {
    document.querySelectorAll('.phone').forEach(function(element) {
        var phoneNumber = element.textContent.trim();
        element.textContent = phoneNumber.replace(/(\d{3})(\d{3})(\d{4})/, '$1-$2-$3');
    });

    var phoneNumber = document.getElementById('phone');
    if (phoneNumber) {
        phoneNumber.value = phoneNumber.value.replace(/(\d{3})(\d{3})(\d{4})/, '$1-$2-$3');
    }
}
