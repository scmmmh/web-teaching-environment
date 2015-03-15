/**
 * Evaluation-specific JS file that logs when the user moves their mouse over
 * one of the given elements of the page.
 */
var url = $(document.currentScript).data('log-url');
var LOGGING_SELECTOR = '#textbook, #files, #viewer';

$(document).ready(function() {
    $(LOGGING_SELECTOR).on('mouseover', function(ev) {
        $.ajax(url, {
            data: {mouse_over: $(this).attr('id')}
        });
    });
});
