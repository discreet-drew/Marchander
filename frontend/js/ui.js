console.log("ui.js loaded");

function money(value){

    if(value===null || value===undefined){

        return "N/A";

    }
    return "₹"+Number(value).toLocaleString("en-IN");
}

function renderProductCard(product){

    if(!product){

        return `
        <div class="card unavailable">

            <h2>Unavailable</h2>

            <div class="price">N/A</div>

            <p>Product not found.</p>

        </div>
        `;
    }

    return `

    <div class="card fade-in">

        <div class="store-header">

            <h2>${product.store}</h2>

        </div>

        <div class="price">

            ${money(product.price)}

        </div>

        <p class="product-title">

            ${product.title || "Unknown Product"}

        </p>

        <p class="availability">

            ${product.availability || "Available"}

        </p>

        ${
            product.url
            ?

            `<a
                href="${product.url}"
                target="_blank"
                class="buy-btn">

                View Product

            </a>`

            :

            ""
        }

    </div>

    `;
}

function renderBestDeal(data){

    const div = document.getElementById("best-deal");

    if(!data){

        div.innerHTML="";

        return;

    }

    div.innerHTML =

    `

    <div class="best-price fade-in">

        <div class="badge">

            🏆 BEST DEAL

        </div>

        <h2>

            ${data.best_store || "Unavailable"}

        </h2>

        <div class="winner">

            ${money(data.lowest_price)}

        </div>

        ${
            data.savings

            ?

            `

            <div class="savings">

                💰 You Save

                ${money(data.savings)}

            </div>

            `

            :

            ""

        }

    </div>

    `;

}

function renderComparison(data){

    document

    .getElementById("result")

    .innerHTML =

    `

    <div class="results">

        ${renderProductCard(data.flipkart)}

        ${renderProductCard(data.amazon)}

    </div>

    `;

    renderBestDeal(data);

}

function renderAchievement(data){

    const achievement =

    document.getElementById("achievement");

    if(

        !data ||

        !data.savings ||

        data.savings<=0

    ){

        achievement.innerHTML="";

        return;

    }

    achievement.innerHTML=

    `

    <div class="achievement-card">

        🎉 Great Choice!

        You saved

        <strong>

        ${money(data.savings)}

        </strong>

        using Marchander.

    </div>

    `;

}

function renderHistory(history){

    const div =

    document.getElementById("history");

    if(

        !history ||

        history.length===0

    ){

        div.innerHTML="";

        return;

    }

    div.innerHTML=

    `

    <h2>

        Recent Price History

    </h2>

    `

    +

    history

    .slice()

    .reverse()

    .map(item=>

    `

    <div class="history-item">

        <span>

            ${item.date}

        </span>

        <span>

            ${item.store}

        </span>

        <strong>

            ${money(item.price)}

        </strong>

    </div>

    `

    )

    .join("");

}

function renderEmptyState(){

    document

    .getElementById("result")

    .innerHTML=

    `

    <div class="card">

        <h2>

            Search Any Product

        </h2>

        <p>

            Compare prices across Amazon and Flipkart.

        </p>

    </div>

    `;

}

function renderError(message){

    document

    .getElementById("result")

    .innerHTML=

    `

    <div class="card">

        <h2>

            Something Went Wrong

        </h2>

        <p>

            ${message}

        </p>

    </div>

    `;

}

function showLoading(){

    document

    .getElementById("loading")

    .style.display="block";

}

function hideLoading(){

    document

    .getElementById("loading")

    .style.display="none";

}

function renderDashboard(

    comparison,

    analytics

){

    renderComparison(comparison);

    renderBestDeal(comparison);

    renderAchievement(comparison);

    renderHistory(

        analytics.history

    );

}