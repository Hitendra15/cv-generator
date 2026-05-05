    function showToast(message, type = 'success') {
        let toast = $('#toast');
        if (!toast.length) {
            $('body').append(`
                <div id="toast" class="toast-success" style="display:none;">
                    <span id="toast-message"></span>
                    <span class="toast-close">&times;</span>
                </div>
            `);
            toast = $('#toast');
        }
        toast.removeClass('toast-success toast-error')
            .addClass(type === 'error' ? 'toast-error' : 'toast-success');
        $('#toast-message').text(message);
        toast.show();
        setTimeout(function () {
            toast.hide();
        }, 5000);
        $('#timelineDrawer').removeClass('open');
        $('body').removeClass('drawer-open');
    }