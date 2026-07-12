let priceChart = null;
console.log("charts.js loaded");

function destroyChart(){

    if(priceChart){

        priceChart.destroy();

        priceChart = null;

    }

}

function renderEmptyChart(){

    destroyChart();

    const canvas = document.getElementById("priceChart");

    const parent = canvas.parentElement;

    canvas.style.display = "none";

    let msg = document.getElementById("chart-message");

    if(!msg){

        msg = document.createElement("div");

        msg.id = "chart-message";

        msg.className = "chart-message";

        parent.appendChild(msg);

    }

    msg.innerHTML =

    `
    <h3>No Price History Yet</h3>

    <p>
        Search this product multiple times to build a historical
        price graph.
    </p>
    `;
}

function clearChartMessage(){

    const canvas = document.getElementById("priceChart");

    canvas.style.display = "block";

    const msg = document.getElementById("chart-message");

    if(msg){

        msg.remove();

    }

}

function renderPriceChart(history){

    const canvas = document.getElementById("priceChart");

    if(!canvas) return;

    if(!history || history.length===0){

        if(priceChart){

            priceChart.destroy();
            priceChart = null;

        }

        return;

    }

    const labels = history.map(h => h.date);

    const prices = history.map(h => h.price);

    if(priceChart){

        priceChart.data.labels = labels;

        priceChart.data.datasets[0].data = prices;

        priceChart.update();

        return;

    }

    const ctx = canvas.getContext("2d");

    priceChart = new Chart(ctx,{

        type:"line",

        data:{

            labels:labels,

            datasets:[{

                label:"Price History",

                data:prices,

                borderWidth:3,

                tension:0.35,

                fill:false

            }]

        },

        options:{

            responsive:true,

            maintainAspectRatio:false,

            animation:false

        }

    });

}

function renderAnalyticsCards(data){

    document.getElementById("stats").innerHTML =

    `
    <div class="stat-card">

        <h3>Current</h3>

        <p>${money(data.current_price)}</p>

    </div>

    <div class="stat-card">

        <h3>Lowest</h3>

        <p>${money(data.lowest_price)}</p>

    </div>

    <div class="stat-card">

        <h3>Highest</h3>

        <p>${money(data.highest_price)}</p>

    </div>

    <div class="stat-card">

        <h3>Average</h3>

        <p>${money(data.average_price)}</p>

    </div>

    `;

}

function renderAnalytics(data){

    renderAnalyticsCards(data);

    renderPriceChart(data.history);

}