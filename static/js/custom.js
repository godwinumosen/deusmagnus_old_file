$(document).ready(function() {
    $(".js-height-full").height($(window).height());
    $(".js-height-parent").each(function() {
        $(this).height($(this).parent().first().height());
    });

    // Fun Facts
    function count($this) {
        var current = parseInt($this.data('current'), 10); // Get the current count from data attribute
        current += 1; // Increment value

        // Update only the numeric part while keeping the + sign
        $this.html(current + ' <span>+</span>');

        // Store the updated current value
        $this.data('current', current); // Update data-current

        if (current < $this.data('count')) {
            setTimeout(function() {
                count($this);
            }, 50);
        } else {
            $this.html($this.data('count') + ' <span class="plus">+</span>'); // Final value
        }
    }

    $(".stat-timer").each(function() {
        var countTo = parseInt($(this).text(), 10); // Get the initial count
        $(this).data('count', countTo); // Set the target count
        $(this).data('current', 0); // Initialize current count

        // Start counting only if the countTo is greater than 0
        if (countTo > 0) {
            count($(this)); // Start the counting
        } else {
            $(this).html(countTo + ' <span>+</span>'); // If it's 0 or not a number, set it directly
        }
    });

    $('.header').affix({
        offset: {
            top: 100,
            bottom: function() {
                return (this.bottom = $('.footer').outerHeight(true));
            }
        }
    });

    $(window).on('load', function() {
        $("#preloader").delay(500).fadeOut();
        $(".preloader").delay(600).fadeOut("slow");
    });
});
