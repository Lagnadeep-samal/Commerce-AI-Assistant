async function sendMessage() {

    const input =
        document.getElementById(
            "message"
        );

    const message = input.value;

    if (!message) return;

    const chatBox =
        document.getElementById(
            "chat-box"
        );

    /* DYNAMIC CHAT HISTORY */

    const historyList =
        document.getElementById(
            "history-list"
        );

    const historyItem =
        document.createElement(
            "div"
        );

    historyItem.className =
        "history-item";

    historyItem.innerHTML = `

    <div class="history-title">
        ${message.substring(0,25)}
    </div>

    <div class="history-time">
        Just now
    </div>

    `;

    historyItem.onclick = function(){

        document.getElementById(
            "message"
        ).value = message;
    };

    historyList.prepend(
        historyItem
    );

    // LIMIT HISTORY

    if(
        historyList.children.length > 5
    ){

        historyList.removeChild(
            historyList.lastChild
        );
    }

    // USER MESSAGE

    chatBox.innerHTML += `
        <div class="user">
            ${message}
        </div>
    `;

    input.value = "";

    // AUTO PRODUCT CARD

    if(
        message.toLowerCase().includes("nike")
    ){

        addProductCard();
    }

    // AUTO TRACKING

    if(
        message.toLowerCase().includes("track")
    ){

        showTracking();
    }

    // BOT MESSAGE

    const botDiv =
        document.createElement(
            "div"
        );

    botDiv.className = "bot";

    botDiv.innerHTML = `
        <span class="typing">
            Typing...
        </span>
    `;

    chatBox.appendChild(botDiv);

    chatBox.scrollTop =
        chatBox.scrollHeight;

    // FETCH

    const response = await fetch(
        "/chat",
        {
            method:"POST",

            headers:{
                "Content-Type":
                "application/json"
            },

            body:JSON.stringify({
                message:message
            })
        }
    );

    const reader =
        response.body.getReader();

    const decoder =
        new TextDecoder();

    botDiv.innerHTML = "";

    // STREAMING RESPONSE

    while(true){

        const {
            done,
            value
        } = await reader.read();

        if(done) break;

        const chunk =
            decoder.decode(value);

        botDiv.innerHTML += chunk;

        chatBox.scrollTop =
            chatBox.scrollHeight;
    }

    // SUGGESTED REPLIES

    const suggestions =
        document.createElement(
            "div"
        );

    suggestions.className =
        "suggestions";

    suggestions.innerHTML = `

    <button onclick="quickMessage('Track my order')">
    Track Order
    </button>

    <button onclick="quickMessage('Refund status')">
    Refund
    </button>

    <button onclick="quickMessage('Cancel order')">
    Cancel
    </button>

    <button onclick="quickMessage('Latest offers')">
    Offers
    </button>

    `;

    chatBox.appendChild(
        suggestions
    );

    chatBox.scrollTop =
        chatBox.scrollHeight;
}

/* QUICK BUTTONS */

function quickMessage(text){

    document.getElementById(
        "message"
    ).value = text;

    sendMessage();
}

/* ENTER KEY */

document
.getElementById("message")
.addEventListener(
    "keypress",
    function(e){

        if(e.key === "Enter"){

            sendMessage();
        }
    }
);

/* SIDEBAR SECTIONS */

function openSection(section){

    const sectionDiv =
        document.getElementById(
            "section-content"
        );

    let html = "";

    if(section === "orders"){

        html = `
            <h2>📦 Orders</h2>

            <div class="card">
                Track your current orders,
                manage purchases,
                and view history.
            </div>
        `;
    }

    else if(section === "returns"){

        html = `
            <h2>🔄 Returns</h2>

            <div class="card">
                Start returns,
                check refund eligibility,
                and manage cancellations.
            </div>
        `;
    }

    else if(section === "delivery"){

        html = `
            <h2>🚚 Delivery</h2>

            <div class="card">
                Check delivery timelines,
                shipment status,
                and shipping policies.
            </div>
        `;
    }

    else if(section === "help"){

        html = `
            <h2>🛠 Help Center</h2>

            <div class="card">
                Get support for orders,
                refunds,
                payments,
                and account issues.
            </div>
        `;
    }

    else if(section === "analytics"){

        html = `

        <h2>
            📊 Analytics Dashboard
        </h2>

        <div class="analytics-grid">

            <div class="analytics-card">
                <h3>1200</h3>
                <p>Total Queries</p>
            </div>

            <div class="analytics-card">
                <h3>320</h3>
                <p>Refund Requests</p>
            </div>

            <div class="analytics-card">
                <h3>89%</h3>
                <p>Customer Satisfaction</p>
            </div>

            <div class="analytics-card">
                <h3>140</h3>
                <p>Live Users</p>
            </div>

        </div>
        `;
    }

    sectionDiv.innerHTML = html;
}

/* PRODUCT CARD */

function addProductCard(){

    const chatBox =
        document.getElementById(
            "chat-box"
        );

    chatBox.innerHTML += `

        <div class="product-card">

            <img
                src="https://images.unsplash.com/photo-1542291026-7eec264c27ff"
                class="product-image"
            >

            <div class="product-info">

                <h3>
                    Nike Air Max
                </h3>

                <p>
                    ₹4,999
                </p>

                <div class="rating">
                    ⭐⭐⭐⭐ 4.5
                </div>

                <button class="buy-btn">
                    Buy Now
                </button>

            </div>

        </div>
    `;
}

/* TRACKING CARD */

function showTracking(){

    const chatBox =
        document.getElementById(
            "chat-box"
        );

    chatBox.innerHTML += `

    <div class="tracking-card">

        <h3>
            📦 Order Tracking
        </h3>

        <div class="track-step active">
            ✅ Order Placed
        </div>

        <div class="track-step active">
            ✅ Packed
        </div>

        <div class="track-step active">
            🚚 Shipped
        </div>

        <div class="track-step pending">
            ⏳ Out for Delivery
        </div>

        <div class="track-step pending">
            📍 Delivered
        </div>

    </div>
    `;
}

/* PAYMENT PIPELINE */

function showPaymentPage(){

    document.getElementById(
        "payment-modal"
    ).style.display = "flex";
}

function closePayment(){

    document.getElementById(
        "payment-modal"
    ).style.display = "none";
}

function processPayment(){

    const name =
        document.getElementById(
            "card-name"
        ).value;

    const card =
        document.getElementById(
            "card-number"
        ).value;

    const amount =
        document.getElementById(
            "amount"
        ).value;

    if(
        !name ||
        !card ||
        !amount
    ){

        alert(
            "Fill all payment fields"
        );

        return;
    }

    alert(
        "✅ Payment Successful"
    );

    closePayment();

    const chatBox =
        document.getElementById(
            "chat-box"
        );

    chatBox.innerHTML += `

    <div class="bot">

        ✅ Payment of ₹${amount}
        completed successfully.

        <br><br>

        Transaction ID:
        TXN${Math.floor(
            Math.random()*100000
        )}

    </div>
    `;
}