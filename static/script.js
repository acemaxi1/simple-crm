let existingItems = [];
let orderList = [];
let customerNames = [];

async function fetchOrders() {
    try {
        const response = await fetch("http://localhost:8080/orders");
        if (response.ok) {
            existingItems = await response.json();
            updateProducts();
        } else {
            console.error("Failed to fetch existing items.");
        }
    } catch (error) {
        console.error("Error fetching existing items:", error);
    }
}

async function fetchCustomersNames() {
    try {
        const response = await fetch("http://localhost:8080/customers/names");
        if (response.ok) {
            customerNames = await response.json();
            updateCustomerFilter();
        } else {
            console.error("Failed to fetch customer names.");
        }
    } catch (error) {
        console.error("Error fetching customer names:", error);
    }
}

function updateCustomerFilter() {
    const customerFilterDropdown = document.getElementById("customerFilter");
    customerFilterDropdown.innerHTML = "";

    const allCustomersOption = document.createElement("option");
    allCustomersOption.value = "";
    allCustomersOption.text = "All Customers";
    customerFilterDropdown.add(allCustomersOption);

    customerNames.forEach(customerName => {
        const option = document.createElement("option");
        option.value = customerName;
        option.text = customerName;
        customerFilterDropdown.add(option);
    });
}

async function filterProducts() {
    const selectedCustomer = document.getElementById("customerFilter").value;

    try {
        let apiUrl = "http://localhost:8080/orders";

        if (selectedCustomer !== "") {
            apiUrl += `?customer=${selectedCustomer}`;
        }
        const response = await fetch(apiUrl);
        if (response.ok) {
            const filteredItems = await response.json();
            displayFilteredItems(filteredItems);
        } else {
            console.error("Failed to fetch filtered existing items.");
        }
    } catch (error) {
        console.error("Error fetching filtered existing items:", error);
    }
}

function displayFilteredItems(filteredItems) {
    const existingItemsContainer = document.getElementById("existingItems");
    existingItemsContainer.innerHTML = "";

    filteredItems.forEach(item => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
            <h5>${item.Order.product_name}</h5>
            <p>Price: $${item.Order.total_price.toFixed(2)}</p>
            <p>Quantity: ${item.Order.quantity}</p>
            <p>Date: ${item.Order.date}</p>
        `;
        card.onclick = function () {
            addProduct(item.Order.product_name, item.Order.total_price, item.Order.quantity, item.Order.date);
        };
        existingItemsContainer.appendChild(card);
    });
}

function updateProducts() {
    const existingItemsContainer = document.getElementById("existingItems");
    existingItemsContainer.innerHTML = "";

    existingItems.forEach(item => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
            <h5>${item.Order.product_name}</h5>
            <p>Price: $${item.Order.total_price.toFixed(2)}</p>
            <p>Quantity: ${item.Order.quantity}</p>
            <p>Date: ${item.Order.date}</p>
        `;
        card.onclick = function () {
            addProduct(item.Order.product_name, item.Order.total_price, item.Order.quantity, item.Order.date);
        };
        existingItemsContainer.appendChild(card);
    });
}

function addProduct(name, price, quantity, date) {
    orderList.push({ name, price, quantity, date });
    updateOrderList();
    updateOrderSummary();
}

function removeFromOrder(name, quantity) {
    orderList = orderList.filter(item => !(item.name === name && item.quantity === quantity));
    updateOrderList();
    updateOrderSummary();
}

function updateOrderList() {
    const orderTableBody = document.getElementById("orderTableBody");
    orderTableBody.innerHTML = "";

    orderList.forEach((item, index) => {
        const newRow = orderTableBody.insertRow();
        newRow.innerHTML = `
            <td>${item.name}</td>
            <td>$${item.price.toFixed(2)}</td>
            <td>${item.quantity}</td>
            <td>${item.date}</td>
            <td><button class="btn btn-danger" onclick="removeFromOrder('${item.name}', ${item.quantity})">Remove</button></td>
        `;
    });
}

function updateOrderSummary() {
    const totalPriceElement = document.getElementById("totalPrice");
    const totalQuantityElement = document.getElementById("totalQuantity");

    // Calculate total price and quantity
    const total = orderList.reduce((acc, item) => {
        acc.price += item.price * item.quantity;
        acc.quantity += item.quantity;
        return acc;
    }, { price: 0, quantity: 0 });

    // Update the displayed total price and quantity
    totalPriceElement.textContent = total.price.toFixed(2);
    totalQuantityElement.textContent = total.quantity;
}

// Fetch on page load
fetchCustomersNames();
fetchOrders();
