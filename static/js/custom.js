$(document).ready(function() {
    // Function to handle quantity decrement
    $('.decrement-btn').on('click', function(e) {
        e.preventDefault();

        var quantityInput = $(this).siblings('.quantity-input');
        var quantityValue = parseInt(quantityInput.val(), 10);
        if (quantityValue > 1) {
            quantityValue--;
            quantityInput.val(quantityValue);
        }
    });

    // Function to handle quantity increment
    $('.increment-btn').on('click', function(e) {
        e.preventDefault();

        var quantityInput = $(this).siblings('.quantity-input');
        var quantityValue = parseInt(quantityInput.val(), 10);
        quantityValue = isNaN(quantityValue) ? 0 : quantityValue;
        // Enforce a maximum quantity of 100
        var maxQuantity = 100;
        if (quantityValue < maxQuantity) {
            quantityValue++;
            quantityInput.val(quantityValue);
        }
    });
});


$('.addtocartbtn').click(function(e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.quantity-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            type: 'POST',
            url: "/add-to-cart",
            data: {
                'product_id': product_id,
                'prodqan': product_qty,
                csrfmiddlewaretoken: token
            },
            success: function(response) {
                console.log(response);
                alertify.success(response.status);
            }
        });
    });




    $('.addtowishlist').click(function(e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/add-to-wishlist",
            data: {
                'product_id': product_id,
                
                csrfmiddlewaretoken: token
            },
            success: function(response) {
               
                alertify.success(response.status);
            }
        });
    });

    
$('.changeQuantity').click(function(e) {
        e.preventDefault();
        var quantityInput = $(this).siblings('.quantity-input');
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = parseInt(quantityInput.val(), 10);
        var token = $('input[name=csrfmiddlewaretoken]').val();
    
        // Update the product_qty based on the button clicked (+ or -)
        if ($(this).hasClass('increment-btn')) {
            product_qty++;
        } else if ($(this).hasClass('decrement-btn')) {
            if (product_qty > 1) {
                product_qty--;
            }
        }
    
        // Capture the reference to the clicked button in a variable
        var clickedButton = $(this);
    
        $.ajax({
            type: 'POST',
            url: "/update-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token
            },
            success: function(response) {
                console.log(response);
                // Update the quantity displayed on the page using the updated value
                quantityInput.val(product_qty);
            },
            error: function(xhr, textStatus, errorThrown) {
                console.error(xhr.responseText);
                // Handle the error if necessary
            }
        });
    });
    
    $('.delete-cart-item').click(function(e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
    
        // Save a reference to the current delete button
        var deleteButton = $(this);
    
        $.ajax({
            method: 'POST',
            url: "/delete-cart-item",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function(response) {
                alertify.success(response.status);
    
                // After successful deletion, remove the deleted item's row from the cart
                deleteButton.closest('.product_data').remove();
    
                // Check if the cart is empty after deletion
                if (response.is_empty) {
                    // If all cart items have been removed, update the cart section with the "Your cart is empty" message
                    var emptyMessage = '<h6>Your cart is empty</h6>';
                    $('.cartdata').html(emptyMessage);
                }
            },
            error: function(response) {
                // Handle the error response if needed
                console.error(response);
            }
        });
    });

    $(document).on('click', '.delete-wishlist-item', function(e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
    
        // Save a reference to the current delete button
        var deleteButton = $(this);
    
        $.ajax({
            method: 'POST',
            url: "/delete-wishlist-item",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function(response) {
                alertify.success(response.status);
    
                // After successful deletion, remove the deleted item's row from the wishlist
                deleteButton.closest('.product_data').remove();
    
                // Check if the wishlist is empty after deletion
                if (response.is_empty) {
                    // If all wishlist items have been removed, update the wishlist section with the "Your wishlist is empty" message
                    var emptyMessage = '<h6>Your wishlist is empty</h6>';
                    $('.wishtdata').html(emptyMessage);
                }
            },
            error: function(response) {
                // Handle the error response if needed
                console.error(response);
            }
        });
    });


    
    
    
    
