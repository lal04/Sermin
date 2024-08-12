
document.addEventListener('DOMContentLoaded', function() {
    var dropdown = document.querySelectorAll('.dropdown-btn');
    dropdown.forEach(function(btn) {
        btn.addEventListener('click', function() {
            var dropdownContent = this.nextElementSibling;
            if (dropdownContent.style.display === 'block') {
                dropdownContent.style.display = 'none';
            } else {
                dropdownContent.style.display = 'block';
            }
        });
    });
});


