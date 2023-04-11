// function addToCart(productId) {
//     // Get the cart from local storage or create a new one
//     let cart = JSON.parse(localStorage.getItem('cart')) || {};
//
//     // If the product is already in the cart, increment its quantity
//     if (cart[productId]) {
//         cart[productId].quantity++;
//     } else {
//         // Otherwise, add the product to the cart with quantity 1
//         cart[productId] = {id: productId, quantity: 1};
//     }
//
//     // Save the updated cart to local storage
//     localStorage.setItem('cart', JSON.stringify(cart));
// }
//
// function removeFromCart(productId) {
//     // Get the cart from local storage
//     let cart = JSON.parse(localStorage.getItem('cart'));
//
//     // Remove the product from the cart
//     delete cart[productId];
//
//     // Save the updated cart to local storage
//     localStorage.setItem('cart', JSON.stringify(cart));
// }
//
// function getCartItems() {
//     // Get the cart from local storage
//     let cart = JSON.parse(localStorage.getItem('cart')) || {};
//
//     // Get the cart items from the database using the product IDs
//     let cartItems = [];
//     for (let productId in cart) {
//         let cartItem = {id: productId, quantity: cart[productId].quantity};
//         // Get the product information from the database using the product ID
//         // and add it to the cart item
//         // ...
//         cartItems.push(cartItem);
//     }
//     console.log(cartItems)
//     return cartItems;
// }
//
